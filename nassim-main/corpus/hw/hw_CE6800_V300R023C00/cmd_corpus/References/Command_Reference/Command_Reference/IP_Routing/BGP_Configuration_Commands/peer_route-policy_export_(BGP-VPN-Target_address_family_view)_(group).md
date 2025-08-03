peer route-policy export (BGP-VPN-Target address family view) (group)
=====================================================================

peer route-policy export (BGP-VPN-Target address family view) (group)

Function
--------



The **peer route-policy export** command specifies a route-policy for filtering routes to be advertised to a peer group.

The **undo peer route-policy export** command deletes a specified route-policy.



By default, no route-policy is configured for the routes to be advertised to a specified BGP peer group.


Format
------

**peer** *group-name* **route-policy** *route-policy-name* **export**

**undo peer** *group-name* **route-policy** *route-policy-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *route-policy-name* | Specifies the name of a route-policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **export** | Applies a route-policy to routes to be advertised to a peer group. | - |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After a route-policy is created, the **peer route-policy export** command is used to apply a Route-Policy to a peer group so that the routes advertised to a peer group can be controlled. To be specific, only the necessary routes are advertised to the peer group. In this manner, route management is implemented, the scale of the routing table is reduced, and fewer network resources are consumed.



**Prerequisites**



If the command specifies a route-policy that does not exist, use the route-policy command to create the route-policy.



**Configuration Impact**



If both a peer group and a peer are configured with a route-policy, the configuration on the peer takes precedence. If a peer group is configured with a route-policy but peers in the group are not configured with their own ones, the peers inherit the configuration of the peer group. If the route-policy configuration of a peer group is the same as that of a peer in the group, the configuration is displayed in the configuration file only for the peer group.If you run both this command and the **peer route-filter** command, the latest configuration overrides the previous one.



**Precautions**



After the **peer route-policy export** command is run, only the routes that match the route-policy are advertised. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be advertised.If **route-policy** *route-policy-name*is configured when you run this command, the following items can be matched: AS\_Path filter, AS\_Path length, community filter, route cost, outbound interface, large-community filter, next-hop ACL, next-hop prefix list, routing protocol type, route source IP address ACL list, route source IPv6 address ACL list, route source IP address prefix list, route type, and route tag. The following items can be set: BGP Large-Community attribute, AS\_Path attribute, BGP community attribute, BGP route MED, route cost type, BGP route color extended community attribute, MPLS label, local preference of BGP routes, next hop address, and Origin attribute of BGP routes.If the referenced policy contains unsupported attribute matching or setting behavior, unexpected results may occur.




Example
-------

# Apply a route-policy named test-policy to the routes advertised to a peer group.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer test enable
[*HUAWEI-bgp-af-vpn-target] peer test route-policy test-policy export

```