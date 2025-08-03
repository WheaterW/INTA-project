bestroute routerid-prior-clusterlist (BGP-VPN-Target address family view)
=========================================================================

bestroute routerid-prior-clusterlist (BGP-VPN-Target address family view)

Function
--------



The **bestroute routerid-prior-clusterlist** command enables Router ID to take precedence over Cluster\_List during BGP route selection.

The **undo bestroute routerid-prior-clusterlist** command restores the default configurations.



By default, Cluster\_List takes precedence over Router ID during BGP route selection.


Format
------

**bestroute routerid-prior-clusterlist**

**undo bestroute routerid-prior-clusterlist**


Parameters
----------

None

Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a BGP network, after a device receives multiple routes with the same prefix but different paths from different peers, the router needs to select an optimal route from these routes to forward packets. By default, Cluster\_List takes precedence over Router ID during BGP route selection. To enable Router ID to take precedence over Cluster\_List during BGP route selection, run the **bestroute routerid-prior-clusterlist** command.




Example
-------

# Enable Router ID to take precedence over Cluster\_List during BGP route selection.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] bestroute routerid-prior-clusterlist

```