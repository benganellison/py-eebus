import pytest
from spine.base_type.bill import (
    BillListDataType,
    BillDataType,
    BillDescriptionDataType,
    BillConstraintsDataType
)
from spine.base_type.commondatatypes import (
    ScaledNumberType
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType
)
from spine.union_type.commondatatypes import (
    UnitOfMeasurementType,
    CurrencyType
)
from spine.union_type.bill import (
    BillTypeType,
    BillCostTypeType,
    BillPositionTypeType
)
from spine.enums.bill import (
    BillTypeEnumType,
    BillCostTypeEnumType,
    BillPositionTypeEnumType,
    BillTypeEnumType
)
from spine.base_type.bill import (
    Anonymous_4495210448, # For Total
    Anonymous_4495211504  # For Position
)
from spine.simple_type.bill import (
    BillPositionCountType,
    BillPositionIdType
)

# EVCS Use Case Tests
# EV Charging Summary

@pytest.mark.requirement("EVCS-001")
def test_evcs_total_cost():
    """
    Verify total cost validation.
    Ref: [EVCS-001]
    Table 8: total.cost
    """
    # Flattened structure: cost, cost_type, currency are siblings in Anonymous_4495210448
    
    cost_val = ScaledNumberType(number=NumberType(value=1550), scale=ScaleType(value=-2)) # 15.50
    
    total_item = Anonymous_4495210448(
        cost=cost_val,
        cost_type=BillCostTypeType(value=BillCostTypeEnumType.absolutePrice),
        currency=CurrencyType(value="EUR")
    )
    
    assert total_item.cost.number.value == 1550
    assert total_item.cost_type.value == "absolutePrice"
    assert total_item.currency.value == "EUR"

@pytest.mark.requirement("EVCS-002")
def test_evcs_total_energy_amount():
    """
    Verify total energy amount (EVCS-002).
    Table 8: total.value
    """
    # Flattened structure: value, unit are siblings
    
    val = ScaledNumberType(number=NumberType(value=5000), scale=ScaleType(value=0)) # 5000 Wh
    
    total_item = Anonymous_4495210448(
        value=val,
        unit=UnitOfMeasurementType(value="Wh")
    )
    
    assert total_item.value.number.value == 5000
    assert total_item.unit.value == "Wh"

@pytest.mark.requirement("EVCS-003")
def test_evcs_self_produced_cost():
    """
    Verify self-produced energy cost (EVCS-003).
    Table 8: position(type=selfProduced...).costPercentage
    """
    # Flattened structure in Anonymous_4495211504
    
    cost_pct = ScaledNumberType(number=NumberType(value=40), scale=ScaleType(value=0)) # 40%
    
    pos_item = Anonymous_4495211504(
        position_type=BillPositionTypeType(value=BillPositionTypeEnumType.selfProducedElectricEnergy),
        cost_percentage=cost_pct
    )
    
    assert pos_item.position_type.value == "selfProducedElectricEnergy"
    assert pos_item.cost_percentage.number.value == 40

@pytest.mark.requirement("EVCS-004")
def test_evcs_self_produced_energy():
    """
    Verify self-produced energy amount (EVCS-004).
    Table 8: position(type=selfProduced...).valuePercentage
    """
    val_pct = ScaledNumberType(number=NumberType(value=40), scale=ScaleType(value=0))
    
    pos_item = Anonymous_4495211504(
        position_type=BillPositionTypeType(value=BillPositionTypeEnumType.selfProducedElectricEnergy),
        value_percentage=val_pct
    )
    
    assert pos_item.position_type.value == "selfProducedElectricEnergy"
    assert pos_item.value_percentage.number.value == 40

@pytest.mark.requirement("EVCS-005")
def test_evcs_grid_cost():
    """
    Verify grid energy cost (EVCS-005).
    Table 8: position(type=grid...).costPercentage
    """
    cost_pct = ScaledNumberType(number=NumberType(value=60), scale=ScaleType(value=0))
    
    pos_item = Anonymous_4495211504(
        position_type=BillPositionTypeType(value=BillPositionTypeEnumType.gridElectricEnergy),
        cost_percentage=cost_pct
    )
    
    assert pos_item.position_type.value == "gridElectricEnergy"
    assert pos_item.cost_percentage.number.value == 60

@pytest.mark.requirement("EVCS-006")
def test_evcs_grid_energy():
    """
    Verify grid energy amount (EVCS-006).
    Table 8: position(type=grid...).valuePercentage
    """
    val_pct = ScaledNumberType(number=NumberType(value=60), scale=ScaleType(value=0))
    
    pos_item = Anonymous_4495211504(
        position_type=BillPositionTypeType(value=BillPositionTypeEnumType.gridElectricEnergy),
        value_percentage=val_pct
    )
    
    assert pos_item.position_type.value == "gridElectricEnergy"
    assert pos_item.value_percentage.number.value == 60

@pytest.mark.requirement("EVCS-009")
def test_evcs_update_required():
    """
    Verify updateRequired mechanism (EVCS-009).
    Table 6: BillDescriptionListData.updateRequired
    """
    desc = BillDescriptionDataType(
        update_required=True,
        supported_bill_type=[BillTypeType(value=BillTypeEnumType.chargingSummary)]
    )
    assert desc.update_required is True
    assert desc.supported_bill_type[0].value == "chargingSummary"

@pytest.mark.requirement("Structure")
def test_evcs_constraints_structure():
    """
    Verify BillConstraints structure.
    Table 7: positionCountMax >= 2
    """
    
    const = BillConstraintsDataType(
        position_count_max=BillPositionCountType(value=BillPositionIdType(value=2))
    )
    assert const.position_count_max.value.value >= 2
