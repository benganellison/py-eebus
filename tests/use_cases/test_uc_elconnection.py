import pytest
import json
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType

from spine.base_type.electricalconnection import (
    ElectricalConnectionDescriptionListDataType,
    ElectricalConnectionDescriptionDataType
)
from spine.simple_type.electricalconnection import ElectricalConnectionIdType
from spine.union_type.electricalconnection import ElectricalConnectionVoltageTypeType

def test_electrical_connection_description_structure():
    """
    Electrical Connection Test: Verify construction of ElectricalConnectionDescriptionListDataType.
    Scenario: Report AC connection details (3-phase, 230V).
    """
    
    # 1. Connection Description
    # Structure:
    # ElectricalConnectionDescriptionListDataType -> list of ElectricalConnectionDescriptionDataType
    
    conn_description = ElectricalConnectionDescriptionDataType(
        electrical_connection_id=ElectricalConnectionIdType(value=1),
        power_supply_type=ElectricalConnectionVoltageTypeType(value="AC"),
        ac_connected_phases=3,
        # acRmsPeriodDuration, positiveEnergyDirection etc. omitted for brevity, checking core fields
    )
    
    conn_list = ElectricalConnectionDescriptionListDataType(
        electrical_connection_description_data=[conn_description]
    )
    
    # 2. Construct Payload
    cmd = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            electrical_connection_description_list_data=conn_list
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
    payload = data["datagram"]["payload"]["cmd"][0]["payload_contribution_group"]["electricalConnectionDescriptionListData"]
    
    item = payload["electricalConnectionDescriptionData"][0]
    assert item["electricalConnectionId"] == 1
    
    # Verify UnionType serialization (patched)
    assert item["powerSupplyType"] == "AC"
    assert item["acConnectedPhases"] == 3
