peer route-policy export (BGP-VPN-Target address family view)
=============================================================

peer route-policy export (BGP-VPN-Target address family view)

Function
--------



The **peer route-policy export** command specifies a route-policy for filtering routes to be advertised to a peer.

The **undo peer route-policy export** command deletes a specified route-policy.



By default, no route-policy is configured for the routes to be advertised to a specified BGP peer.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **route-policy** *route-policy-name* **export**

**undo peer** { *ipv4-address* | *ipv6-address* } **route-policy** *route-policy-name* **export**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **route-policy** *route-policy-name* **export**

**undo peer** *ipv4-address* **route-policy** *route-policy-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters, spaces not supported. |
| **export** | Applies a route-policy to routes to be advertised to a peer. | - |



Views
-----

BGP-VPN-target address family view


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

After the **peer route-policy export** command is run, only the routes that match the route-policy are advertised. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be advertised.If route-policy route-policy-name is configured, the following items can be matched: the AS\_Path filter, AS\_Path length, community filter, route cost, outbound interface, large-community filter, next-hop ACL, next-hop prefix list, routing protocol type, route source IP address ACL list, route source IPv6 address ACL list, route source IP address prefix list, route type, and route tag. The following attributes can be set: BGP Large-Community attribute, AS\_Path attribute, BGP community attribute, BGP route MED, route cost type, BGP route color extended community attribute, MPLS label, local preference of BGP routes, next hop address, and Origin attribute of BGP routes.If the referenced policy contains unsupported attribute matching or setting behavior, unexpected results may occur.


Example
-------

# Apply a route-policy named test-policy to the routes advertised to a peer group.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-vpn-target] peer 10.1.1.1 route-policy test-policy export

```