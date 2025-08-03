source-lifetime
===============

source-lifetime

Function
--------



The **source-lifetime** command sets a timeout period for (S, G) entries.

The **undo source-lifetime** command restores the default value.



By default, the timeout period of (S, G) entries is 210 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**source-lifetime** *src-interval*

**undo source-lifetime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *src-interval* | Specifies a timeout period for (S, G) entries. | The value is an integer ranging from 60 to 65535, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A Router creates a timer for each (S, G) entry. To set a timeout period for those timers, run the **source-lifetime** command. The Router starts the timer after receiving multicast packets from a multicast source for the first time. Each time the Router receives a multicast packet from the source, the Router resets the timer. If no multicast packets are received before timer times out, the (S, G) entry is considered invalid.


Example
-------

# In the public network instance, specify 200 seconds as the timeout period for (S, G) entries.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] source-lifetime 200

```