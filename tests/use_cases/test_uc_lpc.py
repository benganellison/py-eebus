import pytest
from spine.base_message import SpineMessage
from spine.base_type.loadcontrol import (
    LoadControlLimitListDataType, 
    LoadControlLimitDataType
)
from spine.simple_type.loadcontrol import LoadControlLimitIdType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import NumberType, ScaleType
from spine.simple_type.commandframe import MsgCounterType

class TestUCLPC:
    """
    Tests for 'Limitation of Power Consumption' Use Case.
    Focuses on message payload construction and validation for Scenario 1.
    """

    def _create_lpc_datagram(self):
        """Helper to create a standard LPC Datagram for testing."""
        limit_data = LoadControlLimitDataType(
            limit_id=LoadControlLimitIdType(value=1),
            is_limit_active=True,
            is_limit_changeable=True,
            value=ScaledNumberType(
                number=NumberType(value=4200),
                scale=ScaleType(value=0)
            )
        )
        
        payload_list = LoadControlLimitListDataType(
            load_control_limit_data=[limit_data]
        )

        from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
        from spine.base_type.commandframe import CmdType
        from spine.choice_type.commandframe import PayloadContributionGroup
        
        cmd = CmdType(
            payload_contribution_group=PayloadContributionGroup(
                load_control_limit_list_data=payload_list
            )
        )
        
        datagram = DatagramType(
            header=HeaderType(
                msg_counter=MsgCounterType(value=1),
                msg_counter_reference=None,
                cmd_classifier=None 
            ),
            payload=PayloadType(
                cmd=[cmd]
            )
        )
        return datagram

    @pytest.mark.requirement("LPC-TS-001")
    def test_lpc_limit_construction(self):
        """
        Verify that we can correctly construct the LPC hierarchy and simple types.
        """
        datagram = self._create_lpc_datagram()
        
        # Verify Header
        assert datagram.header.msg_counter.value == 1
        
        # Verify Payload Structure
        cmd = datagram.payload.cmd[0]
        payload_group = cmd.payload_contribution_group
        assert payload_group.load_control_limit_list_data is not None
        
        # Verify Values
        limit_data = payload_group.load_control_limit_list_data.load_control_limit_data[0]
        assert limit_data.limit_id.value == 1
        assert limit_data.value.number.value == 4200
        assert limit_data.is_limit_active is True

    def test_lpc_serialization_structure(self):
        """
        Verify that the serialised JSON matches the expected schema structure.
        Crucially, checks that objects are serialized as dicts, not lists of dicts.
        """
        datagram = self._create_lpc_datagram()
        msg = SpineMessage(datagram)
        
        import json
        json_str = msg.get_data()
        json_output = json.loads(json_str) 
        
        # Check Top Level
        assert "datagram" in json_output
        datagram_dict = json_output["datagram"]
        
        # Check Header and Payload exist as keys (proving dict serialization)
        assert "header" in datagram_dict
        assert "payload" in datagram_dict
        
        # Check deep nesting
        payload = datagram_dict["payload"]
        assert "cmd" in payload
        assert isinstance(payload["cmd"], list)
        
        cmd_item = payload["cmd"][0]
        assert isinstance(cmd_item, dict)

    def test_lpc_deserialization_roundtrip(self):
        """
        Verify that we can serialize to JSON and deserialize back to a valid Python object
        without losing data.
        """
        datagram = self._create_lpc_datagram()
        msg = SpineMessage(datagram)
        
        import json
        json_output = json.loads(msg.get_data())
        
        from spine.base_type.datagram import DatagramType
        
        recovered_datagram = DatagramType.from_data(json_output["datagram"])
        
        # Verify Key Values Survived
        assert recovered_datagram.header.msg_counter.value == 1
        
        recovered_limit = recovered_datagram.payload.cmd[0].payload_contribution_group.load_control_limit_list_data.load_control_limit_data[0]
        assert recovered_limit.value.number.value == 4200
        assert recovered_limit.limit_id.value == 1

    @pytest.mark.requirement("LPC-TS-011")
    def test_failsafe_limit_structure(self):
        """
        Scenario 2: Failsafe values.
        Verify we can construct a Failsafe Consumption Active Power Limit.
        """
        # Typically uses the same structure but different ID or Context?
        # Spec says "Failsafe Consumption Active Power Limit ([LPC-021])"
        # Often mapped to a specific Limit ID defined in discovery.
        
        limit_data = LoadControlLimitDataType(
            limit_id=LoadControlLimitIdType(value=2), # Assume 2 is failsafe
            is_limit_active=True,
            value=ScaledNumberType(
                number=NumberType(value=0), 
                scale=ScaleType(value=0)
            ) # 0 Watts
        )
        
        assert limit_data.limit_id.value == 2
        assert limit_data.value.number.value == 0

