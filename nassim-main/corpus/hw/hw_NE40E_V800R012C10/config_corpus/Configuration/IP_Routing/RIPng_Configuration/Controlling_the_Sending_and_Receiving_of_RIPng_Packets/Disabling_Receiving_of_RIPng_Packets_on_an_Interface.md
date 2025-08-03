Disabling Receiving of RIPng Packets on an Interface
====================================================

Disabling interfaces from receiving RIPng packets is a
method of preventing routing loops.

#### Context

When a device running RIPng is connected to a network
running other routing protocols, you can run the [**undo ripng input**](cmdqueryname=undo+ripng+input) command
on the interface that connects the device to the network to prevent
the interface from receiving useless packets from the network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**undo ripng input**](cmdqueryname=undo+ripng+input)
   
   
   
   The interface is disabled from receiving RIPng packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   submitted.