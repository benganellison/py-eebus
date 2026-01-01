import pytest
from spine.base_type.measurement import (
    MeasurementDataType,
    MeasurementDescriptionDataType,
)
from spine.base_type.deviceconfiguration import (
    DeviceConfigurationKeyValueDataType,
    DeviceConfigurationKeyValueDescriptionDataType,
)
from spine.simple_type.deviceconfiguration import DeviceConfigurationKeyIdType
from spine.union_type.deviceconfiguration import DeviceConfigurationKeyNameType
from spine.enums.deviceconfiguration import (
    DeviceConfigurationKeyValueTypeType,
    DeviceConfigurationKeyNameEnumType,
)
from spine.union_type.measurement import MeasurementTypeType
from spine.enums.measurement import MeasurementTypeEnumType
from spine.union_type.commondatatypes import ScopeTypeType
from spine.enums.commondatatypes import ScopeTypeEnumType

# MGCP Use Case Tests
# Monitoring of Grid Connection Point
# Ref: EEBus_UC_TS_MonitoringOfGridConnectionPoint_V1.0.0_public.md

@pytest.mark.requirement("MGCP-TS-001")
def test_mgcp_scenario_1_pv_feed_in():
    """
    Verify Scenario 1: Monitor PV feed-in power limitation factor.
    Ref: [MGCP-TS-001]
    Key: pvCurtailmentLimitFactor (best match for PV Feed-In Power Limitation Factor in standard Enums)
         or potentially proprietary if not standard.
         We will use 'pvCurtailmentLimitFactor' as the likely standard candidate.
    Type: scaledNumber
    """
    config = DeviceConfigurationKeyValueDescriptionDataType(
        key_name=DeviceConfigurationKeyNameType(
            value=DeviceConfigurationKeyNameEnumType.pvCurtailmentLimitFactor
        ),
        value_type=DeviceConfigurationKeyValueTypeType.scaledNumber
    )
    assert config.key_name.value == "pvCurtailmentLimitFactor"
    assert config.value_type.value == "scaledNumber"

@pytest.mark.requirement("MGCP-TS-002")
def test_mgcp_scenario_2_momentary_power():
    """
    Verify Scenario 2: Monitor momentary power consumption/production.
    Ref: [MGCP-TS-002]
    Scope: acPowerTotal
    Type: power
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acPowerTotal),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.power)
    )
    assert meas.scope_type.value == "acPowerTotal"
    assert meas.measurement_type.value == "power"

@pytest.mark.requirement("MGCP-TS-003")
def test_mgcp_scenario_3_total_feed_in():
    """
    Verify Scenario 3: Monitor total feed-in energy.
    Ref: [MGCP-TS-003]
    Scope: gridFeedIn
    Type: energy
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.gridFeedIn),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.energy)
    )
    assert meas.scope_type.value == "gridFeedIn"
    assert meas.measurement_type.value == "energy"

@pytest.mark.requirement("MGCP-TS-004")
def test_mgcp_scenario_4_total_consumed():
    """
    Verify Scenario 4: Monitor total consumed energy.
    Ref: [MGCP-TS-004]
    Scope: gridConsumption
    Type: energy
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.gridConsumption),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.energy)
    )
    assert meas.scope_type.value == "gridConsumption"
    assert meas.measurement_type.value == "energy"

@pytest.mark.requirement("MGCP-TS-005")
def test_mgcp_scenario_5_current_details():
    """
    Verify Scenario 5: Monitor momentary current consumption/production phase details.
    Ref: [MGCP-TS-005]
    Scope: acCurrentA, acCurrentB, acCurrentC
    Type: current
    """
    # Phase A
    meas_a = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acCurrentA),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.current)
    )
    assert meas_a.scope_type.value == "acCurrentA"
    assert meas_a.measurement_type.value == "current"

    # Phase B
    meas_b = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acCurrentB),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.current)
    )
    assert meas_b.scope_type.value == "acCurrentB"

    # Phase C
    meas_c = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acCurrentC),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.current)
    )
    assert meas_c.scope_type.value == "acCurrentC"

@pytest.mark.requirement("MGCP-TS-006")
def test_mgcp_scenario_6_voltage_details():
    """
    Verify Scenario 6: Monitor voltage phase details.
    Ref: [MGCP-TS-006]
    Scope: acVoltageA, acVoltageB, acVoltageC
    Type: voltage
    """
    # Phase A
    meas_a = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acVoltageA),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.voltage)
    )
    assert meas_a.scope_type.value == "acVoltageA"
    assert meas_a.measurement_type.value == "voltage"

    # Phase B
    meas_b = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acVoltageB),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.voltage)
    )
    assert meas_b.scope_type.value == "acVoltageB"

    # Phase C
    meas_c = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acVoltageC),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.voltage)
    )
    assert meas_c.scope_type.value == "acVoltageC"

@pytest.mark.requirement("MGCP-TS-007")
def test_mgcp_scenario_7_frequency():
    """
    Verify Scenario 7: Monitor frequency.
    Ref: [MGCP-TS-007]
    Scope: acFrequency
    Type: frequency
    """
    meas = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acFrequency),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.frequency)
    )
    assert meas.scope_type.value == "acFrequency"
    assert meas.measurement_type.value == "frequency"

