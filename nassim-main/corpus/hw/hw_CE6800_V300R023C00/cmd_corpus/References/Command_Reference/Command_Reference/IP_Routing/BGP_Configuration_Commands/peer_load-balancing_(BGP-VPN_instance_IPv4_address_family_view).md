peer load-balancing (BGP-VPN instance IPv4 address family view)
===============================================================

peer load-balancing (BGP-VPN instance IPv4 address family view)

Function
--------

By default, BGP load balancing is not enabled.


Format
------

**peer** *ipv4-address* **load-balancing** [ **as-path-ignore** | **as-path-relax** ]

**undo peer** *ipv4-address* **load-balancing** [ **as-path-ignore** | **as-path-relax** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **as-path-ignore** | Prevents the device from comparing the AS\_Path attributes of routes when selecting routes for load balancing. | - |
| **as-path-relax** | Prevents the device from comparing the AS\_Path attributes of the same length when selecting routes for load balancing. | - |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a large-scale network, there may be multiple valid routes to the same destination, but BGP advertises only the optimal route to its peers. This may cause unbalanced traffic load. This section describes how to configure BGP load balancing to implement load balancing among multiple BGP routes.After the **peer load-balancing** command is run, the following conditions must be met to implement load balancing:

* From the specified peer.
* The route is the optimal route or is equal-cost with the optimal route.
* If the AS\_Path attribute of the route is the same as that of the optimal route or the *as-path-ignore*or *as-path-relax*parameter is configured for the peer when load balancing is enabled on the peer:*as-path-ignore*: ignores the AS\_Path attribute and does not compare the AS\_Path attributes of the routes to be used for load balancing. That is, load balancing can be implemented even if the AS\_Path attributes of the routes are different.*as-path-relax*: The device ignores the AS\_Path attributes of the same length and does not compare the AS\_Path attributes of the same length when load balancing is performed among the routes. That is, load balancing cannot be performed among the routes with different AS\_Path lengths. For example, the AS\_Path attribute of route A is 10, and the AS\_Path attribute of route B is 10 20. Because the AS\_Path lengths of the two routes are different, load balancing cannot be implemented.

**Precautions**

The maximum load-balancing and **peer load-balancing** commands are mutually exclusive.By default, a BGP device does not change the next hop addresses of routes to a local address before sending the routes to its IBGP peer. However, after peer-based load balancing is enabled, a BGP device changes the next hop addresses of routes to a local address before sending the routes to its IBGP peer.If the **load-balancing as-path-ignore** or **load-balancing as-path-relax** command is run but the **peer load-balancing** command does not contain the *as-path-ignore*or *as-path-relax*parameter, the **load-balancing as-path-ignore** or **load-balancing as-path-relax** command takes effect. If *as-path-ignore*or *as-path-relax*is specified in the **peer load-balancing** command, the configuration specified in the **peer load-balancing** command takes effect.Running the load-balancing as-path-ignore or load-balancing as-path-relax command may cause BGP routing loops.Load balancing cannot be implemented if the **peer load-balancing** command is run in the BGP-labeled-VPN instance IPv4 address family view, but can be implemented if the **maximum load-balancing** command is run in the BGP-labeled-VPN instance IPv4 address family view.


Example
-------

# Enable peer-based load balancing among BGP routes without comparing the AS\_Path attributes of the same length.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 load-balancing as-path-relax

```