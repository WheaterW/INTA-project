Configuring the Maximum Number of Equal-Cost Routes
===================================================

By setting the maximum number of equal-cost RIP routes, you can change the number of routes for load balancing.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing)  *number*
   
   
   
   The maximum number of equal-cost routes is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.