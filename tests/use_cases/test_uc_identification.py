from spine.base_type.identification import (
    IdentificationDataType,
    IdentificationListDataType,
    SessionIdentificationDataType,
    SessionIdentificationListDataType
)
from spine.simple_type.identification import IdentificationIdType, SessionIdType
from spine.union_type.identification import IdentificationTypeType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_identification_data_type():
    """
    Test creation of IdentificationDataType.
    """
    ident_data = IdentificationDataType(
        identification_id=IdentificationIdType(value=1),
        identification_type=IdentificationTypeType(value="eui48"),
        authorized=True
    )
    
    assert ident_data.identification_id.value == 1
    assert ident_data.identification_type.value == "eui48"
    assert ident_data.authorized is True

    # Wrapper
    ident_list = IdentificationListDataType(
        identification_data=[ident_data]
    )
    
    # Payload Integration
    payload = PayloadContributionGroup(
        identification_list_data=ident_list
    )
    
    assert payload.identification_list_data is not None
    assert len(payload.identification_list_data.identification_data) == 1

def test_session_identification_data_type():
    """
    Test creation of SessionIdentificationDataType.
    """
    session_data = SessionIdentificationDataType(
        session_id=SessionIdType(value=100),
        identification_id=IdentificationIdType(value=1),
        is_latest_session=True
    )
    
    assert session_data.session_id.value == 100
    assert session_data.identification_id.value == 1

    # Wrapper
    session_list = SessionIdentificationListDataType(
        session_identification_data=[session_data]
    )
    
    # Payload Integration
    payload = PayloadContributionGroup(
        session_identification_list_data=session_list
    )
    
    val = payload.session_identification_list_data
    assert val is not None
    assert len(val.session_identification_data) == 1
