Configuring an RR to Establish MP-IBGP Peer Relationships with All Client PEs
=============================================================================

You can configure an RR to establish MP-IBGP connections with all its client PEs to reflect VPNv6 routes.

#### Context

Choose either of the following methods to configure an RR to establish MP-IBGP peer relationships with the client PEs.


#### Procedure

* Configure the RR to establish an MP-IBGP peer relationship with a peer group.
  
  
  
  Add all the client PEs to a peer group and establish an MP-IBGP connection with the peer group.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**group**](cmdqueryname=group) *group-name* [ **internal** ]
     
     
     
     An IBGP peer group is created.
  4. Run [**peer**](cmdqueryname=peer) *group-name* **connect-interface** *interface-type* *interface-number*
     
     
     
     The interface used to establish a TCP connection is specified.
  5. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
     
     
     
     The BGP-VPN IPv6 address family view is displayed.
  6. Run [**peer**](cmdqueryname=peer) *group-name* **enable**
     
     
     
     The function to exchange BGP IPv6 VPN routes between the RR and the peer group is enabled.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **group** *group-name*
     
     
     
     The peer is added to the peer group.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the RR to establish an MP-IBGP peer relationship with each client PE.
  
  
  
  Perform Step 1 to Step 6 repeatedly on the RR to establish an MP-IBGP connection between the RR and each client PE.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The client PE is specified as a BGP peer.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface** *interface-type* *interface-number*
     
     
     
     The interface used to establish a TCP connection is specified.
  5. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
     
     
     
     The BGP-VPN IPv6 address family view is displayed.
  6. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
     
     
     
     The function to exchange BGP IPv6 VPN routes between the RR and the client PE is enabled.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.