from spine.base_type.threshold import (
    ThresholdDataType,
    ThresholdListDataType,
    ThresholdDescriptionDataType,
    ThresholdDescriptionListDataType
)
from spine.simple_type.threshold import ThresholdIdType
from spine.union_type.threshold import ThresholdTypeType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_threshold_data_type():
    """
    Test creation of ThresholdDataType and integration with PayloadContributionGroup.
    """
    threshold_data = ThresholdDataType(
        threshold_id=ThresholdIdType(value=1)
        # threshold_value is optional ScaledNumberType
    )
    
    assert threshold_data.threshold_id.value == 1

    # Wrapper
    threshold_list = ThresholdListDataType(
        threshold_data=[threshold_data]
    )
    
    # Payload Integration
    payload = PayloadContributionGroup(
        threshold_list_data=threshold_list
    )
    
    val = payload.threshold_list_data
    assert val is not None
    assert len(val.threshold_data) == 1
    assert val.threshold_data[0].threshold_id.value == 1

def test_threshold_description_data_type():
    """
    Test creation of ThresholdDescriptionDataType.
    """
    desc_data = ThresholdDescriptionDataType(
        threshold_id=ThresholdIdType(value=1),
        threshold_type=ThresholdTypeType(value="absolute")
    )
    
    assert desc_data.threshold_id.value == 1
    assert desc_data.threshold_type.value == "absolute"

    # Wrapper
    desc_list = ThresholdDescriptionListDataType(
        threshold_description_data=[desc_data]
    )
    
    # Payload Integration
    payload = PayloadContributionGroup(
        threshold_description_list_data=desc_list
    )
    
    val = payload.threshold_description_list_data
    assert val is not None
    assert len(val.threshold_description_data) == 1
