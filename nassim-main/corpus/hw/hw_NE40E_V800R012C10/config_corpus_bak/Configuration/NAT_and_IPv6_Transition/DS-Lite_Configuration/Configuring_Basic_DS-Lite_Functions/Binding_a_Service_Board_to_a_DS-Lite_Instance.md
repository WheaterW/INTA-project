Binding a Service Board to a DS-Lite Instance
=============================================

Only after a DS-Lite instance is created and bound to a DS-Lite board, can a device direct packets to the DS-Lite board and run DS-Lite to process the packets.

#### Context

After a service-instance group is bound to a service-location group and a DS-Lite instance is bound to the service-instance group, the DS-Lite instance is bound to the service-location group. In this way, the DS-Lite service traffic can be processed on the service board.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsm on-board-mode disable**](cmdqueryname=vsm+on-board-mode+disable)
   
   
   
   The dedicated board working mode is specified.
3. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
   
   
   
   A service-location group is created, and the service-location group view is displayed.
4. Run [**location**](cmdqueryname=location) **slot** *slot-id* [ **backup** **slot** *slot-id* ]
   
   
   
   The CPU of the service board is bound in the service-location group view.
   
   
   
   When inter-board warm or hot backup is used, run the [**location**](cmdqueryname=location) command with **backup** **slot** configured, and ensure that at least two service boards are installed to work in active/standby mode.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
   
   
   
   A service-instance group is created, and the service-instance group view is displayed.
8. Run [**service-location**](cmdqueryname=service-location) *service-location-id* [ **weight** *weight-value* ]
   
   
   
   The service-location group is bound to the service-instance group.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the system view.
11. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* **id** *id*
    
    
    
    A DS-Lite instance is created, and the DS-Lite instance view is displayed.
12. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
    
    
    
    The DS-Lite instance is bound to the service-instance group.
    
    
    
    A service-instance group is bound to a DS-Lite instance so that services can be processed on the involved service board. Note that each DS-Lite instance can be bound to only a single service-instance group.
    
    After the DS-Lite instance view is created, you can enter the view by running the [**ds-lite instance**](cmdqueryname=ds-lite+instance) command without **id** configured.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.