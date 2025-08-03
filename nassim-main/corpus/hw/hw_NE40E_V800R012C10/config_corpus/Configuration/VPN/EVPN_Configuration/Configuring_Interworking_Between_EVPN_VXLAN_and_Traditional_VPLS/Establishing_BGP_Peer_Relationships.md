Establishing BGP Peer Relationships
===================================

This section describes how to establish a BGP peer relationship between each of PE1 and PE2 and the EOR switch and configure BGP peers.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   BGP is enabled, and its view is displayed.
3. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
   
   
   
   The EOR switch is specified as the BGP peer.
4. Run [**peer**](cmdqueryname=peer+ebgp-max-hop) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
   
   
   
   The maximum number of hops allowed for a BGP peer session is specified.
5. Run [**peer**](cmdqueryname=peer+connect-interface) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number*
   
   
   
   The source interface for sending BGP messages is specified.
6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
7. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
   
   
   
   The function of filtering received EVPN routes based on VPN targets is disabled.
8. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
   
   
   
   The device is enabled to exchange EVPN routes with a peer or peer group.
9. Run [**peer**](cmdqueryname=peer+advertise+encap-type) { *ipv4-address* | *group-name* } **advertise encap-type vxlan**
   
   
   
   The device is configured to advertise EVPN routes carrying the VXLAN encapsulation attribute to the EOR switch.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.