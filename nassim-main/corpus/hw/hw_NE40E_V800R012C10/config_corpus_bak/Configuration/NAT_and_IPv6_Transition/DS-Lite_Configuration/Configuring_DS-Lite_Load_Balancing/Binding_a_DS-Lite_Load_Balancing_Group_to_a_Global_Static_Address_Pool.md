Binding a DS-Lite Load Balancing Group to a Global Static Address Pool
======================================================================

To allow for DS-Lite load balancing, bind a DS-Lite load balancing group to a global static address pool.

#### Context

One DS-Lite service can be bound only to one service board CPU, the service board of a single DS-Lite instance may reach the performance threshold when the number of users goes up. In this case, expand the board to support user traffic forwarding. If a global static address pool is bound to a DS-Lite instance, multiple boards can share the same address pool.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
   
   
   
   The DS-Lite instance view is displayed.
3. Run [**ds-lite address-group**](cmdqueryname=ds-lite+address-group) *address-group-name* **group-id** *group-id* **bind-ip-pool** *pool-name*
   
   
   
   The DS-Lite instance is bound to a global static address pool.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.