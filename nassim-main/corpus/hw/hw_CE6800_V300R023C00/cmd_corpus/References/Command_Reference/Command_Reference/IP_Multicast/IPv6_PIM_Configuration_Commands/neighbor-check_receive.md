neighbor-check receive
======================

neighbor-check receive

Function
--------



The **neighbor-check receive** command enables the IPv6 PIM neighbor check function.

The **undo neighbor-check receive** command restores the default setting.



By default, the IPv6 PIM neighbor check function is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**neighbor-check receive**

**undo neighbor-check receive**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **receive** | Checks whether the Join/Prune and Assert messages are received from an IPv6 PIM neighbor. If not, these messages are discarded. | - |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can specify both receive and send to enable the IPv6 PIM neighbor check function for the received and sent Join/Prune and Assert messages.


Example
-------

# In the public network instance, enable the IPv6 PIM neighbor check function for the received Join/Prune and Assert messages.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] neighbor-check receive

```