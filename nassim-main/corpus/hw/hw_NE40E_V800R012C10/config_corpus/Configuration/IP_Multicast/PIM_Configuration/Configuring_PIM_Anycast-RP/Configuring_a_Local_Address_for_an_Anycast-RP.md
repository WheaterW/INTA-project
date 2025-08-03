Configuring a Local Address for an Anycast-RP
=============================================

When sending a PIM Register message to all Anycast-RP peers, the local Rendezvous Point (RP) needs to use its own IP address (called the local address) as the source address of the Register message.

#### Context

The Routers functioning as Anycast-RPs can be identified by the same logical address so that the RP in the PIM-SM domain is unique. However, the Routers need to distinguish one another during the communication, so the Anycast-RP address cannot be used. To resolve this issue, configure a local address for the Anycast-RP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
3. Run [**anycast-rp**](cmdqueryname=anycast-rp) *rp-address*
   
   
   
   The Anycast-RP view is displayed.
4. Run [**local-address**](cmdqueryname=local-address) *local-address*
   
   
   
   A local address is set for the Anycast-RP.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Setting a Loopback interface address as the local address of the Anycast-RP is recommended.
   
   The local address must be different from the Anycast-RP address.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.