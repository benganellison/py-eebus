# EEBUS LPC Traceability Matrix

| Requirement ID | Description Snippet | Test Status | Implemented In |
| :--- | :--- | :--- | :--- |
| LPC-TS-001 | The APCL SHALL always be greater than or equal to zero as defined in [LPC1.0.0], | Covered | tests/use_cases/test_uc_lpc.py |
| LPC-TS-001/1 | A limit MAY have a duration that states the time the limit is valid for as defined in | Pending |  |
| LPC-TS-001/2 | The EG MAY activate or deactivate the limit as defined in [LPC1.0.0], Ref No: [LPC- | Pending |  |
| LPC-TS-002 | The CS SHALL confirm an accepted APCL with an ACK as defined in [LPC1.0.0], Ref | Pending |  |
| LPC-TS-003 | The CS SHALL confirm an accepted FCAPL with an ACK as defined in [LPC1.0.0], Ref | Pending |  |
| LPC-TS-004 | If the APCL value cannot be applied by the CS, the EG SHALL be informed with a | Pending |  |
| LPC-TS-005 | Write commands on the FCAPL or Failsafe Duration Minimum, that are not | Pending |  |
| LPC-TS-006 | The heartbeat of the EG SHALL be sent at least every 60 seconds as defined in | Covered | tests/use_cases/test_uc_lpc_heartbeat.py |
| LPC-TS-007 | The heartbeat of the CS SHALL be sent at least every 60 seconds as defined in | Pending |  |
| LPC-TS-008 | If the CS has a duration set on the APCL it SHALL deactivate the limit as soon as the | Pending |  |
| LPC-TS-008/1 | The CS MAY remove the duration as soon as the duration is expired as defined in | Pending |  |
| LPC-TS-009 | The CS SHALL set the APCL to "activated" or "deactivated" according to its state as | Pending |  |
| LPC-TS-009/1 | If in state "limited" the APCL SHALL be activated as defined in [LPC1.0.0], Ref No: | Pending |  |
| LPC-TS-009/2 | After a (re)start the APCL SHALL be deactivated by the CS as defined in [LPC1.0.0], | Pending |  |
| LPC-TS-009/3 | If in state "init", "unlimited/controlled", "failsafe state" or | Pending |  |
| LPC-TS-010 | The CS SHALL NOT consume more than the according nominal maximum value as | Pending |  |
| LPC-TS-010/1 | In case the CS is not located on a CEM, it SHOULD inform the EG about its Power | Pending |  |
| LPC-TS-010/2 | The Power Consumption Nominal Max SHOULD be supported if the CS is not | Pending |  |
| LPC-TS-010/3 | In case the CS is located on a CEM, it SHOULD inform the EG about its Contractual | Pending |  |
| LPC-TS-010/4 | The Contractual Consumption Nominal Max SHOULD be supported if the CS is | Pending |  |
| LPC-TS-011 | A default value for the FCAPL SHALL be configured as defined in [LPC1.0.0], Ref No: | Covered | tests/use_cases/test_uc_lpc.py, tests/use_cases/test_uc_lpc_failsafe.py |
| LPC-TS-011/1 | The FCAPL value MAY be changed by the EG as defined in [LPC1.0.0], Ref No: [LPC- | Pending |  |
| LPC-TS-011/2 | As soon as the EG changes the FCAPL value in the CS, the value of the CS SHOULD | Pending |  |
| LPC-TS-012 | The CS SHALL remain in the "failsafe state" for at least the duration specified in the | Pending |  |
| LPC-TS-013 | The Failsafe Duration Minimum SHALL be pre-configured by the vendor of the CS in | Covered | tests/use_cases/test_uc_lpc_failsafe.py |
| LPC-TS-013/1 | The value MAY be changed by the EG as defined in [LPC1.0.0], Ref No: [LPC-022/2], | Pending |  |
| LPC-TS-013/2 | As soon as the EG changes the Failsafe Duration Minimum value in the CS, the | Pending |  |
| LPC-TS-014 | The maximum value for the Failsafe Duration Minimum of the CS is defined as the | Pending |  |
| LPC-TS-015 | The EG SHALL choose a value for the Failsafe Duration Minimum between 2 hours | Pending |  |
| LPC-TS-015/1 | The CS MAY reject a write command of the EG on the Failsafe Duration Minimum if | Pending |  |
| LPC-TS-016 | If the CS rejects the write command on the Failsafe Duration Minimum by the EG | Pending |  |
| LPC-TS-017 | After a restart the CS SHALL begin with a limited consumption stated in the FCAPL | Pending |  |
| LPC-TS-017/1 | If the CS is located on a CEM it MAY exceed the FCAPL while specific conditions | Pending |  |
| LPC-TS-018 | If the CS receives a heartbeat from the EG and a following activated power limit | Pending |  |
| LPC-TS-019 | If there was no change of the FCAPL by the EG before restart or if the earlier | Pending |  |
| LPC-TS-020 | If the CS receives an EG heartbeat and a following activated power limit which is | Pending |  |
| LPC-TS-021 | If the CS receives an EG heartbeat and a following deactivated power limit in state | Pending |  |
| LPC-TS-022 | If in state "init" or "failsafe state" the CS MAY switch into "unlimited/autonomous" | Pending |  |
| LPC-TS-022/1 | If the CS does not receive any Heartbeat or receives a heartbeat but no following | Pending |  |
| LPC-TS-022/2 | The CS MAY leave the "failsafe state" and switch into "unlimited/autonomous" | Pending |  |
| LPC-TS-022/3 | The CS MAY leave the "failsafe state" after expiry of the Failsafe Duration | Pending |  |
| LPC-TS-022/4 | If the CS is located on a CEM it MAY exceed the FCAPL, but only if and just as long | Pending |  |
| LPC-TS-022/5 | If the CS is not located on a CEM it MAY exceed the FCAPL, but only if and just as | Pending |  |
| LPC-TS-023 | If the CS rejects the write command on the APCL, the CS SHALL stay in its state if it | Pending |  |
| LPC-TS-024 | If the CS rejects the write command on the APCL, the CS SHALL stay in its state if it | Pending |  |
| LPC-TS-025 | If in state "limited" the CS SHALL switch into state "unlimited/controlled" after the | Pending |  |
| LPC-TS-026 | If in state "limited" the CS SHALL switch into state "unlimited/controlled" after | Pending |  |
| LPC-TS-027 | If in state "unlimited/controlled" the CS SHALL switch into state "limited" after | Pending |  |
| LPC-TS-028 | If in state "unlimited/controlled" the CS SHALL switch into state "failsafe state" | Covered | tests/use_cases/test_uc_lpc_statemachine.py |
| LPC-TS-029 | If in state "limited" the CS SHALL switch into state "failsafe state" after not | Covered | tests/use_cases/test_uc_lpc_statemachine.py |
| LPC-TS-030 | After initial connection or restoration of communication, the EG SHALL send a | Pending |  |
| LPC-TS-031 | If in state "failsafe state" or "unlimited/autonomous" the CS SHALL switch into | Pending |  |
| LPC-TS-032 | If in state "failsafe state" or "unlimited/autonomous" the CS SHALL switch into | Pending |  |
| LPC-TS-033 | If in state "failsafe state" or "unlimited/autonomous" the CS SHALL switch into | Pending |  |
| LPC-TS-034 | If the CS is on a CEM, the CEM SHALL manage its connected devices in a way that | Pending |  |
| LPC-TS-035 | Upon receival of the APCL the CS SHALL evaluate its ability or inability to apply the | Pending |  |
| LPC-TS-035/1 | An APCL lower than 0W SHALL be rejected by the CS as defined in [LPC1.0.0], 2.2. | Pending |  |
| LPC-TS-035/2 | If the CS is located on a CEM, the CS SHALL apply the APCL unless the rejection of | Pending |  |
| LPC-TS-035/3 | If the CS is not located on a CEM, the CS SHALL apply the APCL unless the rejection | Pending |  |
| LPC-TS-035/4 | An APCL MAY be larger than the device's possible maximum consumption. If this | Pending |  |
| LPC-TS-036 | In state "init", "failsafe state" or "unlimited/autonomous", only after a heartbeat | Pending |  |
| LPC-TS-037 | In state "init", "failsafe state" or "unlimited/autonomous", only after a heartbeat | Pending |  |
| LPC-TS-038 | The FCAPL, Power Consumption Nominal Max and Contractual Consumption | Pending |  |
| LPC-TS-039 | The Power Consumption Nominal Max value SHALL NOT be supported if the CS is a | Pending |  |
| LPC-TS-040 | The Contractual Consumption Nominal Max value SHALL NOT be supported if the | Pending |  |
| LPC-TS-041 | The data point Failsafe Duration Minimum of this Use Case SHALL be the same as | Pending |  |
| LPC-TS-042 | In case of an implementation of this Use Case on an Inverter, the Use Case | Pending |  |
| LPC-TS-042/1 | The rules regarding the resource hierarchy of the Inverter SHALL be followed as | Pending |  |
| LPC-TS-043 | The EG SHOULD support both "Monitoring of Grid Connection Point" and | Pending |  |
| LPC-TS-043/1 | The EG SHOULD monitor the actual power consumption of the CS as defined in | Pending |  |
| LPC-TS-043/2 | The CS SHOULD provide its actual power consumption as defined in [LPC1.0.0], 2.2. | Pending |  |
| LPC-TS-043/3 | If the CS is located on a CEM, the Use Case "Monitoring of Grid Connection Point" | Pending |  |
| LPC-TS-043/4 | If the CS is not located on a CEM, the Use Case "Monitoring of Power | Pending |  |
| LPC-TS-044 | The CS SHOULD store changed FCAPL and Failsafe Duration Minimum values | Pending |  |
| LPC-TS-045 | If in state "limited" the CS MAY deactivate the APCL and switch into state | Pending |  |
| LPC-TS-046 | An EG should be aware of the possibility of its write commands being rejected (due | Pending |  |
