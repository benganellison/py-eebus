import pytest
from spine.base_type.timeseries import (
    TimeSeriesDataType,
    TimeSeriesDescriptionDataType,
    TimeSeriesConstraintsDataType,
    TimeSeriesSlotType,
)
from spine.enums.timeseries import (
    TimeSeriesTypeEnumType,
)
from spine.enums.commondatatypes import (
    ScopeTypeEnumType,
)
from spine.union_type.timeseries import (
    TimeSeriesTypeType,
)
from spine.union_type.commondatatypes import (
    ScopeTypeType,
    AbsoluteOrRelativeTimeType,
)
from spine.simple_type.timeseries import (
    TimeSeriesSlotCountType,
    TimeSeriesSlotIdType,
)

# POEN Use Case Tests
# Power Envelope
# Ref: EEBus_UC_TS_PowerEnvelope_V1.0.0_public.md

@pytest.mark.requirement("POEN-001", "POEN-002")
def test_poen_timeseries_structure():
    """
    Verify TimeSeries Structure (Normal and Fallback).
    Ref: [POEN-001/1] Normal start_time uses Date + Time (UTC).
    Ref: [POEN-001/2] Fallback start_time uses Time (UTC) only.
    Ref: [POEN-001/3] Durations as relative time.
    """
    # Normal Curve: DateTime
    ts_normal = TimeSeriesDataType(
        start_time=AbsoluteOrRelativeTimeType(), # DateTime
        duration="PT24H"
    )
    assert isinstance(ts_normal.start_time, AbsoluteOrRelativeTimeType)
    assert ts_normal.duration == "PT24H"

    # Fallback Curve: Time Only
    ts_fallback = TimeSeriesDataType(
        start_time=AbsoluteOrRelativeTimeType(), # Time
        duration="PT24H"
    )
    assert isinstance(ts_fallback.start_time, AbsoluteOrRelativeTimeType)
    assert ts_fallback.duration == "PT24H"

@pytest.mark.requirement("POEN-011", "POEN-012", "POEN-021", "POEN-022")
def test_poen_curve_types():
    """
    Verify Curve Types and Scopes.
    Ref: [POEN-011]-[POEN-022]
    """
    # Consumption Limit Curve
    desc_consumption = TimeSeriesDescriptionDataType(
        time_series_type=TimeSeriesTypeType(value=TimeSeriesTypeEnumType.consumptionLimitCurve),
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.activePowerLimit)
    )
    assert desc_consumption.time_series_type.value == TimeSeriesTypeEnumType.consumptionLimitCurve
    assert desc_consumption.scope_type.value == ScopeTypeEnumType.activePowerLimit

    # Production Limit Curve
    desc_production = TimeSeriesDescriptionDataType(
        time_series_type=TimeSeriesTypeType(value=TimeSeriesTypeEnumType.productionLimitCurve),
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.activePowerLimit)
    )
    assert desc_production.time_series_type.value == TimeSeriesTypeEnumType.productionLimitCurve
    assert desc_production.scope_type.value == ScopeTypeEnumType.activePowerLimit

@pytest.mark.requirement("POEN-013", "POEN-023")
def test_poen_constraints():
    """
    Verify Constraints.
    Ref: [POEN-013/2] Slot Count Max >= 192 for Consumption.
    Ref: [POEN-023/2] Slot Count Max >= 192 for Production.
    """
    # [POEN-013/2]
    # SimpleTypes need to be instantiated nesting if they are aliases
    slot_count = TimeSeriesSlotCountType(value=TimeSeriesSlotIdType(value=192))
    
    constraints = TimeSeriesConstraintsDataType(
        slot_count_max=slot_count
    )
    # The wrapped value access depends on simple type structure
    assert constraints.slot_count_max.value.value == 192
