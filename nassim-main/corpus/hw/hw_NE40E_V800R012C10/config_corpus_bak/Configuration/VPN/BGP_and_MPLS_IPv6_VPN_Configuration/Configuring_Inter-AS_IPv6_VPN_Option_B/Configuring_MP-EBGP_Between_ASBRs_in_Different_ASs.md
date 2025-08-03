Configuring MP-EBGP Between ASBRs in Different ASs
==================================================

After the MP-EBGP peer relationship is established between ASBRs, an ASBR can advertise the VPNv6 routes of its AS to the other ASBR.

#### Context

In inter-AS IPv6 VPN Option B, you need not create VPN instances on ASBRs. The ASBR does not filter the VPNv6 routes received from the PE in the same AS based on VPN targets. Instead, it advertises the received routes to the peer ASBR through MP-EBGP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the ASBR is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface connected to the peer ASBR is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   An IP address is configured for the interface.
4. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS capability is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   The peer ASBR is specified as an EBGP peer.
9. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6** [ **unicast** ]
   
   
   
   The BGP-VPN IPv6 address family view is displayed.
10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
    
    
    
    The capability of exchanging VPNv6 routes with the peer ASBR is enabled.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.