Enabling Exchange of the IPv4 Routes with Labels
================================================

In inter-AS IPv6 VPN Option C, an inter-AS BGP LSP needs to be established on the backbone network, and BGP peers on the backbone network can exchange labeled IPv4 routes with each other.

#### Procedure

* Configure the PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
     
     
     
     The exchange of the labeled IPv4 routes with the ASBR in the same AS is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the ASBR.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connected to the peer ASBR is displayed.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     An IPv4 address is configured for the interface.
  4. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS capability is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
     
     
     
     The capability of exchanging the labeled IPv4 routes with the PE of the same AS is enabled.
     
     In the Option C solution, you must establish an inter-AS VPN LSP. The related PEs and ASBRs exchange public network routes carrying MPLS labels.
     
     The ASBR establishes an EBGP peer relationship with the remote ASBR to exchange labeled IPv4 routes.
     
     The public network routes with MPLS labels are advertised by MP-BGP. According to relevant standards (Carrying Label Information in BGP-4), the label mapping information of a route is piggybacked in BGP Update messages. This feature is implemented through a BGP extension, which requires BGP peers to process labeled IPv4 routes.
  9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
     
     
     
     The peer ASBR is specified as the EBGP peer.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The exchange of the labeled IPv4 routes with the peer ASBR is enabled.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.