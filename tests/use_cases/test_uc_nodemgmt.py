import pytest
import json
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType

from spine.base_type.nodemanagement import (
    NodeManagementDetailedDiscoveryDataType,
    NodeManagementDetailedDiscoveryDeviceInformationType,
    Anonymous_4503567168
)
from spine.simple_type.commondatatypes import AddressDeviceType
from spine.union_type.commondatatypes import DeviceTypeType

def test_node_management_discovery_structure():
    """
    Node Management Test: Verify construction of NodeManagementDetailedDiscoveryDataType.
    Scenario: Report device information (Generic).
    """
    
    # 1. Device Information
    # Structure: 
    # device_information -> device_address (Anonymous) -> device (AddressDeviceType)
    
    device_info = NodeManagementDetailedDiscoveryDeviceInformationType(
        device_address=Anonymous_4503567168(
            device=AddressDeviceType(value="d:_i:1234")
        ),
        device_type=DeviceTypeType(value="generic")
    )
    
    # 2. Detailed Discovery Data
    discovery_data = NodeManagementDetailedDiscoveryDataType(
        device_information=device_info
    )
    
    # 3. Construct Payload
    cmd = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            node_management_detailed_discovery_data=discovery_data
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
    
    # 4. Serialization
    msg = SpineMessage(datagram)
    json_str = msg.get_data()
    data = json.loads(json_str)
    
    # Verify Content
    payload = data["datagram"]["payload"]["cmd"][0]["payload_contribution_group"]["nodeManagementDetailedDiscoveryData"]
    
    # Verify Device Address
    assert payload["deviceInformation"]["deviceAddress"]["device"] == "d:_i:1234"
    
    # Verify Device Type
    # Note: UnionType 'DeviceTypeType' might serialize as just string or {"value": ...} depending on fix status
    assert payload["deviceInformation"]["deviceType"] == "generic"
