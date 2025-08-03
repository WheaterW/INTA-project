nexthop recursive-lookup route-policy (BGP multi-instance VPN instance IPv4 address family view)
================================================================================================

nexthop recursive-lookup route-policy (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **nexthop recursive-lookup route-policy** command configures route-policy next hop recursion.

The **undo nexthop recursive-lookup route-policy** command disables route-policy next hop recursion.



By default, route-policy-based next hop recursion is disabled.


Format
------

**nexthop recursive-lookup route-policy** *route-policy-name*

**undo nexthop recursive-lookup route-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BGP needs route recursion in case of next hops. If route recursion is not limited, BGP routes may be incorrectly iterated, causing traffic loss. Therefore, next hops should perform recursion according to certain conditions.To control route recursion based on a route-policy, run the **nexthop recursive-lookup route-policy** command. If a target recursive route is filtered out by the route-policy, the route is considered unreachable. In this manner, BGP route recursion will fail.



**Prerequisites**



The target recursive route has been determined, and a route-policy has been configured.Note:Before configuring a route-policy, ensure that all desired target recursive routes will not be filtered out by the route-policy.



**Precautions**



This command does not take effect for the routes received from LinkLocal peers.When configuring **route-policy** *route-policy-name*, you can run this command to match the IPv4 ACL, route cost, outbound interface, MPLS label, next-hop IP address ACL, next-hop IP prefix list, route priority, destination IP prefix list, route modulo, routing protocol type, route source IP address ACL list, route source IP address prefix list, route type, and route tag.If the referenced policy contains an unsupported attribute matching behavior, unexpected results may occur.




Example
-------

# Configure BGP to filter routes based on a specified route-policy.
```
<HUAWEI> system-view
[*HUAWEI] route-policy rp_nexthop permit node 0
[*HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] nexthop recursive-lookup route-policy rp_nexthop

```