from spine.base_type.datagram import DatagramType, PayloadType, HeaderType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType
from spine.base_type.powersequences import (
    PowerSequenceStateDataType,
    PowerSequenceStateListDataType
)
from spine.simple_type.powersequences import PowerSequenceIdType
from spine.union_type.powersequences import PowerSequenceStateType

class TestPowerSequences:
    def test_power_sequence_state_construction(self):
        # Create Power Sequence State Data
        # Tests UnionType PowerSequenceStateType
        
        state_data = PowerSequenceStateDataType(
            sequence_id=PowerSequenceIdType(value=1),
            state=PowerSequenceStateType(value="running") # UnionType test
        )
        
        state_list = PowerSequenceStateListDataType(
            power_sequence_state_data=[state_data]
        )
        
        data = state_list.get_data()
        
        assert len(data["powerSequenceStateData"]) == 1
        assert data["powerSequenceStateData"][0]["sequenceId"] == 1
        assert data["powerSequenceStateData"][0]["state"] == "running"

    def test_power_sequence_full_serialization(self):
        # Verify full message nesting
        
        state_data = PowerSequenceStateDataType(
            sequence_id=PowerSequenceIdType(value=10),
            state=PowerSequenceStateType(value="paused")
        )
        
        state_list = PowerSequenceStateListDataType(
            power_sequence_state_data=[state_data]
        )

        cmd = CmdType(
            payload_contribution_group=PayloadContributionGroup(
                power_sequence_state_list_data=state_list
            )
        )
        
        datagram = DatagramType(
            header=HeaderType(
                msg_counter=MsgCounterType(value=123),
                msg_counter_reference=None,
                cmd_classifier=None
            ),
            payload=PayloadType(cmd=[cmd])
        )
        
        serialized = datagram.get_data()
        
        cmd_data = serialized["payload"]["cmd"][0]
        
        assert "payload_contribution_group" in cmd_data
        group = cmd_data["payload_contribution_group"]
        assert "powerSequenceStateListData" in group
        
        item = group["powerSequenceStateListData"]["powerSequenceStateData"][0]
        assert item["sequenceId"] == 10
        assert item["state"] == "paused"
