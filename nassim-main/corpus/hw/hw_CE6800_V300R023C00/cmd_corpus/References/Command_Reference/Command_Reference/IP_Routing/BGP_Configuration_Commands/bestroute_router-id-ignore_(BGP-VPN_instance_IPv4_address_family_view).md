bestroute router-id-ignore (BGP-VPN instance IPv4 address family view)
======================================================================

bestroute router-id-ignore (BGP-VPN instance IPv4 address family view)

Function
--------



The **bestroute router-id-ignore** command prevents BGP from comparing router IDs when selecting the optimal route.

The **undo bestroute router-id-ignore** command restores the default configuration.



By default, BGP uses the router ID as one of route selection rules.


Format
------

**bestroute router-id-ignore**

**undo bestroute router-id-ignore**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv4 address family view


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
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] bestroute router-id-ignore

```