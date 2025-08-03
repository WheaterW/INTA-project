(Optional) Setting the Default Priority for IPv6 Static Routes
==============================================================

You can change default priority for IPv6 static routes.

#### Context

After an IPv6 static route is configured, the default priority is used if no priority is specified for the static route. After the default priority is re-set, the new default priority takes effect only on new IPv6 static routes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 route-static default-preference**](cmdqueryname=ipv6+route-static+default-preference) *preference*
   
   
   
   The default preference value is configured for IPv6 static routes.
   
   
   
   By default, the priority of IPv6 static routes is lower than those of OSPF and IS-IS routes. To allow IPv6 static routes to take effect when OSPF or IS-IS routes exist, configure the default priority of IPv6 static routes to be higher than that of OSPF or IS-IS routes before you configure IPv6 static routes. A smaller preference value indicates a higher priority.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.