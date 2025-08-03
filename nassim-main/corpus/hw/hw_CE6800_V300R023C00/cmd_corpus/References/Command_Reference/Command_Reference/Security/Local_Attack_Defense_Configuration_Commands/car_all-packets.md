car all-packets
===============

car all-packets

Function
--------



The **car all-packets** command limits the number of packets sent to the CPU per second.

The **undo car all-packets** command restores the default maximum number of packets sent to the CPU per second.



By default, you can run the display cpu-defend configuration command to view the CAR of packets sent to the CPU.


Format
------

**car all-packets pps** *pps-value*

**undo car all-packets**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pps** *pps-value* | Specifies the maximum number of packets that are sent to the CPU per second. | The value is an integer ranging from 5000 to 100000. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a large number of packets are sent to the CPU, CPU performance deteriorates. The device limits the number of packets sent to the CPU per second to protect the CPU. The device provides 2-level CAR:

* Level-1 CAR: limits the number of packets based on packet types using the **car** command.
* Level-2 CAR: limits the number of all packets sent to the CPU regardless of the protocol types or queues. This function is configured using the **car all-packets** command.The **car all-packets** command is applicable to the scenario where burst packets are sent to the CPU. The maximum number of packets sent to the CPU specified using the **car all-packets** command must be smaller than that specified by level-1 CAR; otherwise, the **car all-packets** command takes no effect.

**Precautions**

If you run the **car all-packets** command in the same attack defense policy view multiple times, only the latest configuration takes effect.The **car all-packets** command is required only when the current CAR configuration cannot reduce the high CPU usage.When the actual and configured rates of packets sent to the CPU are large, the CPU usage may be high and the performance may deteriorate. In the worst situation, the device breaks.


Example
-------

# Configure the attack defense policy named test to limit the rate of packets sent to the CPU to 5000 pps.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] car all-packets pps 5000

```