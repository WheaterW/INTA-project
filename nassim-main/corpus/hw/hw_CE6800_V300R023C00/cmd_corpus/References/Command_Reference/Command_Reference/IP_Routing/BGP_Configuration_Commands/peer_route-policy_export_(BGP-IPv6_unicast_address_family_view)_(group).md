peer route-policy export (BGP-IPv6 unicast address family view) (group)
=======================================================================

peer route-policy export (BGP-IPv6 unicast address family view) (group)

Function
--------



The **peer route-policy export** command specifies a route-policy for the routes to be advertised to a peer group.

The **undo peer route-policy export** command deletes a specified route-policy.



By default, no route-policy is configured for filtering routes to be advertised to a peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **route-policy** *route-policy-name* **export**

**undo peer** *group-name* **route-policy** *route-policy-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **export** | Applies a route-policy to routes to be advertised to a peer group. | - |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a route-policy is created, the **peer route-policy export** command is used to apply a Route-Policy to a peer group so that the routes advertised to a peer group can be controlled. To be specific, only the necessary routes are advertised to the peer group. In this manner, route management is implemented, the scale of the routing table is reduced, and fewer network resources are consumed.

**Prerequisites**

If a route-policy that does not exist is specified in the command, use the route-policy command to create the route-policy.

**Configuration Impact**

If both a peer group and a peer are configured with a route-policy, the configuration on the peer takes precedence. If a peer group is configured with a route-policy but peers in the group are not configured with their own ones, the peers inherit the configuration of the peer group. If the route-policy configuration of a peer group is the same as that of a peer in the group, the configuration is displayed in the configuration file only for the peer group.

**Precautions**

After the **peer route-policy export** command is run, only the routes that match the route-policy are advertised. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be advertised.If **route-policy** *route-policy-name*is configured, the following items can be matched: RPKI origin AS validation, AS\_Path filter, AS\_Path length, community filter, route cost, destination address of IPv6 routes, VPN-Target extended community filter, bandwidth extended community filter, outbound interface, MPLS label, Large-community filter, ACL for the next hop address of a route, ACL for the next hop address of an IPv6 route, prefix list for the next hop address of a route, prefix list for the next hop address of an IPv6 route, route preference, destination address prefix list, route modulo, routing protocol type, route source IP address ACL list, route source IPv6 address ACL list, route source IP address prefix list, route type, and route tag. The following attributes can be set: the BGP Large-Community attribute, AIGP value, AS\_Path attribute, BGP community attribute, BGP route MED, route cost type, BGP route VPN-Target extended community attribute, BGP route color extended community attribute, SoO extended community attribute, bandwidth extended community attribute, MPLS label, local preference, IPv6 next hop address, and origin attribute for BGP routes.If the referenced policy contains unsupported attribute matching or setting behaviors, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.


Example
-------

# Apply a route-policy to the routes to be advertised to a peer.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test route-policy test-policy export

```