peer route-policy export (BGP-IPv4 unicast address family view) (IPv6)
======================================================================

peer route-policy export (BGP-IPv4 unicast address family view) (IPv6)

Function
--------



The **peer route-policy export** command specifies a route-policy for filtering routes to be advertised to a peer.

The **undo peer route-policy export** command deletes a specified route-policy.



By default, no route-policy is configured for the routes to be advertised to a specified BGP peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **route-policy** *policy-name* **export**

**undo peer** *peerIpv6Addr* **route-policy** *policy-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters, spaces not supported. |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a route-policy is created, the **peer route-policy export** command is used to apply a Route-Policy to a peer so that the routes advertised to the peer can be controlled. To be specific, only the necessary routes are advertised to the peer. In this manner, route management is implemented, the scale of the routing table is reduced, and fewer network resources are consumed.

**Prerequisites**

If the command specifies a route-policy that does not exist, use the route-policy command to create the route-policy.

**Configuration Impact**

If both a peer group and a peer are configured with a route-policy, the configuration on the peer takes precedence. If a peer group is configured with a route-policy but peers in the group are not configured with their own ones, the peers inherit the configuration of the peer group. If the route-policy configuration of a peer group is the same as that of a peer in the group, the configuration is displayed in the configuration file only for the peer group.If you run both this command and the **peer route-filter** command, the latest configuration overrides the previous one.

**Precautions**

After the **peer route-policy export** command is run, only the routes that match the route-policy are advertised. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be advertised.If **route-policy** *route-policy-name*is configured, the following items can be matched: RPKI origin AS validation, IPv4 ACL, AS\_Path filter, AS\_Path length, community filter, route cost, VPN-Target extended community filter, bandwidth extended community filter, outbound interface, MPLS label, Large-community filter, ACL for the next hop address of a route, ACL for the next hop address of an IPv6 route, prefix list for the next hop address of a route, prefix list for the next hop address of an IPv6 route, route preference, destination address prefix list, route modulo, routing protocol type, route source IP address ACL list, route source IPv6 address ACL list, route source IP address prefix list, route type, and route tag. The following attributes can be set: BGP Large-Community attribute, AIGP value, AS\_Path attribute, BGP community attribute, MED attribute, cost type, entropy label of discarded routes, VPN-Target extended community attribute, color extended community attribute of BGP routes, SoO extended community attribute, bandwidth extended community attribute, MPLS label, local preference, next hop address, and origin attribute for BGP routes.If the referenced policy contains unsupported attribute matching or setting behaviors, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.


Example
-------

# Apply a route-policy named test-policy to routes to be advertised to a peer.
```
<HUAWEI> system-view
[~HUAWEI] route-policy aaa permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer FE80::1 as-number 200
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer FE80::1 enable
[*HUAWEI-bgp-af-ipv4] peer FE80::1 route-policy aaa export

```