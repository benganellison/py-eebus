import pytest
from unittest.mock import MagicMock
from ship.state_protocol import HandleProtocol, ProtocolState
from ship.connection import MessageProtocolHandshake, ProtocolHandshakeTypeType

class TestShipStateProtocol:
    
    @pytest.fixture
    def handle_protocol(self, mock_connection):
        return HandleProtocol(mock_connection)

    def test_initial_state(self, handle_protocol):
        """Verify initial state is CLIENT_INIT"""
        assert handle_protocol.proto_state == ProtocolState.SME_PROT_H_STATE_CLIENT_INIT

    def test_client_init_sends_announcemax(self, handle_protocol, mock_connection):
        """
        Verify that in CLIENT_INIT, we send ANNOUNCEMAX and transition to LISTEN_CHOICE.
        """
        # Execute handler for INIT state
        result = handle_protocol.handle_state_sme_prot_h_state_client_init()
        
        # Should return False (not done yet)
        assert result is False
        
        # Should have transitioned to LISTEN_CHOICE
        assert handle_protocol.proto_state == ProtocolState.SME_PROT_H_STATE_CLIENT_LISTEN_CHOICE
        
        # Should have sent ANNOUNCEMAX
        mock_connection.send_message.assert_called_once()
        args, _ = mock_connection.send_message.call_args
        sent_msg = args[0]
        assert isinstance(sent_msg, MessageProtocolHandshake)
        assert sent_msg.msg().handshake_type == ProtocolHandshakeTypeType.ANNOUNCEMAX

    def test_client_listen_choice_success(self, handle_protocol, mock_connection):
        """
        Verify that receiving SELECT in LISTEN_CHOICE transitions to OK.
        """
        # Setup state
        handle_protocol.set_proto_state(ProtocolState.SME_PROT_H_STATE_CLIENT_LISTEN_CHOICE)
        
        # Mock incoming SELECT message
        incoming_msg = MagicMock(spec=MessageProtocolHandshake)
        incoming_msg.msg.return_value.handshake_type = ProtocolHandshakeTypeType.SELECT
        
        # Execute handler
        result = handle_protocol.handle_state(incoming_msg)
        
        # Should return True (handshake complete)
        assert result is True
        
        # Should have transitioned to OK
        assert handle_protocol.proto_state == ProtocolState.SME_PROT_H_STATE_CLIENT_OK
        
        # Should have echoed the message back
        mock_connection.send_message.assert_called_once_with(incoming_msg)

    def test_client_listen_choice_invalid_type(self, handle_protocol, mock_connection):
        """
        Verify that receiving wrong handshake type triggers close.
        """
        # Setup state
        handle_protocol.set_proto_state(ProtocolState.SME_PROT_H_STATE_CLIENT_LISTEN_CHOICE)
        
        # Mock incoming ANNOUNCEMAX message (invalid at this stage)
        incoming_msg = MagicMock(spec=MessageProtocolHandshake)
        incoming_msg.msg.return_value.handshake_type = ProtocolHandshakeTypeType.ANNOUNCEMAX
        
        # Execute handler
        result = handle_protocol.handle_state(incoming_msg)
        
        # Should return False (failed)
        assert result is False
        
        # Connection should be closed
        mock_connection.close.assert_called_once()

