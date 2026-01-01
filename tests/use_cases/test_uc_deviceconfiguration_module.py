from spine.base_type.deviceconfiguration import (
    DeviceConfigurationKeyValueDataType,
    DeviceConfigurationKeyValueDescriptionDataType,
    DeviceConfigurationKeyValueListDataType,
    DeviceConfigurationKeyValueDescriptionListDataType
)
from spine.simple_type.deviceconfiguration import DeviceConfigurationKeyIdType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_device_config_key_value_description_data_type():
    """
    Test creation of DeviceConfigurationKeyValueDescriptionDataType.
    """
    dc_desc = DeviceConfigurationKeyValueDescriptionDataType(
        key_id=DeviceConfigurationKeyIdType(value=1)
    )
    assert dc_desc.key_id.value == 1

    # Wrapper
    dc_desc_list = DeviceConfigurationKeyValueDescriptionListDataType(
        device_configuration_key_value_description_data=[dc_desc]
    )
    
    # Payload Integration
    payload = PayloadContributionGroup(
        device_configuration_key_value_description_list_data=dc_desc_list
    )
    
    val = payload.device_configuration_key_value_description_list_data
    assert val is not None
    assert len(val.device_configuration_key_value_description_data) == 1

def test_device_config_key_value_data_type():
    """
    Test creation of DeviceConfigurationKeyValueDataType.
    """
    dc_data = DeviceConfigurationKeyValueDataType(
        key_id=DeviceConfigurationKeyIdType(value=1),
        is_value_changeable=True
    )
    assert dc_data.key_id.value == 1
    assert dc_data.is_value_changeable is True

    # Wrapper
    dc_list = DeviceConfigurationKeyValueListDataType(
        device_configuration_key_value_data=[dc_data]
    )
    
    # Payload Integration
    payload = PayloadContributionGroup(
        device_configuration_key_value_list_data=dc_list
    )
    
    val = payload.device_configuration_key_value_list_data
    assert val is not None
    assert len(val.device_configuration_key_value_data) == 1
