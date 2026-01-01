import pytest
from unittest.mock import MagicMock, patch
from ship.connection import ShipConnection, ConState
from ship.device import ShipDevice
from ship.message import ShipMessage, Cmi

class TestShipConnectionState:
    
    @pytest.fixture
    def mock_device(self):
        dev = MagicMock(spec=ShipDevice)
        dev.ip_addresses = ["127.0.0.1"]
        dev.port = 47051
        dev.path = "/ship/"
        dev.ski = "fake_ski"
        return dev

    @pytest.fixture
    def ship_connection(self, mock_device):
        local_dev = mock_device
        remote_dev = mock_device
        return ShipConnection(local_dev, remote_dev, "cert.pem", "key.pem")

    def test_on_message_calls_handle_state(self, ship_connection):
        """
        Verify on_message parses data and calls handle_state.
        """
        bindata = b'\x00' # Cmi message parsed is Cmi
        
        # Mock handle_state
        ship_connection.handle_state = MagicMock()
        
        # Call on_message
        ship_connection.on_message(None, bindata)
        
        ship_connection.handle_state.assert_called_once()
        args, kwargs = ship_connection.handle_state.call_args
        if len(args) > 1:
             assert args[1] == "RECV"
        else:
             assert kwargs['reason'] == "RECV"

    def test_check_server_certificate_success(self, ship_connection):
        """
        Verify _check_server_certificate logic success path.
        """
        # We need to mock ssl context and socket
        with patch('ship.connection.ssl.SSLContext') as mock_ssl_ctx:
             with patch('ship.connection.socket.socket'):
                 with patch('ship.connection.x509.load_pem_x509_certificate') as mock_load_cert:
                     
                     # Setup context mock
                     ctx_instance = mock_ssl_ctx.return_value
                     sock_instance = ctx_instance.wrap_socket.return_value
                     
                     # Setup peer cert return
                     sock_instance.getpeercert.return_value = b"der_data"
                     
                     # Setup loaded cert and extension
                     cert_instance = mock_load_cert.return_value
                     ext_instance = MagicMock()
                     ext_instance.value.digest.hex.return_value = "fake_ski"
                     cert_instance.extensions.get_extension_for_oid.return_value = ext_instance
                     
                     ship_connection._check_server_certificate()
                     
                     # Check connection made
                     sock_instance.connect.assert_called_with(("127.0.0.1", 47051))
                     
                     # Check ski verification passed (no exception)

    def test_check_server_certificate_ski_mismatch(self, ship_connection):
        """
        Verify _check_server_certificate raises RuntimeError on SKI mismatch.
        """
        with patch('ship.connection.ssl.SSLContext') as mock_ssl_ctx:
             with patch('ship.connection.socket.socket'):
                 with patch('ship.connection.x509.load_pem_x509_certificate') as mock_load_cert:
                     
                     ctx_instance = mock_ssl_ctx.return_value
                     sock_instance = ctx_instance.wrap_socket.return_value
                     sock_instance.getpeercert.return_value = b"der_data"
                     
                     cert_instance = mock_load_cert.return_value
                     ext_instance = MagicMock()
                     ext_instance.value.digest.hex.return_value = "wrong_ski" # Mismatch
                     cert_instance.extensions.get_extension_for_oid.return_value = ext_instance
                     
                     with pytest.raises(RuntimeError, match="Ski announced via MDNS does not match"):
                         ship_connection._check_server_certificate()

    def test_on_close(self, ship_connection, capsys):
        """
        Verify on_close logs status.
        """
        ship_connection.on_close(None, 1000, "Normal Close")
        captured = capsys.readouterr()
        assert "closed: 1000 / Normal Close" in captured.out
