interval (TCP test instance)
============================

interval (TCP test instance)

Function
--------



The **interval** command sets the interval at which TCP test packets are sent.

The **undo interval** command restores the default interval.



By default, the interval is 4 seconds.


Format
------

**interval seconds** *interval*

**undo interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **seconds** *interval* | Specifies the interval at which test packets are sent, in seconds. | The value is an integer that ranges from 1 to 60, in seconds. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **probe-count** command sets the number of probes to be sent for an NQA test instance. Based on statistics about these probes, you can evaluate network quality. To set the interval at which test packets are sent in each probe, run the **interval** command.

* On networks with poor quality, the interval at which test packets are sent must be long; otherwise, performing jitter test instances deteriorates the network quality.
* On networks with good quality, the interval at which test packets are sent can be short, because test instances do not take long.

**Configuration Impact**

The interval at which test packets are sent must be longer than or equal to the timeout period specified using the **timeout** command.If the interval at which test packets are sent has been configured, running the **interval** command overrides the configured interval.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the interval at which test packets of the test instance named user test are sent to 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type tcp
[*HUAWEI-nqa-user-test] interval seconds 30

```