import sys
import pytest
from unittest.mock import MagicMock, patch

# Mock 'rel' module before importing ship.connection
sys.modules['rel'] = MagicMock()
sys.modules['websocket'] = MagicMock()
sys.modules['cryptography'] = MagicMock()
sys.modules['cryptography.x509'] = MagicMock()
# Create robust mocks for zeroconf classes to allow inheritance and instantiation
mock_zeroconf_module = MagicMock()

class MockServiceListener:
    pass

class MockServiceInfo:
    def __init__(self, type_, name, **kwargs):
        self.type = type_
        self.name = name
        self.port = kwargs.get('port', 0)
        self.properties = kwargs.get('properties', {})
        self.parsed_addresses_arg = kwargs.get('parsed_addresses', [])
        # Provide method expected by consumers if any, or just property
        self.parsed_addresses = lambda: self.parsed_addresses_arg
        self.parsed_scoped_addresses = lambda: []

class MockZeroconf:
    def __init__(self, *args, **kwargs):
        pass
    def get_service_info(self, type_, name):
        return None
    def close(self):
        pass

class MockServiceBrowser:
    def __init__(self, zc, type_, listener):
        pass
    def cancel(self):
        pass

# Assign these classes to the mock module
mock_zeroconf_module.ServiceListener = MockServiceListener
mock_zeroconf_module.ServiceInfo = MockServiceInfo
mock_zeroconf_module.Zeroconf = MockZeroconf
mock_zeroconf_module.ServiceBrowser = MockServiceBrowser
mock_zeroconf_module.IPVersion = MagicMock()
mock_zeroconf_module.IPVersion.V4Only = 1
mock_zeroconf_module.IPVersion.V6Only = 2
mock_zeroconf_module.IPVersion.All = 3

sys.modules['zeroconf'] = mock_zeroconf_module
sys.modules['zeroconf.asyncio'] = MagicMock()
sys.modules['cryptography.hazmat'] = MagicMock()
sys.modules['cryptography.hazmat.backends'] = MagicMock()
sys.modules['cryptography.hazmat.primitives'] = MagicMock()
sys.modules['cryptography.hazmat.primitives.asymmetric'] = MagicMock()
sys.modules['psutil'] = MagicMock()

from ship.connection import ShipConnection
from ship.timer import ShipTimer

@pytest.fixture
def mock_socket():
    return MagicMock()

@pytest.fixture
def mock_connection(mock_socket):
    """
    Creates a ShipConnection object with mocked dependencies.
    """
    # We need to mock the arguments required for ShipConnection __init__
    mock_local_device = MagicMock()
    mock_remote_device = MagicMock()
    
    # We shouldn't actually instantiate ShipConnection if it does complex setup in __init__
    # But let's try to mock what we can.
    # Alternatively, we can use MagicMock(spec=ShipConnection) if we don't need real logic
    # But for state machine tests, we might want the real object but with mocked IO.
    
    # Let's try to patch __init__ if it's too complex.
    # Looking at ShipConnection.__init__, it does quite a bit of setup.
    
    # Let's mock the complex parts using patch context or just mock arguments.
    with patch('ship.connection.ShipTimer'), \
         patch('ship.connection.HandleCMI'), \
         patch('ship.connection.HandleHello'), \
         patch('ship.connection.HandleProtocol'), \
         patch('ship.connection.HandlePin'), \
         patch('ship.connection.HandleAccessMethods'):
         
        conn = ShipConnection(
            local_device=mock_local_device,
            remote_device=mock_remote_device,
            client_cert="cert.pem",
            client_key="key.pem"
        )
    
    conn.ws = MagicMock()  # Mock websocket object
    conn.send_message = MagicMock() # Mock send_message to avoid websocket calls
    conn.close = MagicMock() # Mock close method
    
    return conn
