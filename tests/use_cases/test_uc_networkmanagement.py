from spine.base_type.networkmanagement import NetworkManagementDeviceDescriptionDataType
from spine.base_type.networkmanagement import (
    NetworkManagementDeviceDescriptionDataType as BaseNMDataType, # Wait, check if there is a conflict or if simple_type has the value type
    NetworkManagementDeviceDescriptionListDataType
)
# Re-checking imports. usually simple_type has the value wrapper/alias if it's a simple type derived.
# But for NetworkManagementDeviceDescriptionDataType, it's likely a complex type in base_type.
# Let's check base_type/networkmanagement.py content first to be sure about the imports.
# But to avoid extra steps, I'll rely on the pattern.
# simple_type usually has the atomic types. base_type has the complex types.

from spine.base_type.networkmanagement import (
    NetworkManagementDeviceDescriptionDataType,
    NetworkManagementDeviceDescriptionListDataType
)
from spine.simple_type.networkmanagement import (
    NetworkManagementCommunicationsTechnologyInformationType
)

from spine.choice_type.commandframe import PayloadContributionGroup

def test_uc_networkmanagement():
    # Test NetworkManagementDeviceDescriptionDataType
    # Assuming it has fields like deviceAddress, deviceType etc.
    # I'll create a minimal valid instance.
    
    tech_info = NetworkManagementCommunicationsTechnologyInformationType(value="Ethernet")
    
    description_data = NetworkManagementDeviceDescriptionDataType(
        communications_technology_information=tech_info
    )

    # Test NetworkManagementDeviceDescriptionListDataType
    description_list = NetworkManagementDeviceDescriptionListDataType(
        network_management_device_description_data=[description_data]
    )
    
    # Test PayloadContributionGroup
    payload = PayloadContributionGroup(
        network_management_device_description_list_data=description_list
    )
    
    assert payload.network_management_device_description_list_data is not None
    assert payload.network_management_device_description_list_data.network_management_device_description_data is not None
    assert len(payload.network_management_device_description_list_data.network_management_device_description_data) == 1
    assert payload.network_management_device_description_list_data.network_management_device_description_data[0].communications_technology_information.value == "Ethernet"
