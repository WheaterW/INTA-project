peer route-policy import (BGP-EVPN address family view) (IPv6)
==============================================================

peer route-policy import (BGP-EVPN address family view) (IPv6)

Function
--------



The **peer route-policy import** command specifies a route-policy for filtering routes received from a peer.

The **undo peer route-policy import** command deletes a specified route-policy.



By default, no route-policy is configured for filtering routes received from a peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **route-policy** *route-policy-name* **import**

**undo peer** *peerIpv6Addr* **route-policy** *route-policy-name* **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The format is X:X:X:X:X:X:X:X. |
| *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a route-policy is created, the **peer route-policy import** command is used to apply a Route-Policy to a peer so that the routes received from the peer can be controlled. To be specific, only the necessary routes are received from the peer. In this manner, route management is implemented, the scale of the routing table is reduced, and fewer network resources are consumed.

**Prerequisites**

If a routing policy needs to be specified in the command, run the route-policy command to create the routing policy first.

**Configuration Impact**

If a BGP peer relationship is established, then an import policy is bound to the peer or the import policy bound to the peer is modified, and the device does not support the Refresh capability, the peer relationship is re-established because the import policy addition or modification causes the peer to resend Refresh messages.

**Precautions**



After the **peer route-policy import** command is run, only the routes that match the route-policy are received. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be received.

When **route-policy** *route-policy-name*is configured in the BGP multi-instance EVPN address family view, the following items can be matched: IPv4 ACL, AS\_Path filter, AS\_Path length, community filter, route cost, IPv6 route destination address, VPN target extended community filter, priority-based coloring extended community filter, SoO extended community filter, outbound interface, MPLS label, Large-community filter, MAC address list, ACL for the next hop address of a route, ACL for the next hop address of an IPv6 route, next hop address prefix list of routing information, next hop address prefix list of IPv6 routing information, destination address prefix list of IP routing information, destination address prefix list of IPv6 routing information, route modulo, routing protocol type, RD attribute filter, route source IP address ACL, route source IPv6 address ACL, route source IP address prefix list, route source IPv6 address prefix list, route type, route tag, and encapsulation extended community filter.The following attributes can be set: BGP Large-community, AS\_Path, BGP community, BGP route MED, BGP route VPN target extended community, BGP route coloring extended community, BGP route SoO extended community, EVPN route priority coloring extended community, gateway IP address, gateway IPv6 address, BGP route local preference, next-hop address (IPv4), next-hop address (IPv6), BGP route source, BGP route preferred value, QoS parameters, and EVPN route VN-ID attributes.

When **route-policy** *route-policy-name*is configured in the BGP-EVPN address family view, the following items can be matched: IPv4 ACL, AS\_Path filter, AS\_Path length, community filter, route cost, IPv6 route destination address, VPN target extended community filter, priority-based coloring extended community filter, SoO extended community filter, outbound interface, MPLS label, Large-community filter, MAC address list, next-hop address ACL of routing information, next-hop address ACL of IPv6 routing information, next-hop address prefix list based on IP routing information, next-hop address prefix list based on IPv6 routing information, destination address prefix list of IP routing information, destination address prefix list of IPv6 routing information, route modulo, routing protocol type, RD attribute filter, route source IP address ACL, route source IPv6 address ACL, route source IP address prefix list, route source IPv6 address prefix list, route type, route tag, and encapsulation extended community filter.The following attributes can be set: BGP Large-community, AS\_Path, BGP community, BGP route MED, BGP route VPN target extended community, BGP route coloring extended community, BGP route SoO extended community, EVPN route priority-based coloring extended community, route gateway IP address, route gateway IPv6 address, BGP route local preference, route next-hop address (IPv4), route next-hop address (IPv6), BGP route source, BGP route preferred value, QoS parameters, and EVPN route VN-ID attributes.If the referenced policy contains unsupported attribute matching or behavior setting, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level information.




Example
-------

# Apply the routing policy named test-policy to the routes received from a peer in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:db8:1::1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 2001:db8:1::1 enable
[*HUAWEI-bgp-af-evpn] peer 2001:db8:1::1 route-policy test-policy import

```