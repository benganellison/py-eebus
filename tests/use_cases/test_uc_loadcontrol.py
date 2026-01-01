from spine.simple_type.loadcontrol import LoadControlLimitIdType
from spine.union_type.loadcontrol import LoadControlCategoryType
from spine.base_type.loadcontrol import LoadControlLimitDescriptionDataType, LoadControlLimitDescriptionListDataType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_uc_loadcontrol():
    # Test LoadControlLimitIdType
    limit_id = LoadControlLimitIdType(value=1)
    assert limit_id.value == 1

    # Test LoadControlCategoryType
    category = LoadControlCategoryType(value="recommendation")
    assert category.value == "recommendation"

    # Test LoadControlLimitDescriptionDataType
    desc = LoadControlLimitDescriptionDataType(
        limit_id=limit_id,
        limit_category=category
    )
    assert desc.limit_id.value == 1
    assert desc.limit_category.value == "recommendation"

    # Test LoadControlLimitDescriptionListDataType
    desc_list = LoadControlLimitDescriptionListDataType(
        load_control_limit_description_data=[desc]
    )

    # Test PayloadContributionGroup
    payload = PayloadContributionGroup(
        load_control_limit_description_list_data=desc_list
    )
    
    assert payload.load_control_limit_description_list_data is not None
    assert payload.load_control_limit_description_list_data.load_control_limit_description_data[0].limit_category.value == "recommendation"
