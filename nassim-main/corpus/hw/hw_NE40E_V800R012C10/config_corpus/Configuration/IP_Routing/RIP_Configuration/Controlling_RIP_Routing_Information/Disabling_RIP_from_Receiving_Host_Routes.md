Disabling RIP from Receiving Host Routes
========================================

You can disable RIP from receiving host routes on a device
to prevent the device from receiving a large number of unwanted routes.
Such configuration can reduce network resource consumption.

#### Context

In some situations, the Router may receive a large number of host routes from the same network
segment. These routes, useless for routing, consume many network resources.
By disabling RIP from receiving host routes, you can configure the Router to reject the received host routes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Run [**undo host-route**](cmdqueryname=undo+host-route)
   
   
   
   RIP is disabled from receiving host routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.