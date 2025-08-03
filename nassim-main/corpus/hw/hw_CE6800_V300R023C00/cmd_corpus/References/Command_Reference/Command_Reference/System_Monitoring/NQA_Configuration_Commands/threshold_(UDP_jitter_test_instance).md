threshold (UDP jitter test instance)
====================================

threshold (UDP jitter test instance)

Function
--------



The **threshold** command sets thresholds for the round-trip delay and one-way transmission delay in an NQA UDP jitter test.

The **undo threshold** command deletes the thresholds.



By default, no threshold is configured.


Format
------

**threshold owd-ds** *thresholdOwdDS*

**threshold owd-sd** *thresholdOwdSD*

**threshold rtd** *thresholdRtd*

**undo threshold owd-ds**

**undo threshold owd-sd**

**undo threshold rtd**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **owd-sd** *thresholdOwdSD* | Specifies the threshold for a one-way (from the source to the destination) delay. | The value is an integer ranging from 1 to 60000. |
| **rtd** *thresholdRtd* | Specifies the threshold for a round-trip delay. | The value is an integer ranging from 1 to 60000. |
| **owd-ds** *thresholdOwdDS* | Specifies the threshold for a one-way transmission (from the destination to the source) delay. | The value is an integer ranging from 1 to 60000. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set delay thresholds after NQA is configured, run the **threshold** command.The conditions for alarm generation are as follows:

* If the one-way delay from the destination to the source exceeds the parameter thresholdOwdDS, the nqaJitterStatsOWDThresholdNotificationDS alarm is generated.
* If the one-way delay from the destination to the source is less than the parameter thresholdOwdDS, the one-way delay is within an allowable range, and no alarm is generated.
* If the one-way delay from the source to the destination exceeds the parameter thresholdOwdSD, the nqaJitterStatsOWDThresholdNotificationSD alarm is generated.
* If the one-way delay from the source to the destination is less than the parameter thresholdOwdSD, the one-way delay is within an allowable range, and no alarm is generated.
* If the round-trip delay exceeds the parameter thresholdRtd, the nqaJitterStatsRTDThresholdNotification alarm is generated.
* If the round-trip delay is less than the parameter thresholdRtd, the round-trip delay is within an allowable range, and no alarm is generated.

**Prerequisites**

Before using the send-trap command, run the **test-type** command to specify a test type.

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
[*HUAWEI-nqa-user-test] test-type jitter
[*HUAWEI-nqa-user-test] threshold rtd 2

```

# Set the threshold for the one-way transmission (from the source to the destination) delay to
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type jitter
[*HUAWEI-nqa-user-test] threshold owd-sd 1

```