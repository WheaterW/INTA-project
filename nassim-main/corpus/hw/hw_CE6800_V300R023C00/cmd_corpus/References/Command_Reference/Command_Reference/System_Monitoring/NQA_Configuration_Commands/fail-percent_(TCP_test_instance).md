fail-percent (TCP test instance)
================================

fail-percent (TCP test instance)

Function
--------



The **fail-percent** command sets the failure percent threshold for an NQA test instance of TCP test type.

The **undo fail-percent** command deletes the failure percent threshold.



By default, the failure percent threshold is 100. A test is considered failed only after all probes fail.


Format
------

**fail-percent** *percent*

**undo fail-percent**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *percent* | Specifies the percent threshold of the failed NQA probes. | The value is an integer that ranges from 1 to 100. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A test consists of several probes. On an unreliable network, the **probe-count** command can be used to set the number of probes for an NQA test instance. The analysis on statistics about probe packets helps you monitor network quality.Some or all sent probe packets may be discarded. In this case, you can run the **fail-percent** command to set the failure percent threshold. When the number of failed probes reaches the specified percent threshold, the test is considered failed.For example, 10 probes are set using the **probe-count** command, and seven probes fail.

* If the failure percent threshold is set to 80, the probe failure percentage (70%) is lower than 80%, and therefore, the test instance is successful.
* If the failure percent threshold is set to 60, the probe failure percentage (70%) is higher than 60%, and therefore, the test instance fails.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the failure percent threshold to 10 for a test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type tcp
[*HUAWEI-nqa-user-test] fail-percent 10

```