import pytest
from unittest.mock import MagicMock
from ship.state_pin import HandlePin, PinState, PinSubState
from ship.connection import ConnectionPinState, PinStateType

class TestShipStatePin:
    
    @pytest.fixture
    def handle_pin(self, mock_connection):
        return HandlePin(mock_connection)

    def test_initial_state(self, handle_pin):
        """Verify initial state is ASK_INIT"""
        assert handle_pin.pin_state == PinState.SME_PIN_STATE_ASK
        assert handle_pin.pin_sub_state == PinSubState.SME_PIN_STATE_ASK_INIT

    def test_ask_init_sends_none_pin(self, handle_pin, mock_connection):
        """
        Verify that in ASK_INIT, we send PinState=NONE (skip) and transition to ASK_PROCESS.
        """
        # Execute handler for INIT state
        result = handle_pin.handle_state_sme_pin_state_ask_init()
        
        # Should return False (not done yet)
        assert result is False
        
        # Should have transitioned to ASK_PROCESS
        assert handle_pin.pin_sub_state == PinSubState.SME_PIN_STATE_ASK_PROCESS
        
        # Should have sent ConnectionPinState(NONE)
        mock_connection.send_message.assert_called_once()
        args, _ = mock_connection.send_message.call_args
        sent_msg = args[0]
        assert isinstance(sent_msg, ConnectionPinState)
        assert sent_msg.msg().pin_state == PinStateType.NONE

    def test_ask_process_success(self, handle_pin, mock_connection):
        """
        Verify that receiving PinState=NONE in ASK_PROCESS transitions to OK.
        """
        # Setup state
        handle_pin.set_pin_sub_state(PinSubState.SME_PIN_STATE_ASK_PROCESS)
        
        # Mock incoming ConnectionPinState(NONE) message
        incoming_msg = MagicMock(spec=ConnectionPinState)
        incoming_msg.msg.return_value.pin_state = PinStateType.NONE
        
        # Execute handler
        result = handle_pin.handle_state(incoming_msg)
        
        # Should return True (handshake complete)
        assert result is True
        
        # Should have transitioned to OK
        assert handle_pin.pin_sub_state == PinSubState.SME_PIN_STATE_ASK_OK

    def test_ask_process_invalid_pin_req(self, handle_pin, mock_connection):
        """
        Verify that receiving REQUIRED instead of NONE triggers close (since we don't support PIN yet).
        """
        # Setup state
        handle_pin.set_pin_sub_state(PinSubState.SME_PIN_STATE_ASK_PROCESS)
        
        # Mock incoming ConnectionPinState(REQUIRED) - assuming there's such a state, or just not NONE
        incoming_msg = MagicMock(spec=ConnectionPinState)
        incoming_msg.msg.return_value.pin_state = PinStateType.REQUIRED
        
        # Execute handler
        result = handle_pin.handle_state(incoming_msg)
        
        # Should return False (failed)
        assert result is False
        
        # Connection should be closed
        mock_connection.close.assert_called_once()
