preference (BGP-VPN instance IPv6 address family view)
======================================================

preference (BGP-VPN instance IPv6 address family view)

Function
--------



The **preference** command sets a priority for EBGP routes, IBGP routes, or local BGP routes. BGP routes are configured with different priorities in different address family views.

The **undo preference** command restores the default setting.



By default, the priorities of EBGP routes, IBGP routes, and local BGP routes are all 255.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**preference** { *external* *internal* *local* | **route-policy** *route-policy-name* }

**undo preference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *external* | Specifies a protocol preference of EBGP external routes, which are the optimal routes learned from peers outside the local AS. | The value is an integer that ranges from 1 to 255. A smaller value indicates a higher priority. |
| *internal* | Specifies the protocol preference of IBGP routes (those learned from peers in the same AS). | The value is an integer that ranges from 1 to 255. A smaller value indicates a higher priority. |
| *local* | Specifies the protocol preference of a local BGP route. | The value is an integer that ranges from 1 to 255. A smaller value indicates a higher priority.  This parameter takes effect for the following routes:   * Routes obtained through manually summarization using the aggregate (BGP) command. * Routes obtained through automatic summarization using the summary automatic command. * Routes generated through remote leaking. * Routes generated through local leaking.   For details about how to identify the preceding types of routes, see Precautions. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Running the **preference** command to set priorities for BGP routes affects route selection among BGP routes and routes of other routing protocols.After a route-policy or route-filter is configured on a device, the device sets priorities only for the routes received from peers, which meet the matching rules. The routes that do not meet the rules use the default priority.The smaller the priority value, the higher the priority.

**Prerequisites**

If the **preference** command uses the route-policy to set the preference, you need to create a route-policy first.

**Precautions**

Currently, the **peer route-policy** or **peer route-filter** command cannot be used to apply a route-policy to a peer to set the preference of BGP.The **preference** command cannot be used to change the preference of the routes imported using the network or **import-route** command. The preferences of the routes imported using the network or **import-route** command inherit the preferences of the imported routes.In this command, the local parameter specifies the protocol preference of the summary route and leaked route. This parameter takes effect for the following types of routes:

* Summary routes manually generated using the aggregate (BGP) command. The route type of such a route is displayed as Aggregated route.
* Summary routes automatically generated using the **summary automatic** command. The route type of such a route is displayed as Summary automatic route.
* Remotely leaked routes. The route type of such a route is displayed as Remote-Cross route.
* Locally leaked routes. The route type of such a route is displayed as Local-Cross route.If **route-policy** *route-policy-name*is configured, the following items can be matched: AS\_Path filter, AS\_Path length, community filter, route cost, destination address of IPv6 routes, VPN-Target extended community filter, SoO extended community filter, MPLS label, Large-Community filter, next-hop address ACL list of routing information, next-hop address ACL list of IPv6 routing information, next-hop address prefix list of routing information, next-hop address prefix list based on IPv6 routing information, route priority, destination address prefix list of IPv6 routing information, route modulo, route source IP address ACL list, route source IPv6 address ACL list, route source IP address prefix list, route source IPv6 address prefix list, route type attribute, and route priority.If the referenced policy contains unsupported attribute matching or setting behaviors, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.Setting the BGP preference affects route selection between BGP and other routing protocols, such as the type and direction of active routes. In addition, routes may fail to be imported.

Example
-------

# Set a BGP route priority based on a specified route-filter.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] preference 2 2 20

```