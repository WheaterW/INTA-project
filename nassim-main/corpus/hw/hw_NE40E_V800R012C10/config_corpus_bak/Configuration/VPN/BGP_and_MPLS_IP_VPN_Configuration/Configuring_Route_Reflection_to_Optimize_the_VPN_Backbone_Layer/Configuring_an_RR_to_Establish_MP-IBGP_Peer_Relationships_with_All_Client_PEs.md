Configuring an RR to Establish MP-IBGP Peer Relationships with All Client PEs
=============================================================================

You can configure an RR to establish MP-IBGP peer relationships with all its client PEs to reflect VPNv4 routes.

#### Procedure

* Configure the RR to establish an MP-IBGP peer relationship with each client PE.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) Perform Steps 3 to 6 repeatedly on the RR to establish MP-IBGP peer relationships with all client PEs.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **as-number** *as-number*
     
     
     
     The client PE is specified
     as a BGP peer.
  4. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **connect-interface** *interface-type* *interface-number*
     
     
     
     The interface used to establish a TCP connection is specified.
     
     The IP address of the interface must be the same as the MPLS LSR ID. It is recommended that you specify a loopback interface to establish the TCP connection.
  5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
     
     
     
     The BGP-VPNv4 address family view is displayed.
  6. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **enable**
     
     
     
     The function to exchange VPNv4 routes with client PEs is
     enabled.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.