tos (TCP test instance)
=======================

tos (TCP test instance)

Function
--------



The **tos** command sets the ToS value for TCP test packets.

The **undo tos** command restores the default ToS value.



The default ToS value is 0.


Format
------

**tos** *tos-value*

**undo tos**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tos-value* | Specifies the ToS value in test packets. | The value is an integer ranging from 0 to 255. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

ToS is an 8-bit field in the IP header. To set the ToS value for NQA test packets, run the **tos** command.By configuring ToS, you can apply policy-based routing or CAR to test packets.

**Configuration Impact**



If the ToS value has been set for packets in a test instance, running the **tos** command again overrides the previous configuration.



**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the ToS value for packets in the test instance named user test to 10.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type tcp
[*HUAWEI-nqa-user-test] tos 10

```