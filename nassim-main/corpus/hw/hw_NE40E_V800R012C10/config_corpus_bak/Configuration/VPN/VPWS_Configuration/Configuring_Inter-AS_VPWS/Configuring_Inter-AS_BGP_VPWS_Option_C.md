Configuring Inter-AS BGP VPWS Option C
======================================

ASBRs do not need to maintain inter-AS L2VPN information or reserve AC interfaces for inter-AS L2VPN PWs. As L2VPN information is exchanged only between PEs, this solution requires fewer resources and less configuration workload.

#### Procedure

1. Configure the capability to exchange labeled IPv4 routes.
   
   
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
   3. Run the [**if-match mpls-label**](cmdqueryname=if-match+mpls-label) command to match IPv4 routes with MPLS labels.
   4. Run the [**apply mpls-label**](cmdqueryname=apply+mpls-label) command to configure the function to allocate MPLS labels to IPv4 routes.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   6. Run the [**route-policy**](cmdqueryname=route-policy) *policy-name2* **permit** **node** *seq-number* command to create a route-policy for the remote ASBR.
   7. Run the [**apply mpls-label**](cmdqueryname=apply+mpls-label) command to configure the function to allocate MPLS labels to IPv4 routes.
   8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   9. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   10. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *policy-name1* **export** command to specify the route-policy applied when routes are advertised to the local PE.
   11. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *policy-name2* **export** command to specify the route-policy applied when routes are advertised to the remote ASBR.
   12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   13. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
3. Enable BGP peers to exchange VPWS information.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *peer-as*
      
      
      
      A BGP peer and its AS number are specified.
   3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface** *interface-type* *interface-number*
      
      
      
      The source interface for sending BGP packets is specified.
   4. Run [**l2vpn-ad-family**](cmdqueryname=l2vpn-ad-family)
      
      
      
      The L2VPN-AD address family view is displayed.
   5. (Optional) Run [**vpn-orf enable**](cmdqueryname=vpn-orf+enable)
      
      
      
      ORF is enabled.
   6. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The route exchange capability is enabled.
   7. Run [**signaling vpws**](cmdqueryname=signaling+vpws) or [**peer**](cmdqueryname=peer) *ip-address* **signaling** **vpws**
      
      
      
      BGP VPWS is enabled.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Configure a remote VPWS connection.
   1. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) *l2vpn-name* [ **encapsulation** *encapsulation-type* [ **control-word** | **no-control-word** ] ]
      
      
      
      A BGP VPWS VPN instance is created, and the MPLS L2VPN instance view is displayed.
      
      
      
      If heterogeneous interworking is required, specify *encapsulation-type* as **ip-interworking** for successful PW establishment.
   2. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is configured for the MPLS L2VPN instance.
   3. (Optional) Run [**mtu**](cmdqueryname=mtu) *mtu-value*
      
      
      
      An MTU is configured for the MPLS L2VPN instance.
      
      
      
      The MTU size determines the maximum packet size allowed by a VPWS network. If the MTU exceeds the maximum packet size allowed by a VPWS network or an intermediate node (P), packet fragmentation or even drop will occur, affecting network transmission. The MTU is one of the VPWS negotiation parameters. If the MTUs of the same MPLS L2VPN instance on the endpoint PEs are different, the two PEs cannot exchange reachability information or establish a PW. An appropriate MTU must be set for an MPLS L2VPN instance based on the MTU of the interface bound to the instance. Specifically, the MTU of an MPLS L2VPN instance must be smaller than or equal to the MTU of the interface bound to the instance.
   4. (Optional) Run [**ignore-mtu-match**](cmdqueryname=ignore-mtu-match)
      
      
      
      The current device is configured not to perform the MTU match check for the MPLS L2VPN instance.
      
      
      
      If the MTUs of the same MPLS L2VPN instance on the two endpoint PEs do not match, the VC cannot go up. If devices provided by other vendors do not support the MTU match check function provided by the MPLS L2VPN instance, run the **ignore-mtu-match** command to disable this function.
   5. Run [**vpn-target**](cmdqueryname=vpn-target) { *vpn-target* } & <1-16> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      
      
      VPN targets are configured.
   6. Run [**ce**](cmdqueryname=ce) *ce-Name* [ **id** *ce-id* [ **range** *ce-range* ] [ **default-offset** *ce-offset* ] ]
      
      
      
      A CE is created in the MPLS L2VPN instance.
   7. Run [**connection**](cmdqueryname=connection) [ **ce-offset** *ce-offset-id* ] **interface** **interface-type** *interface-number* [ **tunnel-policy** *tunnel-policy-name* ] [ **raw** | **tagged** ] [ **secondary** ]
      
      
      
      A remote BGP VPWS connection is configured.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.