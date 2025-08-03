holdtime join-prune (IPv6 PIM view/VPN instance IPv6 PIM view)
==============================================================

holdtime join-prune (IPv6 PIM view/VPN instance IPv6 PIM view)

Function
--------



The **holdtime join-prune** command globally sets the holdtime for Join/Prune messages sent by PIM interfaces.

The **undo holdtime join-prune** command restores the default value.



By default, the holdtime value in Join/Prune messages sent by all PIM interfaces is 210 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**holdtime join-prune** *joinPruneHoldVal*

**undo holdtime join-prune**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *joinPruneHoldVal* | Specifies the holdtime for Join/Prune messages sent by PIM interfaces. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After receiving a Join/Prune message from a downstream interface, an upstream Router determines the time period for keeping the join or prune state of a downstream interface based on the holdtime field carried in the Join/Prune message. To set a value for the holdtime field, run the holdtime join-prune command. Generally, the holdtime is 3.5 times the interval (specified using the **timer join-prune** command) at which Join/Prune messages are sent.


Example
-------

# In the public network instance, specify 280 seconds as the holdtime value in Join/Prune messages sent by all PIM interfaces.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] holdtime join-prune 280

```