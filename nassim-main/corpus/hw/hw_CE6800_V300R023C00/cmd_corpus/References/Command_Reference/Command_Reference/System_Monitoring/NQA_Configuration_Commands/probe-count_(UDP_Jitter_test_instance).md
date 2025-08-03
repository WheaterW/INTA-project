probe-count (UDP Jitter test instance)
======================================

probe-count (UDP Jitter test instance)

Function
--------



The **probe-count** command sets the number of probes for an NQA test instance of UDP Jitter test.

The **undo probe-count** command restores the default number of probes.



By default, the number of probes is 3.


Format
------

**probe-count** *number*

**undo probe-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the number of probes in a test instance. | The value is an integer ranging from 1 to 15. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On unreliable networks, to set the number of probes for an NQA test instance, run the **probe-count** command. Then, you can monitor network quality by analyzing the probe statistics.

**Configuration Impact**

In a jitter test instance, the product of the number of the jitter tests specified using the **probe-count** command multiplied by the number of the test packets specified using the **jitter-packetnum** command cannot be greater than 3000.If the number of probes has been configured for an NQA test instance, running the **probe-count** command again overrides the previous configuration.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the number of the probes for the test instance named user test to 15.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type jitter
[*HUAWEI-nqa-user-test] probe-count 15

```