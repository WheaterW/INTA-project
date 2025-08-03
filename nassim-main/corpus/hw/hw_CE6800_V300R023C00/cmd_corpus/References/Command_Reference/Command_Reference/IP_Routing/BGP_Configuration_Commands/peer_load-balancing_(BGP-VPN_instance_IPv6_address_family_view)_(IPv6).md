peer load-balancing (BGP-VPN instance IPv6 address family view) (IPv6)
======================================================================

peer load-balancing (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------

By default, BGP load balancing is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **load-balancing** [ **as-path-ignore** | **as-path-relax** ]

**undo peer** *ipv6-address* **load-balancing** [ **as-path-ignore** | **as-path-relax** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **as-path-ignore** | Prevents the device from comparing the AS\_Path attributes of routes when selecting routes for load balancing. | - |
| **as-path-relax** | Prevents the device from comparing the AS\_Path attributes of the same length when selecting routes for load balancing. | - |



Views
-----

BGP-VPN instance IPv6 address family view


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

The maximum load-balancing and **peer load-balancing** commands are mutually exclusive.By default, a BGP device does not change the next hop addresses of routes to a local address before sending the routes to its IBGP peer. However, after peer-based load balancing is enabled, a BGP device changes the next hop addresses of routes to a local address before sending the routes to its IBGP peer.If the **load-balancing as-path-ignore** or **load-balancing as-path-relax** command is run but the **peer load-balancing** command does not contain the *as-path-ignore*or *as-path-relax*parameter, the **load-balancing as-path-ignore** or **load-balancing as-path-relax** configuration takes effect. If *as-path-ignore*or *as-path-relax*is specified in the **peer load-balancing** command, the configuration specified in the **peer load-balancing** command takes effect.Running the load-balancing as-path-ignore or load-balancing as-path-relax command may cause BGP routing loops.


Example
-------

# Enable peer-based load balancing among BGP routes without comparing the AS\_Path attributes of the same length.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:2::2 as-number 100
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 load-balancing as-path-relax
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:2::2 load-balancing as-path-relax

```