bestroute igp-metric-ignore (BGP-VPN instance IPv4 address family view)
=======================================================================

bestroute igp-metric-ignore (BGP-VPN instance IPv4 address family view)

Function
--------



The **bestroute igp-metric-ignore** command configures BGP to ignore the IGP cost when selecting the optimal route.

The **undo bestroute igp-metric-ignore** command restores the default configuration.



By default, BGP uses the IGP cost as one of route selection rules.


Format
------

**bestroute igp-metric-ignore**

**undo bestroute igp-metric-ignore**


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

On a BGP network, a device often receives multiple routes with the same prefix but different paths from different peers. To forward traffic to that prefix address, BGP needs to select an optimal route from these routes. By default, BGP will compare the IGP costs of these routes to their BGP next hops and select a route with the smallest IGP cost.The **bestroute igp-metric-ignore** command can be run to configure BGP to ignore the IGP costs in route selection.

**Configuration Impact**



After the **bestroute igp-metric-ignore** command is run, BGP does not compare the IGP costs of routes to BGP next hops.




Example
-------

# Configure BGP to ignore the IGP cost when selecting the optimal route.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] bestroute igp-metric-ignore

```