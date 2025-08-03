test-failtimes (ICMP Jitter test instance)
==========================================

test-failtimes (ICMP Jitter test instance)

Function
--------



The **test-failtimes** command sets the threshold for the number of consecutive failures of an NQA ICMP jitter test instance. Once this threshold is reached, a trap is sent to the NMS.

The **undo test-failtimes** command restores the default threshold for the number of consecutive failures of an NQA ICMP jitter test instance.



By default, an NQA test instance sends a trap message for each test failure.


Format
------

**test-failtimes** *failTimes*

**undo test-failtimes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *failTimes* | Specifies the number of consecutive failures of an NQA test. | The value is an integer ranging from 1 to 15. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a test, each time a packet is sent for a test, it is called a probe. The difference between this command and the **probe-failtimes** command is that the **probe-failtimes** command is used to configure the number of consecutive probe failures, that is, the number of consecutive packet sending failures. This command is used to set the number of consecutive test failures. Multiple packets may be sent in a test, that is, a test may contain multiple probes.By default, a test is considered as a success if one or more probes in the test succeed; a test is considered failed if all probes in the test fail.After the **test-failtimes** command is run for an NQA test instance, traps will be sent only when send-trap is enabled.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the threshold for the number of consecutive failures to 10 for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmpjitter
[*HUAWEI-nqa-user-test] test-failtimes 10

```