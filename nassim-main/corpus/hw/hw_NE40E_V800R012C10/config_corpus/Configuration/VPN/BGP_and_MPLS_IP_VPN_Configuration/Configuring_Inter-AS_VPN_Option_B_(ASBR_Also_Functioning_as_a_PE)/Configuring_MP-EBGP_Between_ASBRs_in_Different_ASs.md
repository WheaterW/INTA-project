Configuring MP-EBGP Between ASBRs in Different ASs
==================================================

After an MP-EBGP peer relationship is established between
ASBRs, ASBRs can exchange VPNv4 routes.

#### Context

In inter-AS VPN Option B (ASBR also functioning as a PE),
VPN instances also need to be created on ASBRs. The ASBR does not
filter the VPNv4 routes received from the PE in the same AS based
on VPN targets. Instead, it advertises the received routes to the
peer ASBR through MP-EBGP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   An IP address is configured for the interface.
4. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS capability is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
8. Run [**peer**](cmdqueryname=peer) *peer-address* **as-number** *as-number*
   
   
   
   The peer ASBR is specified as an EBGP
   peer.
9. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP-VPNv4 address family view is displayed.
10. Run [**peer**](cmdqueryname=peer) *peer-address* **enable**
    
    
    
    The function to exchange VPNv4 routes with the peer ASBR is enabled.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is
    committed.