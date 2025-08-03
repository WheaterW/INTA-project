Setting the Maximum Number of RIP Routes
========================================

You can set the maximum number of RIP routes to make full use of
network resources and improve network performance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Run [**maximum-routes**](cmdqueryname=maximum-routes) *max-number* [ **threshold** *threshold-value* ]
   
   
   
   The maximum number
   of routes is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.