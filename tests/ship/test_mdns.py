import pytest
import asyncio
from unittest.mock import MagicMock, patch, Mock, AsyncMock
import socket
from zeroconf import IPVersion

# Mock ServiceInfo class before importing MdnsAnnounceService to avoid isinstance check failure
# However, we mocked zeroconf in conftest, so ServiceInfo is a MagicMock.
# The issue is `isinstance(info, ServiceInfo)` fails if ServiceInfo is a MagicMock 
# unless we spec it or patch it correctly relative to where it is used.
# Since sys.modules['zeroconf'] is a mock, `from zeroconf import ServiceInfo` gets a Mock.
# But `isinstance(mock_obj, mock_class)` should work if setup right, or we skip isinstance check.

# Better approach: We need to import MdnsAnnounceService after setting up specific return values?
# No, imports happen at top.

# Let's patch ServiceInfo in the test file to be a real class or a robust mock.
from ship.mdns_announce import MdnsAnnounceService

class TestShipMdnsAnnounce:
    """
    Tests anchored to SHIP Specification Section 11: Discovery and Attributes.
    Verifies proper mDNS service parameters and registration.
    """

    @pytest.fixture
    def mock_certificate(self):
        # Create a mock certificate with a subject key identifier extension
        mock_cert = MagicMock()
        mock_extension = MagicMock()
        mock_extension.value.digest.hex.return_value = "fake_ski_hash"
        mock_cert.extensions.get_extension_for_oid.return_value = mock_extension
        return mock_cert

    @pytest.fixture
    def mock_x509_load(self, mock_certificate):
        with patch('ship.mdns_announce.x509.load_pem_x509_certificate', return_value=mock_certificate) as mock:
            yield mock

    @pytest.fixture
    def mock_psutil(self):
        with patch('ship.mdns_announce.psutil') as mock:
            snic_v4 = Mock(family=socket.AF_INET, address="192.168.1.10")
            snic_v6 = Mock(family=socket.AF_INET6, address="fe80::1")
            
            mock.net_if_addrs.return_value = {
                "en0": [snic_v4, snic_v6],
                "lo0": [Mock(family=socket.AF_INET, address="127.0.0.1")]
            }
            yield mock

    @pytest.fixture
    def mock_zeroconf(self):
        with patch('ship.mdns_announce.AsyncZeroconf') as mock:
            mock_instance = MagicMock()
            
            # The code in mdns_announce.py awaits the result of the register/unregister calls.
            # tasks = [self.aiozc.async_register_service(self.mdsn_info)]
            # background_tasks = await asyncio.gather(*tasks)  <-- awaits the call, gets result
            # await asyncio.gather(*background_tasks)          <-- awaits the result
            # Therefore, the async method must return an awaitable.

            async def async_inner_task():
                return None

            async def async_outer_result(*args, **kwargs):
                return async_inner_task()
                
            # Assign side_effect to return the coroutine (outer) which returns awaitable (inner)
            mock_instance.async_register_service = MagicMock(side_effect=async_outer_result)
            mock_instance.async_unregister_service = MagicMock(side_effect=async_outer_result)
            
            # async_close seems to serve only one await: await self.aiozc.async_close()
            # So straightforward async_noop is fine for close if it's awaited directly.
            # Check code: await self.aiozc.async_close() -> YES.
            
            async def async_simple(*args, **kwargs):
                return None
                
            mock_instance.async_close = MagicMock(side_effect=async_simple)
            
            mock.return_value = mock_instance
            yield mock_instance

    def test_ship_11_2_mdns_properties(self, mock_x509_load, mock_psutil, mock_zeroconf):
        """
        Req: SHIP-11.2 (TXT Record Attributes)
        """
        device_id = "TestDevice123"
        
        service = MdnsAnnounceService(
            device_id=device_id,
            tls_cert=b"fake_cert_data",
            device_brand="TestBrand",
            device_type="TestType",
            device_model="TestModel"
        )
        
        info = service.mdsn_info
        
        # Verify attributes on the MockServiceInfo object
        # Note: MockServiceInfo stores properties exactly as passed.
        # MdnsAnnounceService passes them as strings.
        assert info.type == "_ship._tcp.local."
        assert info.name == f"{device_id}._ship._tcp.local."
        assert info.port == 47051
        
        assert info.properties['txtvers'] == '1'
        assert info.properties['id'] == device_id
        assert info.properties['path'] == '/ship/'
        assert info.properties['ski'] == 'fake_ski_hash'
        assert info.properties['register'] == 'true'
        assert info.properties['brand'] == 'TestBrand'
        assert info.properties['model'] == 'TestModel'
        assert info.properties['type'] == 'TestType'

    def test_register_services(self, mock_x509_load, mock_psutil, mock_zeroconf):
        """
        Verify start() calls async_register_service.
        """
        service = MdnsAnnounceService(
            device_id="TestDevice123",
            tls_cert=b"fake_cert_data"
        )
        
        service.start()
        
        mock_zeroconf.async_register_service.assert_called_once()
        args, _ = mock_zeroconf.async_register_service.call_args
        assert args[0] == service.mdsn_info

    def test_unregister_services(self, mock_x509_load, mock_psutil, mock_zeroconf):
        """
        Verify stop() calls async_unregister_service and async_close.
        """
        service = MdnsAnnounceService(
            device_id="TestDevice123",
            tls_cert=b"fake_cert_data"
        )
        
        service.stop()
        
        mock_zeroconf.async_unregister_service.assert_called_once()
        mock_zeroconf.async_close.assert_called_once()

    def test_ip_filtering(self, mock_x509_load, mock_psutil, mock_zeroconf):
        """
        Verify that IP address filtering logic passes correct list to ServiceInfo.
        """
        # Mock psutil to return specific interfaces
        nic = MagicMock(address="192.168.1.50", family=socket.AF_INET)
        nic_v6 = MagicMock(address="fe80::1", family=socket.AF_INET6)
        
        mock_psutil.net_if_addrs.return_value = {
            "en0": [nic, nic_v6]
        }
        
        # Case 1: IPv4
        service = MdnsAnnounceService(
            device_id="V4Device",
            tls_cert=b"fake_cert_data",
            ip_version=IPVersion.V4Only
        )
        ips = service.mdsn_info.parsed_addresses()
        assert "192.168.1.50" in ips
        assert "fe80::1" not in ips # Should be filtered out
        
        # Case 2: IPv6
        # Need new service instance
        service_v6 = MdnsAnnounceService(
            device_id="V6Device",
            tls_cert=b"fake_cert_data",
            ip_version=IPVersion.V6Only
        )
        ips_v6 = service_v6.mdsn_info.parsed_addresses()
        assert "fe80::1" in ips_v6
        assert "192.168.1.50" not in ips_v6
