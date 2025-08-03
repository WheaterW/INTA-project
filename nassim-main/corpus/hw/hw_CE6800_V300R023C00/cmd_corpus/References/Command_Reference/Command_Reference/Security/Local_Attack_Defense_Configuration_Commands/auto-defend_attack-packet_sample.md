auto-defend attack-packet sample
================================

auto-defend attack-packet sample

Function
--------



The **auto-defend attack-packet sample** command sets the packet sampling ratio for attack source tracing.

The **undo auto-defend attack-packet sample** command restores the default packet sampling ratio.



By default, the packet sampling ratio is 8. That is, one packet is sampled in every 8 packets.


Format
------

**auto-defend attack-packet sample** *sample-value*

**undo auto-defend attack-packet sample**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sample-value* | Specifies the packet sampling ratio for attack source tracing. | The value is an integer in the range from 1 to 1024. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Attack source tracing samples packets to identify attacks. Errors may occur in attack packet identification or packet rate calculation. A proper packet sampling ratio can reduce errors. A small sampling ratio makes the attack source tracing result accurate, but increases CPU usage. For example, when the sampling ratio is set to 1, every packet is sampled. The attack source tracing result is accurate, but the CPU usage is high because every packet is resolved.The **auto-defend attack-packet sample** command sets the sampling ratio. You can set a proper value based on the requirements of attack source tracing precision and CPU usage.

**Prerequisites**

Attack source tracing has been enabled using the **auto-defend enable** command.

**Precautions**

When a smaller attack source tracing threshold is used, the sampling ratio has greater impact on the attack source tracing result.


Example
-------

# Set the sampling ratio for attack source tracing in the attack defense policy named test to 2.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-defend enable
[*HUAWEI-cpu-defend-policy-test] auto-defend attack-packet sample 2

```