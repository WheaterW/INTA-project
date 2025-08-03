send-trap (Trace test instance)
===============================

send-trap (Trace test instance)

Function
--------



The **send-trap** command configures conditions for sending a trap message in an NQA trace test.

The **undo send-trap** command deletes the configured conditions for sending a trap message.



By default, no trap messages are sent in any condition.


Format
------

**send-trap** { **all** | { **rtd** | **testfailure** | **testcomplete** | **testresult-change** } \* }

**undo send-trap** { **all** | { **rtd** | **testfailure** | **testcomplete** | **testresult-change** } \* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Indicates that trap messages are sent in any of the following situations. | - |
| **rtd** | Indicates that a trap message is sent if the RTD reaches the specified threshold. | - |
| **testfailure** | Indicates that a trap message is sent if a test fails. | - |
| **testcomplete** | Indicates that a trap message is sent after a test is complete. | - |
| **testresult-change** | Indicates that a trap message is sent when the test result changes. | - |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Traps are generated no matter whether the NQA test succeeds or fails. You can determine whether traps are sent to the NMS by enabling or disabling the trap function.The send-trap command can be used to configure conditions for sending a trap message. If the specified conditions are met, the system sends a trap to the NMS.

**Prerequisites**



Before using the send-trap command, run the **test-type** command to specify a test type.



**Precautions**

1. When the trap function is enabled for multiple test instances at the same time, a large number of traps (logs) may be generated. As a result, the CPU usage increases and other services are affected.
2. probefailure indicates that probes fail to be sent consecutively within a test period. If the number of consecutive probe failures reaches the threshold specified using the **probe-failtimes** command, a trap is generated. testfailure indicates that all probes fail to be sent within a test period. If the number of failures reaches the threshold specified using the **test-failtimes** command, a trap is generated. For example, if three probes are sent in a test period and the thresholds specified using the probe-failtimes and **test-failtimes** commands are both set to 1, a probefailure alarm is triggered when one probe fails to be sent and two probes are successfully sent. If all three probes fail to be sent, a testfailure alarm is triggered.
3. If you change the value of this parameter during the running of a test instance, the system prompts you whether to stop the test instance. Press "Y" or "N" as required.

* If you enter Y, the current test instance is stopped and parameters are modified. After you submit the modification, the modified parameters take effect. To restart the test instance, run the **start** command.
* If you enter N, the parameter modification fails and the current test instance continues to run.

Example
-------

# Configure a test instance named user test to send a trap message if the RTD reaches the specified threshold.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type trace
[*HUAWEI-nqa-user-test] send-trap rtd

```