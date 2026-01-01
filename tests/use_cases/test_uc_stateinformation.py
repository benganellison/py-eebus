from spine.base_type.stateinformation import (
    StateInformationDataType,
    StateInformationListDataType
)
from spine.simple_type.stateinformation import stateInformationIdType
from spine.union_type.stateinformation import StateInformationType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_state_information_data_type():
    """
    Test creation of StateInformationDataType and integration with PayloadContributionGroup.
    """
    state_data = StateInformationDataType(
        state_information_id=stateInformationIdType(value=1),
        state_information=StateInformationType(value="ok"),
        is_active=True
    )
    
    # Verify standard attribute access
    assert state_data.state_information_id.value == 1
    assert state_data.state_information.value == "ok"
    assert state_data.is_active is True

    # Wrapper
    state_list = StateInformationListDataType(
        state_information_data=[state_data]
    )
    
    # Payload Integration
    payload = PayloadContributionGroup(
        state_information_list_data=state_list
    )
    
    assert payload.state_information_list_data is not None
    assert len(payload.state_information_list_data.state_information_data) == 1
    assert payload.state_information_list_data.state_information_data[0].state_information_id.value == 1
