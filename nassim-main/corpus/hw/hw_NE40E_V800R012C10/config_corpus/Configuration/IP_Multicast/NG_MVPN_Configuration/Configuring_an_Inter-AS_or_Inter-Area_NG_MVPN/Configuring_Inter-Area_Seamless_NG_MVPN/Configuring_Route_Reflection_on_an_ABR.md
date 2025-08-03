Configuring Route Reflection on an ABR
======================================

Route reflection on an ABR is used to reflect the VPNv4 routes advertised by the PE to other devices in the same AS. As a result, PE does not need to set up BGP peer relationship with other devices, which simplifies configurations.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
   
   
   
   The unicast IPv4 address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **reflect-client**
   
   
   
   The ABR is configured as a route reflector. If you need to configure multiple devices as clients, repeatedly run this command.
5. (Optional) Repeatedly run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **next-hop-local**
   
   
   
   The ABR is configured to set its IP address as the next hop of the routes to be advertised to each specified IBGP peer.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
7. Run [**ipv4-family**](cmdqueryname=ipv4-family) **mvpn**
   
   
   
   The BGP-MVPN address family view is displayed.
8. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **reflect-client**
   
   
   
   The ABR is configured as a route reflector. If you need to configure multiple devices as clients, repeatedly run this command.
9. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
   
   
   
   The function to filter received MVPN routes based on VPN targets is disabled.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the BGP view.
11. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
    
    
    
    The BGP-VPNv4 address family view is displayed.
12. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **reflect-client**
    
    
    
    The ABR is configured as a route reflector. If you need to configure multiple devices as clients, repeatedly run this command.
13. (Optional) Repeatedly run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **next-hop-local**
    
    
    
    The ABR is configured to set its IP address as the next hop of the routes to be advertised to each specified IBGP peer.
14. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
    
    
    
    The function to filter received VPNv4 routes based on VPN targets is disabled.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.