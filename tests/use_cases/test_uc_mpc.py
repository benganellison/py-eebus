import pytest
from spine.base_type.measurement import (
    MeasurementDescriptionDataType,
    MeasurementDataType,
)
from spine.union_type.measurement import (
    MeasurementTypeType,
    MeasurementValueTypeType,
)
from spine.enums.measurement import (
    MeasurementTypeEnumType,
    MeasurementValueTypeEnumType,
)
from spine.union_type.commondatatypes import (
    ScopeTypeType,
    UnitOfMeasurementType,
)
from spine.enums.commondatatypes import (
    ScopeTypeEnumType,
    UnitOfMeasurementEnumType,
)
from spine.base_type.commondatatypes import (
    ScaledNumberType,
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType,
)

# MPC Use Case Tests
# Monitoring of Power Consumption
# Ref: EEBus_UC_TS_MonitoringOfPowerConsumption_V1.0.0_public.md

@pytest.mark.requirement("MPC-011")
def test_mpc_total_active_power():
    """
    Verify Total Active Power (Scenario 1).
    Ref: [MPC-011]
    """
    # Total Active Power: acPowerTotal
    # Description check
    meas_desc = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acPowerTotal),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.power)
    )
    assert meas_desc.scope_type.value == "acPowerTotal"
    assert meas_desc.measurement_type.value == "power"

    # Value check
    meas_val = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=1000),
            scale=ScaleType(value=0)
        ),
        value_type=MeasurementValueTypeType(value=MeasurementValueTypeEnumType.value)
    )
    assert meas_val.value.number.value == 1000

@pytest.mark.requirement("MPC-012")
def test_mpc_phase_active_power():
    """
    Verify Phase-Specific Active Power (Scenario 1).
    Ref: [MPC-012]
    """
    # Phase A, B, C
    meas_a = MeasurementDescriptionDataType(scope_type=ScopeTypeType(value=ScopeTypeEnumType.acPowerA))
    meas_b = MeasurementDescriptionDataType(scope_type=ScopeTypeType(value=ScopeTypeEnumType.acPowerB))
    meas_c = MeasurementDescriptionDataType(scope_type=ScopeTypeType(value=ScopeTypeEnumType.acPowerC))
    
    assert meas_a.scope_type.value == "acPowerA"
    assert meas_b.scope_type.value == "acPowerB"
    assert meas_c.scope_type.value == "acPowerC"

    # Value check example (Phase A)
    val_a = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=2300),
            scale=ScaleType(value=-1) # 230.0 W
        )
    )
    assert val_a.value.number.value == 2300
    assert val_a.value.scale.value == -1

@pytest.mark.requirement("MPC-021")
def test_mpc_total_consumed_energy():
    """
    Verify Total Consumed Energy (Scenario 2).
    Ref: [MPC-021]
    """
    # acEnergyConsumed
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acEnergyConsumed),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.Wh),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.energy)
    )
    assert meas.scope_type.value == "acEnergyConsumed"
    assert meas.unit.value == "Wh"
    assert meas.measurement_type.value == "energy"

    # Value check
    val = MeasurementDataType(
        value=ScaledNumberType(number=NumberType(value=5000))
    )
    assert val.value.number.value == 5000

@pytest.mark.requirement("MPC-022")
def test_mpc_total_produced_energy():
    """
    Verify Total Produced Energy (Scenario 2).
    Ref: [MPC-022]
    """
    # acEnergyProduced
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acEnergyProduced),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.energy)
    )
    assert meas.scope_type.value == "acEnergyProduced"

    # Value check
    val = MeasurementDataType(
        value=ScaledNumberType(number=NumberType(value=120))
    )
    assert val.value.number.value == 120

@pytest.mark.requirement("MPC-031")
def test_mpc_phase_current():
    """
    Verify Phase-Specific AC Current (Scenario 3).
    Ref: [MPC-031]
    """
    # acCurrentA, B, C
    meas_a = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acCurrentA),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.current)
    )
    assert meas_a.scope_type.value == "acCurrentA"
    assert meas_a.measurement_type.value == "current"

    # Value check (16A)
    val = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=16)
        )
    )
    assert val.value.number.value == 16

@pytest.mark.requirement("MPC-041")
def test_mpc_phase_voltage():
    """
    Verify Phase-Specific AC Voltage (Scenario 4).
    Ref: [MPC-041]
    """
    # acVoltageA, B, C
    meas_a = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acVoltageA),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.voltage)
    )
    assert meas_a.scope_type.value == "acVoltageA"
    assert meas_a.measurement_type.value == "voltage"

    # Value check (230V)
    val = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=230)
        )
    )
    assert val.value.number.value == 230

@pytest.mark.requirement("MPC-051")
def test_mpc_frequency():
    """
    Verify AC Frequency (Scenario 5).
    Ref: [MPC-051]
    """
    # acFrequency
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acFrequency),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.frequency)
    )
    assert meas.scope_type.value == "acFrequency"
    assert meas.measurement_type.value == "frequency"

    # Value check (50Hz)
    val = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=50)
        )
    )
    assert val.value.number.value == 50
