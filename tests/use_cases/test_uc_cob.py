import pytest
from spine.base_type.setpoint import (
    SetpointDataType,
    SetpointConstraintsDataType,
    SetpointDescriptionDataType,
)
from spine.base_type.deviceconfiguration import (
    DeviceConfigurationKeyValueDataType,
    DeviceConfigurationKeyValueDescriptionDataType,
)
from spine.enums.commondatatypes import (
    ScopeTypeEnumType,
    UnitOfMeasurementEnumType,
)
from spine.enums.setpoint import (
    SetpointTypeEnumType,
)
from spine.enums.deviceconfiguration import (
    DeviceConfigurationKeyNameEnumType,
)
from spine.base_type.commondatatypes import (
    ScaledNumberType,
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType,
)
from spine.union_type.setpoint import (
    SetpointTypeType,
)
from spine.union_type.deviceconfiguration import (
    DeviceConfigurationKeyNameType,
)
from spine.union_type.commondatatypes import (
    UnitOfMeasurementType,
    ScopeTypeType,
)

# COB Use Case Tests
# Control of Battery
# Ref: EEBus_UC_TS_ControlOfBattery_V1.0.0_public.md

@pytest.mark.requirement("COB-011", "COB-012", "COB-021")
def test_cob_setpoint_structure():
    """
    Verify Setpoint Structures (Scenarios 1 & 2).
    Ref: [COB-011] Battery AC Power Setpoint.
    Ref: [COB-012] Battery DC Power Setpoint.
    Ref: [COB-021] PCC Power Setpoint.
    """
    # [COB-011] Battery AC Power
    desc_ac = SetpointDescriptionDataType(
        setpoint_type=SetpointTypeType(value=SetpointTypeEnumType.valueAbsolute),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.W),
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.batteryAcPower)
    )
    assert desc_ac.scope_type.value == ScopeTypeEnumType.batteryAcPower

    # [COB-012] Battery DC Power
    desc_dc = SetpointDescriptionDataType(
        setpoint_type=SetpointTypeType(value=SetpointTypeEnumType.valueAbsolute),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.W),
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.batteryDcPower)
    )
    assert desc_dc.scope_type.value == ScopeTypeEnumType.batteryDcPower

    # [COB-021] PCC Power
    desc_pcc = SetpointDescriptionDataType(
        setpoint_type=SetpointTypeType(value=SetpointTypeEnumType.valueAbsolute),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.W),
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.pccPower)
    )
    assert desc_pcc.scope_type.value == ScopeTypeEnumType.pccPower


@pytest.mark.requirement("COB-022", "COB-031", "COB-041")
def test_cob_configuration_parameters():
    """
    Verify Configuration Parameters (Scenarios 2, 3 & 4).
    Ref: [COB-022] Max AC Charge Power.
    Ref: [COB-031] Battery Active Control Mode.
    Ref: [COB-041] Failsafe AC Power Setpoint.
    """
    # [COB-022] Max AC Charge Power (Scenario 2)
    # Using Key Name "maxAcChargePower"
    config_max_ac = DeviceConfigurationKeyValueDescriptionDataType(
        key_name=DeviceConfigurationKeyNameType(value=DeviceConfigurationKeyNameEnumType.maxAcChargePower),
        value_type="scaledNumber",
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.W)
    )
    assert config_max_ac.key_name.value == "maxAcChargePower"

    # [COB-031] Battery Active Control Mode (Scenario 3)
    # Using Key Name "batteryActiveControlMode" (values: power/pcc/auto)
    config_mode = DeviceConfigurationKeyValueDescriptionDataType(
        key_name=DeviceConfigurationKeyNameType(value=DeviceConfigurationKeyNameEnumType.batteryActiveControlMode),
        value_type="string"
    )
    assert config_mode.key_name.value == "batteryActiveControlMode"

    # [COB-041] Failsafe AC Power Setpoint (Scenario 4)
    # Using Key Name "failsafeAcPowerSetpoint"
    config_failsafe = DeviceConfigurationKeyValueDescriptionDataType(
        key_name=DeviceConfigurationKeyNameType(value=DeviceConfigurationKeyNameEnumType.failsafeAcPowerSetpoint),
        value_type="scaledNumber",
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.W)
    )
    assert config_failsafe.key_name.value == "failsafeAcPowerSetpoint"

@pytest.mark.requirement("COB-001/1")
def test_cob_setpoint_values():
    """
    Verify Setpoint Value Constraints.
    Ref: [COB-001/1] Values via ScaledNumber.
    """
    sp_value = SetpointDataType(
        value=ScaledNumberType(number=NumberType(value=1000), scale=ScaleType(value=0))
    )
    assert sp_value.value.number.value == 1000
    assert sp_value.value.scale.value == 0
