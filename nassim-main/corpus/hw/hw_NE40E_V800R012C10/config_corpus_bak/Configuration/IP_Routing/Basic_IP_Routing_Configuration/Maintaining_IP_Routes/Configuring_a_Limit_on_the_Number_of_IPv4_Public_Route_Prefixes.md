Configuring a Limit on the Number of IPv4 Public Route Prefixes
===============================================================

Configuring a limit on the number of IPv4 public route prefixes can improve system security and reliability.

#### Context

If the Router imports a large number of routes, system performance may be affected when processing services because the routes consume a lot of system resources. To improve system security and reliability, configure a limit on the number of IPv4 public route prefixes. When the number of IPv4 public route prefixes exceeds the limit, an alarm is generated, prompting you to check whether unneeded IPv4 public route prefixes exist.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip prefix-limit**](cmdqueryname=ip+prefix-limit) *number* { *alert-percent* [ **route-unchanged** ] | **simply-alert**}
   
   
   
   A limit is configured for the maximum number of IPv4 public network route prefixes.
   
   
   
   If the **route-unchanged** parameter is configured, routes in the routing table remain unchanged after the number of routes exceeds the limit. When the number of route prefixes in the routing table exceeds the *number*, if you decrease the *alert-percent* value, the system processes routes according to the following rules:
   * If the **route-unchanged** parameter is configured, routes in the routing table remain unchanged.
   * If the **route-unchanged** parameter is not configured, the device deletes all routes from the routing table and re-adds routes.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.