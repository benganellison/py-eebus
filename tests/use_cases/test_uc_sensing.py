from spine.union_type.sensing import SensingTypeType, SensingStateType
from spine.base_type.sensing import SensingDataType, SensingDescriptionDataType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_uc_sensing():
    # Test Union Types
    s_type = SensingTypeType(value="temperature")
    assert s_type.value == "temperature"
    
    state = SensingStateType(value="active")
    assert state.value == "active"

    # Test SensingDataType (Assuming structure similar to others, but verifying fields)
    # SensingDataType usually contains 'value' (ScaledNumber) and 'timestamp' etc.
    # It might not take 'sensing_type' directly (usually in Description).
    
    # Test SensingDescriptionDataType
    desc = SensingDescriptionDataType(
        sensing_type=s_type
    )
    assert desc.sensing_type.value == "temperature"

    # Test PayloadContributionGroup
    payload = PayloadContributionGroup(
        sensing_description_data=desc
    )
    
    assert payload.sensing_description_data is not None
    assert payload.sensing_description_data.sensing_type.value == "temperature"
