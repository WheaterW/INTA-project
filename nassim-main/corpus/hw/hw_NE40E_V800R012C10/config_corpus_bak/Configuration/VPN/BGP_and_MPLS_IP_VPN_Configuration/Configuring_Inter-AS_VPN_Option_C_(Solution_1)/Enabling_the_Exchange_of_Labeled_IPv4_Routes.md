Enabling the Exchange of Labeled IPv4 Routes
============================================

In inter-AS VPN Option C mode, a BGP LSP needs to be established
between ASs, and labeled IPv4 routes need to be exchanged between
BGP peers.

#### Procedure

* Configure the PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
     
     
     
     The function to exchange labeled IPv4 routes with the ASBR
     in the same AS is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the ASBR.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     The IP address of the interface is configured.
  4. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS capability is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
     
     
     
     The function to exchange labeled IPv4 routes with the PE
     in the same AS is enabled.
     
     In inter-AS VPN Option C mode, you
     must establish an inter-AS VPN LSP. The related PEs and the ASBRs
     exchange public network routes with the MPLS labels.
     
     The ASBR
     establishes a common EBGP peer relationship with the remote ASBR to
     switch labeled IPv4 routes.
     
     The public network routes with the
     MPLS labels are advertised by MP-BGP. According to relevant standards
     (Carrying Label Information in BGP-4), the label mapping information
     of a route is carried in advertised BGP update packets. This feature
     is implemented using extended BGP attributes, which requires BGP peers
     to process the labeled IPv4 routes.
  9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The peer ASBR is specified as an EBGP peer.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The function to exchange labeled IPv4 routes with the peer
      ASBR is enabled.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.