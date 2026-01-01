import pytest
from unittest.mock import MagicMock, patch
from ship.mdsn_scanner import MdnsScannerService, MdnsServiceListener
from zeroconf import IPVersion, ServiceInfo

class TestMdnsScanner:
    @pytest.fixture
    def mock_zeroconf(self):
        with patch('ship.mdsn_scanner.Zeroconf') as mock:
            yield mock

    @pytest.fixture
    def mock_service_browser(self):
        with patch('ship.mdsn_scanner.ServiceBrowser') as mock:
            yield mock

    def test_listener_update_service(self, mock_zeroconf):
        """
        Verify MdnsServiceListener.update_service calls get_service_info and stores it.
        """
        listener = MdnsServiceListener()
        zc = MagicMock()
        
        # Setup get_service_info return value
        info = MagicMock(spec=ServiceInfo)
        zc.get_service_info.return_value = info
        
        listener.update_service(zc, "_ship._tcp.local.", "device._ship._tcp.local.")
        
        zc.get_service_info.assert_called_with("_ship._tcp.local.", "device._ship._tcp.local.")
        assert listener.get_services()["device._ship._tcp.local."] == info

    def test_listener_remove_service(self, mock_zeroconf):
        """
        Verify MdnsServiceListener.remove_service removes the entry.
        """
        listener = MdnsServiceListener()
        # Add a service first manually
        listener._service_entries["device._ship._tcp.local."] = MagicMock()
        
        zc = MagicMock()
        listener.remove_service(zc, "_ship._tcp.local.", "device._ship._tcp.local.")
        
        assert "device._ship._tcp.local." not in listener.get_services()

    def test_listener_add_service(self, mock_zeroconf):
        """
        Verify MdnsServiceListener.add_service calls get_service_info and stores it.
        """
        listener = MdnsServiceListener()
        zc = MagicMock()
        info = MagicMock(spec=ServiceInfo)
        zc.get_service_info.return_value = info
        
        listener.add_service(zc, "_ship._tcp.local.", "device._ship._tcp.local.")
        
        assert listener.get_services()["device._ship._tcp.local."] == info

    def test_search_devices(self, mock_zeroconf, mock_service_browser):
        """
        Verify search_devices creates browser, waits, isolates devices, and parses info.
        """
        service = MdnsScannerService()
        
        # Mock data
        mock_info = MagicMock()
        mock_info.name = "TestDevice"
        mock_info.port = 47051
        mock_info.properties = {
            b'ski': b'fake_ski',
            b'model': b'TestModel',
            b'type': b'TestType',
            b'id': b'TestId',
            b'path': b'/ship/'
        }
        mock_info.parsed_scoped_addresses.return_value = ["192.168.1.50"]
        
        # Define side effect to populate listener during sleep
        def sleep_side_effect(duration):
            service.listener._service_entries = {"TestDevice": mock_info}
        
        with patch('ship.mdsn_scanner.time.sleep', side_effect=sleep_side_effect) as mock_sleep:
             devices = service.search_devices(duration_sec=1)
             mock_sleep.assert_called_with(1)
        
        # Check browser created
        mock_service_browser.assert_called()
        
        # Check result processing
        assert len(devices) == 1
        dev = devices[0]
        assert dev.ski == "fake_ski"
        assert dev.model == "TestModel"
        assert dev.type == "TestType"
        assert dev.id == "TestId"
        assert dev.path == "/ship/"
        assert "192.168.1.50" in dev.ip_addresses

    def test_search_devices_ip_filter(self, mock_zeroconf, mock_service_browser):
        """
        Verify IP version filtering in search_devices.
        """
        service = MdnsScannerService()
        
        mock_info = MagicMock()
        mock_info.properties = {b'ski': b'', b'model': b'', b'type': b'', b'id': b'', b'path': b''}
        mock_info.parsed_scoped_addresses.return_value = ["192.168.1.50", "fe80::1"]
        
        def sleep_side_effect(duration):
            service.listener._service_entries = {"TestDevice": mock_info}
            
        with patch('ship.mdsn_scanner.time.sleep', side_effect=sleep_side_effect):
            # Test V4Only
            devices_v4 = service.search_devices(ip_version=IPVersion.V4Only)
            
            ips = devices_v4[0].ip_addresses
            assert "192.168.1.50" in ips
            # "fe80::1" (IPv6) should be filtered out when requesting V4Only if ip_address detection works.
            # Using pythons ipaddress module.
            assert "fe80::1" not in ips

            # Test V6Only
            devices_v6 = service.search_devices(ip_version=IPVersion.V6Only)
            ips_v6 = devices_v6[0].ip_addresses
            assert "fe80::1" in ips_v6
            assert "192.168.1.50" not in ips_v6
