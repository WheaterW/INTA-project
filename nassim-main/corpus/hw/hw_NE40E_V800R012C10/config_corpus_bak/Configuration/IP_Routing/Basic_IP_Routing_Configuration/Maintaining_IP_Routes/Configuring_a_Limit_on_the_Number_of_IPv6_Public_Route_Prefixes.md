Configuring a Limit on the Number of IPv6 Public Route Prefixes
===============================================================

Configuring a limit on the number of IPv6 public route prefixes can improve system security and reliability.

#### Context

If the Router imports a large number of routes, system performance may be affected when processing services because the routes consume a lot of system resources. To improve system security and reliability, configure a limit on the number of IPv6 public route prefixes. When the number of IPv6 public route prefixes exceeds the limit, an alarm is generated, prompting you to check whether unneeded IPv6 public route prefixes exist.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 prefix-limit**](cmdqueryname=ipv6+prefix-limit) *number* { *alert-percent* [ **route-unchanged** ] | **simply-alert** }
   
   
   
   A limit is configured on the number of IPv6 public route prefixes.
   
   
   
   If you decrease *alert-percent* after the number of IPv6 public route prefixes exceeds *number*, whether the routing table remains unchanged is determined by **route-unchanged**.
   * If you specify **route-unchanged** in the command, the routing table remains unchanged.
   * If you do not specify **route-unchanged** in the command, the system deletes the routes from the routing table and re-adds routes.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.