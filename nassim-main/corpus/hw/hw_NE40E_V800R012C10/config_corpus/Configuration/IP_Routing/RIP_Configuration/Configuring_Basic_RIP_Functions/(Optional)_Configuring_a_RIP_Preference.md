(Optional) Configuring a RIP Preference
=======================================

When there are routes discovered by multiple routing protocols on the same device, you can set a preference for RIP to control the route selection result.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Run [**preference**](cmdqueryname=preference) { *preference* | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }  } \*
   
   
   
   A preference is set for RIP.
   
   
   
   The [**preference**](cmdqueryname=preference) command can be used together with a route-policy to set a preference for the matched routes.
   
   If the RIP preference is changed after RIP routing information is delivered to the routing management (RM) module, the RM module re-updates the routing table.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.