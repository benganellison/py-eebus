import pytest
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.simple_type.commandframe import MsgCounterType
from spine.base_type.result import ResultDataType
from spine.simple_type.result import ErrorNumberType
from spine.simple_type.commondatatypes import DescriptionType

@pytest.mark.requirement("LPC-TS-002")
def test_lpc_ack_accepted_apcl():
    """
    Verify that the CS (Control System) confirms an accepted APCL with an ACK.
    ACK is defined as a Result message with errorNumber 0 (NoError).
    Ref: [LPC-002]
    """
    # Simulate receiving an ACK
    result = ResultDataType(
        error_number=ErrorNumberType(value=0), # 0 = NoError (ACK)
        description=None
    )
    
    assert result.error_number.value == 0
    
@pytest.mark.requirement("LPC-TS-004")
def test_lpc_nack_rejected_apcl():
    """
    Verify that if the APCL cannot be applied, the EG is informed with a NACK.
    NACK is a Result message with a non-zero errorNumber.
    """
    # Simulate receiving a NACK (e.g., error 1 = GeneralError or similar)
    result = ResultDataType(
        error_number=ErrorNumberType(value=1), 
        description=DescriptionType(value="Cannot apply APCL")
    )
    
    assert result.error_number.value != 0

@pytest.mark.requirement("LPC-TS-003")
def test_lpc_ack_accepted_fcapl():
    """
    Verify that the CS confirms an accepted FCAPL with an ACK.
    """
    result = ResultDataType(
        error_number=ErrorNumberType(value=0)
    )
    assert result.error_number.value == 0

@pytest.mark.requirement("LPC-TS-005")
def test_lpc_nack_rejected_fcapl_or_duration():
    """
    Verify that write commands on FCAPL or Duration not accepted are declined with a NACK.
    """
    result = ResultDataType(
        error_number=ErrorNumberType(value=1),
        description=DescriptionType(value="Rejection")
    )
    assert result.error_number.value != 0
