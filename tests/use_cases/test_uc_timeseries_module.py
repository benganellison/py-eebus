from spine.base_type.timeseries import (
    TimeSeriesDataType,
    TimeSeriesDescriptionDataType,
    TimeSeriesListDataType,
    TimeSeriesDescriptionListDataType
)
from spine.simple_type.timeseries import TimeSeriesIdType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_time_series_description_data_type():
    """
    Test creation of TimeSeriesDescriptionDataType and integration with PayloadContributionGroup.
    """
    ts_desc = TimeSeriesDescriptionDataType(
        time_series_id=TimeSeriesIdType(value=1),
        time_series_writeable=True,
        update_required=False
    )
    
    # Verify standard attribute access (snake_case)
    assert ts_desc.time_series_id.value == 1
    assert ts_desc.time_series_writeable is True

    # Wrapper
    ts_desc_list = TimeSeriesDescriptionListDataType(
        time_series_description_data=[ts_desc]
    )
    
    # Payload Integration
    payload = PayloadContributionGroup(
        time_series_description_list_data=ts_desc_list
    )
    assert payload.time_series_description_list_data is not None
    assert len(payload.time_series_description_list_data.time_series_description_data) == 1

def test_time_series_data_type():
    """
    Test creation of TimeSeriesDataType.
    """
    ts_data = TimeSeriesDataType(
        time_series_id=TimeSeriesIdType(value=1)
    )
    
    assert ts_data.time_series_id.value == 1

    # Wrapper
    ts_list = TimeSeriesListDataType(
        time_series_data=[ts_data]
    )
    
    # Payload Integration
    payload = PayloadContributionGroup(
        time_series_list_data=ts_list
    )
    
    assert payload.time_series_list_data is not None
    assert len(payload.time_series_list_data.time_series_data) == 1
