from spine.simple_type.bindingmanagement import BindingIdType
from spine.base_type.bindingmanagement import (
    BindingManagementEntryDataType,
    BindingManagementEntryListDataType
)
from spine.choice_type.commandframe import PayloadContributionGroup


def test_uc_bindingmanagement():
    # Test BindingManagementEntryDataType
    binding_id = BindingIdType(value=123)
    entry_data = BindingManagementEntryDataType(
        binding_id=binding_id
    )

    # Test BindingManagementEntryListDataType
    entry_list = BindingManagementEntryListDataType(
        binding_management_entry_data=[entry_data]
    )
    
    # Test PayloadContributionGroup
    # msg_counter = MessageCounterType(1)
    # Check if we can put it into PayloadContributionGroup
    payload = PayloadContributionGroup(
        binding_management_entry_list_data=entry_list
    )
    
    assert payload.binding_management_entry_list_data is not None
    assert payload.binding_management_entry_list_data.binding_management_entry_data is not None
    assert len(payload.binding_management_entry_list_data.binding_management_entry_data) == 1
    assert payload.binding_management_entry_list_data.binding_management_entry_data[0].binding_id.value == 123
