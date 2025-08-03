Encapsulating a Multicast Data Packet into an SA Message
========================================================

By default, a source active (SA) message contains only (S, G) information. To ensure successful multicast data packet transmission, enable the source Rendezvous Point (RP) configured with MSDP peer relationships to encapsulate multicast data packets into SA messages.

#### Context

To ensure successful multicast data forwarding on a network that has a small volume of multicast traffic, configure the source RP of MSDP peers to encapsulate multicast data packets into SA messages.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MSDP view is displayed.
3. Run [**encap-data-enable**](cmdqueryname=encap-data-enable)
   
   
   
   The function to encapsulate multicast data packets into SA messages is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.