bestroute igp-metric-ignore (BGP-IPv4 unicast address family view)
==================================================================

bestroute igp-metric-ignore (BGP-IPv4 unicast address family view)

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

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a BGP network, a device often receives multiple routes with the same prefix but different paths from multiple peers. In this case, BGP needs to select the optimal route to the prefix to guide packet forwarding. By default, BGP compares the IGP metrics of the next hops of these routes and prefers the route with the smallest IGP metric.To customize route selection policies based on user requirements, run the **bestroute igp-metric-ignore** command to change BGP route selection rules. After the **bestroute igp-metric-ignore** command is run, BGP does not compare the IGP metrics of routes to next hops during route selection.


Example
-------

# Configure BGP to ignore the IGP cost when selecting the optimal route.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] bestroute igp-metric-ignore

```