Configuring Inter-AS BGP VPLS Option C
======================================

In inter-AS Option C, a network device only needs to establish a public tunnel with a PE in a different AS. ASBRs do not need to maintain inter-AS L2VPN information or reserve AC interfaces for inter-AS L2VPN connections. As L2VPN information is exchanged only between PEs, this solution requires fewer resources and less configuration workload.

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
     4. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS.
     5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     6. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     7. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability** command to configure the function to exchange labeled IPv4 routes with the PE in the local AS.
        
        In inter-AS Option C, an inter-AS VPN LSP must be established, and the public network routes advertised between PEs and ASBRs must carry MPLS labels.
        
        An EBGP peer relationship must be established between ASBRs in different ASs for them to exchange labeled IPv4 routes.
        
        The public network routes carrying MPLS labels are advertised through MP-BGP. According to the relevant standard (Carrying Label Information in BGP-4), label mapping information about a route can be piggybacked inside the BGP Update message that is used to advertise the route. This feature is implemented through a BGP extension attribute, which enables BGP peers to process labeled IPv4 routes.
     8. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the peer ASBR as an EBGP peer.
     9. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability** [ **check-tunnel-reachable** ] command to configure the function to exchange labeled IPv4 routes with the peer ASBR.
        
        + If the **check-tunnel-reachable** parameter is configured, BGP advertises IPv4 unicast routes to peers when the tunnels for routes are unreachable or advertises labeled routes to peers when the tunnels for routes are reachable. This parameter helps prevent traffic forwarding failures in VPN scenarios where an MP-EBGP peer relationship is established between two PEs but an LSP segment over the peer session fails to be established.
        + If the **check-tunnel-reachable** parameter is not configured, labeled routes are advertised regardless of whether the tunnels for imported routes are reachable.
     10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure a route-policy on each ASBR to control label distribution.
   
   
   
   Configure a route-policy to control MPLS label distribution for IPv4 routes on each ASBR. The ASBR assigns labels only to routes that match filter rules defined in the policy. Other routes are still IPv4 routes without MPLS labels.
   
   Configure each ASBR.
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *seq-number* command to create a route-policy for the local PE.
      
      
      
      The local ASBR reallocates MPLS labels to labeled IPv4 routes before advertising these routes to PEs in the same AS.
   3. Run the [**if-match mpls-label**](cmdqueryname=if-match+mpls-label) command to match labeled IPv4 routes against the route-policy.
   4. Run the [**apply mpls-label**](cmdqueryname=apply+mpls-label) command to configure the function to allocate labels to IPv4 routes.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   6. Run the [**route-policy**](cmdqueryname=route-policy) *policy-name2* **permit** **node** *seq-number* command to create a route-policy for the peer ASBR.
      
      
      
      This policy ensures that the local ASBR allocates a new MPLS label to each route received from PEs in the local AS before advertising these routes to the peer ASBR.
   7. Run the [**apply mpls-label**](cmdqueryname=apply+mpls-label) command to configure the function to allocate labels to IPv4 routes.
   8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   9. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   10. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   11. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name1* **export** command to specify the route-policy applied when routes are advertised to the local PE.
   12. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name2* **export** command to specify the route-policy applied when routes are advertised to the peer ASBR.
   13. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. Establish MP-EBGP VPLS peer relationships.
   
   
   * This configuration requires each ASBR to advertise the local PEs' loopback interface addresses used for BGP sessions to the peer ASBR and then to PEs in the same AS as the peer ASBR. Configure each ASBR.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     3. Run the [**network**](cmdqueryname=network) *ip-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ] command to advertise the loopback interface addresses used for BGP sessions on the PEs in the local AS.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Configure each PE.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     3. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to specify the remote PE as an EBGP peer.
     4. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ] command to specify the maximum number of hops allowed for an EBGP peer session.
        
        The PEs in different ASs are generally indirectly connected. To set up an EBGP peer relationship between two PEs in different ASs, configure the maximum number of hops allowed between the PEs and ensure that the PEs are reachable to each other.
     5. Enable the VPLS signaling capability between BGP peers.
        1. Run the [**l2vpn-ad-family**](cmdqueryname=l2vpn-ad-family) command to enter the L2VPN AD address family view.
        2. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **enable** command to enable the function to routing information with the specified BGP peer.
        3. Run the [**signaling vpls**](cmdqueryname=signaling+vpls) or [**peer**](cmdqueryname=peer) *ip-address* **signaling** **vpls** command to enable the VPLS signaling capability.
        4. (Optional) Run the [**signaling vpls-ad disable**](cmdqueryname=signaling+vpls-ad+disable) command to disable the BGP AD signaling capability.
           
           After the [**peer**](cmdqueryname=peer) *ipv4-address* **enable** command is run, the BGP AD signaling capability is enabled by default. Therefore, you can disable the BGP AD signaling capability when configuring BGP VPLS.
     6. (Optional) Run the [**peer**](cmdqueryname=peer) *ipv4-address* **next-hop-invariable** command to configure the function to advertise label block information to EBGP peers without changing the next hops of routes.
        
        This step is used in scenarios where an RR is used to advertise label block information. The next hops of routes cannot be changed when label block information is exchanged between RRs. For other scenarios, skip this step.
   * Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
4. Configure BGP VPLS on each PE. For configuration details, see [Configuring BGP VPLS](dc_vrp_vpls_cfg_6005.html).