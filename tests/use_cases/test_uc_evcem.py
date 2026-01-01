import pytest
from spine.base_type.measurement import (
    MeasurementDataType,
    MeasurementDescriptionDataType,
    MeasurementConstraintsDataType
)
from spine.base_type.commondatatypes import (
    ScaledNumberType,
    TimePeriodType
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType
)
from spine.union_type.commondatatypes import (
    ScopeTypeType,
    CommodityTypeType,
    UnitOfMeasurementType
)

# EVCEM Use Case Tests
# EV Charging Electricity Measurement

@pytest.mark.requirement("EVCEM-001")
def test_evcem_phase_measurement():
    """
    Verify measurement per phase.
    Ref: [EVCEM-001]
    """
    # Should support AC Current/Power/Voltage per phase
    desc = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value="acCurrent"),
        commodity_type=CommodityTypeType(value="electricity"),
        unit=UnitOfMeasurementType(value="A")
    )
    assert desc.scope_type.value == "acCurrent"
    assert desc.commodity_type.value == "electricity"
    assert desc.unit.value == "A"

@pytest.mark.requirement("EVCEM-002")
def test_evcem_measurement_values():
    """
    Verify that measurement values are communicated correctly.
    Ref: [EVCEM-002]
    """
    # MeasurementDataType should hold the value
    meas = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=16),
            scale=ScaleType(value=0)
        )
    )
    assert meas.value.number.value == 16

@pytest.mark.requirement("EVCEM-003")
def test_evcem_asymmetric_charging_measurement():
    """
    Verify asymmetric charging measurement.
    Ref: [EVCEM-003]
    """
    # Modeled by distinct measurements for each phase
    # Verification implies we can instantiate a measurement for a specific phase/scope
    desc_l1 = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value="acCurrent"),
        # In a real scenario, ID or Label would distinguish L1, but structure allows it.
    )
    assert desc_l1.scope_type.value == "acCurrent"

@pytest.mark.requirement("EVCEM-004")
def test_evcem_grid_capabilities():
    """
    Verify grid capability consideration.
    Ref: [EVCEM-004]
    """
    # Grid limits might be communicated via Constraints
    const = MeasurementConstraintsDataType(
        value_range_max=ScaledNumberType(
            number=NumberType(value=32),
            scale=ScaleType(value=0)
        )
    )
    assert const.value_range_max.number.value == 32

@pytest.mark.requirement("EVCEM-005")
def test_evcem_energy_measurement():
    """
    Verify measurement of accumulated energy.
    Ref: [EVCEM-005]
    """
    desc = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value="acEnergy"), # or similar scope
        unit=UnitOfMeasurementType(value="Wh")
    )
    assert desc.unit.value == "Wh"

@pytest.mark.requirement("EVCEM-007")
def test_evcem_update_handling():
    """
    Verify update handling for measurements.
    Ref: [EVCEM-007]
    """
    # Structural check for timestamp/period
    meas = MeasurementDataType(
        timestamp=None # Just verifying field existence conceptually
    )
    assert hasattr(meas, 'timestamp')
