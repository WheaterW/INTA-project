probe-failtimes (TCP test instance)
===================================

probe-failtimes (TCP test instance)

Function
--------



The **probe-failtimes** command configures a threshold for the number of consecutive probe failures in an NQA TCP test instance. Once this threshold is reached, a trap is sent to the NMS.

The **undo probe-failtimes** command restores the default configuration.



By default, a trap is sent for each probe failure.


Format
------

**probe-failtimes** *failTimes*

**undo probe-failtimes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *failTimes* | Specifies the threshold for the number of consecutive probe failures in an NQA test instance. | The value is an integer ranging from 1 to 15. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An NQA test checks whether response packets are received in a probe. If no response to a probe packet is received, the probe fails. When the number of consecutive probe failures in an NQA test instance reaches the specified threshold, a trap is sent to the NMS.This command is used to set the number of consecutive probe failures, that is, the number of consecutive packet sending failures. The **test-failtimes** command is used to set the number of consecutive test failures. Multiple packets may be sent in a test, that is, a test may contain multiple probes.

**Prerequisites**

The type of an NQA test instance has been specified using the **test-type** command.

**Follow-up Procedure**

After the **probe-failtimes** command is executed, run the **send-trap probefailure** command to enable the system to send traps to the NMS after the number of consecutive probe failures reaches the specified threshold.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set times in an NQA test instance named user test to 10.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type tcp
[*HUAWEI-nqa-user-test] probe-failtimes 10

```