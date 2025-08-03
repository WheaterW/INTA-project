preference (BGP view)
=====================

preference (BGP view)

Function
--------



The **preference** command sets a priority for EBGP routes, IBGP routes, or local BGP routes. BGP routes are configured with different priorities in different address family views.

The **undo preference** command restores the default setting.



By default, the priorities of EBGP routes, IBGP routes, and local BGP routes are all 255.


Format
------

**preference** { *external* *internal* *local* | **route-policy** *route-policy-name* }

**undo preference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *external* | Specifies the priority of an EBGP route. An EBGP route is the optimal route learned from a peer outside the local AS. | The value is an integer that ranges from 1 to 255. A smaller value indicates a higher priority. |
| *internal* | Specifies a protocol preference of IBGP external routes, which are the optimal routes learned from peers inside the local AS. | The value is an integer that ranges from 1 to 255. A smaller value indicates a higher priority. |
| *local* | Specifies the priority for local routes. This parameter takes effect for the following routes:   * Manually summary routes generated using the aggregate (BGP) command. * Automatically summary routes generated using the summary automatic command. * Routes generated through remote route leaking. * Routes generated through local route leaking. For details about these routes, see Precautions. | The value is an integer that ranges from 1 to 255. A smaller value indicates a higher priority.  This parameter takes effect for the following routes:   * Summary routes that are generated using the aggregate (BGP) command. * Automatic summary routes generated using the summary automatic command. * Remotely leaked routes. * Locally leaked routes.   For details about how to identify the preceding types of routes, see Precautions. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP view


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

Currently, the **peer route-policy** or **peer route-filter** command cannot be used to apply a routing policy to a peer to set the preference of BGP.The **preference** command cannot be used to change the preference of the routes imported using the network or **import-route** command. The priority of the route imported using the network or **import-route** command inherits the priority of the referenced route.In this command, the local parameter specifies the protocol preference of the summary route and leaked route. This parameter takes effect for the following types of routes:

* Summary routes manually generated using the aggregate (BGP) command. The route type of such a route is displayed as Aggregated route.
* Summary routes automatically generated using the **summary automatic** command. The route type of such a route is displayed as Summary automatic route.
* Remotely leaked routes. The route type of such a route is displayed as Remote-Cross route.
* Locally leaked routes. The route type of such a route is displayed as Local-Cross route.If **route-policy** *route-policy-name*is configured, the following items can be matched: IPv4 ACL, AS\_Path filter, AS\_Path length filter, community filter, route cost filter, VPN-Target extended community filter, bandwidth extended community filter, MPLS label filter, Large-Community filter, next-hop address ACL list of routing information, next-hop address ACL list of IPv6 routing information, next-hop address prefix list of routing information, next-hop address prefix list based on IPv6 routing information, route priority, destination address prefix list of IP routing information, route modulo, route source IP address ACL list, route source IPv6 address ACL list, route source IP address prefix list, and route type. The route priority attribute can be set.If the referenced policy contains unsupported attribute matching or setting behaviors, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.Setting the BGP preference affects route selection between BGP and other routing protocols, such as the type and direction of active routes. In addition, routes may fail to be imported.

Example
-------

# Configure a route-filter to set a priority for BGP.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] preference route-filter aa

```