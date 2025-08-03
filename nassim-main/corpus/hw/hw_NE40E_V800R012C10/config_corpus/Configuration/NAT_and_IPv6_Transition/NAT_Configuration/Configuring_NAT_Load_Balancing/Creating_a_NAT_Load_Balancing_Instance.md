Creating a NAT Load Balancing Instance
======================================

Multiple service-location groups need to be created and bound to the same service-instance group.

#### Context

After service-location groups are bound to CPUs of the specified [dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595), one service-instance group can be bound to these service-location groups and bound to a NAT instance.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
   
   
   
   A service-location group is created, and its view is displayed.
3. Run [**location**](cmdqueryname=location) **slot** *slot-id* [ **backup** **slot** *slot-id* ]
   
   
   
   The CPU of the service board is bound in the service-location group view.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the number of session resources of all load balancing members be set to the same value.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
   
   
   
   A service-instance group is created, and its view is displayed.
7. Run [**service-location**](cmdqueryname=service-location) *service-location-id* [ **weight** *weight-value* ]
   
   
   
   The service-location group is bound to the service-instance group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A service-instance group must be bound to multiple service-location groups, and the service-location groups must be bound to different service boards ([dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595)) or different CPUs of the same service board.
   
   In the CGN load balancing over inter-board hot backup scenario, when a load balancing instance group is bound to multiple service-location groups, the CPUs bound to the service-location groups cannot back up each other, and the positions of these CPUs cannot duplicate.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
    
    
    
    The NAT instance view is displayed.
11. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
    
    
    
    The NAT instance is bound to the service-instance group.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In an online upgrade or capacity expansion scenario with centralized load balancing, some user traffic will be interrupted temporarily and then recover automatically.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.