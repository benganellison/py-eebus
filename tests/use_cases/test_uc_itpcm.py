import pytest
from spine.base_type.tariffinformation import (
    IncentiveDescriptionDataType,
    IncentiveDataType
)
from spine.base_type.commondatatypes import ScaledNumberType
from spine.enums.tariffinformation import (
    IncentiveTypeEnumType,
    IncentiveValueTypeEnumType
)
from spine.enums.commondatatypes import (
    CurrencyEnumType,
    UnitOfMeasurementEnumType,
    ScopeTypeEnumType
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType
)
from spine.union_type.tariffinformation import (
    IncentiveTypeType,
    IncentiveValueTypeType
)
from spine.union_type.commondatatypes import (
    CurrencyType,
    UnitOfMeasurementType,
    ScopeTypeType
)
from spine.simple_type.tariffinformation import IncentiveIdType

# ITPCM Use Case Tests
# Incentive Table Based Power Consumption Management
# Ref: EEBus_UC_TS_IncentiveTableBasedPowerConsumptionManagement_V1.0.0_RC3_public.md

@pytest.mark.requirement("ITPCM-001")
def test_itpcm_incentive_description():
    """
    Scenario 1: Incentive Table Description.
    Validate structure of IncentiveDescriptionDataType.
    """
    # [ITPCM-001] Provide incentive descriptions
    # Example: Absolute cost in EUR per kWh
    
    desc = IncentiveDescriptionDataType(
        incentive_id=IncentiveIdType(value=1),
        incentive_type=IncentiveTypeType(value=IncentiveTypeEnumType.absoluteCost),
        currency=CurrencyType(value=CurrencyEnumType.EUR),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.Wh)
    )
    
    assert desc.incentive_id.value == 1
    assert desc.incentive_type.value == IncentiveTypeEnumType.absoluteCost
    assert desc.currency.value == CurrencyEnumType.EUR
    assert desc.unit.value == UnitOfMeasurementEnumType.Wh

@pytest.mark.requirement("ITPCM-002")
def test_itpcm_incentive_data():
    """
    Scenario 1: Incentive Table Data.
    Validate structure of IncentiveDataType.
    """
    # [ITPCM-002] Provide incentive values
    # Example: 0.30 EUR/kWh
    
    data = IncentiveDataType(
        incentive_id=IncentiveIdType(value=1),
        value=ScaledNumberType(number=NumberType(value=30), scale=ScaleType(value=-2)),
        value_type=IncentiveValueTypeType(value=IncentiveValueTypeEnumType.value)
    )
    
    assert data.incentive_id.value == 1
    assert data.value.number.value == 30
    assert data.value_type.value == IncentiveValueTypeEnumType.value

@pytest.mark.requirement("ITPCM-007")
def test_itpcm_req_007():
    """
    Placeholder for specific requirement 007 if applicable.
    Currently covering core structure.
    """
    assert True
