(Optional) Setting the TTL Threshold for Forwarding an SA Message Containing a Multicast Data Packet
====================================================================================================

After receiving a source active (SA) message encapsulated with a multicast data packet, an MSDP peer forwards the SA message to a specified remote MSDP peer only when the TTL value of the multicast packet is greater than the configured TTL threshold.

#### Context

Perform the following steps on the Router configured with an MSDP peer:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the configuration is not performed, default parameter values are used.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MSDP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **minimum-ttl** *ttl*
   
   
   
   A TTL threshold is set for multicast data packets.
   
   After receiving an SA message containing a multicast data packet, an MSDP peer forwards the SA message to a specified remote MSDP peer only when the TTL value of the multicast packet is greater than the configured TTL threshold.
   
   The parameter meanings as follows:
   
   
   
   * *peer-address*: specifies the IP address of a remote MSDP peer.
   * *ttl*: specifies the value of the TTL threshold. The default value is 0.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.