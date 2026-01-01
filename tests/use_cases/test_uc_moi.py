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
from spine.base_type.electricalconnection import (
    ElectricalConnectionCharacteristicDataType,
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
from spine.enums.devicediagnosis import DeviceDiagnosisOperatingStateEnumType
from spine.union_type.devicediagnosis import DeviceDiagnosisOperatingStateType
from spine.union_type.electricalconnection import (
    ElectricalConnectionCharacteristicContextType,
    ElectricalConnectionCharacteristicTypeType,
)
from spine.enums.electricalconnection import (
    ElectricalConnectionCharacteristicContextEnumType,
    ElectricalConnectionCharacteristicTypeEnumType,
)
from spine.base_type.commondatatypes import (
    ScaledNumberType,
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType,
)
from spine.simple_type.deviceclassification import (
    DeviceClassificationStringType,
)

# MOI Use Case Tests
# Monitoring of Inverter
# Ref: EEBus_UC_TS_MonitoringOfInverter_V1.0.0_public.md

@pytest.mark.requirement("MOI-011")
def test_moi_identification():
    """
    Verify Inverter Identification (Scenario 1).
    Ref: [MOI-011]
    """
    ident = DeviceClassificationManufacturerDataType(
        device_name=DeviceClassificationStringType(value="Hybrid Inverter"),
        device_code=DeviceClassificationStringType(value="INV-HYB-5000"),
        serial_number=DeviceClassificationStringType(value="SN-INV-001"),
        vendor_name=DeviceClassificationStringType(value="BestInverterCo"),
        brand_name=DeviceClassificationStringType(value="BestBrand")
    )
    assert ident.device_name.value == "Hybrid Inverter"
    assert ident.vendor_name.value == "BestInverterCo"

@pytest.mark.requirement("MOI-021")
def test_moi_inverter_state():
    """
    Verify Inverter State (Scenario 2).
    Ref: [MOI-021]
    """
    # Uses DeviceDiagnosisStateDataType
    state = DeviceDiagnosisStateDataType(
        operating_state=DeviceDiagnosisOperatingStateType(value=DeviceDiagnosisOperatingStateEnumType.normalOperation)
    )
    assert state.operating_state.value == "normalOperation"

@pytest.mark.requirement("MOI-031")
def test_moi_ac_total_apparent_power():
    """
    Verify Inverter Total Apparent Power (Scenario 3).
    Ref: [MOI-031]
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acPowerApparentTotal),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.power)
    )
    assert meas.scope_type.value == "acPowerApparentTotal"
    assert meas.measurement_type.value == "power"

@pytest.mark.requirement("MOI-032")
def test_moi_ac_phase_apparent_power():
    """
    Verify Inverter Phase-Specific Apparent Power (Scenario 3).
    Ref: [MOI-032]
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acPowerApparent),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.power)
    )
    assert meas.scope_type.value == "acPowerApparent"

@pytest.mark.requirement("MOI-033")
def test_moi_ac_total_reactive_power():
    """
    Verify Inverter Total Reactive Power (Scenario 3).
    Ref: [MOI-033]
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acPowerReactiveTotal),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.power)
    )
    assert meas.scope_type.value == "acPowerReactiveTotal"

@pytest.mark.requirement("MOI-035")
def test_moi_ac_total_active_power():
    """
    Verify Inverter Total Active Power (Scenario 3).
    Ref: [MOI-035]
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acPowerTotal),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.power)
    )
    assert meas.scope_type.value == "acPowerTotal"

@pytest.mark.requirement("MOI-041")
def test_moi_ac_yield_total():
    """
    Verify Inverter Total AC Yield (Scenario 4).
    Ref: [MOI-041]
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acYieldTotal),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.energy)
    )
    assert meas.scope_type.value == "acYieldTotal"
    assert meas.measurement_type.value == "energy"

@pytest.mark.requirement("MOI-042")
def test_moi_ac_yield_day():
    """
    Verify Inverter AC Yield Day (Scenario 4).
    Ref: [MOI-042]
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acYieldDay),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.energy)
    )
    assert meas.scope_type.value == "acYieldDay"

@pytest.mark.requirement("MOI-051")
def test_moi_cos_phi():
    """
    Verify Power Factor (Cos Phi) (Scenario 5).
    Ref: [MOI-051]
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acCosPhi),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.powerFactor)
    )
    assert meas.scope_type.value == "acCosPhi"
    assert meas.measurement_type.value == "powerFactor"

@pytest.mark.requirement("MOI-06x")
def test_moi_capabilities():
    """
    Verify Inverter Capabilities (Scenario 6).
    Ref: Table 36, 37, 38 etc.
    """
    # Nominal Max Power Production
    char = ElectricalConnectionCharacteristicDataType(
        characteristic_type=ElectricalConnectionCharacteristicTypeType(
            value=ElectricalConnectionCharacteristicTypeEnumType.powerProductionNominalMax
        ),
        characteristic_context=ElectricalConnectionCharacteristicContextType(
            value=ElectricalConnectionCharacteristicContextEnumType.entity
        ),
        value=ScaledNumberType(number=NumberType(value=10000))
    )
    assert char.characteristic_type.value == "powerProductionNominalMax"
    assert char.characteristic_context.value == "entity"
    assert char.value.number.value == 10000

@pytest.mark.requirement("MOI-07x")
def test_moi_internal_data():
    """
    Verify Inverter Internal Data (Scenario 7).
    Ref: [MOI-07x]
    Example: DC String Voltage
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.dcVoltage),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.voltage)
    )
    assert meas.scope_type.value == "dcVoltage"
    assert meas.measurement_type.value == "voltage"

    # Value
    val = MeasurementDataType(
        value=ScaledNumberType(number=NumberType(value=400)),
        value_type=MeasurementValueTypeType(value=MeasurementValueTypeEnumType.value)
    )
    assert val.value.number.value == 400
