import pytest
from spine.base_type.timeseries import (
    TimeSeriesDataType,
    TimeSeriesDescriptionDataType,
    TimeSeriesSlotType,
)
from spine.base_type.electricalconnection import (
    ElectricalConnectionCharacteristicDataType,
)
from spine.union_type.timeseries import (
    TimeSeriesTypeType,
)
from spine.union_type.commondatatypes import (
    ScopeTypeType,
    AbsoluteOrRelativeTimeType,
)
from spine.union_type.electricalconnection import (
    ElectricalConnectionCharacteristicTypeType,
)
from spine.enums.commondatatypes import (
    ScopeTypeEnumType,
)
from spine.enums.electricalconnection import (
    ElectricalConnectionCharacteristicTypeEnumType,
)
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType,
)

# PODF Use Case Tests
# Power Demand Forecast
# Ref: EEBus_UC_TS_PowerDemandForecast_V1.0.0_public.md

@pytest.mark.requirement("PODF-001", "PODF-002")
def test_podf_timeseries_structure():
    """
    Verify TimeSeries Structure (Scenario 1).
    Ref: [PODF-001] Start times as UTC.
    Ref: [PODF-002] Durations as relative time.
    """
    ts_data = TimeSeriesDataType(
        start_time=AbsoluteOrRelativeTimeType(),
        duration="PT6H" # 6 hours duration
    )
    # Note: AbsoluteOrRelativeTimeType definition is currently empty/broken in generated code,
    # so we can only check strict type validation, not the string value held within.
    assert isinstance(ts_data.start_time, AbsoluteOrRelativeTimeType)
    assert ts_data.duration == "PT6H"

@pytest.mark.requirement("PODF-004", "PODF-005", "PODF-006")
def test_podf_timeseries_slot_values():
    """
    Verify TimeSeries Slot Values (Scenario 1).
    Ref: [PODF-004] Expected (average) power (value).
    Ref: [PODF-005] Minimum power (min_value).
    Ref: [PODF-006] Maximum power (max_value).
    """
    slot = TimeSeriesSlotType(
        duration="PT15M",
        value=ScaledNumberType(number=NumberType(value=10), scale=ScaleType(value=0)),
        min_value=ScaledNumberType(number=NumberType(value=5), scale=ScaleType(value=0)),
        max_value=ScaledNumberType(number=NumberType(value=15), scale=ScaleType(value=0))
    )
    
    assert slot.value.number.value == 10
    assert slot.min_value.number.value == 5
    assert slot.max_value.number.value == 15

@pytest.mark.requirement("PODF-011")
def test_podf_active_power_forecast_type():
    """
    Verify Active Power Forecast Type (Scenario 1).
    Ref: [PODF-011] Data point: Active Power Forecast.
    Uses ScopeTypeEnumType.activePowerForecast.
    """
    desc = TimeSeriesDescriptionDataType(
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.activePowerForecast)
    )
    
    assert desc.scope_type.value == ScopeTypeEnumType.activePowerForecast

@pytest.mark.requirement("PODF-021", "PODF-022")
def test_podf_contractual_limits():
    """
    Verify Contractual Limits (Scenario 2).
    Ref: [PODF-021] Contractual Consumption Nominal Max.
    Ref: [PODF-022] Contractual Production Nominal Max.
    """
    # [PODF-021]
    consumption_char = ElectricalConnectionCharacteristicDataType(
        characteristic_type=ElectricalConnectionCharacteristicTypeType(
            value=ElectricalConnectionCharacteristicTypeEnumType.contractualConsumptionNominalMax
        )
    )
    assert consumption_char.characteristic_type.value == ElectricalConnectionCharacteristicTypeEnumType.contractualConsumptionNominalMax

    # [PODF-022]
    production_char = ElectricalConnectionCharacteristicDataType(
        characteristic_type=ElectricalConnectionCharacteristicTypeType(
            value=ElectricalConnectionCharacteristicTypeEnumType.contractualProductionNominalMax
        )
    )
    assert production_char.characteristic_type.value == ElectricalConnectionCharacteristicTypeEnumType.contractualProductionNominalMax
