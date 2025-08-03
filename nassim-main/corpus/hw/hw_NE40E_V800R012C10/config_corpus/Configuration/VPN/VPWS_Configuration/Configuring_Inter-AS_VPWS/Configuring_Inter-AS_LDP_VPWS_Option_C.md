Configuring Inter-AS LDP VPWS Option C
======================================

ASBRs do not need to maintain inter-AS L2VPN information or reserve AC interfaces for inter-AS L2VPN connections. As L2VPN information is exchanged only between PEs, this solution requires fewer resources and less configuration workload.

#### Procedure

1. Enable the function to exchange labeled IPv4 routes.
   
   
   * Configure each PE.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     3. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability** command to configure the function to exchange labeled IPv4 routes with the ASBR in the local AS.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Configure each ASBR.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface connecting to the peer ASBR.
     3. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IP address for the interface.
     4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     5. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS.
     6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     7. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     8. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability** command to configure the function to exchange labeled IPv4 routes with the PE in the local AS.
     9. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *peer-as* command to configure the remote ASBR as an EBGP peer.
     10. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability** command to configure the function to exchange labeled IPv4 routes with the peer ASBR.
         
         In inter-AS Option C, an inter-AS VPN LSP must be established, and the public network routes advertised between PEs and ASBRs must carry MPLS labels.
         
         The local ASBR establishes an EBGP peer relationship with the remote ASBR to exchange labeled IPv4 routes.
         
         The public network routes carrying MPLS labels are advertised through MP-BGP. According to the relevant standard (Carrying Label Information in BGP-4), label mapping information about a route can be piggybacked inside the BGP Update message that is used to advertise the route. This feature is implemented through a BGP extension attribute, which enables BGP peers to process labeled IPv4 routes.
     11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure a route-policy on each ASBR to control label distribution.
   
   
   
   After the route-policy is applied to an ASBR, the ASBR allocates MPLS labels to routes received from a PE in the local AS before advertising the routes to the remote ASBR, and reallocates MPLS labels to labeled IPv4 routes before advertising the routes to a PE in the local AS.
   
   Configure each ASBR.
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *seq-number* command to create a route-policy for the local PE.
   3. Run the [**if-match mpls-label**](cmdqueryname=if-match+mpls-label) command to match IPv4 routes carrying MPLS labels against the route-policy.
   4. Run the [**apply mpls-label**](cmdqueryname=apply+mpls-label) command to configure the function to allocate MPLS labels to IPv4 routes.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   6. Run the [**route-policy**](cmdqueryname=route-policy) *policy-name2* **permit** **node** *seq-number* command to create a route-policy for the peer ASBR.
   7. Run the [**apply mpls-label**](cmdqueryname=apply+mpls-label) command to configure the function to allocate MPLS labels to IPv4 routes.
   8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   9. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   10. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *policy-name1* **export** command to specify the route-policy applied when routes are advertised to the local PE.
   11. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *policy-name2* **export** command to specify the route-policy applied when routes are advertised to the remote ASBR.
   12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. Establish a remote MPLS LDP session between the PEs.
   
   This configuration requires each ASBR to advertise the local PEs' loopback interface addresses used for BGP sessions to the peer ASBR and then to PEs in other ASs.
   * Configure each ASBR.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     3. Run the [**network**](cmdqueryname=network) *ip-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ] command to advertise the local PEs' loopback interface addresses used for BGP sessions to the peer ASBR and then to PEs in the same AS as the peer ASBR.
     4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Configure each PE.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *peer-name* command to specify the name of the remote LDP session.
        
        To exchange PW information between PEs, you must establish remote MPLS LDP sessions between them.
     3. Run the [**remote-ip**](cmdqueryname=remote-ip) *ip-address* command to specify a peer IP address for the remote LDP session.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
4. Configure LDP VPWS on each PE. For configuration details, see [Configuring LDP VPWS](dc_vrp_vpws_cfg_3004.html).