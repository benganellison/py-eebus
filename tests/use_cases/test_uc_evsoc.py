import pytest
from spine.base_type.measurement import (
    MeasurementDataType,
    MeasurementDescriptionDataType,
    MeasurementConstraintsDataType,
    MeasurementListDataType
)
from spine.base_type.electricalconnection import (
    ElectricalConnectionCharacteristicDataType,
    ElectricalConnectionCharacteristicListDataType
)
from spine.base_type.commondatatypes import (
    ScaledNumberType
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType
)
from spine.union_type.commondatatypes import (
    ScopeTypeType,
    UnitOfMeasurementType,
    CommodityTypeType
)
from spine.union_type.measurement import (
    MeasurementTypeType,
    MeasurementValueSourceType,
    MeasurementValueStateType
)
from spine.union_type.electricalconnection import (
    ElectricalConnectionCharacteristicContextType,
    ElectricalConnectionCharacteristicTypeType
)


# EVSOC Use Case Tests
# EV State of Charge V1.0.0 RC1

@pytest.mark.requirement("EVSOC-001")
def test_evsoc_scenario1_state_of_charge():
    """
    Scenario 1: Monitor EV state of charge.
    Ref: Table 12: Content of Specialization "Measurement_StateOfCharge"
    """
    # 1. Measurement Description
    # scopeType "stateOfCharge", measurementType "percentage", unit "pct", commodityType "electricity"
    desc = MeasurementDescriptionDataType(
        measurement_id=None, # Placeholder
        measurement_type=MeasurementTypeType(value="percentage"),
        commodity_type=CommodityTypeType(value="electricity"),
        unit=UnitOfMeasurementType(value="pct"),
        scope_type=ScopeTypeType(value="stateOfCharge")
    )
    
    assert desc.measurement_type.value == "percentage"
    assert desc.commodity_type.value == "electricity"
    assert desc.unit.value == "pct"
    assert desc.scope_type.value == "stateOfCharge"

    # 2. Measurement Constraints (Recommended)
    # valueRangeMin, valueRangeMax, valueStepSize
    constraints = MeasurementConstraintsDataType(
        measurement_id=None,
        value_range_min=ScaledNumberType(number=NumberType(value=0), scale=ScaleType(value=0)),
        value_range_max=ScaledNumberType(number=NumberType(value=100), scale=ScaleType(value=0)),
        value_step_size=ScaledNumberType(number=NumberType(value=1), scale=ScaleType(value=0))
    )
    
    assert constraints.value_range_min.number.value == 0
    assert constraints.value_range_max.number.value == 100
    assert constraints.value_step_size.number.value == 1

    # 3. Measurement Data
    # valueSource "calculatedValue", value mandatory
    meas_data = MeasurementDataType(
        measurement_id=None,
        value_type=None, # "value" sub identifier
        value=ScaledNumberType(number=NumberType(value=50), scale=ScaleType(value=0)),
        value_source=MeasurementValueSourceType(value="calculatedValue")
    )

    assert meas_data.value.number.value == 50
    assert meas_data.value_source.value == "calculatedValue"


@pytest.mark.requirement("EVSOC-002")
def test_evsoc_scenario2_nominal_capacity():
    """
    Scenario 2: Monitor EV nominal capacity.
    Ref: Table 11: Content of Specialization "ElectricalConnection_EntityEnergyCapacityNominalMax"
    """
    # characteristicContext "entity", characteristicType "energyCapacityNominalMax", unit "Wh"
    char_data = ElectricalConnectionCharacteristicDataType(
        electrical_connection_id=None,
        parameter_id=None,
        characteristic_id=None,
        characteristic_context=ElectricalConnectionCharacteristicContextType(value="entity"),
        characteristic_type=ElectricalConnectionCharacteristicTypeType(value="energyCapacityNominalMax"),
        unit=UnitOfMeasurementType(value="Wh"),
        value=ScaledNumberType(number=NumberType(value=50000), scale=ScaleType(value=0))
    )

    assert char_data.characteristic_context.value == "entity"
    assert char_data.characteristic_type.value == "energyCapacityNominalMax"
    assert char_data.unit.value == "Wh"
    assert char_data.value.number.value == 50000


@pytest.mark.requirement("EVSOC-003")
def test_evsoc_scenario3_state_of_health():
    """
    Scenario 3: Monitor EV state of health.
    Ref: Table 13: Content of Specialization "Measurement_StateOfHealth"
    """
    # 1. Measurement Description
    # scopeType "stateOfHealth", measurementType "percentage", unit "pct"
    desc = MeasurementDescriptionDataType(
        measurement_id=None,
        measurement_type=MeasurementTypeType(value="percentage"),
        unit=UnitOfMeasurementType(value="pct"),
        scope_type=ScopeTypeType(value="stateOfHealth")
    )

    assert desc.measurement_type.value == "percentage"
    assert desc.unit.value == "pct"
    assert desc.scope_type.value == "stateOfHealth"

    # 2. Measurement Constraints (Recommended)
    # valueRangeMin, valueRangeMax, valueStepSize
    constraints = MeasurementConstraintsDataType(
        value_range_min=ScaledNumberType(number=NumberType(value=0), scale=ScaleType(value=0)),
        value_range_max=ScaledNumberType(number=NumberType(value=100), scale=ScaleType(value=0)),
        value_step_size=ScaledNumberType(number=NumberType(value=1), scale=ScaleType(value=0))
    )
    
    assert constraints.value_range_min.number.value == 0
    assert constraints.value_range_max.number.value == 100

    # 3. Measurement Data
    # valueSource can be measured, calculated, or empirical
    meas_data = MeasurementDataType(
        value=ScaledNumberType(number=NumberType(value=95), scale=ScaleType(value=0)),
        value_source=MeasurementValueSourceType(value="measuredValue"),
        value_state=MeasurementValueStateType(value="normal")
    )

    assert meas_data.value_source.value == "measuredValue"
    assert meas_data.value_state.value == "normal"


@pytest.mark.requirement("EVSOC-004")
def test_evsoc_scenario4_travel_range():
    """
    Scenario 4: Monitor EV actual travel range.
    Ref: Table 14: Content of Specialization "Measurement_TravelRange"
    """
    # 1. Measurement Description
    # scopeType "travelRange", measurementType "distance", unit "m"
    desc = MeasurementDescriptionDataType(
        measurement_id=None,
        measurement_type=MeasurementTypeType(value="distance"),
        unit=UnitOfMeasurementType(value="m"),
        scope_type=ScopeTypeType(value="travelRange")
    )

    assert desc.measurement_type.value == "distance"
    assert desc.unit.value == "m"
    assert desc.scope_type.value == "travelRange"

    # 2. Measurement Constraints (Recommended)
    # valueRangeMin, valueRangeMax, valueStepSize
    constraints = MeasurementConstraintsDataType(
        value_range_min=ScaledNumberType(number=NumberType(value=0), scale=ScaleType(value=3)),
        value_range_max=ScaledNumberType(number=NumberType(value=1000), scale=ScaleType(value=3)),
        value_step_size=ScaledNumberType(number=NumberType(value=100), scale=ScaleType(value=0))
    )
    
    assert constraints.value_range_min.number.value == 0
    assert constraints.value_range_max.number.value == 1000

    # 3. Measurement Data
    # valueState is Mandatory [Value state rules]
    meas_data = MeasurementDataType(
        value=ScaledNumberType(number=NumberType(value=300000), scale=ScaleType(value=0)), # 300km
        value_source=MeasurementValueSourceType(value="calculatedValue"),
        value_state=MeasurementValueStateType(value="normal")
    )

    assert meas_data.value.number.value == 300000
    assert meas_data.value_source.value == "calculatedValue"
    # valueState is mandatory R or M depending on condition, but strictly required if set
    assert meas_data.value_state.value == "normal"

