from spine.union_type.directcontrol import DirectControlActivityStateType
from spine.base_type.directcontrol import DirectControlDescriptionDataType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_uc_directcontrol():
    # Test DirectControlActivityStateType
    state = DirectControlActivityStateType(value="active")
    assert state.value == "active"

    # Test PayloadContributionGroup
    # DirectControl doesn't have a simple wrapper class shown in the plan, checking usage...
    # Assuming DirectControlDescriptionDataType exists
    desc = DirectControlDescriptionDataType()
    
    payload = PayloadContributionGroup(
        direct_control_description_data=desc
    )
    
    assert payload.direct_control_description_data is not None
