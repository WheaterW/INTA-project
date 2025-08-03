Adding a BGP Peer to the Labeled Address Family
===============================================

To establish an inter-AS BGP LSP, enable ASBRs to exchange labeled IPv4 routes.

#### Procedure

* Enabling the function to exchange labeled IPv4 routes
  
  
  
  Perform the following steps on ASBRs:
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface connected to the peer ASBR.
  3. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  6. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  7. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the peer ASBR as an EBGP peer.
  8. Run the [**ipv4-family labeled-unicast**](cmdqueryname=ipv4-family+labeled-unicast) command to enter the BGP labeled-unicast address family view.
  9. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **enable** command to specify a peer address in the labeled-unicast address family view, so that the local ASBR can exchange labeled IPv4 routes with the peer ASBR.
  10. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.