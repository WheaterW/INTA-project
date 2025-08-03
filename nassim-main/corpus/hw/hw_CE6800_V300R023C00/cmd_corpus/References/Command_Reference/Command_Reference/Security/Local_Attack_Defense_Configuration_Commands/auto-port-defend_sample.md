auto-port-defend sample
=======================

auto-port-defend sample

Function
--------



The **auto-port-defend sample** command sets the protocol packet sampling ratio for port attack defense.

The **undo auto-port-defend sample** command restores the default protocol packet sampling ratio for port attack defense.



By default, the packet sampling ratio is 8. That is, one packet is sampled in every 8 packets.


Format
------

**auto-port-defend sample** *sample-value*

**undo auto-port-defend sample**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sample-value* | Specifies the packet sampling ratio for auto port defend. | The value is an integer in the range from 1 to 1024. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A device with port attack defense enabled identifies attacks by analyzing sampled packets. There may be errors in attack packet identification or packet rate calculation. Errors influence the attack defense effect. An appropriate sampling ratio helps you control attack defense accuracy.A small sampling ratio improves attack defense accuracy, but consumes more CPU resources. When the sampling ratio is set to 1, the device analyzes every packet. The attack packets can be detected quickly, but CPU usage becomes high and services are affected. Therefore, make a balance between the attack defense requirement and CPU usage to decide a sampling ratio.

**Precautions**

If the protocol packet rate threshold for port attack defense is set to a small value, the attack identification error caused by packet sampling ratio is large.


Example
-------

# Set the protocol packet sampling ratio to 4 in the attack defense policy test view.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-port-defend sample 4

```