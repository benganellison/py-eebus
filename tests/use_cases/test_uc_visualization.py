import pytest
from spine.base_type.measurement import (
    MeasurementDescriptionDataType,
    MeasurementDataType
)
from spine.base_type.networkmanagement import (
    NetworkManagementEntityDescriptionDataType,
)
from spine.enums.commondatatypes import (
    ScopeTypeEnumType,
    UnitOfMeasurementEnumType,
)
from spine.enums.measurement import (
    MeasurementTypeEnumType,
    MeasurementValueTypeEnumType,
)
from spine.union_type.commondatatypes import (
    ScopeTypeType,
    UnitOfMeasurementType,
)
from spine.union_type.measurement import (
    MeasurementTypeType,
    MeasurementValueTypeType,
)
from spine.simple_type.commondatatypes import (
    LabelType,
)
from spine.base_type.commondatatypes import ScaledNumberType

# Visualization Use Case Tests
# Covers: VHAN, VABD, VAPD
# Ref: EEBus_UC_TS_VisualizationOfAggregatedBatteryData_V1.0.0_RC1_public.md
# Ref: EEBus_UC_TS_VisualizationOfAggregatedPhotovoltaicData_V1.0.0_RC1_public.md
# Ref: EEBus_UC_TS_VisualizationOfHeatingAreaName_V1.0.0_public.md

# VABD (Visualization of Aggregated Battery Data)
@pytest.mark.requirement("VABD-005")
def test_vabd_aggregated_battery_measurement():
    """
    Verify Aggregated Battery Data (State of Charge).
    """
    # Measurement Description: SOC
    desc = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.stateOfCharge),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.percentage),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.pct)
    )
    assert desc.scope_type.value == ScopeTypeEnumType.stateOfCharge
    assert desc.measurement_type.value == MeasurementTypeEnumType.percentage
    assert desc.unit.value == UnitOfMeasurementEnumType.pct

# VAPD (Visualization of Aggregated PV Data)
@pytest.mark.requirement("VAPD-001")
def test_vapd_aggregated_pv_measurement():
    """
    Verify Aggregated PV Data (AC Power Total).
    """
    # Measurement Description: AC Power Total
    desc = MeasurementDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.acPowerTotal),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.power),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.W)
    )
    assert desc.scope_type.value == ScopeTypeEnumType.acPowerTotal
    assert desc.measurement_type.value == MeasurementTypeEnumType.power
    assert desc.unit.value == UnitOfMeasurementEnumType.W

# VHAN (Visualization of Heating Area Name)
@pytest.mark.requirement("VHAN-001")
def test_vhan_heating_area_name():
    """
    Verify Heating Area Name.
    Uses NetworkManagementEntityDescriptionDataType label.
    """
    # Entity Description: Heating Area
    # [VHAN-001] "Kitchen" or "Living Room"
    entity_desc = NetworkManagementEntityDescriptionDataType(
        label=LabelType(value="Living Room"),
        description=None
    )
    assert entity_desc.label.value == "Living Room"
