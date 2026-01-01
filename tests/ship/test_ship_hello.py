import pytest
from unittest.mock import MagicMock
from ship.state_hello import HandleHello, HelloState, HelloSubState
from ship.connection import ConnectionHello, ConnectionHelloPhaseType
from ship.timer import ShipTimer

class TestShipStateHello:
    @pytest.fixture
    def handle_hello(self, mock_connection):
        # Initialize HandleHello with partner_known=True for READY state
        return HandleHello(mock_connection, partner_known=True)

    def test_initial_state_ready(self, handle_hello):
        """
        Verify initial state is READY_INIT when partner is known.
        """
        assert handle_hello.hello_state == HelloState.SME_HELLO_STATE_READY
        assert handle_hello.hello_sub_state == HelloSubState.SME_HELLO_STATE_READY_INIT

    def test_handle_state_ready_init(self, handle_hello, mock_connection):
        """
        Verify transition from READY_INIT to READY_LISTEN and sending of Hello Update.
        """
        # handle_state returns False when transitioning within same main state
        result = handle_hello.handle_state_sme_hello_state_ready_init()
        
        assert result is False
        assert handle_hello.hello_sub_state == HelloSubState.SME_HELLO_STATE_READY_LISTEN
        
        # Verify message sent
        mock_connection.send_message.assert_called_once()
        args, _ = mock_connection.send_message.call_args
        sent_msg = args[0]
        assert isinstance(sent_msg, ConnectionHello)
        assert sent_msg.msg().phase == ConnectionHelloPhaseType.READY

    def test_handle_state_ready_listen_success(self, handle_hello, mock_connection):
        """
        Verify handling of valid ConnectionHello (READY) in LISTEN state.
        """
        handle_hello.set_hello_sub_state(HelloSubState.SME_HELLO_STATE_READY_LISTEN)
        
        # Mock incoming message
        incoming_msg = MagicMock(spec=ConnectionHello)
        incoming_msg.msg.return_value.phase = ConnectionHelloPhaseType.READY
        
        # Should return True indicating handshake complete (or phase complete)
        result = handle_hello.handle_state(incoming_msg)
        
        assert result is True
        assert handle_hello.hello_sub_state == HelloSubState.SME_HELLO_STATE_OK

    def test_initial_state_pending(self, mock_connection):
        """
        Req: SHIP-13.4.4.1.3 (Hello Pending)
        Verify that if partner_known is False, state is PENDING.
        """
        handler = HandleHello(mock_connection, partner_known=False)
        assert handler.hello_state == HelloState.SME_HELLO_STATE_PENDING
        assert handler.hello_sub_state == HelloSubState.SME_HELLO_STATE_PENDING_INIT

    def test_handle_state_pending_init_sends_pending(self, mock_connection):
        """
        Req: SHIP-13.4.4.1.3 (Hello Pending)
        Verify that in PENDING_INIT, we send ConnectionHello(phase=PENDING).
        """
        handler = HandleHello(mock_connection, partner_known=False)
        
        # Execute handler
        result = handler.handle_state_sme_hello_state_pending_init()
        
        assert result is False
        assert handler.hello_sub_state == HelloSubState.SME_HELLO_STATE_PENDING_LISTEN
        
        # Verify message sent
        mock_connection.send_message.assert_called_once()
        args, _ = mock_connection.send_message.call_args
        msg = args[0]
        assert isinstance(msg, ConnectionHello)
        
        # Expected behavior: Send PENDING
        assert msg.msg().phase == ConnectionHelloPhaseType.PENDING

    def test_handle_state_pending_listen_success(self, mock_connection):
        """
        Req: SHIP-13.4.4.1.3 (Hello Pending)
        Verify transition to OK when receiving READY.
        """
        handler = HandleHello(mock_connection, partner_known=False)
        handler.set_hello_sub_state(HelloSubState.SME_HELLO_STATE_PENDING_LISTEN)
        
        # Mock incoming READY
        incoming = MagicMock(spec=ConnectionHello)
        incoming.msg.return_value.phase = ConnectionHelloPhaseType.READY
        incoming.msg.return_value.waiting = None
        
        result = handler.handle_state(incoming)
        
        assert result is True
        assert handler.hello_sub_state == HelloSubState.SME_HELLO_STATE_OK

    def test_handle_state_pending_listen_prolongation(self, mock_connection):
        """
        Verify timer updates when receiving READY with waiting time (Prolongation).
        """
        handler = HandleHello(mock_connection, partner_known=False)
        handler.set_hello_sub_state(HelloSubState.SME_HELLO_STATE_PENDING_LISTEN)
        
        # Mock incoming READY with waiting
        incoming = MagicMock(spec=ConnectionHello)
        incoming.msg.return_value.phase = ConnectionHelloPhaseType.READY
        incoming.msg.return_value.waiting = 60000 
        
        # We need to mock inner timers to verify interactions
        handler._timer_wait_for_ready = MagicMock(spec=ShipTimer)
        handler._timer_prolongation_request = MagicMock(spec=ShipTimer)
        handler._timer_prolongation_reply = MagicMock(spec=ShipTimer)
        
        result = handler.handle_state(incoming)
        
        # Stays in loop
        assert result is False
        
        # Verify timers updated
        handler._timer_wait_for_ready.stop.assert_called()
        handler._timer_prolongation_request.start.assert_called()
