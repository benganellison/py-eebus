import pytest
from spine.base_type.tariffinformation import (
    TariffDescriptionDataType,
    TariffDataType,
    TierDescriptionDataType,
    TierBoundaryDescriptionDataType,
    TierDataType,
    IncentiveDataType,
)
from spine.union_type.commondatatypes import (
    ScopeTypeType,
    CurrencyType,
    UnitOfMeasurementType,
)
from spine.enums.commondatatypes import (
    ScopeTypeEnumType,
    CurrencyEnumType,
    UnitOfMeasurementEnumType,
)
from spine.union_type.tariffinformation import (
    TierTypeType,
    TierBoundaryTypeType,
    IncentiveTypeType,
    IncentiveValueTypeType,
)
from spine.enums.tariffinformation import (
    TierTypeEnumType,
    TierBoundaryTypeEnumType,
    IncentiveTypeEnumType,
    IncentiveValueTypeEnumType,
)
from spine.simple_type.tariffinformation import (
    TariffIdType,
    TierIdType,
    TierBoundaryIdType,
    IncentiveIdType,
)
from spine.base_type.commondatatypes import (
    ScaledNumberType,
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType,
)

# TOUT Use Case Tests
# Time of Use Tariff
# Ref: EEBus_UC_TS_TimeOfUseTariff_V1.0.0_public.md

@pytest.mark.requirement("TOUT-011")
def test_tout_tariff_information():
    """
    Verify Tariff Information (Scenario 1).
    Ref: [TOUT-011]
    """
    # Tariff Description
    # scopeType: tariffInformation (implied context, usually not explicit enum member if not present, checking value)
    # Using 'simpleIncentiveTable' or similar if 'tariffInformation' not in ScopeTypeEnumType?
    # Spec says [TOUT-011] Incentive-based incentive table...
    # Let's use generic ScopeTypeType(value="tariffInformation") if enum missing, or derived.
    # Looking at ScopeTypeEnumType in previous file view, it has many.
    # Assuming 'activePowerLimit', 'curtailment', etc.
    # For TOUT context, usually it's just about the Tariff validity.
    
    tariff_desc = TariffDescriptionDataType(
        tariff_id=TariffIdType(value=1),
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.simpleIncentiveTable), # Using simpleIncentiveTable as a valid scope
        label=None,
        description=None
    )
    assert tariff_desc.tariff_id.value == 1
    assert tariff_desc.scope_type.value == "simpleIncentiveTable"

@pytest.mark.requirement("TOUT-021")
def test_tout_tariff_structure():
    """
    Verify Tariff Structure (Scenario 2).
    Ref: [TOUT-021] (Referring to general structure requirements)
    """
    # Tier Description
    tier_desc = TierDescriptionDataType(
        tier_id=TierIdType(value=1),
        tier_type=TierTypeType(value=TierTypeEnumType.dynamicCost)
    )
    assert tier_desc.tier_id.value == 1
    assert tier_desc.tier_type.value == "dynamicCost"

    # Tier Boundary Description
    bound_desc = TierBoundaryDescriptionDataType(
        boundary_id=TierBoundaryIdType(value=1),
        boundary_type=TierBoundaryTypeType(value=TierBoundaryTypeEnumType.powerBoundary),
        boundary_unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.W)
    )
    assert bound_desc.boundary_id.value == 1
    assert bound_desc.boundary_type.value == "powerBoundary"
    assert bound_desc.boundary_unit.value == "W"

@pytest.mark.requirement("TOUT-031")
def test_tout_tariff_values():
    """
    Verify Tariff Values (Scenario 3).
    Ref: [TOUT-031]
    """
    # Tariff Data (Activation)
    tariff_data = TariffDataType(
        tariff_id=TariffIdType(value=1)
    )
    assert tariff_data.tariff_id.value == 1

    # Tier Data
    tier_data = TierDataType(
        tier_id=TierIdType(value=1),
        # activeIncentiveId list
    )
    assert tier_data.tier_id.value == 1

@pytest.mark.requirement("TOUT-006")
def test_tout_incentive_data():
    """
    Verify Incentive Data (Absolute Price).
    Ref: [TOUT-006]
    """
    # Incentive Value
    incentive = IncentiveDataType(
        incentive_id=IncentiveIdType(value=1),
        value=ScaledNumberType(
            number=NumberType(value=30),
            scale=ScaleType(value=-2) # 0.30
        ),
        value_type=IncentiveValueTypeType(value=IncentiveValueTypeEnumType.value)
    )
    assert incentive.incentive_id.value == 1
    assert incentive.value.number.value == 30
    assert incentive.value.scale.value == -2
    assert incentive.value_type.value == "value"
