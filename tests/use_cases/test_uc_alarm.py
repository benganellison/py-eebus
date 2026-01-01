from spine.base_type.alarm import (
    AlarmDataType,
    AlarmListDataType
)
from spine.simple_type.alarm import AlarmIdType
from spine.union_type.alarm import AlarmTypeType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_alarm_data_type():
    """
    Test creation of AlarmDataType and integration with PayloadContributionGroup.
    """
    alarm_data = AlarmDataType(
        alarm_id=AlarmIdType(value=1),
        alarm_type=AlarmTypeType(value="generic"),
        measured_value=None # Optional
    )
    
    # Verify standard attribute access
    assert alarm_data.alarm_id.value == 1
    assert alarm_data.alarm_type.value == "generic"

    # Wrapper
    alarm_list = AlarmListDataType(
        alarm_data=[alarm_data]
    )
    
    # Payload Integration
    payload = PayloadContributionGroup(
        alarm_list_data=alarm_list
    )
    
    assert payload.alarm_list_data is not None
    assert len(payload.alarm_list_data.alarm_data) == 1
    assert payload.alarm_list_data.alarm_data[0].alarm_id.value == 1
