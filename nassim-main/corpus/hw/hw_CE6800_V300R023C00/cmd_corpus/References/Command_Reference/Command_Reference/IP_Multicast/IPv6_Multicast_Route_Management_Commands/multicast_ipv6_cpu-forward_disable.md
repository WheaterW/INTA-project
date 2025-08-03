multicast ipv6 cpu-forward disable
==================================

multicast ipv6 cpu-forward disable

Function
--------



The **multicast ipv6 cpu-forward disable** command disables soft forwarding for IPv6 multicast packets.

The **undo multicast ipv6 cpu-forward disable** command restores the default configuration.



By default, soft forwarding for IPv6 multicast packets is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast ipv6 cpu-forward disable**

**undo multicast ipv6 cpu-forward disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In most cases, the Router forwards packets based on software before the hardware forwarding is completed. After that, the forwards packets based on hardware.Soft forwarding for IPv6 multicast packets must be disabled on the router to prevent the low forwarding speed and first packet cache mechanism of soft forwarding from causing disorder of the first packet transmitted at a high speed.


Example
-------

# Disable soft forwarding for IPv6 multicast packets.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] multicast ipv6 cpu-forward disable

```