import pytest
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType

from spine.base_type.loadcontrol import (
    LoadControlLimitConstraintsListDataType,
    LoadControlLimitConstraintsDataType
)
from spine.simple_type.loadcontrol import LoadControlLimitIdType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import NumberType, ScaleType

def test_lpc_constraints_construction():
    """
    Scenario 4: Constraints.
    Verify we can construct a LoadControlLimitConstraintsDataType.
    """
    # 0.1A to 100A, Step 0.1A (Scale -1)
    constraints = LoadControlLimitConstraintsDataType(
        limit_id=LoadControlLimitIdType(value=1),
        value_range_min=ScaledNumberType(
            number=NumberType(value=1),
            scale=ScaleType(value=-1)
        ),
        value_range_max=ScaledNumberType(
            number=NumberType(value=1000),
            scale=ScaleType(value=-1)
        ),
        value_step_size=ScaledNumberType(
            number=NumberType(value=1),
            scale=ScaleType(value=-1)
        )
    )

    assert constraints.limit_id.value == 1
    assert constraints.value_range_min.number.value == 1
    assert constraints.value_range_max.number.value == 1000

    # Wrap in List
    constraints_list = LoadControlLimitConstraintsListDataType(
        load_control_limit_constraints_data=[constraints]
    )

    # Wrap in Datagram
    cmd = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            load_control_limit_constraints_list_data=constraints_list
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

    # Verify serialization structure
    msg = SpineMessage(datagram)
    import json
    json_output = json.loads(msg.get_data())
    
    payload = json_output["datagram"]["payload"]["cmd"][0]
    
    # Correct path including PayloadContributionGroup wrapper
    constraints_json_list = payload["payload_contribution_group"]["loadControlLimitConstraintsListData"]
    
    item = constraints_json_list["loadControlLimitConstraintsData"][0]
    assert item["limitId"] == 1
    assert item["valueRangeMin"]["number"] == 1
    assert item["valueRangeMax"]["number"] == 1000
