threshold rtd (TCP test instance)
=================================

threshold rtd (TCP test instance)

Function
--------



The **threshold rtd** command sets thresholds for the round-trip delay in an NQA TCP test instance.

The **undo threshold rtd** command deletes the thresholds.



By default, no threshold is configured.


Format
------

**threshold rtd** *thresholdRtd*

**undo threshold rtd**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *thresholdRtd* | Specifies the threshold for a round-trip delay. | The value is an integer ranging from 1 to 60000. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set delay thresholds after NQA is configured, run the **threshold rtd** command.The conditions for alarm generation are as follows:

* If the round-trip delay exceeds the parameter thresholdRtd, the nqaJitterStatsRTDThresholdNotification alarm is generated.
* If the round-trip delay is less than the parameter thresholdRtd, the round-trip delay is within an allowable range, and no alarm is generated.

**Prerequisites**

Before using the **threshold rtd** command, run the **test-type** command to specify a test type.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the threshold for the round-trip delay to 2 milliseconds.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type tcp
[*HUAWEI-nqa-user-test] threshold rtd 2

```