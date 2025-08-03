peer default-route-advertise(BGP multi-instance VPN instance IPv4 address family view)(group)
=============================================================================================

peer default-route-advertise(BGP multi-instance VPN instance IPv4 address family view)(group)

Function
--------



The **peer default-route-advertise** command configures a device to advertise default routes to a peer group.

The **undo peer default-route-advertise** command restores the default configuration.



By default, a BGP device does not advertise any default route to its peer group.


Format
------

**peer** *group-name* **default-route-advertise** [ **route-policy** *route-policy-name* ]

**peer** *group-name* **default-route-advertise** [ **route-policy** *route-policy-name* ] { **conditional-route-match-all** | **conditional-route-match-any** } { *ipv4-address* { *mask-length* | *mask* } } &<1-4>

**undo peer** *group-name* **default-route-advertise**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **route-policy** *route-policy-name* | Specifies the name of the route-policy. | The value is a string of 1 to 200 case-sensitive characters. It cannot contain spaces. If spaces are used, the string must start and end with double quotation marks ("). |
| **conditional-route-match-all** | Configures the device to send the default route when all conditional routes are matched. | - |
| **conditional-route-match-any** | Configures the device to send the default route when any conditional route is matched. | - |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of the conditional routes. | The value is an integer in the range from 0 to 32. |
| *mask* | Specifies the mask of the conditional routes. | It is in dotted decimal notation. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Default routes are usually used on networks with the following characteristics:

* There are multiple EBGP peers, and full Internet routes are received from each peer.
* There are multiple RRs, and each RR receives full Internet routes.If load balancing is not performed on a network, a BGP peer receives at most one copy of active full Internet routes. If load balancing is performed on a network, the number of active routes received by a BGP peer increases sharply, causing the number of routes on the network to sharply increase. In this case, you can configure the device to advertise default routes to BGP peer groups and use default routes for load balancing to reduce the number of routes on the network.This command does not require a default route in the routing table. Instead, the device unconditionally sends a default route with the next hop being itself to the peer group.

**Precautions**



The default route is generated and advertised by the device, and condition-based matching is not used. Therefore, you are not advised to configure if-match clauses in a route-policy.




Example
-------

# Configure a BGP device to advertise default routes to its peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] group test
[*HUAWEI-bgp-instance-a-vpna] peer test default-route-advertise

```