bestroute igp-metric-ignore (BGP-EVPN address family view)
==========================================================

bestroute igp-metric-ignore (BGP-EVPN address family view)

Function
--------



The **bestroute igp-metric-ignore** command configures BGP to ignore the IGP cost when selecting the optimal route.

The **undo bestroute igp-metric-ignore** command restores the default configuration.



By default, BGP uses the IGP cost as one of route selection rules.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bestroute igp-metric-ignore**

**undo bestroute igp-metric-ignore**


Parameters
----------

None

Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a BGP EVPN network, the router often receives multiple routes with the same prefix but different paths from different peers. To forward traffic to that prefix address, BGP needs to select an optimal route from these routes. By default, BGP will compare the IGP costs of these routes to their BGP next hops and select a route with the smallest IGP cost.The **bestroute igp-metric-ignore** command can be run to configure BGP to ignore the IGP costs in route selection.

**Configuration Impact**

After the **bestroute igp-metric-ignore** command is run, BGP does not compare the IGP costs of routes to BGP next hops.


Example
-------

# Configure BGP to ignore the IGP cost when selecting the optimal route in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] bestroute igp-metric-ignore

```