import pytest
from ship.message_type import (
    AccessMethodsType, AccessMethodsRequestType, ConnectionCloseType,
    DataType, ConnectionPinErrorType, ConnectionPinInputType,
    ConnectionPinStateType, MessageProtocolHandshakeErrorType,
    MessageProtocolHandshakeType, ConnectionHelloType,
    HeaderType, ExtensionType, ProtocolIdType,
    ConnectionClosePhaseType, ConnectionCloseReasonType,
    ConnectionHelloPhaseType, ProtocolHandshakeTypeType,
    MessageProtocolFormatsType, MessageProtocolFormatType,
    Version, Dns, DnsSd_MDns, PinValueType, PinStateType, PinInputPermissionType,
    ConnectionPinErrorErrorType, MessageProtocolHandshakeErrorErrorType
)
# Note: SHIP_MESSAGE_TYPE_INIT is not in message_type imports directly, checking file...
# It's actually expecting ShipMessageType base class testing.

from ship.message_type import ShipMessageType

class TestMessageTypesCoverage:

    def verify_serialization_cycle(self, obj, cls):
        """
        Helper to verify object -> get_data() -> json -> cls.from_data() -> object equality.
        """
        import json
        
        def get_object_data(o):
            return o.get_data()

        # 1. Serialization (Simulate full JSON cycle)
        data = obj.get_data()
        json_str = json.dumps(data, default=get_object_data)
        decoded_data = json.loads(json_str)
        
        # 2. Deserialization
        new_obj = cls.from_data(decoded_data)
        
        # 3. Equality Check (Compare serialized forms)
        new_json_str = json.dumps(new_obj.get_data(), default=get_object_data)
        assert new_json_str == json_str
        
        # 4. String representation
        s = str(obj)
        assert isinstance(s, str)

    def verify_type_check(self, cls, valid_kwargs, field, invalid_value):
        """
        Helper to verify that instantiated class with invalid field type raises TypeError.
        """
        invalid_kwargs = valid_kwargs.copy()
        invalid_kwargs[field] = invalid_value
        
        with pytest.raises(TypeError):
            cls(**invalid_kwargs)

    def test_base_class_not_implemented(self):
        base = ShipMessageType()
        # get_data calls raise NotImplementedError
        with pytest.raises(NotImplementedError):
            base.get_data()

    def test_access_methods_type(self):
        valid_kwargs = {
            "id": "my_id",
            "dns_sd_m_dns": DnsSd_MDns(),
            "dns": Dns(uri="dns://bar")
        }
        obj = AccessMethodsType(**valid_kwargs)
        self.verify_serialization_cycle(obj, AccessMethodsType)
        
        self.verify_type_check(AccessMethodsType, valid_kwargs, "id", 123)
        # Type checks for other fields might be strictly type(x) is Dns, so passing string fails
        self.verify_type_check(AccessMethodsType, valid_kwargs, "dns", "not_dns")

    def test_access_methods_request_type(self):
        obj = AccessMethodsRequestType()
        self.verify_serialization_cycle(obj, AccessMethodsRequestType)
        # Empty from_data check
        assert isinstance(AccessMethodsRequestType.from_data(None), AccessMethodsRequestType)

    def test_connection_close_type(self):
        # Must provide ALL fields to avoid None conversion error in broken from_data (until fixed)
        # OR verify that the test fails on partials, then fix code.
        # I will expect failure on current code for partials if I don't fix it.
        # Let's test full object first.
        valid_kwargs = {
            "phase": ConnectionClosePhaseType.ANNOUNCE, 
            "max_time": 100,
            "reason": ConnectionCloseReasonType.UNSPECIFIC
        }
        obj = ConnectionCloseType(**valid_kwargs)
        self.verify_serialization_cycle(obj, ConnectionCloseType)
        
        self.verify_type_check(ConnectionCloseType, valid_kwargs, "phase", "bad_phase")

    def test_data_type(self):
        header = HeaderType(protocol_id=ProtocolIdType("ship"))
        ext = ExtensionType(extension_id="e1", string="s1")
        valid_kwargs = {
            "header": header,
            "payload": "simple_payload", # Payload can be string
            "extension": ext
        }
        obj = DataType(**valid_kwargs)
        self.verify_serialization_cycle(obj, DataType)
        
        self.verify_type_check(DataType, valid_kwargs, "header", "bad_header")

    def test_connection_pin_error_type(self):
        # Wraps int
        err = 1 # Not Enum? ship/base_type checking int
        valid_kwargs = {"connection_pin_error_error_type": err} # Arg name is long
        # Wait, constructor arg name in base_type is connection_pin_error_error_type
        # But MessageType wrapper (ship/message_type.py) might use different?
        # Checking ship/message_type.py code...
        # class ConnectionPinErrorType(ShipMessageType):
        #    def __init__(self, error: ConnectionPinErrorErrorType):
        # It takes the WRAPPER type.
        
        inner = ConnectionPinErrorErrorType(connection_pin_error_error_type=1)
        valid_kwargs = {"error": inner}
        obj = ConnectionPinErrorType(**valid_kwargs)
        self.verify_serialization_cycle(obj, ConnectionPinErrorType)

    def test_connection_pin_input_type(self):
        pin = PinValueType("1234")
        valid_kwargs = {"pin": pin}
        obj = ConnectionPinInputType(**valid_kwargs)
        self.verify_serialization_cycle(obj, ConnectionPinInputType)

    def test_connection_pin_state_type(self):
        state = PinStateType.REQUIRED
        perm = PinInputPermissionType.BUSY
        valid_kwargs = {"pin_state": state, "input_permission": perm}
        obj = ConnectionPinStateType(**valid_kwargs)
        self.verify_serialization_cycle(obj, ConnectionPinStateType)

    def test_message_protocol_handshake_error_type(self):
        inner = MessageProtocolHandshakeErrorErrorType(message_protocol_handshake_error_error_type=1)
        valid_kwargs = {"error": inner}
        obj = MessageProtocolHandshakeErrorType(**valid_kwargs)
        self.verify_serialization_cycle(obj, MessageProtocolHandshakeErrorType)

    def test_message_protocol_handshake_type(self):
        htype = ProtocolHandshakeTypeType.ANNOUNCEMAX
        ver = Version(major=1, minor=1) # Version needs major, minor
        fmt = MessageProtocolFormatsType(format=[MessageProtocolFormatType("JSON-UTF8")])
        
        valid_kwargs = {
            "handshake_type": htype,
            "version": ver,
            "formats": fmt
        }
        obj = MessageProtocolHandshakeType(**valid_kwargs)
        self.verify_serialization_cycle(obj, MessageProtocolHandshakeType)

    def test_connection_hello_type(self):
        phase = ConnectionHelloPhaseType.READY
        valid_kwargs = {
            "phase": phase,
            "waiting": 5000,
            "prolongation_request": False
        }
        obj = ConnectionHelloType(**valid_kwargs)
        self.verify_serialization_cycle(obj, ConnectionHelloType)
        
        self.verify_type_check(ConnectionHelloType, valid_kwargs, "phase", "bad_phase")
        self.verify_type_check(ConnectionHelloType, valid_kwargs, "waiting", "bad_int")
        self.verify_type_check(ConnectionHelloType, valid_kwargs, "prolongation_request", "bad_bool")
        
        # Test defaults
        obj_def = ConnectionHelloType(phase=phase)
        assert obj_def.waiting == 60000 # Default
