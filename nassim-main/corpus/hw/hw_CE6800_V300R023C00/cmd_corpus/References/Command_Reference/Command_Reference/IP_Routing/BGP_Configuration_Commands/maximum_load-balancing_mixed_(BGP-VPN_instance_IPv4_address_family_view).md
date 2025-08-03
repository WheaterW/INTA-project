maximum load-balancing mixed (BGP-VPN instance IPv4 address family view)
========================================================================

maximum load-balancing mixed (BGP-VPN instance IPv4 address family view)

Function
--------

By default, the maximum number of equal-cost BGP routes for load balancing with routes of other protocols is 0, and load balancing is not implemented.


Format
------

**maximum load-balancing mixed** *number*

**undo maximum load-balancing mixed**

**undo maximum load-balancing mixed** *number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of equal-cost BGP routes for load balancing with routes of other protocols. | The value is an integer ranging from 1 to 128. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **maximum load-balancing mixed** command is used in the scenario where traffic is transmitted between different VNFs in the symmetric telco cloud. To set the maximum number of equal-cost BGP routes for load balancing with routes of other protocols, run this command so that the BGP routes and routes of other protocols can implement load balancing.Description:BGP equal-cost routes can be generated only when the following conditions are met:

* The original next hops are different.
* The preferred values (PrefVal) are the same.
* The Local\_Pref values are the same.
* All routes are summary routes or none of them is a summary route.
* The AS\_Path lengths are the same.
* Origin types (IGP, EGP, and Incomplete) are the same.
* The Multi\_Exit Discriminator (MED) values are the same.
* The AS\_Path attributes are the same.Among the routes with the same prefix in the BGP routing table:
* If the optimal route is a labeled route, the selected routes for load balancing are also labeled routes. The number of routes for load balancing is controlled by the **maximum load-balancing ingress-lsp** or **maximum load-balancing transit-lsp** command.
* If the optimal route is a common route, the selected routes for load balancing are also common routes. The **maximum load-balancing mixed** command controls the number of routes for load balancing.If BGP labeled routes work in load balancing mode and the routes meet the conditions for creating ingress LSPs, ingress LSPs are created for the labeled routes. If BGP labeled routes work in load balancing mode and the routes meet the conditions for creating transit LSPs, transit LSPs are created for the labeled routes.BGP equal-cost routes can implement inter-protocol load balancing with routes of other protocols in the IP routing table only when the following conditions are met:
* The BGP route is the optimal or sub-optimal route.
* BGP routes have the same priority as routes of other protocols.

**Configuration Impact**

If the command is run more than once, the latest configuration overrides the previous one.

**Precautions**

After this command is run, EBGP and IBGP routes can load-balance traffic, and leaked routes and non-leaked routes can also load-balance traffic.


Example
-------

# Set the maximum number of equal-cost BGP routes for load balancing with routes of other protocols to 3.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 1:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp] maximum load-balancing mixed 3

```