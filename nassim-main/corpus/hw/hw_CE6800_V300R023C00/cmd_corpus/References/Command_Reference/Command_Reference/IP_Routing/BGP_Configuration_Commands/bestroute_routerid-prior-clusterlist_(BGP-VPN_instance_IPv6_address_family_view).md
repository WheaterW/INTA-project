bestroute routerid-prior-clusterlist (BGP-VPN instance IPv6 address family view)
================================================================================

bestroute routerid-prior-clusterlist (BGP-VPN instance IPv6 address family view)

Function
--------



The **bestroute routerid-prior-clusterlist** command enables Router ID to take precedence over Cluster\_List during BGP route selection.

The **undo bestroute routerid-prior-clusterlist** command restores the default configurations.



By default, Cluster\_List takes precedence over Router ID during BGP route selection.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bestroute routerid-prior-clusterlist**

**undo bestroute routerid-prior-clusterlist**


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

On a BGP network, after a device receives multiple routes with the same prefix but different paths from different peers, the router needs to select an optimal route from these routes to forward packets. By default, Cluster\_List takes precedence over Router ID during BGP route selection. To enable Router ID to take precedence over Cluster\_List during BGP route selection, run the **bestroute routerid-prior-clusterlist** command.

**Precautions**



If each route carries an Originator\_ID, the Originator\_IDs rather than router IDs are compared during route selection. The route with the smallest Originator\_ID is preferred. Therefore, after the **bestroute routerid-prior-clusterlist** command is run, the Originator\_ID takes precedence over the Cluster-List during BGP optimal route selection.




Example
-------

# Enable Router ID to take precedence over Cluster\_List during BGP route selection.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[~HUAWEI-vpn-instance-vrf1] ipv6-family
[~HUAWEI-vpn-instance-vrf1-af-ipv6] quit
[~HUAWEI-vpn-instance-vrf1] quit
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vrf1
[*HUAWEI-bgp6-vrf1] bestroute routerid-prior-clusterlist

```