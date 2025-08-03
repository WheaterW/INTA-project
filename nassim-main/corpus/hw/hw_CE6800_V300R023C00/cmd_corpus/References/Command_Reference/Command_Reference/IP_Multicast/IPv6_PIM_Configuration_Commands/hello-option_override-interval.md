hello-option override-interval
==============================

hello-option override-interval

Function
--------



The **hello-option override-interval** command sets the interval for overriding the prune action.

The **undo hello-option override-interval** command restores the default value.



By default, the interval for overriding the prune action is 2500 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**hello-option override-interval** *overIntvValue*

**undo hello-option override-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *overIntvValue* | Specifies the interval for overriding the Prune action. | The value is an integer ranging from 1 to 65535, in milliseconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Hello messages sent by the router carry lan-delay and override-interval. override-interval specifies the period during which a downstream router overrides the prune action. When the override-interval values on all routers on the same link are different, the maximum value of these values is used.If one router receives a Prune message from an upstream interface, other downstream routers still exist in the LAN. If the router still needs to receive multicast data, it must send a Join message to the upstream interface to override the prune action within the set override-interval value.When receiving a Prune message from a downstream device, the router does not perform the prune action immediately until the PPT expires. The PPT equals the lan-delay value plus the override-interval value. If a device receives a Join message from its downstream device before the PPT expires, it cancels the prune action.


Example
-------

# In the public network instance, set the interval for overriding the prune action to 2000 ms.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] hello-option override-interval 2000

```