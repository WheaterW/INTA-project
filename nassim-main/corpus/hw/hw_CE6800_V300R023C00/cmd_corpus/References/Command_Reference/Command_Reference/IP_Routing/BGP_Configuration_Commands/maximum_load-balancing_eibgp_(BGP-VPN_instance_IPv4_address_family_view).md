maximum load-balancing eibgp (BGP-VPN instance IPv4 address family view)
========================================================================

maximum load-balancing eibgp (BGP-VPN instance IPv4 address family view)

Function
--------

By default, the maximum number of EBGP and IBGP routes for load balancing is 1, and load balancing is not implemented.


Format
------

**maximum load-balancing eibgp** *number*

**maximum load-balancing eibgp** *number* **ecmp-nexthop-changed**

**undo maximum load-balancing eibgp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of equal-cost EBGP and IBGP routes. | The value is an integer ranging from 1 to 128. |
| **ecmp-nexthop-changed** | Configures the device to change the next hop addresses of only the routes that carry out load balancing to its address. | - |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **maximum load-balancing eibgp** command is mainly used in the scenario where a CE in a VPN is multi-homed to the same PE. In this case, you can set the number of EBGP and IBGP routes for load balancing in another VPN so that the route type (EBGP or IBGP) is not used as a judgment condition, in this manner, private network traffic can be load balanced among EBGP and IBGP routes.Description:After the **maximum load-balancing eibgp** command is run, the changes the next hop addresses of the routes to be advertised to a local address, regardless of whether the routes are used for load balancing. However, in RR and BGP confederation scenarios, the device does not change the next hop of a non-local route to the local address.After the **maximum load-balancing eibgp ecmp-nexthop-changed** command is run, the device changes the next hop addresses of the routes to be advertised to a local address only when the routes are used for load balancing. When advertising routes that are not used for load balancing, the device does not process the next hops of the routes. That is, the original next hops of the routes are the same as the next hops of the routes that are not used for load balancing.In Add-Path scenarios, the next hops of Add-Path routes to be advertised are processed in the same way as those of optimal routes, regardless of whether load balancing is implemented.After BGP load balancing is configured, the BGP routes that meet the following conditions and have the same AS\_Path attribute become equal-cost routes for load balancing:

* The preferred values (PrefVal) are the same.
* The Local\_Pref values are the same.
* All routes are summary routes or none of them is a summary route.
* The AS\_Path lengths are the same.
* Origin types (IGP, EGP, and Incomplete) are the same.
* The Multi\_Exit Discriminator (MED) values are the same.
* The AS\_Path attributes are the same.This section describes how to configure BGP load balancing to improve network resource usage.Among the routes with the same prefix in the BGP routing table:
* If the optimal route is a labeled route, the selected routes for load balancing are also labeled routes. The number of routes for load balancing is controlled by the maximum load-balancing ingress-lsp or maximum load-balancing transit-lsp command.
* If the optimal route is a common route, the selected routes for load balancing are also common routes. The **maximum load-balancing eibgp** command controls the number of routes for load balancing.If BGP labeled routes work in load balancing mode and the routes meet the conditions for creating ingress LSPs, ingress LSPs are created for the labeled routes. If BGP labeled routes work in load balancing mode and the routes meet the conditions for creating transit LSPs, transit LSPs are created for the labeled routes.

**Configuration Impact**



If the **maximum load-balancing eibgp** command is run more than once, the latest configuration overrides the previous one.



**Precautions**



The maximum load-balancing and the **maximum load-balancing eibgp** commands are mutually exclusive.Load balancing cannot be implemented between leaked and non-leaked routes.




Example
-------

# Set the maximum number of EBGP and IBGP routes for load balancing to 3.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[~HUAWEI-vpn-instance-vpna] ipv4-family
[~HUAWEI-vpn-instance-vpna-af-ipv4] quit
[~HUAWEI-vpn-instance-vpna] quit
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] maximum load-balancing eibgp 3

```