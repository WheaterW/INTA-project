Binding a Service Board to a NAT Instance
=========================================

Creating a NAT instance is a prerequisite for NAT. However, you need to bind the NAT instance to a board so that pre-NAT packets can be processed by the corresponding service board.

#### Context

After a NAT instance is bound to a service-instance group that is bound to a service-location group, the NAT instance is bound to the service-location group, enabling the NAT service board to process NAT services.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
   
   
   
   The service-location group view is displayed.
3. Run [**location**](cmdqueryname=location) **slot** *slot-id*
   
   
   
   A NAT service board is bound to the service-location group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
   
   
   
   A service-instance group is created, and its view is displayed.
7. Run [**service-location**](cmdqueryname=service-location) *service-location-id* [ **weight** *weight-value* ]
   
   
   
   The service-location group is bound to the service-instance group.
   
   
   
   In load balancing scenarios where different types of boards are installed on the same device, to improve CPU utilization, you can set the **weight** parameter to adjust the load balancing weight.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
    
    
    
    The NAT instance view is displayed.
11. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
    
    
    
    The NAT instance is bound to the service-instance group.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    * Only one [**location**](cmdqueryname=location) command can be configured in a service-location group.
    * Note that one NAT instance can be bound to only one service-instance group.