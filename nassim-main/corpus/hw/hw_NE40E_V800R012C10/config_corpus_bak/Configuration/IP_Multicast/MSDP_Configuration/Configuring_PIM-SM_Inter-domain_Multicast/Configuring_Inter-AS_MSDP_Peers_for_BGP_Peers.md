Configuring Inter-AS MSDP Peers for BGP Peers
=============================================

To enable PIM-SM domains in different ASs to share multicast source information, configure an MSDP peer relationship between Rendezvous Points (RPs) in different ASs in which a BGP peer relationship is set up.

#### Context

Establish a BGP peer relationship between the RPs in different ASs and then perform the following steps:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MSDP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **connect-interface** *interface-type* *interface-number*
   
   
   
   An MSDP peer connection is set up.
   
   
   
   * *peer-address*: specifies the IP address of a remote MSDP peer. The address is the same as that of the remote BGP peer.
   * *interface-type* *interface-number*: specifies the local interface connected with the remote MSDP peer. This interface is the local BGP peer interface.
4. (Optional) Run [**peer**](cmdqueryname=peer) *peer-address* **description** *text*
   
   
   
   A description is added for the remote MSDP peer.
   
   This configuration helps you differentiate remote MSDP peers and manage the connections with the remote MSDP peers.
   
   * *peer-address*: specifies the IP address of a remote MSDP peer.
   * *text*: specifies the description text. The text is a string of a maximum of 80 characters.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.