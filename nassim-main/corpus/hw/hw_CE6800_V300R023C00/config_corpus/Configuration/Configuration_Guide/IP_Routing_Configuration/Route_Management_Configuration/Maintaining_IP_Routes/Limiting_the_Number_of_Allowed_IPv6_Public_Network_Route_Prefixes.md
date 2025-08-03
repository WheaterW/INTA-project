Limiting the Number of Allowed IPv6 Public Network Route Prefixes
=================================================================

Limiting the Number of Allowed IPv6 Public Network Route Prefixes

#### Context

If a device imports a large number of routes, excessive system resources are consumed and system performance may deteriorate when the device is busy. To improve system security and reliability, set a limit on the number of IPv6 public network route prefixes. When the number of IPv6 public network route prefixes exceeds a specified alarm threshold, no more route prefixes can be added, and an alarm is generated, prompting you to check whether unneeded IPv6 public network route prefixes exist.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the limit on the number of allowed IPv6 public network route prefixes.
   
   
   ```
   [ipv6 prefix-limit](cmdqueryname=ipv6+prefix-limit) number { alert-percent [ route-unchanged ] | simply-alert }
   ```
   
   
   If the **route-unchanged** parameter is configured, routes in the routing table remain unchanged after the number of routes exceeds the upper limit. If you decrease the *alert-percent* value and the number of IPv6 public network route prefixes in the routing table exceeds the specified upper limit, the processing is as follows:
   * If the **route-unchanged** parameter is configured, routes in the routing table remain unchanged.
   * If the **route-unchanged** parameter is not configured, all routes in the routing table are deleted and routes are then re-added to the routing table.
   By default, the **route-unchanged** parameter is not configured.![](public_sys-resources/note_3.0-en-us.png) When the number of IPv6 route prefixes exceeds the upper limit, note the following:
   * If you run the [**ipv6 prefix-limit**](cmdqueryname=ipv6+prefix-limit) command to increase the *number* value or the [**undo ipv6 prefix-limit**](cmdqueryname=undo+ipv6+prefix-limit) command to cancel the limit, the device relearns IPv6 public network route prefixes.
   * You can run the [**display ipv6 routing-table limit**](cmdqueryname=display+ipv6+routing-table+limit) [ **all-vpn-instance** | **vpn-instance** *vpn-instance-name* ] command to view the limit on the number of allowed routes and prefixes.
   * Direct and static routes can still be added to the IPv6 routing table.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```