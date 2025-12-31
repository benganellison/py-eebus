import pytest
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType

from spine.base_type.deviceconfiguration import (
    DeviceConfigurationKeyValueDescriptionListDataType,
    DeviceConfigurationKeyValueDescriptionDataType,
    DeviceConfigurationKeyValueListDataType,
    DeviceConfigurationKeyValueDataType,
    DeviceConfigurationKeyValueValueType
)
from spine.simple_type.deviceconfiguration import (
    DeviceConfigurationKeyIdType
)
from spine.union_type.deviceconfiguration import DeviceConfigurationKeyNameType
from spine.enums.deviceconfiguration import DeviceConfigurationKeyValueTypeType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import NumberType, ScaleType

def test_lpc_failsafe_structure():
    """
    Scenario 2: Failsafe Values.
    Verify we can construct Failsafe Consumption Active Power Limit and Failsafe Duration Minimum.
    Ref: [LPC-021], [LPC-022]
    """
    # 1. Define Descriptions (mapping IDs to Names and Types)
    # ID 0: FailsafeConsumptionActivePowerLimit (ScaledNumber)
    # ID 1: FailsafeDurationMinimum (Duration)
    
    desc_power = DeviceConfigurationKeyValueDescriptionDataType(
        key_id=DeviceConfigurationKeyIdType(value=0),
        key_name=DeviceConfigurationKeyNameType(value="FailsafeConsumptionActivePowerLimit"),
        value_type=DeviceConfigurationKeyValueTypeType(value="scaledNumber")
    )
    
    desc_duration = DeviceConfigurationKeyValueDescriptionDataType(
        key_id=DeviceConfigurationKeyIdType(value=1),
        key_name=DeviceConfigurationKeyNameType(value="FailsafeDurationMinimum"),
        value_type=DeviceConfigurationKeyValueTypeType(value="duration")
    )

    # Wrap Descriptions in List
    desc_list = DeviceConfigurationKeyValueDescriptionListDataType(
        device_configuration_key_value_description_data=[desc_power, desc_duration]
    )

    # 2. Define Values
    # Value for ID 0: 0 Watts (Safe state)
    val_power = DeviceConfigurationKeyValueDataType(
        key_id=DeviceConfigurationKeyIdType(value=0),
        value=DeviceConfigurationKeyValueValueType(
            scaled_number=ScaledNumberType(
                number=NumberType(value=0),
                scale=ScaleType(value=0)
            )
        )
    )

    # Value for ID 1: 2 Hours (PT2H)
    val_duration = DeviceConfigurationKeyValueDataType(
        key_id=DeviceConfigurationKeyIdType(value=1),
        value=DeviceConfigurationKeyValueValueType(
            duration="PT2H"
        )
    )

    # Wrap Values in List
    val_list = DeviceConfigurationKeyValueListDataType(
        device_configuration_key_value_data=[val_power, val_duration]
    )

    # 3. Construct Datagram (simulating a response containing both descriptions and values)
    # Note: In reality these might be separate messages, but checking structure here.
    
    cmd_desc = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            device_configuration_key_value_description_list_data=desc_list
        )
    )
    
    cmd_val = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            device_configuration_key_value_list_data=val_list
        )
    )

    datagram = DatagramType(
        header=HeaderType(
            msg_counter=MsgCounterType(value=1),
            msg_counter_reference=None,
            cmd_classifier=None
        ),
        payload=PayloadType(
            cmd=[cmd_desc, cmd_val]
        )
    )

    # 4. Serialization & Verification
    msg = SpineMessage(datagram)
    import json
    json_output = json.loads(msg.get_data())
    
    payload = json_output["datagram"]["payload"]["cmd"]
    
    # Check Description
    payload_desc = payload[0]["payload_contribution_group"]
    desc_items = payload_desc["deviceConfigurationKeyValueDescriptionListData"]["deviceConfigurationKeyValueDescriptionData"]
    assert desc_items[0]["keyId"] == 0
    assert desc_items[0]["keyName"] == "FailsafeConsumptionActivePowerLimit"
    assert desc_items[0]["valueType"] == "scaledNumber"
    
    # Check Values
    payload_vals = payload[1]["payload_contribution_group"]
    val_items = payload_vals["deviceConfigurationKeyValueListData"]["deviceConfigurationKeyValueData"]
    
    # Power Value
    assert val_items[0]["keyId"] == 0
    assert val_items[0]["value"]["scaledNumber"]["number"] == 0
    
    # Duration Value
    assert val_items[1]["keyId"] == 1
    assert val_items[1]["value"]["duration"] == "PT2H"
