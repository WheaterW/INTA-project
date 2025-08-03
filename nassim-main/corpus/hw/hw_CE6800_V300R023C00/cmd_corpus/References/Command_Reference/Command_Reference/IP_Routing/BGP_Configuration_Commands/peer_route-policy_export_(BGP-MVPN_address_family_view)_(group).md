peer route-policy export (BGP-MVPN address family view) (group)
===============================================================

peer route-policy export (BGP-MVPN address family view) (group)

Function
--------



The **peer route-policy export** command specifies a route-policy for the routes to be advertised to a peer group.

The **undo peer route-policy export** command deletes a specified route-policy.



By default, no route-policy is configured for filtering routes to be advertised to a peer group.


Format
------

**peer** *group-name* **route-policy** *route-policy-name* **export**

**undo peer** *group-name* **route-policy** *route-policy-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| *route-policy-name* | Specifies a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **export** | Applies a route-policy to routes to be advertised to a peer group. | - |



Views
-----

BGP-MVPN address family view


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

If both a peer group and a peer are configured with a route-policy, the configuration on the peer takes precedence. If a peer group is configured with a route-policy but peers in the group are not configured with their own ones, the peers inherit the configuration of the peer group. If the route-policy configuration of a peer group is the same as that of a peer in the group, the configuration is displayed in the configuration file only for the peer group.If you run both this command and the **peer route-filter** command, the latest configuration overrides the previous one.

**Precautions**

After the **peer route-policy export** command is run, only the routes that match the route-policy are advertised. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be advertised.You can run the **route-policy** *route-policy-name*command to filter routes based on the AS\_Path filter, AS\_Path length, community filter, route cost, VPN-Target extended community filter, outbound interface, IP address of the NG MVPN route advertiser, and Large-Community filter, next-hop address ACL list of routing information, next-hop address ACL list of IPv6 routing information, next-hop address prefix list of routing information, next-hop address prefix list based on IPv6 routing information, routing protocol type, RD attribute filter, and route source IP address ACL list, route source IPv6 address ACL List, route source IP address prefix list, route source IPv6 address prefix list, route type, and route tag. You can set the BGP Large-Community attribute, AS\_Path attribute, BGP community attribute, BGP route MED, route cost type, VPN-Target extended community attribute of BGP routes, BGP route color extended community attribute, MPLS label, and local preference of BGP route information, next-hop address (IPv4) of the route, route source of the BGP route, and stitching PMSI attribute.If the referenced policy contains unsupported attribute matching or setting behavior, unexpected results may occur.


Example
-------

# Apply a route-policy named test-policy to the routes received from a peer group.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer test enable
[*HUAWEI-bgp-af-mvpn] peer test route-policy test-policy export

```