preference (BGP multi-instance VPN instance IPv4 address family view)
=====================================================================

preference (BGP multi-instance VPN instance IPv4 address family view)

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
| *external* | Specifies a protocol preference of EBGP external routes, which are the optimal routes learned from peers outside the local AS. | The value is an integer that ranges from 1 to 255. A smaller value indicates a higher priority. |
| *internal* | Specifies the protocol preference of IBGP routes (those learned from peers in the same AS). | The value is an integer that ranges from 1 to 255. A smaller value indicates a higher priority. |
| *local* | Specifies the priority for local routes. This parameter takes effect for the following routes:   * Manually summary routes generated using the aggregate (BGP) command. * Automatically summary routes generated using the summary automatic command. * Routes generated through remote route leaking. * Routes generated through local route leaking. For details about these routes, see Precautions. | The value is an integer that ranges from 1 to 255. A smaller value indicates a higher priority. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


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
* Locally leaked routes. The route type of such a route is displayed as Local-Cross route.If **route-policy** *route-policy-name*is configured, the following items can be matched: IPv4 ACLs, AS\_Path filters, AS\_Path length filters, community filters, route costs, VPN-Target extended community filters, SoO extended community filters, MPLS label filters, Large-Community filters, next-hop address ACL list, next-hop address prefix list, route priority, destination address prefix list, route modulo, source IP address ACL list, source IP address prefix list, and route type. The route priority attribute can be set.If the referenced policy contains unsupported attribute matching or setting behavior, unexpected results may occur.Setting the BGP preference affects route selection between BGP and other routing protocols, such as the type and direction of active routes. In addition, routes may fail to be imported.


Example
-------

# Set the priority to 2 for EBGP routes, 2 for IBGP routes, and 20 for local BGP routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-instance-vpn1] quit
[~HUAWEI] bgp 100 instance aa
[~HUAWEI-bgp-instance-aa] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-instance-aa-vpn1] preference 2 2 20

```