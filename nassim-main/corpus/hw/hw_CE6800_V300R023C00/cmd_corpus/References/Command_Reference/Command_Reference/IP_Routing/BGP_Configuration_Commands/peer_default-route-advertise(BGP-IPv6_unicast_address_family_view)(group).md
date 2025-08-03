peer default-route-advertise(BGP-IPv6 unicast address family view)(group)
=========================================================================

peer default-route-advertise(BGP-IPv6 unicast address family view)(group)

Function
--------



The **peer default-route-advertise** command configures a device to advertise default routes to a peer group.

The **undo peer default-route-advertise** command restores the default configuration.



By default, a device does not advertise default routes to a peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **default-route-advertise** [ **route-policy** *route-policy-name* ]

**peer** *group-name* **default-route-advertise** [ **route-policy** *route-policy-name* ] { **conditional-route-match-all** | **conditional-route-match-any** } { *ipv6-address* *mask-length* } &<1-4>

**undo peer** *group-name* **default-route-advertise**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **route-policy** *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **conditional-route-match-all** | Configures the device to send the default route when all conditional routes are matched. | - |
| **conditional-route-match-any** | Configures the device to send the default route when any conditional route is matched. | - |
| *ipv6-address* | Specifies the IPv6 address of a conditional route. | The value is in the format of X:X:X:X:X:X:X:X. |
| *mask-length* | Specifies the IPv6 mask length of a conditional route. | It is an integer ranging from 0 to 128. |



Views
-----

BGP-IPv6 unicast address family view


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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test default-route-advertise

```