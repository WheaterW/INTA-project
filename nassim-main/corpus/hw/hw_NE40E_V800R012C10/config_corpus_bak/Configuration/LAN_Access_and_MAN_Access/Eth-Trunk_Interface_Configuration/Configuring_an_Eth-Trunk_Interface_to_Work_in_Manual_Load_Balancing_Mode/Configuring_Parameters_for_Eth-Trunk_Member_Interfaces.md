Configuring Parameters for Eth-Trunk Member Interfaces
======================================================

To ensure reliable communication between Eth-Trunk interfaces, configure proper parameters for Eth-Trunk member interfaces.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of an Eth-Trunk member interface is displayed.
3. Run [**distribute-weight**](cmdqueryname=distribute-weight) *weight-value*
   
   
   
   A load-balancing weight is configured for the Eth-Trunk member interface.
   
   
   
   The number of member interfaces of an Eth-Trunk interfaces cannot exceed the maximum number of member interfaces allowed.
   
   An Eth-Trunk interface performs load balancing based on the weights of its member interfaces. The greater the weight of an Eth-Trunk member interface, the heavier the load carried by the member interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.