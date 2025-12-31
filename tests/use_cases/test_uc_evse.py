import pytest
import json
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType

from spine.base_type.operatingconstraints import (
    OperatingConstraintsPowerRangeDataType,
    OperatingConstraintsPowerRangeListDataType,
    OperatingConstraintsDurationDataType,
    OperatingConstraintsDurationListDataType
)
from spine.simple_type.powersequences import PowerSequenceIdType
from spine.simple_type.commondatatypes import NumberType, ScaleType
from spine.base_type.commondatatypes import ScaledNumberType

def test_evse_constraints_structure():
    """
    EVSE Test: Verify construction of Operating Constraints.
    Scenario: EVSE defines a power range (Min: 0W, Max: 11000W) for a sequence.
    """
    
    # 1. Power Range (0W - 11kW)
    power_range = OperatingConstraintsPowerRangeDataType(
        sequence_id=PowerSequenceIdType(value=1),
        power_min=ScaledNumberType(
            number=NumberType(value=0),
            scale=ScaleType(value=0)
        ),
        power_max=ScaledNumberType(
            number=NumberType(value=11000),
            scale=ScaleType(value=0)
        )
    )
    
    power_range_list = OperatingConstraintsPowerRangeListDataType(
        operating_constraints_power_range_data=[power_range]
    )
    
    # 2. Duration Constraint (Max 4 hours)
    # Using simple strings for xs:duration as per previous experience with basic types
    duration = OperatingConstraintsDurationDataType(
        sequence_id=PowerSequenceIdType(value=1),
        active_duration_max="PT4H"
    )
    
    duration_list = OperatingConstraintsDurationListDataType(
        operating_constraints_duration_data=[duration]
    )
    
    # 3. Construct Payload
    cmd_power = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            operating_constraints_power_range_list_data=power_range_list
        )
    )
    
    cmd_duration = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            operating_constraints_duration_list_data=duration_list
        )
    )
    
    datagram = DatagramType(
        header=HeaderType(
            msg_counter=MsgCounterType(value=1),
            msg_counter_reference=None,
            cmd_classifier=None
        ),
        payload=PayloadType(
            cmd=[cmd_power, cmd_duration]
        )
    )
    
    # 4. Serialization
    msg = SpineMessage(datagram)
    json_str = msg.get_data()
    data = json.loads(json_str)
    
    # Verify Power Range
    payload_cmds = data["datagram"]["payload"]["cmd"]
    power_payload = payload_cmds[0]["payload_contribution_group"]["operatingConstraintsPowerRangeListData"]["operatingConstraintsPowerRangeData"][0]
    assert power_payload["sequenceId"] == 1
    assert power_payload["powerMax"]["number"] == 11000
    
    # Verify Duration
    duration_payload = payload_cmds[1]["payload_contribution_group"]["operatingConstraintsDurationListData"]["operatingConstraintsDurationData"][0]
    assert duration_payload["sequenceId"] == 1
    assert duration_payload["activeDurationMax"] == "PT4H"
