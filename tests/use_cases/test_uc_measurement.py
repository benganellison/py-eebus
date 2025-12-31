from spine.simple_type.measurement import MeasurementIdType
from spine.union_type.measurement import MeasurementValueStateType, MeasurementTypeType, MeasurementValueTypeType
from spine.base_type.measurement import MeasurementDataType, MeasurementDataElementsType, MeasurementListDataType, MeasurementDescriptionDataType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_uc_measurement():
    # Test MeasurementIdType
    meas_id = MeasurementIdType(value=1)
    assert meas_id.value == 1

    # Test Union Types
    state = MeasurementValueStateType(value="required")
    assert state.value == "required"
    
    m_type = MeasurementTypeType(value="current")
    assert m_type.value == "current"

    val_type = MeasurementValueTypeType(value="average")
    assert val_type.value == "average"

    # Test MeasurementDataType
    data = MeasurementDataType(
        measurement_id=meas_id,
        value_state=state,
        value_type=val_type
    )
    assert data.measurement_id.value == 1
    assert data.value_state.value == "required"
    assert data.value_type.value == "average"

    # Test MeasurementDescriptionDataType
    desc = MeasurementDescriptionDataType(
        measurement_id=meas_id,
        measurement_type=m_type
    )
    assert desc.measurement_id.value == 1
    assert desc.measurement_type.value == "current"

    # Test List wrapper
    data_list = MeasurementListDataType(
        measurement_data=[data]
    )

    # Test PayloadContributionGroup
    payload = PayloadContributionGroup(
        measurement_list_data=data_list
    )
    
    assert payload.measurement_list_data is not None
    assert payload.measurement_list_data.measurement_data[0].value_type.value == "average"
