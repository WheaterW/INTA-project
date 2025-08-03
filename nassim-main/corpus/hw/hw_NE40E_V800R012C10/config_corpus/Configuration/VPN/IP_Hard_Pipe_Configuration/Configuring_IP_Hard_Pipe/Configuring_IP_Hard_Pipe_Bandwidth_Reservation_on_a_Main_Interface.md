Configuring IP Hard Pipe Bandwidth Reservation on a Main Interface
==================================================================

This section describes how to configure IP hard pipe bandwidth reservation on a main interface. The physical interface bandwidth on the public network is divided and allocated to both hard and soft pipes, and the bandwidth of the hard and soft pipes is isolated.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**qos hard-pipe**](cmdqueryname=qos+hard-pipe) **share-mode** **bandwidth** *bandwidth-value* **outbound**
   
   
   
   IP hard pipe bandwidth is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.