from spine.simple_type.supplycondition import ConditionIdType
from spine.union_type.supplycondition import GridConditionType
from spine.base_type.supplycondition import SupplyConditionDescriptionDataType, SupplyConditionDataType, SupplyConditionListDataType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_uc_supplycondition():
    # Test ConditionIdType
    cond_id = ConditionIdType(value=1)
    assert cond_id.value == 1

    # Test Union Types
    grid_cond = GridConditionType(value="ok")
    assert grid_cond.value == "ok"

    # Test SupplyConditionDescriptionDataType
    desc = SupplyConditionDescriptionDataType(
        condition_id=cond_id
    )
    assert desc.condition_id.value == 1

    # Test SupplyConditionDataType
    data = SupplyConditionDataType(
        condition_id=cond_id,
        grid_condition=grid_cond
    )
    assert data.grid_condition.value == "ok"

    # Test SupplyConditionListDataType
    data_list = SupplyConditionListDataType(
        supply_condition_data=[data]
    )

    # Test PayloadContributionGroup
    payload = PayloadContributionGroup(
        supply_condition_list_data=data_list
    )
    
    assert payload.supply_condition_list_data is not None
    assert payload.supply_condition_list_data.supply_condition_data[0].grid_condition.value == "ok"
