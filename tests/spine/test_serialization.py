import json
import pytest
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType
from spine.simple_type.commandframe import MsgCounterType

def test_spine_message_roundtrip():
    """
    Test that we can create a SpineMessage, serialize it to JSON/bytes,
    and then deserialize it back to an equivalent object.
    covers: SpineMessage.from_data, SpineMessage.get_data, and deserialization paths in Base
    """
    # 1. Create a simple valid SpineMessage
    # Using HeaderType as a simple component
    header = HeaderType(
        msg_counter=MsgCounterType(value=123)
    )
    datagram = DatagramType(header=header)
    original_msg = SpineMessage(datagram=datagram)

    # 2. Serialize
    msg_bytes = original_msg.get_msg_bytes()
    assert isinstance(msg_bytes, bytes)
    
    # 3. Deserialize
    new_msg = SpineMessage.from_data(msg_bytes)
    
    # 4. Verify content
    # Access the inner datagram
    assert new_msg.msg() is not None
    assert new_msg.msg().header is not None
    assert new_msg.msg().header.msg_counter.value == 123
    
    # Verify str() representation (covers __str__)
    msg_str = str(new_msg)
    assert "SpineMessage" in msg_str
    assert "123" in str(new_msg.msg())


def test_spine_base_str_representation():
    """
    Test __str__ implementation for various types (Value, NoAttrib, Complex)
    covers: SpineBase.__str__ paths
    """
    # Value Type
    counter = MsgCounterType(value=42)
    assert str(counter) == "value: 42"

    # Complex Type
    header = HeaderType(msg_counter=counter)
    # The str representation usually joins fields: "xml_name: value"
    header_str = str(header)
    assert "msgCounter: value: 42" in header_str


def test_deserialization_invalid_input():
    """
    Test handling of invalid input in deserialization.
    """
    # 1. Malformed JSON
    with pytest.raises(json.JSONDecodeError):
        SpineMessage.from_data(b"{invalid_json")

    # 2. Valid JSON but wrong root tag (not 'datagram')
    # Currently code might crash or raise KeyError depending on implementation
    # ROOT_TAG_2_TYPE only has 'datagram'
    with pytest.raises(KeyError):
        SpineMessage.from_data(b'{"wrong_root": {}}')
