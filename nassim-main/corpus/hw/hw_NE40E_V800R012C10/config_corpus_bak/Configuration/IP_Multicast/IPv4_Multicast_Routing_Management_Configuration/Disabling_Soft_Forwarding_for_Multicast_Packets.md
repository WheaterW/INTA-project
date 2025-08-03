Disabling Soft Forwarding for Multicast Packets
===============================================

Disabling soft forwarding for multicast packets on a multicast Router prevents packet loss and disorder.

#### Usage Scenario

In most cases, the Router forwards packets based on software before the hardware forwarding is completed. After that, the Router forwards packets based on hardware.

Soft forwarding for multicast packets must be disabled on the Router to prevent the low forwarding speed and first packet cache mechanism of soft forwarding from causing disorder of the first packet transmitted at a high speed.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast cpu-forward disable**](cmdqueryname=multicast+cpu-forward+disable)
   
   
   
   Soft forwarding is disabled for multicast packets.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.