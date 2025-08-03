timer join-prune(IPv6)
======================

timer join-prune(IPv6)

Function
--------



The **timer join-prune** command globally sets an interval at which PIM interfaces send Join/Prune messages upstream.

The **undo timer join-prune** command restores the default value.



By default, all PIM interfaces send Join/Prune messages upstream at an interval of 60 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**timer join-prune** *interval*

**undo timer join-prune**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which PIM interfaces send Join/Prune messages upstream. | The value is an integer ranging from 1 to 18000, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a router receives a Join/Prune message, the router updates the downstream interface status to maintain the (S, G) or (\*, G) entry. To set the interval at which PIM interfaces send Join/Prune messages upstream, run the timer join-prune command.


Example
-------

# In the public network instance, specify 80 seconds as the interval at which PIM interfaces send Join/Prune messages upstream.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] timer join-prune 80

```