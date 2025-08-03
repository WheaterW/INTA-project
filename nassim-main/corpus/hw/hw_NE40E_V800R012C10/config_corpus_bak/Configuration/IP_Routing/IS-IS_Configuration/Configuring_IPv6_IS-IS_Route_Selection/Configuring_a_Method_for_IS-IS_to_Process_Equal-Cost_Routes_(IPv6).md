Configuring a Method for IS-IS to Process Equal-Cost Routes (IPv6)
==================================================================

If multiple equal-cost IPv6 routes are available on an IS-IS network, you can configure load balancing to increase the bandwidth utilization of each link, or configure weights for the equal-cost routes to facilitate service traffic management.

#### Context

When there are multiple redundant IPv6 links on an IPv6 IS-IS network, multiple equal-cost IPv6 routes may exist. You can configure a method for IPv6 IS-IS to process these equal-cost routes as required:

* Configure load balancing so that traffic is balanced among links.
  
  This method improves link utilization and reduces the possibility of congestion caused by link overload. However, load balancing randomly forwards traffic, which may affect service traffic management.
* Configure weights for equal-cost routes so that the route with the highest priority is preferentially selected, with others functioning as backups.
  
  In this mode, you can allow one or more routes to be preferentially selected without modifying the original configuration. This ensures network reliability and facilitates service traffic management.

#### Procedure

* Configure IPv6 IS-IS load balancing.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run **[**ipv6 enable**](cmdqueryname=ipv6+enable)**
     
     
     
     IPv6 is enabled for the IS-IS process.
  4. Run [**ipv6 maximum load-balancing**](cmdqueryname=ipv6+maximum+load-balancing) *number*
     
     
     
     The maximum number of equal-cost routes for load balancing is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) If the equal-cost routes on the network outnumber the value specified in the [**ipv6 maximum load-balancing**](cmdqueryname=ipv6+maximum+load-balancing) command, routes are selected for load balancing based on the following rules:
     1. Route weight: Routes with smaller weight values (higher priorities) are selected for load balancing.
     2. Next-hop system ID: If routes have the same weight, those with lower next-hop system IDs are selected for load balancing.
     3. Outbound interface index: If routes have the same weight and system ID, those with smaller outbound interface indexes are selected for load balancing.
     4. Next-hop IP address: If routes have the same weight, next-hop system ID, and outbound interface index, those with higher next-hop IP addresses are selected for load balancing.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure weights for equal-cost IPv6 IS-IS routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run **[**ipv6 enable**](cmdqueryname=ipv6+enable)**
     
     
     
     IPv6 is enabled for the IS-IS process.
  4. Run [**ipv6 nexthop**](cmdqueryname=ipv6+nexthop) *ip-address* **weight** *weight-value*
     
     
     
     A weight is set for an equal-cost route. A smaller *weight-value* indicates a higher priority.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.