Enabling BGP Peers to Exchange Labeled IPv4 Routes
==================================================

In inter-AS VPN Option C networking, a BGP LSP needs to be established between ASs, and labeled IPv4 routes need to be exchanged between BGP peers.

#### Procedure

* Configure PEs.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure a BGP peer.
  4. Run the [**ipv4-family labeled-unicast**](cmdqueryname=ipv4-family+labeled-unicast) command to enter the BGP labeled-unicast address family view.
  5. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **enable** command to enable the function to exchange labeled IPv4 routes with ASBRs in the local AS.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure ASBRs.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface connected to the peer ASBR.
  3. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IP address for the interface.
  4. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  7. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  8. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the peer ASBR as an EBGP peer.
  9. Run the [**ipv4-family labeled-unicast**](cmdqueryname=ipv4-family+labeled-unicast) command to enter the BGP labeled-unicast address family view.
  10. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **enable** command to specify a peer address in the labeled-unicast address family view, so that the local ASBR can exchange labeled IPv4 routes with the peer ASBR.
      
      
      
      In inter-AS Option C networking, an inter-AS VPN LSP must be established, and the public network routes advertised between PEs and ASBRs must carry MPLS labels.
      
      The local ASBR establishes an EBGP peer relationship with the remote ASBR to exchange labeled IPv4 routes.
      
      The public network routes carrying MPLS labels are advertised through MP-BGP. According to relevant protocols, label mapping information about a route can be piggybacked inside the BGP Update message that is used to advertise the route. This feature is implemented through BGP extensions, requiring BGP peers to process labeled IPv4 routes.
  11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.