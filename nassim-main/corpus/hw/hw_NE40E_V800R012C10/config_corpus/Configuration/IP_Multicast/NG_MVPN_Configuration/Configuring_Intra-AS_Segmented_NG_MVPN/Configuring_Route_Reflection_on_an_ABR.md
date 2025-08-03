Configuring Route Reflection on an ABR
======================================

Route reflection on an ABR is used to reflect the VPNv4 routes advertised by the PE to other devices in the same AS.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
   
   
   
   The BGP-IPv4 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **reflect-client**
   
   
   
   The ABR is configured as a route reflector. If you need to configure multiple devices as clients, repeatedly run this command.
5. (Optional) Repeatedly run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **next-hop-local**
   
   
   
   The ABR is configured to set its IP address as the next hop of the routes to be advertised to each specified IBGP peer.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   The BGP view is displayed.
7. Run [**ipv4-family**](cmdqueryname=ipv4-family) **mvpn**
   
   
   
   The BGP-MVPN address family view is displayed.
8. Run [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute)
   
   
   
   The RR can modify route attributes of BGP routes.
9. Repeatedly run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **reflect-client**
   
   
   
   The ABR is configured as a route reflector. If you need to configure multiple devices as clients, repeatedly run this command.
10. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
    
    
    
    The function to filter received MVPN routes based on VPN targets is disabled.
11. Run [**quit**](cmdqueryname=quit)
    
    
    
    The BGP view is displayed.
12. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
    
    
    
    The BGP-VPNv4 address family view is displayed.
13. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **reflect-client**
    
    
    
    The ABR is configured as a route reflector. If you need to configure multiple devices as clients, repeatedly run this command.
14. (Optional) Repeatedly run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **next-hop-local**
    
    
    
    The ABR is configured to set its IP address as the next hop of the routes to be advertised to each specified IBGP peer.
15. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
    
    
    
    The function to filter received VPNv4 routes based on VPN targets is disabled.
16. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.