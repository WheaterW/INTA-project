maximum load-balancing (BGP view)
=================================

maximum load-balancing (BGP view)

Function
--------



The **maximum load-balancing** command sets the maximum number of equal-cost routes for load balancing.

The **undo maximum load-balancing** command restores the default setting.



By default, the maximum number of equal-cost routes for load balancing is 1, and load balancing is not implemented.


Format
------

**maximum load-balancing** *number*

**maximum load-balancing ebgp** *ebgpNumber*

**maximum load-balancing ibgp** *ibgpNumber*

**maximum load-balancing** *number* **ecmp-nexthop-changed**

**maximum load-balancing ebgp** *ebgpNumber* **ecmp-nexthop-changed**

**maximum load-balancing ibgp** *ibgpNumber* **ecmp-nexthop-changed**

**undo maximum load-balancing**

**undo maximum load-balancing ebgp**

**undo maximum load-balancing ibgp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of equal-cost routes for load balancing. | The value is an integer ranging from 1 to 128. |
| **ebgp** *ebgpNumber* | Specifies the maximum number of equal-cost EBGP routes for load balancing. | The value is an integer ranging from 1 to 128. |
| **ibgp** *ibgpNumber* | Specifies the maximum number of equal-cost IBGP routes for load balancing. | The value is an integer ranging from 1 to 128. |
| **ecmp-nexthop-changed** | Configures the device to change the next hop addresses of only the routes that carry out load balancing to its address. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After this command is run, multiple BGP equal-cost routes will implement load balancing, improving network resource efficiency.After this command is run, the routes that meet the following conditions will become equal-cost routes and implement load balancing:

* The original next hops are different.
* The PrefVal values are the same.
* Local\_Pref values are the same.
* All routes are summary routes or none of them are summary routes.
* Origin types (IGP, EGP, and Incomplete) are the same.
* The MED values are the same.
* All routes are EBGP or IBGP routes.
* The IGP metric values within an AS are the same.
* The AS\_Path attributes are the same.For BGP routes with the same prefix in the routing table:
* If the optimal routes are labeled routes, the routes selected for load balancing are also labeled routes. The number of routes for load balancing is determined by the **maximum load-balancing ingress-lsp** or **maximum load-balancing transit-lsp** command.
* If the optimal route is a common route, the routes selected for load balancing are also common routes, and the maximum number of routes for load balancing is determined by the **maximum load-balancing** command.When load balancing is performed among BGP labeled routes, ingress LSPs are created for the labeled routes if the routes meet the conditions for creating ingress LSPs. When load balancing is performed among BGP labeled routes, transit LSPs are created for the labeled routes if the routes meet the conditions for creating transit LSPs.After the **maximum load-balancing ebgp** command is run, only EBGP routes implement load balancing. After the **maximum load-balancing ibgp** command is run, only IBGP routes implement load balancing. If [ ebgp | ibgp ] is not specified, both EBGP and IBGP routes can carry out load balancing, and the number of EBGP routes for load balancing is the same as the number of IBGP routes for load balancing.By default, after the **maximum load-balancing** command is run, a BGP device changes the next hop of a route to itself before advertising the route to a peer, regardless of whether the route is used for load balancing. After ecmp-nexthop-changed is set, a BGP device changes the next-hop of only routes that participate in load balancing to itself before advertising them to peers and keeps the next-hop of the routes that do not participate in load balancing unchanged.Note:After the **maximum load-balancing** command is run, the device changes the next hop addresses of the routes to be advertised to a local address, regardless of whether the routes are used for load balancing. However, in RR and BGP confederation scenarios, the device does not change the next hop address of non-local routes to the local address.After the maximum load-balancing { ebgp | ibgp } command is run, the device does not forcibly change the next hop addresses of the routes to be advertised to a local address, regardless of whether the routes are used for load balancing.After the maximum load-balancing [ ebgp | ibgp ] ecmp-nexthop-changed command is run, the device changes the next hop addresses of the routes to be advertised to a local address only when the routes are used for load balancing. When advertising the routes that are not used for load balancing, the device does not process the next hops of these routes. That is, the original next hop of these routes is the same as the next hop of the routes that are advertised when load balancing is not configured.In the Add-Path scenario, the next hop of Add-Path routes is processed in the same way as that of optimal routes, regardless of whether Add-Path routes are used for load balancing.

**Configuration Impact**



If the command is run for multiple times, the latest configuration overrides the previous one.



**Precautions**



If the **maximum load-balancing** command has been configured, the **maximum load-balancing ebgp** or **maximum load-balancing ibgp** command configuration does not take effect. If the **maximum load-balancing ebgp** or **maximum load-balancing ibgp** command has been configured, the **maximum load-balancing** command configuration does not take effect.If either the ebgp or the ibgp parameter is configured in the **maximum load-balancing** command, this parameter must be also configured in the **undo maximum load-balancing** command when deleting load balancing.The maximum load-balancing and **peer load-balancing** commands are mutually exclusive.When the number of equal-cost routes for load balancing reaches 16, the number of next hops of a route is limited to 128. When the number of equal-cost routes for load balancing reaches 254, the number of next hops of a route is limited to 2.




Example
-------

# Set two equal-cost routes to a specified destination.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] maximum load-balancing 2

```