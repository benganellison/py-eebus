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
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup

class TestUCLPP:
    """
    Tests for 'Limitation of Power Production' Use Case.
    Focuses on message payload construction and validation for Scenario 1.
    """

    def _create_lpp_datagram(self):
        """Helper to create a standard LPP Datagram for testing."""
        limit_data = LoadControlLimitDataType(
            limit_id=LoadControlLimitIdType(value=1),
            is_limit_active=True,
            is_limit_changeable=True,
            value=ScaledNumberType(
                number=NumberType(value=-1000), # Negative for Production
                scale=ScaleType(value=0)
            )
        )
        
        payload_list = LoadControlLimitListDataType(
            load_control_limit_data=[limit_data]
        )
        
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

    @pytest.mark.requirement("LPP-TS-001")
    def test_lpp_limit_construction(self):
        """
        Verify that we can correctly construct the LPP hierarchy and simple types.
        """
        datagram = self._create_lpp_datagram()
        
        # Verify Header
        assert datagram.header.msg_counter.value == 1
        
        # Verify Payload Structure
        cmd = datagram.payload.cmd[0]
        payload_group = cmd.payload_contribution_group
        assert payload_group.load_control_limit_list_data is not None
        
        # Verify Values
        limit_data = payload_group.load_control_limit_list_data.load_control_limit_data[0]
        assert limit_data.limit_id.value == 1
        assert limit_data.value.number.value == -1000 # Verify Negative Value
        assert limit_data.is_limit_active is True

    def test_lpp_serialization_structure(self):
        """
        Verify that the serialised JSON matches the expected schema structure.
        Crucially, checks that objects are serialized as dicts, not lists of dicts.
        """
        datagram = self._create_lpp_datagram()
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
