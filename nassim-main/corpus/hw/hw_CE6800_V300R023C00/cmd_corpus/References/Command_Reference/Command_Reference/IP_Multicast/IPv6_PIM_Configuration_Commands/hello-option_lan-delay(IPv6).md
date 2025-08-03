hello-option lan-delay(IPv6)
============================

hello-option lan-delay(IPv6)

Function
--------



The **hello-option lan-delay** command sets the delay in transmitting Prune messages on a shared network segment.

The **undo hello-option lan-delay** command restores the default value.



By default, the delay in transmitting Prune messages on a shared network segment is 500 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**hello-option lan-delay** *lanDelayValue*

**undo hello-option lan-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *lanDelayValue* | Specifies the period from the time when the router receives a Prune message from a downstream device to the time when the router performs the prune action. | The value is an integer ranging from 1 to 32767, in milliseconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Hello messages sent by the router carry lan-delay and override-interval. lan-delay indicates the delay in transmitting Prune messages in a LAN. When the lan-delay values on all routers on the same link are different, the maximum value of these values is used.If one router receives a Prune message from an upstream interface, other downstream routers still exist in the LAN. If the router still needs to receive multicast data, it must send a Join message to the upstream interface to override the prune action within the set override-interval value.The PPT means the period from the time when the router receives a Prune message from a downstream device to the time when the router performs the prune action. The value of the PPT equals the lan-delay value plus the override-interval value. If a device receives a Join message from its downstream device before the PPT expires, it cancels the prune action.

**Prerequisites**

The **multicast ipv6 routing-enable** command is run in the public network instance view.

**Configuration Impact**

If the hello-option lan-delay command is run more than once, the latest configuration overrides the previous one.

**Precautions**

If the delay in transmitting Prune message is too short, the upstream router will stop forwarding multicast packets before it determines whether to override the Prune action or not. Exercise caution when running this command.


Example
-------

# In the public network instance, set the delay in transmitting Prune messages on a shared network segment to 200 ms.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] hello-option lan-delay 200

```