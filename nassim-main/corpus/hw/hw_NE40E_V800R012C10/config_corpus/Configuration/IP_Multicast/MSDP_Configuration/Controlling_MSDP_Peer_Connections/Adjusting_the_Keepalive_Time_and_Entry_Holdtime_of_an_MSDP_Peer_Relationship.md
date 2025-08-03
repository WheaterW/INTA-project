Adjusting the Keepalive Time and Entry Holdtime of an MSDP Peer Relationship
============================================================================

You can adjust the keepalive time and entry holdtime of an MSDP peer relationship, so that the device will delete the relationship in time when it is not needed.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MSDP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **hold-time-interval** *holdtime-value*Router
   
   
   
   A holdtime timer value is set for the entry of an MSDP peer relationship.
4. Run [**peer**](cmdqueryname=peer) *peer-address* **keepalive-interval** *keepalive-time-value*
   
   
   
   A keepalive timer value is set for the MSDP peer.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The keepalive timer value set on the local end must be less than the holdtime timer value set on the peer end for the corresponding MSDP peer relationship entry.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.