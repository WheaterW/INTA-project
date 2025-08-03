Disabling Soft Forwarding for IPv6 Multicast Packets
====================================================

Disabling soft forwarding for multicast packets on a multicast Router prevents packet loss and disorder.

#### Usage Scenario

In most cases, the Router forwards packets based on software before the hardware forwarding is completed. After that, the forwards packets based on hardware.

Soft forwarding for IPv6 multicast packets must be disabled on the router to prevent the low forwarding speed and first packet cache mechanism of soft forwarding from causing disorder of the first packet transmitted at a high speed.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast ipv6 cpu-forward disable**](cmdqueryname=multicast+ipv6+cpu-forward+disable)
   
   
   
   Soft forwarding is disabled for multicast packets.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.