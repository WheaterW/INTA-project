peer route-policy export (BGP-EVPN address family view)
=======================================================

peer route-policy export (BGP-EVPN address family view)

Function
--------



The **peer route-policy export** command specifies a route-policy for filtering routes to be advertised to a peer.

The **undo peer route-policy export** command deletes a specified route-policy.



By default, no route-policy is configured for filtering routes to be advertised to a peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv4Addr* **route-policy** *route-policy-name* **export**

**undo peer** *peerIpv4Addr* **route-policy** *route-policy-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *route-policy-name* | Specifies the name of a route-policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a route-policy is created, the **peer route-policy export** command is used to apply a Route-Policy to a peer group so that the routes advertised to peer group can be controlled. To be specific, only the necessary routes are advertised to the peer group. In this manner, route management is implemented, the scale of the routing table is reduced, and fewer network resources are consumed.

**Prerequisites**

If a routing policy needs to be specified in the command, run the route-policy command to create the routing policy first.

**Configuration Impact**

If both a peer group and a peer are configured with a route-policy, the configuration on the peer takes precedence. If a peer group is configured with a route-policy but peers in the group are not configured with their own ones, the peers inherit the configuration of the peer group. If the route-policy configuration of a peer group is the same as that of a peer in the group, the configuration is displayed in the configuration file only for the peer group.

**Precautions**

After the peer route-policy import command is run, only the routes that match the route-policy are received. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be received.When **route-policy** *route-policy-name*is configured, the following items can be matched: IPv4 ACL, AS\_Path filter, AS\_Path length, community filter, route cost, IPv6 route destination address, VPN target extended community filter, priority-based coloring extended community filter, SoO extended community filter, outbound interface, MPLS label, Large-community filter, MAC address list, next-hop address ACL of routing information, next-hop address ACL of IPv6 routing information, next-hop address prefix list based on IP routing information, next-hop address prefix list based on IPv6 routing information, destination address prefix list of IP routing information, destination address prefix list of IPv6 routing information, route modulo, routing protocol type, RD attribute filter, route source IP address ACL, route source IPv6 address ACL, route source IP address prefix list, route source IPv6 address prefix list, route type, route tag, and encapsulation extended community filter.The following attributes can be set: BGP Large-community, AS\_Path, BGP community, BGP route MED, BGP route VPN target extended community, BGP route coloring extended community, BGP route SoO extended community, EVPN route priority-based coloring extended community, route gateway IP address, route gateway IPv6 address, BGP route local preference, route next-hop address (IPv4), route next-hop address (IPv6), BGP route source, and EVPN route VN-ID attributes.If the referenced policy contains unsupported attribute matching or behavior setting, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level information.


Example
-------

# Apply the route-policy named test-policy to the routes advertised to a BGP EVPN peer.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.9 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 10.1.1.9 enable
[*HUAWEI-bgp-af-evpn] peer 10.1.1.9 route-policy test-policy export

```