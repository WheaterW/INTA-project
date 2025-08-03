Disabling Sending of RIPng Packets on an Interface
==================================================

Disabling an interface from sending RIPng packets is a
method of preventing routing loops.

#### Context

When a device running RIPng is connected to a network
running other routing protocols, you can run the [**undo ripng output**](cmdqueryname=undo+ripng+output) command
on the interface that connects the device to the network to prevent
the interface from sending useless packets to the network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**undo ripng output**](cmdqueryname=undo+ripng+output)
   
   
   
   The interface is disabled from sending RIPng packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   submitted.