from spine.simple_type.setpoint import SetpointIdType
from spine.union_type.setpoint import SetpointTypeType
from spine.base_type.setpoint import SetpointDataType, SetpointDescriptionDataType, SetpointDescriptionListDataType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_uc_setpoint():
    # Test SetpointIdType (Simple Type)
    # Check if snake_case is used for internal value or standard initialization
    sp_id = SetpointIdType(value=99)
    assert sp_id.value == 99

    # Test SetpointTypeType (Union Type)
    sp_type = SetpointTypeType(value="temperature")
    assert sp_type.value == "temperature"

    # Test SetpointDescriptionDataType
    desc = SetpointDescriptionDataType(
        setpoint_id=sp_id,
        setpoint_type=sp_type
    )
    assert desc.setpoint_id.value == 99
    assert desc.setpoint_type.value == "temperature"

    # Test SetpointDescriptionListDataType
    desc_list = SetpointDescriptionListDataType(
        setpoint_description_data=[desc]
    )

    # Test PayloadContributionGroup
    payload = PayloadContributionGroup(
        setpoint_description_list_data=desc_list
    )
    
    assert payload.setpoint_description_list_data is not None
    assert payload.setpoint_description_list_data.setpoint_description_data is not None
    assert len(payload.setpoint_description_list_data.setpoint_description_data) == 1
    assert payload.setpoint_description_list_data.setpoint_description_data[0].setpoint_type.value == "temperature"
