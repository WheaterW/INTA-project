Configuring MP-IBGP Between a PE and an ASBR in the Same AS
===========================================================

By introducing extended community attributes into BGP,
MP-IBGP can advertise VPNv4 routes between the PE and ASBR.

#### Procedure

* Configure the ASBR to establish an MP-IBGP peer relationship
  with each client PE.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) Perform Steps 1 to 6 repeatedly on the ASBR
  and its client PEs to establish MP-IBGP peer relationships between
  them.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **as-number** *as-number*
     
     
     
     The client PE is specified as a BGP
     peer.
  4. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **connect-interface** *interface-type* *interface-number*
     
     
     
     The interface used to establish a TCP connection is specified.
  5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
     
     
     
     The BGP-VPNv4 address family view
     is displayed.
  6. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **enable**
     
     
     
     The capability of exchanging VPNv4 routes between the ASBR and
     the client PE is enabled.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In the NE40E, an ASBR can change the next-hop address of a VPNv4 route
     to the ASBR's address before advertising the route to a PE.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is
     committed.