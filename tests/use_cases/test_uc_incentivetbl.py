import pytest
import json
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType

from spine.base_type.incentivetable import (
    IncentiveTableDataType,
    IncentiveTableType,
    Anonymous_4503009584,
    Anonymous_4503010992
)
from spine.simple_type.tariffinformation import TariffIdType
from spine.simple_type.timetable import TimeTableIdType
from spine.simple_type.commondatatypes import DescriptionType

def test_incentive_table_structure():
    """
    Incentive Table Test: Verify construction of IncentiveTableDataType.
    Scenario: Define a simple Incentive Table associated with a Tariff.
    """
    
    # 1. Incentive Table Data
    # IncentiveTableDataType has 'tariff' (Anonymous) and 'incentive_table' (list of IncentiveTableType)
    # IncentiveTableType has 'time_interval' (Anonymous) which holds 'time_table_id'
    
    table_data = IncentiveTableDataType(
        tariff=Anonymous_4503009584(
            tariff_id=TariffIdType(value=1)
        ),
        incentive_table=[
            IncentiveTableType(
                tariff_id=TariffIdType(value=1),
                time_interval=Anonymous_4503010992(
                    time_table_id=TimeTableIdType(value=1)
                )
            )
        ]
    )
    
    # 2. Construct Payload
    cmd = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            incentive_table_data=table_data
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
    
    # 3. Serialization
    msg = SpineMessage(datagram)
    json_str = msg.get_data()
    data = json.loads(json_str)
    
    # Verify Content
    payload = data["datagram"]["payload"]["cmd"][0]["payload_contribution_group"]["incentiveTableData"]
    
    # Verify Tariff relation (in 'tariff' field)
    assert payload["tariff"]["tariffId"] == 1
    
    # Verify Table Series (in 'incentiveTable' field)
    # tariffId is direct on IncentiveTableType
    assert payload["incentiveTable"][0]["tariffId"] == 1
    
    # timeTableId is inside 'timeInterval' anonymous object
    assert payload["incentiveTable"][0]["timeInterval"]["timeTableId"] == 1
