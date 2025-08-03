Creating a DS-Lite Load Balancing Instance
==========================================

Multiple service-location groups need to be created and be bound to the same service-instance group.

#### Context

Different service-location groups are bound to different CPUs of service boards. One service-instance group can be bound to multiple service-location groups, and a DS-Lite instance must be bound to the service-instance group.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
   
   
   
   A service-location group is created, and the service-location group view is displayed.
3. Run [**location**](cmdqueryname=location) **slot** *slot-id* [ **backup** **slot** *slot-id* ]
   
   
   
   The CPU of the service board is bound in the service-location group view.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
   
   
   
   A service-instance group is created, and the service-instance group view is displayed.
7. Run [**service-location**](cmdqueryname=service-location) *service-location-id* [ **weight** *weight-value* ]
   
   
   
   The service-location group is bound to the service-instance group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A service-instance group must be bound to multiple service-location groups, and each of these service-location groups must be bound to a different service board or a different CPU on the same service board.
   
   In the DS-Lite load balancing over inter-board hot backup scenario, when a load balancing instance group is bound to multiple service-location groups, the CPUs bound to the service-location groups cannot back up each other, and the positions of these CPUs must be unique.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
    
    
    
    The DS-Lite instance view is displayed.
11. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
    
    
    
    The DS-Lite instance is bound to the service-instance group.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In the centralized load balancing and online upgrade and capacity expansion scenario, some user traffic may be interrupted temporarily and then recover automatically.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.