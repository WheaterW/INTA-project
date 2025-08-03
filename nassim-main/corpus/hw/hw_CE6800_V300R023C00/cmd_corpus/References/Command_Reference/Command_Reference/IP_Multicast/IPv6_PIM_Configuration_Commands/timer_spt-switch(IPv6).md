timer spt-switch(IPv6)
======================

timer spt-switch(IPv6)

Function
--------



The **timer spt-switch** command sets the interval for checking whether the rate at which multicast data is transmitted exceeds the threshold that can trigger data switching from a rendezvous point tree (RPT) to a shortest path tree (SPT).

The **undo timer spt-switch** command restores the default value.



By default, the interval is 15 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**timer spt-switch** *interval*

**undo timer spt-switch**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Interval for checking whether the rate at which multicast data is transmitted exceeds the threshold that can trigger data switching from an RPT to an SPT. | The value is an integer that ranges from 15 to 65535, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before using the **timer spt-switch** command, you must use the **spt-switch-threshold** command to set the rate threshold that can trigger data switching from an RPT to an SPT. Otherwise, running the **timer spt-switch** command is meaningless.

**Prerequisites**

The **multicast ipv6 routing-enable** command is run in the public network instance view.

**Configuration Impact**

If the **timer spt-switch** command is run several times, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, set the interval for checking whether the rate at which multicast data is transmitted exceeds the threshold that can trigger data switching from an RPT to an SPT to 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] timer spt-switch 30

```