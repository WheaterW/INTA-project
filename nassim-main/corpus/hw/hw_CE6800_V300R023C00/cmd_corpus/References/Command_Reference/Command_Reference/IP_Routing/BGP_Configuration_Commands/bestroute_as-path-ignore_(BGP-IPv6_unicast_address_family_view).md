bestroute as-path-ignore (BGP-IPv6 unicast address family view)
===============================================================

bestroute as-path-ignore (BGP-IPv6 unicast address family view)

Function
--------



The **bestroute as-path-ignore** command configures BGP to ignore the AS\_Path attribute when it selects optimal routes.

The **undo bestroute as-path-ignore** command restores the default configuration.



By default, BGP uses the AS\_Path attribute as one of route selection rules.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bestroute as-path-ignore**

**undo bestroute as-path-ignore**


Parameters
----------

None

Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the **bestroute as-path-ignore** command is used, BGP does not compare the AS path attributes of routes (including the AS\_Path length and content).

**Configuration Impact**

If the **bestroute as-path-ignore** command is run, the AS\_Path attribute is not used as a BGP route selection rule, which may affect the route selection result. Therefore, exercise caution when running this command.


Example
-------

# Configure BGP to ignore the AS\_Path attribute when selecting the optimal route.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] bestroute as-path-ignore

```