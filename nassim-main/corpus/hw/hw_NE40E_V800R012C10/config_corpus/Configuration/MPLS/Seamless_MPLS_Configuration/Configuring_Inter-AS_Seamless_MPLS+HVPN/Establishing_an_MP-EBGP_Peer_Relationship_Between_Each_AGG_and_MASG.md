Establishing an MP-EBGP Peer Relationship Between Each AGG and MASG
===================================================================

MP-EBGP supports BGP extended community attributes that are used to advertise VPNv4 routes between each pair of the AGG and MASG.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer+as-number) { *ipv4-address* | *group-name* } **as-number** { *as-number-plain* | *as-number-dot* }
   
   
   
   A BGP peer is configured.
4. Run [**peer**](cmdqueryname=peer+connect-interface+loopback) { *ipv4-address* | *group-name* } **connect-interface loopback** *interface-number*
   
   
   
   The interface on which a TCP connection to the specified EBGP peer is established is specified.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The AGG and MASG must use loopback interface addresses with 32-bit masks to establish an MP-EBGP peer relationship so that the MP-EBGP connection can recurse to a tunnel.
5. Run [**peer**](cmdqueryname=peer+ebgp-max-hop) { *ipv4-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ]
   
   
   
   The maximum number of hops for an EBGP peer relationship is set.
6. Run [**ipv4-family**](cmdqueryname=ipv4-family+vpnv4) **vpnv4**
   
   
   
   The BGP-VPNv4 address family view is displayed.
7. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
   
   
   
   The ability to exchange BGP-VPNv4 routes with the specified BGP peer is enabled.
8. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
9. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The BGP-IPv4 unicast address family view is displayed.
10. (Optional) Run [**undo peer**](cmdqueryname=undo+peer+enable) { *ipv4-address* | *group-name* } **enable**
    
    
    
    The capability to exchange BGP-IPv4 unicast routes between BGP peers is disabled.
    
    
    
    If multiple links exist between two ASs, the capability to exchange BGP-IPv4 unicast routes between BGP peers must be disabled to prevent route loops between BGP peers that need to establish MP-EBGP peer relationships.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.