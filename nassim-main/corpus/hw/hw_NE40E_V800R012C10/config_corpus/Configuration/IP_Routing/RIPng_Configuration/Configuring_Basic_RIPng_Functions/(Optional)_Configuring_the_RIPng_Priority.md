(Optional) Configuring the RIPng Priority
=========================================

When multiple routing protocols are running on the same
device, you can adjust the priority of RIPng for route selection.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ripng**](cmdqueryname=ripng) [ *process-id* ]
   
   
   
   The RIPng process is created and the RIPng view is displayed.
3. Run [**preference**](cmdqueryname=preference) { *preference* | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } } \*
   
   
   
   The RIPng priority is set.
   
   The [**preference**](cmdqueryname=preference) command can be used with the routing policy to set the priority
   for the routes that meet the matching conditions.
   
   After RIPng
   routes are delivered to the Routing Management (RM), if the RIPng
   priority changes, the RM updates the routing table.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   submitted.