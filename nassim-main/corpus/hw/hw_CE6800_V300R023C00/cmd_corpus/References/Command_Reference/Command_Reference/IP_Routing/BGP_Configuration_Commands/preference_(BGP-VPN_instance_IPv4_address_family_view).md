preference (BGP-VPN instance IPv4 address family view)
======================================================

preference (BGP-VPN instance IPv4 address family view)

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
| *external* | Specifies the priority of an EBGP route. An EBGP route is the optimal route learned from a peer outside the local AS. | The value is an integer ranging from 1 to 255. The smaller the value is, the higher the priority is. |
| *internal* | Specifies the priority of an IBGP route. An IBGP route is a route learned from a peer inside the AS. | The value is an integer ranging from 1 to 255. The smaller the value is, the higher the priority is. |
| *local* | Specifies the priority for summary and leaked routes. This parameter takes effect for the following routes:   * Manually summary routes generated using the aggregate (BGP) command. * Automatically summary routes generated using the summary automatic command. * Routes generated through remote route leaking. * Routes generated through local route leaking. For details about these routes, see. Precautions. | The value is an integer ranging from 1 to 255. The smaller the value is, the higher the priority is. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Running the **preference** command to set priorities for BGP routes affects route selection among BGP routes and routes of other routing protocols.After a route-policy or route-filter is configured on a device, the device sets priorities only for the received routes that meet the matching rules. The routes that do not meet the rules use the default priority.The smaller the priority value, the higher the priority.A route learned from a VPNv4 peer can be matched to a VPN instance through RT matching, and then the **preference** command can be run in the VPN address family view to configure a priority for the route.

**Prerequisites**

If the **preference** command uses the route-policy to set the preference, you need to create a route-policy first.

**Precautions**

Currently, the **peer route-policy** or **peer route-filter** command cannot be used to apply a route-policy to a peer to set the preference of BGP.The **preference** command cannot be used to change the preference of the routes imported using the network or **import-route** command. The preferences of the routes imported using the network or **import-route** command inherit the preferences of the imported routes.In this command, the local parameter specifies the protocol preference of the summary route and leaked route. This parameter takes effect for the following types of routes:

* Summary routes manually generated using the aggregate (BGP) command. The route type of such a route is displayed as Aggregated route.
* Summary routes automatically generated using the **summary automatic** command. The route type of such a route is displayed as Summary automatic route.
* Remotely leaked routes. The route type of such a route is displayed as Remote-Cross route.
* Locally leaked routes. The route type of such a route is displayed as Local-Cross route.If **route-policy** *route-policy-name*is configured, the following items can be matched: IPv4 ACLs, AS\_Path filters, AS\_Path length filters, community filters, route costs, VPN-Target extended community filters, SoO extended community filters, MPLS label filters, Large-Community filters, Next-hop address ACL list, next-hop address prefix list, route priority, destination address prefix list, route modulo, source IP address ACL list, source IP address prefix list, and route type. The route priority attribute can be set.If the referenced policy contains unsupported attribute matching or setting behaviors, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.Setting the BGP preference affects route selection between BGP and other routing protocols, such as the type and direction of active routes. In addition, routes may fail to be imported.

Example
-------

# Set the priority to 2 for EBGP routes, 2 for IBGP routes, and 20 for local BGP routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] preference 2 2 20

```