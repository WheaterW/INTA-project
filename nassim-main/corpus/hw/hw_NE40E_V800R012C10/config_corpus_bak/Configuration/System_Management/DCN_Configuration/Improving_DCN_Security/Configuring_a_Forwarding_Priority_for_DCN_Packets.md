Configuring a Forwarding Priority for DCN Packets
=================================================

If DCN packets are carried by IP packets, the forwarding priority of the DCN packets is lower than other packets. In this scenario, configure a forwarding priority, based on which a GNE forwards the DCN packets.

#### Context

Packets have protocol priorities, based on which they are transmitted. On a DCN network, you can configure a forwarding priority for DCN packets as follows:

* If service packet transmission must be ensured, reduce the forwarding priority of DCN packets to be lower than that of service packets, which prevents service packet loss.
* If service packet transmission requirement is not high, increase the forwarding priority of DCN packets to be higher than that of service packets, which ensures the communication between NEs and between each NE and the NMS.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dcn**](cmdqueryname=dcn)
   
   
   
   The DCN view is displayed.
3. Run [**data-packet priority**](cmdqueryname=data-packet+priority) *priority*
   
   
   
   A protocol priority is configured for DCN packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.