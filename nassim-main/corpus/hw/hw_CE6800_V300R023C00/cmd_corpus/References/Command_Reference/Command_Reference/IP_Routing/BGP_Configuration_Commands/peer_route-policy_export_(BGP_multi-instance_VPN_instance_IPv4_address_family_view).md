peer route-policy export (BGP multi-instance VPN instance IPv4 address family view)
===================================================================================

peer route-policy export (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **peer route-policy export** command specifies a route-policy for filtering routes to be advertised to a peer.

The **undo peer route-policy export** command deletes a specified route-policy.



By default, no route-policy is configured for the routes to be advertised to a specified peer.


Format
------

**peer** *ipv4-address* **route-policy** *route-policy-name* **export**

**undo peer** *ipv4-address* **route-policy** *route-policy-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters, spaces not supported. |
| **export** | Applies a route-policy to the routes to be advertised to a peer. | - |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **peer route-policy export** command is used to apply a created route-policy to a peer so that the routes advertised to the peer can be controlled. To be specific, only the necessary routes are advertised to the peer. In this manner, route management is implemented, the scale of the routing table is reduced, and fewer network resources are consumed.



**Prerequisites**



If a route-policy that does not exist is specified in the command, use the route-policy command to create the route-policy.



**Configuration Impact**



If both a peer group and a peer are configured with a route-policy, the configuration on the peer takes precedence. If a peer group is configured with a route-policy but peers in the group are not configured with their own ones, the peers inherit the configuration of the peer group. If the route-policy configuration of a peer group is the same as that of a peer in the group, the configuration is displayed in the configuration file only for the peer group.



**Precautions**



After the **peer route-policy export** command is run, only the routes that match the route-policy are advertised. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be advertised.If **route-policy** *route-policy-name*is configured when you run this command, the following items can be matched: source AS validation, IPv4 ACL, AS\_Path filter, AS\_Path length, community filter, route cost, VPN-Target extended community filter, SoO extended community filter, outbound interface, and MPLS label, Large-community filter, next-hop address ACL list, next-hop address prefix list, route priority, destination address prefix list, route modulo, routing protocol type, source IP address ACL list, route source IP address prefix list, route type, and route tag. The following attributes can be set: BGP Large-Community, AS\_Path, BGP community, MED, cost type, VPN-Target extended community, color extended community, SoO extended community, MPLS label, Local preference, next hop address, and origin attribute of BGP routes.If the referenced policy contains unsupported attribute matching or setting behavior, unexpected results may occur.




Example
-------

# Apply a route-policy named test-policy to routes to be advertised to a peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-vpna] peer 10.1.1.1 route-policy test-policy export

```