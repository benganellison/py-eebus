import pytest
from spine.base_type.measurement import (
    MeasurementDataType,
    MeasurementDescriptionDataType,
)
from spine.base_type.deviceclassification import (
    DeviceClassificationManufacturerDataType,
)
from spine.base_type.devicediagnosis import (
    DeviceDiagnosisStateDataType,
)
from spine.base_type.deviceconfiguration import (
    DeviceConfigurationKeyValueDataType,
    DeviceConfigurationKeyValueDescriptionDataType,
)
from spine.base_type.electricalconnection import (
    ElectricalConnectionCharacteristicDataType,
)
from spine.base_type.commondatatypes import (
    ScaledNumberType,
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType,
    LabelType,
)
from spine.union_type.measurement import MeasurementTypeType
from spine.enums.measurement import MeasurementTypeEnumType, MeasurementValueTypeEnumType
from spine.union_type.commondatatypes import ScopeTypeType
from spine.enums.commondatatypes import ScopeTypeEnumType
from spine.union_type.devicediagnosis import DeviceDiagnosisOperatingStateType
from spine.enums.devicediagnosis import DeviceDiagnosisOperatingStateEnumType
from spine.union_type.deviceconfiguration import DeviceConfigurationKeyNameType
from spine.enums.deviceconfiguration import DeviceConfigurationKeyNameEnumType
from spine.simple_type.deviceclassification import (
    DeviceClassificationStringType,
)

# MOB Use Case Tests
# Monitoring of Battery
# Ref: EEBus_UC_TS_MonitoringOfBattery_V1.0.0_public.md

@pytest.mark.requirement("MOB-001")
def test_mob_req_001():
    """
    Verify MOB-001: Sign conventions.
    Load convention: Positive = Consumption (Charge), Negative = Production (Discharge).
    """
    # This is a convention rule, so we verify we can set positive and negative values.
    val_pos = ScaledNumberType(number=NumberType(value=100), scale=ScaleType(value=0))
    val_neg = ScaledNumberType(number=NumberType(value=-100), scale=ScaleType(value=0))
    assert val_pos.number.value == 100
    assert val_neg.number.value == -100

@pytest.mark.requirement("MOB-021")
def test_mob_state_of_charge():
    """
    Verify Battery State of Charge.
    Ref: [MOB-021]
    Scope: stateOfCharge, Type: percentage
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.stateOfCharge),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.percentage)
    )
    assert meas.scope_type.value == "stateOfCharge"
    assert meas.measurement_type.value == "percentage"

@pytest.mark.requirement("MOB-022")
def test_mob_state_of_health():
    """
    Verify Battery State of Health.
    Ref: [MOB-022]
    Scope: stateOfHealth, Type: percentage
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.stateOfHealth),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.percentage)
    )
    assert meas.scope_type.value == "stateOfHealth"

@pytest.mark.requirement("MOB-023")
def test_mob_state_of_energy():
    """
    Verify Battery State of Energy.
    Ref: [MOB-023]
    Scope: stateOfEnergy, Type: energy
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.stateOfEnergy),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.energy)
    )
    assert meas.scope_type.value == "stateOfEnergy"
    assert meas.measurement_type.value == "energy"

@pytest.mark.requirement("MOB-024")
def test_mob_usable_capacity():
    """
    Verify Battery Usable Capacity.
    Ref: [MOB-024]
    Scope: useableCapacity, Type: capacity
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.useableCapacity),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.capacity)
    )
    assert meas.scope_type.value == "useableCapacity"
    assert meas.measurement_type.value == "capacity"

@pytest.mark.requirement("MOB-025")
def test_mob_battery_state():
    """
    Verify Battery State (Operating State).
    Ref: [MOB-025]
    """
    # Uses DeviceDiagnosisStateDataType
    state = DeviceDiagnosisStateDataType(
        operating_state=DeviceDiagnosisOperatingStateType(
            value=DeviceDiagnosisOperatingStateEnumType.normalOperation
        )
    )
    assert state.operating_state.value == "normalOperation"

    failure_state = DeviceDiagnosisStateDataType(
        operating_state=DeviceDiagnosisOperatingStateType(
            value=DeviceDiagnosisOperatingStateEnumType.failure
        )
    )
    assert failure_state.operating_state.value == "failure"

@pytest.mark.requirement("MOB-031")
def test_mob_dc_power():
    """
    Verify Battery DC Power.
    Ref: [MOB-031]
    Scope: dcPower, Type: power
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.dcPower),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.power)
    )
    assert meas.scope_type.value == "dcPower"
    assert meas.measurement_type.value == "power"

@pytest.mark.requirement("MOB-041")
def test_mob_dc_current():
    """
    Verify Battery DC Current.
    Ref: [MOB-041]
    Scope: dcCurrent, Type: current
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.dcCurrent),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.current)
    )
    assert meas.scope_type.value == "dcCurrent"
    assert meas.measurement_type.value == "current"

@pytest.mark.requirement("MOB-051")
def test_mob_dc_voltage():
    """
    Verify Battery DC Voltage.
    Ref: [MOB-051]
    Scope: dcVoltage, Type: voltage
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.dcVoltage),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.voltage)
    )
    assert meas.scope_type.value == "dcVoltage"
    assert meas.measurement_type.value == "voltage"

@pytest.mark.requirement("MOB-061")
def test_mob_dc_charge_energy():
    """
    Verify Battery Total DC Charge Energy.
    Ref: [MOB-061]
    Scope: dcChargeEnergy, Type: energy
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.dcChargeEnergy),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.energy)
    )
    assert meas.scope_type.value == "dcChargeEnergy"
    assert meas.measurement_type.value == "energy"

@pytest.mark.requirement("MOB-062")
def test_mob_dc_discharge_energy():
    """
    Verify Battery Total DC Discharge Energy.
    Ref: [MOB-062]
    Scope: dcDischargeEnergy, Type: energy
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.dcDischargeEnergy),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.energy)
    )
    assert meas.scope_type.value == "dcDischargeEnergy"

@pytest.mark.requirement("MOB-071")
def test_mob_cycle_count():
    """
    Verify Cumulated Load Cycle Count.
    Ref: [MOB-071]
    Scope: loadCycleCount, Type: count
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.loadCycleCount),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.count)
    )
    assert meas.scope_type.value == "loadCycleCount"
    assert meas.measurement_type.value == "count"

@pytest.mark.requirement("MOB-072")
def test_mob_battery_type():
    """
    Verify Battery Type (Config).
    Ref: [MOB-072]
    KeyName: batteryType
    """
    # Assuming batteryType is a valid DeviceConfigurationKeyName
    conf = DeviceConfigurationKeyValueDescriptionDataType(
        key_name=DeviceConfigurationKeyNameType(
            value=DeviceConfigurationKeyNameEnumType.batteryType
        )
    )
    assert conf.key_name.value == "batteryType"

@pytest.mark.requirement("MOB-081")
def test_mob_nominal_capacity():
    """
    Verify Battery Capacity Nominal Max (Capability).
    Ref: [MOB-081]
    Scope: nominalEnergyCapacity, Type: capacity
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.nominalEnergyCapacity),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.capacity)
    )
    assert meas.scope_type.value == "nominalEnergyCapacity"
    assert meas.measurement_type.value == "capacity"

@pytest.mark.requirement("MOB-091")
def test_mob_internal_temperature():
    """
    Verify Internal Temperature.
    Ref: [MOB-091]
    Scope: componentTemperature, Type: temperature
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.componentTemperature),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.temperature)
    )
    assert meas.scope_type.value == "componentTemperature"

@pytest.mark.requirement("MOB-011")
def test_mob_identification():
    """
    Verify Battery Identification.
    Ref: [MOB-011] to [MOB-016]
    """
    ident = DeviceClassificationManufacturerDataType(
        device_name=DeviceClassificationStringType(value="Battery 1"),
        device_code=DeviceClassificationStringType(value="BAT-123"),
        serial_number=DeviceClassificationStringType(value="SN-999"),
        vendor_name=DeviceClassificationStringType(value="BatteryMaker"),
        brand_name=DeviceClassificationStringType(value="BestBat"),
        manufacturer_label=LabelType(value="My Battery Label")
    )
    assert ident.vendor_name.value == "BatteryMaker"
    assert ident.device_code.value == "BAT-123"
    assert ident.manufacturer_label.value == "My Battery Label"


