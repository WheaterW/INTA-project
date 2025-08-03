Binding a Service Board to a NAT64 Instance
===========================================

This section describes how to bind a service board to a NAT64 instance. A NAT64 instance is a logical carrier that implements NAT64 functions.

#### Context

The creation of NAT64 instances is the basis of NAT64 configuration because NAT64 instances are used in many subsequent configurations. For example, you may configure the CPUs of the master and backup service boards in a NAT64 instance to work in inter-board hot backup mode; you may also configure the CPUs of a service board on a master device and a service board on a slave device in a NAT64 instance to work in inter-chassis hot backup mode.

The NAT64 instance needs to be bound to a service-instance group so that the instance is indirectly bound to CPUs of service boards. To bind a NAT64 instance to the CPU of a service board, create a service-location group, bind the group to the CPU of the service board, bind the service-instance group to the service-location group, and bind the NAT64 instance to the service-instance group in the NAT64 instance view.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
   
   
   
   A service-location group is created, and the service-location group view is displayed.
3. Run [**location**](cmdqueryname=location) **slot** *slot-id*
   
   
   
   The CPU of the service board is bound in the service-location group view.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
   
   
   
   A service-instance group is created, and the service-instance group view is displayed.
7. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
   
   
   
   The service-location group is bound.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* [ **id** *id* ]
    
    
    
    The NAT64 instance view is displayed.
11. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
    
    
    
    The service-instance group is bound.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.