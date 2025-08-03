peer route-policy export (BGP view)
===================================

peer route-policy export (BGP view)

Function
--------



The **peer route-policy export** command specifies a route-policy for filtering routes to be advertised to a peer.

The **undo peer route-policy export** command deletes a specified route-policy.



By default, no route-policy is configured for the routes to be advertised to a specified BGP peer.


Format
------

**peer** *ipv4-address* **route-policy** *route-policy-name* **export**

**undo peer** *ipv4-address* **route-policy** *route-policy-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. |
| **export** | Applies a route-policy to the routes to be advertised to a peer. | - |



Views
-----

BGP view


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



If both a peer group and a peer are configured with a route-policy, the configuration on the peer takes precedence. If a peer group is configured with a route-policy but peers in the group are not configured with their own ones, the peers inherit the configuration of the peer group. If the route-policy configuration of a peer group is the same as that of a peer in the group, the configuration is displayed in the configuration file only for the peer group.



**Precautions**

After the **peer route-policy export** command is run, only the routes that match the route-policy are advertised. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be advertised.If route-policy route-policy-name is specified in this command, the following items can be matched: the RPKI origin AS validation, IPv4 ACL list, AS\_Path filter, AS\_Path length, community filter, route cost, VPN-Target extended community filter, bandwidth extended community filter, outbound interface, MPLS label, Large-Community filter, IPv4 route next-hop address ACL list, IPv6 route next-hop address ACL list, IPv4 route next-hop address prefix list, IPv6 route next-hop address prefix list, route preference, IP route destination address prefix list, route modulo, routing protocol type, route source IPv4 address ACL list, route source IPv6 address ACL list, route source IPv4 address prefix list, route source IPv6 address prefix list, route type, and route tag. The following items can be set: the BGP Large-Community attribute, BGP route AIGP value, AS\_Path attribute, BGP community attribute, BGP route MED, route cost type, discarding the entropy label of routes, BGP route VPN-Target extended community attribute, BGP route color extended community attribute, BGP route SoO extended community attribute, BGP route bandwidth extended community attribute, MPLS label, BGP route local preference, route next-hop address, and BGP route origin.If the referenced policy contains unsupported attribute matching or setting behaviors, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.


Example
-------

# Apply a route-policy named test-policy to routes to be advertised to a peer.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] peer 10.1.1.1 route-policy test-policy export

```