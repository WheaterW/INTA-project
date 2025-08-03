Configuring MP-EBGP Between ASBRs in Different ASs
==================================================

After an MP-EBGP peer relationship is established between ASBRs, an ASBR can advertise the EVPN routes of its AS to the other ASBR.

#### Context

In inter-AS EVPN Option B, you do not need to create VPN instances on ASBRs. The ASBR does not filter the EVPN routes received from the PE in the same AS based on VPN targets. Instead, it advertises the received routes to the peer ASBR through MP-EBGP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the ASBR is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface connected to the peer ASBR is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   An IP address is configured for the interface.
4. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS capability is enabled.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
7. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
   
   
   
   The peer ASBR is specified as an EBGP peer.
8. Run [**peer**](cmdqueryname=peer+enable) *ipv4-address* **enable**
   
   
   
   The function to exchange IPv4 routes with the peer ASBR is enabled.
9. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
10. Run [**peer**](cmdqueryname=peer+enable) *ipv4-address* **enable**
    
    
    
    The function to exchange EVPN routes with the peer ASBR is enabled.
11. Run [**peer**](cmdqueryname=peer+esad-route-compatible) *ipv4-address* **esad-route-compatible** **enable**
    
    
    
    Enable ASBRs to exchange ES-AD routes in the standard format defined in relevant standards.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.