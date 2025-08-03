bestroute routerid-prior-clusterlist (BGP-VPN instance IPv4 address family view)
================================================================================

bestroute routerid-prior-clusterlist (BGP-VPN instance IPv4 address family view)

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

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a BGP network, after a device receives multiple routes with the same prefix but different paths from different peers, the router needs to select an optimal route from these routes to forward packets. By default, Cluster\_List takes precedence over Router ID during BGP route selection. To enable Router ID to take precedence over Cluster\_List during BGP route selection, run the **bestroute routerid-prior-clusterlist** command.

**Precautions**



If each route carries an Originator\_ID, the Originator\_IDs rather than router IDs are compared during route selection. The route with the smallest Originator\_ID is preferred. Therefore, after the **bestroute routerid-prior-clusterlist** command is run, the Originator\_ID takes precedence over the Cluster-List during BGP optimal route selection.




Example
-------

# Enable Router ID to take precedence over Cluster\_List during BGP route selection.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] bestroute routerid-prior-clusterlist

```