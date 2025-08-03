Configuring Inter-AS BGP VPLS Option C (with RRs Deployed)
==========================================================

In inter-AS Option C, a network device only needs to establish a public tunnel with a PE in a different AS. ASBRs do not need to maintain inter-AS L2VPN information or reserve AC interfaces for inter-AS L2VPN connections. As L2VPN information is exchanged only between PEs, this solution requires fewer resources and less configuration workload.

#### Procedure

1. Enable the function to exchange labeled IPv4 routes.
   
   
   * Configure each PE.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
        
        The PE is enabled to exchange labeled IPv4 routes with the local ASBR.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure each ASBR.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The view of a local interface connected to the peer ASBR in another AS is displayed.
     3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
        
        An IP address is configured for the interface.
     4. Run [**mpls**](cmdqueryname=mpls)
        
        MPLS is enabled.
     5. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     6. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
        
        The function to exchange labeled IPv4 routes with each PE in the local AS is enabled.
        
        In inter-AS Option C, an inter-AS VPN LSP must be established, and the public network routes advertised between PEs and ASBRs must carry MPLS labels.
        
        An EBGP peer relationship must be established between ASBRs in different ASs for them to exchange labeled IPv4 routes.
        
        The public network routes carrying MPLS labels are advertised through MP-BGP. According to relevant standard protocols, label mapping information about a route can be piggybacked inside the BGP Update message that is used to advertise the route. This feature is implemented through a BGP extension attribute, which enables BGP peers to process labeled IPv4 routes.
     8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *peer-as*
        
        The peer ASBR is specified as an EBGP peer.
     9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability** [ **check-tunnel-reachable** ]
        
        The local ASBR is enabled to exchange labeled IPv4 routes with the peer ASBR.
        + If **check-tunnel-reachable** is configured, the ASBR advertises IPv4 unicast routes to the peer ASBR if the tunnel between them is unreachable and advertises labeled IPv4 routes if the tunnel is reachable. This parameter helps prevent traffic forwarding failures in VPN scenarios where an MP-EBGP peer relationship is established between two PEs but an LSP segment over the peer session fails to be established.
        + If **check-tunnel-reachable** is not configured, the ASBR advertises labeled IPv4 routes to the peer ASBR regardless of whether the tunnel between them is reachable.
     10. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.
2. Configure a route-policy on each ASBR to control label distribution.
   
   
   
   Configure a route-policy to control MPLS label distribution for IPv4 routes on each ASBR. The ASBR assigns labels only to routes that match filter rules defined in the policy. Other routes are still IPv4 routes without MPLS labels.
   
   By default, no MPLS labels are assigned to IPv4 routes.
   
   Configure each ASBR.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *seq-number*
      
      
      
      A route-policy is created to allow the ASBR to allocate MPLS labels to the matching IPv4 routes that are to be advertised to the local PE.
      
      
      
      After the route-policy is configured, if labeled IPv4 routes are to be advertised to the PE within the same AS, the ASBR reallocates MPLS labels to the routes.
   3. Run [**if-match mpls-label**](cmdqueryname=if-match+mpls-label)
      
      
      
      The ASBR is enabled to match labeled IPv4 routes against the route-policy.
   4. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
      
      
      
      The function to allocate labels to IPv4 routes is configured.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Run [**route-policy**](cmdqueryname=route-policy) *policy-name2* **permit** **node** *seq-number*
      
      
      
      A route-policy is created to allow the ASBR to allocate MPLS labels to the matching IPv4 routes that are to be advertised to the peer ASBR.
      
      
      
      For matching routes accepted from the PE in the same AS, the ASBR allocates MPLS labels to these routes before advertising them to the peer ASBR.
   7. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
      
      
      
      The function to allocate labels to IPv4 routes is configured.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   9. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   10. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       
       
       The BGP view is displayed.
   11. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name1* **export**
       
       
       
       The route-policy applied to routes to be advertised to the local PE is specified.
   12. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name2* **export**
       
       
       
       The configured route-policy is applied to the routes to be advertised to the peer ASBR.
   13. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
3. Configure the VPLS signaling capability for BGP peers.
   
   
   * This configuration requires each ASBR to advertise the local PEs' loopback interface addresses used for BGP sessions to the peer ASBR and then to PEs in the same AS as the peer ASBR. Configure each ASBR.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**network**](cmdqueryname=network) *ip-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ]
        
        Loopback interface addresses used for BGP session creation on the PEs are advertised in the AS.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure the VPLS signaling capability between the ASBR and the local RR and between the ASBR and the peer ASBR. Configure each ASBR.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *peer-as*
        
        A peer is specified.
     4. Enable the VPLS signaling capability between BGP peers.
        1. Run [**l2vpn-ad-family**](cmdqueryname=l2vpn-ad-family)
           
           The L2VPN AD address family view is displayed.
        2. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
           
           The device is enabled to exchange routing information with a specified BGP peer.
        3. Run [**signaling vpls**](cmdqueryname=signaling+vpls) or [**peer**](cmdqueryname=peer) *ipv4-address* **signaling** **vpls**
           
           The VPLS signaling capability is enabled.
     5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **next-hop-invariable**
        
        The device is enabled to advertise label block information to the local RR and peer ASBR without changing the next hops of routes.
   * Configure each PE.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *peer-as*
        
        The local RR is specified as an IBGP peer of the PE.
     4. Enable the VPLS signaling capability between BGP peers.
        1. Run [**l2vpn-ad-family**](cmdqueryname=l2vpn-ad-family)
           
           The L2VPN AD address family view is displayed.
        2. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
           
           The PE is enabled to exchange routing information with a specified BGP peer.
        3. Run [**signaling vpls**](cmdqueryname=signaling+vpls) or [**peer**](cmdqueryname=peer) *ipv4-address* **signaling** **vpls**
           
           The VPLS signaling capability is enabled.
   * Configure each RR.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *peer-as*
        
        An IBGP peer is specified. Run this command with the *ipv4-address* value set to the local PE's IPv4 address and then run it again with the value set to the local ASBR's IPv4 address.
     4. Enable the VPLS signaling capability between BGP peers.
        1. Run [**l2vpn-ad-family**](cmdqueryname=l2vpn-ad-family)
           
           The L2VPN AD address family view is displayed.
        2. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
           
           The device is enabled to exchange routing information with a specified local PE or local ASBR.
        3. Run [**signaling vpls**](cmdqueryname=signaling+vpls) or [**peer**](cmdqueryname=peer) *ipv4-address* **signaling** **vpls**
           
           The VPLS signaling capability is enabled.
        4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **reflect-client**
           
           The device is configured as an RR, and its peer is configured as the client of the RR.
4. Configure BGP VPLS on each PE. For configuration details, see [Configuring BGP VPLS](dc_vrp_vpls_cfg_6005.html).