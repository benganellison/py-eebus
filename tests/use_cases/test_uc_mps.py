import pytest
from spine.base_type.measurement import (
    MeasurementDataType,
    MeasurementDescriptionDataType,
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
)
from spine.enums.commondatatypes import (
    ScopeTypeEnumType,
)
from spine.base_type.commondatatypes import (
    ScaledNumberType,
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType,
)

# MPS Use Case Tests
# Monitoring of PV String
# Ref: EEBus_UC_TS_MonitoringOfPVString_V1.0.0_RC4_public.md

@pytest.mark.requirement("MPS-011")
def test_mps_dc_power():
    """
    Verify PV String DC Power (Scenario 1).
    Ref: [MPS-011]
    """
    # DC Power: dcPower
    meas_desc = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.dcPower),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.power)
    )
    assert meas_desc.scope_type.value == "dcPower"
    assert meas_desc.measurement_type.value == "power"

    # Value check
    meas_val = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=1500),
            scale=ScaleType(value=0)
        ),
        value_type=MeasurementValueTypeType(value=MeasurementValueTypeEnumType.value)
    )
    assert meas_val.value.number.value == 1500

@pytest.mark.requirement("MPS-021")
def test_mps_dc_current():
    """
    Verify PV String DC Current (Scenario 2).
    Ref: [MPS-021]
    """
    # DC Current: dcCurrent
    meas_desc = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.dcCurrent),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.current)
    )
    assert meas_desc.scope_type.value == "dcCurrent"
    assert meas_desc.measurement_type.value == "current"

    # Value check
    meas_val = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=10),
            scale=ScaleType(value=0)
        ),
        value_type=MeasurementValueTypeType(value=MeasurementValueTypeEnumType.value)
    )
    assert meas_val.value.number.value == 10

@pytest.mark.requirement("MPS-031")
def test_mps_dc_voltage():
    """
    Verify PV String DC Voltage (Scenario 3).
    Ref: [MPS-031]
    """
    # DC Voltage: dcVoltage
    meas_desc = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.dcVoltage),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.voltage)
    )
    assert meas_desc.scope_type.value == "dcVoltage"
    assert meas_desc.measurement_type.value == "voltage"

    # Value check
    meas_val = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=400),
            scale=ScaleType(value=0)
        ),
        value_type=MeasurementValueTypeType(value=MeasurementValueTypeEnumType.value)
    )
    assert meas_val.value.number.value == 400

@pytest.mark.requirement("MPS-041")
def test_mps_dc_energy():
    """
    Verify PV String DC Energy (Scenario 4).
    Ref: [MPS-041]
    """
    # DC Energy: dcEnergy
    meas_desc = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.dcEnergy),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.energy)
    )
    assert meas_desc.scope_type.value == "dcEnergy"
    assert meas_desc.measurement_type.value == "energy"

    # Value check
    meas_val = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=50000),
            scale=ScaleType(value=0)
        ),
        value_type=MeasurementValueTypeType(value=MeasurementValueTypeEnumType.value)
    )
    assert meas_val.value.number.value == 50000

@pytest.mark.requirement("MPS-061")
def test_mps_internal_temperature():
    """
    Verify PV String Internal Temperature (Scenario 6).
    Ref: [MPS-061]
    """
    # Internal Temperature: componentTemperature
    meas_desc = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.componentTemperature),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.temperature)
    )
    assert meas_desc.scope_type.value == "componentTemperature"
    assert meas_desc.measurement_type.value == "temperature"

    # Value check
    meas_val = MeasurementDataType(
        value=ScaledNumberType(
            number=NumberType(value=45),
            scale=ScaleType(value=0)
        ),
        value_type=MeasurementValueTypeType(value=MeasurementValueTypeEnumType.value)
    )
    assert meas_val.value.number.value == 45
