Configuring a Method for IS-IS to Process Equal-Cost Routes (IPv4)
==================================================================

If multiple equal-cost routes are available on an IS-IS network, you can configure load balancing to increase the bandwidth usage of each link, or configure weights for the equal-cost routes to facilitate service traffic management.

#### Context

If there are multiple redundant links on an IS-IS network, multiple equal-cost routes may exist. In this case, you can use either of the following methods:

* Configure load balancing so that traffic is balanced among links.
  
  This method improves link utilization and reduces the possibility of congestion caused by link overload. However, load balancing randomly forwards traffic, which may affect service traffic management.
* Configure weights for equal-cost routes so that the route with the highest priority is preferentially selected, with others functioning as backups.
  
  In this mode, you can allow one or more routes to be preferentially selected without modifying the original configuration. This ensures network reliability and facilitates service traffic management.


#### Procedure

* Configure load balancing for equal-cost IS-IS routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number*
     
     
     
     The maximum number of equal-cost IS-IS routes for load balancing is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) If the actual equal-cost routes outnumber the value specified in the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) command, routes are selected for load balancing based on the following rules:
     1. Route weight: Routes with small weight values (high priority) are selected for load balancing. For details about route preference configuration, see [Configure priorities for equal-cost IS-IS routes](#EN-US_TASK_0172365982__dc_vrp_isis_cfg_100801).
     2. Next-hop system ID: If routes have the same weight, those with small system IDs are selected for load balancing.
     3. Outbound interface index: If routes have the same weight and system ID, those with small outbound interface indexes are selected for load balancing.
     4. Next-hop IP address: If the weights, next-hop system IDs, and interface indexes of the routes are the same, their next-hop IP addresses are compared. The routes with high IP addresses are selected for load balancing.
  4. (Optional) Run [**ecmp-prefer**](cmdqueryname=ecmp-prefer) [ **te-tunnel** | **intact** ]
     
     
     
     The priority is set for the routes with a TE tunnel interface or an IPv4 interface as the outbound interface.
     
     If both an IGP-Shortcut-enabled TE tunnel and IP link are available, you can configure a priority for the routes with a TE tunnel interface or an IPv4 interface as the outbound interface for route selection.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure weights for equal-cost IS-IS routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**nexthop**](cmdqueryname=nexthop) *ip-address* **weight** *value*
     
     
     
     A weight is configured for an equal-cost route.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A smaller *value* indicates a higher priority.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.