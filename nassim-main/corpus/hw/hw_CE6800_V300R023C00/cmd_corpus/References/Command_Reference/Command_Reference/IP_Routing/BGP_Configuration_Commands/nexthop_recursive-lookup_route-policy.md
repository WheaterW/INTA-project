nexthop recursive-lookup route-policy
=====================================

nexthop recursive-lookup route-policy

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
| *route-policy-name* | Indicates the name of a route-policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP view


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
[~HUAWEI] route-policy aa permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] nexthop recursive-lookup route-policy aa

```