Configuring MSDP Peers on RPs
=============================

MSDP peer relationships need to be set up between Rendezvous Points (RPs). If there are more than three Routers, MSDP peer relationships must be set up between any two Routers and all MSDP peers must be added to one mesh group.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MSDP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **connect-interface** *interface-type* *interface-number*
   
   
   
   An MSDP peer connection is set up.
   
   
   
   * *peer-address*: specifies the IP address of a remote MSDP peer.
   * *interface-type* *interface-number*: specifies the local interface connected with the remote MSDP peer.
4. (Optional) Run [**peer**](cmdqueryname=peer) *peer-address* **description** *text*
   
   
   
   A description is added for the remote MSDP peer.
   
   
   
   This configuration helps you differentiate remote MSDP peers and manage the connections with the remote MSDP peers.
   
   * *peer-address*: specifies the IP address of a remote MSDP peer.
   * *text*: specifies the description text. The text is a string of a maximum of 80 characters.
5. (Optional) Run [**peer**](cmdqueryname=peer) *peer-address* **mesh-group** *name*
   
   
   
   The remote MSDP peer is configured to join a mesh group. That is, the remote MSDP peer is acknowledged as a member of the mesh group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If only two Routers are configured with Anycast-RP, this configuration is not necessary.
   
   * *peer-address*: specifies the IP address of a remote MSDP peer.
   * *name*: specifies the name of a mesh group. The members of the same mesh group use the same mesh group name.
   
   Note the following during configuration:
   
   * MSDP peer connections must be set up between all members of the same mesh group.
   * All members of the mesh group must acknowledge each other as a member of the group.
   * An MSDP peer can belong to only one mesh group. If an MSDP peer is configured to join different mesh groups for multiple times, only the latest configuration is valid.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.