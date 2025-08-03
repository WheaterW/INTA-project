Configuring an Anycast-RP Peer
==============================

When sending a Register message to an Anycast-Rendezvous Point (RP) peer, a device needs to change the destination address of the Register message to the peer address.

#### Context

The Routers functioning as Anycast-RPs can be identified by the same logical address so that the RP in the PIM-SM domain is unique. The anycast RP-enabled Routers, however, need to distinguish one another during communication. Therefore, the configured anycast RP address cannot be used. In this case, you need to configure a local address for an anycast RP and an anycast RP peer relationship.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The PIM-IPv6 view is displayed.
3. Run [**anycast-rp**](cmdqueryname=anycast-rp) *rp-address*
   
   
   
   The IPv6 Anycast-RP view is displayed.
4. Run [**peer**](cmdqueryname=peer) *peer-address*
   
   
   
   An Anycast-RP peer is specified.
   
   
   
   *peer-address*: specifies the address of an Anycast-RP peer.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In a PIM-SM domain, all Anycast-RP-capable devices must be fully connected logically. That is, anycast-RP peer relationships must be configured between every two Anycast-RPs.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.