import pytest
import json
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType

from spine.base_type.smartenergymanagementps import (
    SmartEnergyManagementPsDataType,
    SmartEnergyManagementPsDataSelectorsType
)
from spine.simple_type.powersequences import PowerSequenceIdType, PowerTimeSlotNumberType
from spine.base_type.commondatatypes import ScaledNumberType

def test_sem_structure():
    """
    SEM Test: Verify construction of SmartEnergyManagementPsDataType.
    This type is huge, so we will test a minimal valid instance.
    """
    # Create a minimal SEM Data object
    # According to XSD/generated code, most fields are optional.
    # We will set a sequence ID to verify basic structure.
    
    # Note: Using dictionaries as mock values for nested complex types if constructor allows, 
    # but strictly we should use the proper types. 
    # For this test, we verify that we can import and instantiate the top-level class.
    
    sem_data = SmartEnergyManagementPsDataType(
        timestamp=None, # Optional
        p_count=None,
        active_power_limit=None 
    )
    
    # Let's try to set the data selectors
    selectors = SmartEnergyManagementPsDataSelectorsType(
        sequence_id=PowerSequenceIdType(value=1)
    )
    
    # Construct Payload
    cmd = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            smart_energy_management_ps_data=sem_data
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
    
    # Serialization Test
    msg = SpineMessage(datagram)
    json_str = msg.get_data()
    data = json.loads(json_str)
    
    # Verify structure exists
    # Note: Since we passed None/Empty, we expect 'smartEnergyManagementPsData': {} 
    # or just the key presence depending on serialization logic for empty fields.
    payload = data["datagram"]["payload"]["cmd"][0]["payload_contribution_group"]
    assert "smartEnergyManagementPsData" in payload
