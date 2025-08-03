rpf-switch-delay max-time
=========================

rpf-switch-delay max-time

Function
--------



The **rpf-switch-delay max-time** command sets the maximum delay in delivering forwarding entries on the new link after a switchback in PIM-SM or PIM-SSM mode.

The **undo rpf-switch-delay max-time** command restores the default delay in delivering forwarding entries on the new link after a switchback in PIM-SM or PIM-SSM mode.



By default, the maximum delay in delivering forwarding entries on a new link after a switchback is the default value. The default value is 350 seconds in PIM-SM mode and 150 seconds in PIM-SSM mode.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**rpf-switch-delay mode sm max-time** *smTimeValue*

**rpf-switch-delay mode ssm max-time** *ssmTimeValue*

**undo rpf-switch-delay mode sm max-time** [ *smTimeValue* ]

**undo rpf-switch-delay mode ssm max-time** [ *ssmTimeValue* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *smTimeValue* | Specifies the maximum SM time, in seconds. | The value is an integer ranging from 1 to 1800, in seconds. |
| **mode** | Indicates the PIM mode. | - |
| **ssm** | Indicates the PIM-SSM mode. | - |
| *ssmTimeValue* | Specifies the maximum SSM time, in seconds. | The value is an integer ranging from 1 to 1800, in seconds. |
| **sm** | Indicates the PIM-SM mode. | - |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a common Layer 3 multicast or PIM FRR switchback scenario, to prevent packet loss caused by the delivery of new interface forwarding entries before traffic on a new forwarding link is received, run the **rpf-switch-delay max-time** command to configure the maximum delay in delivering forwarding entries on the new forwarding link.


Example
-------

# Set the maximum delay in delivering forwarding entries on the new link after a switchback in PIM SSM mode to 160 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] rpf-switch-delay mode ssm max-time 160

```

# Set the maximum delay in delivering forwarding entries on the new link after a switchback in PIM SM mode to 360 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] rpf-switch-delay mode sm max-time 360

```