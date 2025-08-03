nexthop recursive-lookup route-policy (BGP-IPv4 unicast address family view)
============================================================================

nexthop recursive-lookup route-policy (BGP-IPv4 unicast address family view)

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

BGP-IPv4 unicast address family view


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

This command does not take effect for the routes received from link-local peers.If **route-policy** *route-policy-name*is configured in the BGP-IPv4 unicast address family view, the following items can be matched: IPv4 ACLs, route costs, destination addresses, outbound interfaces, MPLS labels, next-hop addresses, next-hop addresses of IPv6 routes, next-hop prefix list of routing information, next-hop prefix list based on IPv6 routing information, route priority, destination prefix list of IP routing information, destination prefix list of IPv6 routing information, route modulo, routing protocol type, route type, and route tag.If the referenced policy contains unsupported attribute matching or setting behaviors, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.


Example
-------

# Configure BGP to filter routes based on a specified route-policy.
```
<HUAWEI> system-view
[~HUAWEI] route-policy aa permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] nexthop recursive-lookup route-policy aa

```