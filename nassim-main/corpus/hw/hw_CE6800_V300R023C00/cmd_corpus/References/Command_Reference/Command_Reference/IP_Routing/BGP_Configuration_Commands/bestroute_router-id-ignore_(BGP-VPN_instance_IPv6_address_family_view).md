bestroute router-id-ignore (BGP-VPN instance IPv6 address family view)
======================================================================

bestroute router-id-ignore (BGP-VPN instance IPv6 address family view)

Function
--------



The **bestroute router-id-ignore** command prevents BGP from comparing router IDs when selecting the optimal route.

The **undo bestroute router-id-ignore** command restores the default configuration.



By default, BGP uses the router ID as one of route selection rules.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bestroute router-id-ignore**

**undo bestroute router-id-ignore**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When receiving multiple routes with the same prefix from different peers, BGP needs to select an optimal route from these routes. To prevent BGP from comparing the router IDs contained in routes when it selects the optimal route, run the **bestroute router-id-ignore** command.

**Configuration Impact**



When selecting the optimal route, BGP does not compare the router IDs and peer IP addresses contained in routes after the **bestroute router-id-ignore** command is run.




Example
-------

# Prevent BGP from comparing router IDs and peer IP addresses contained in routes when selecting the optimal route.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] bestroute router-id-ignore

```