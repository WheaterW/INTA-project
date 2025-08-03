Configuring MP-IBGP Between a PE and an ASBR in the Same AS
===========================================================

By introducing extended community attributes into BGP, MP-IBGP can advertise EVPN routes between the PE and ASBR.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the ASBR or PE is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
   
   
   
   The IBGP peer relationship is set up between the PE and ASBR in the same AS.
4. Run [**peer**](cmdqueryname=peer+connect-interface) *ipv4-address* **connect-interface** **loopback** *interface-number*
   
   
   
   The loopback interface is specified as the outbound interface of the BGP session.
5. Run [**peer**](cmdqueryname=peer+enable) *ipv4-address* **enable**
   
   
   
   The function to exchange IPv4 routes between the PE and ASBR in the same AS is enabled.
6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
7. Run [**peer**](cmdqueryname=peer+enable) *ipv4-address* **enable**
   
   
   
   The function to exchange EVPN routes between the PE and ASBR is enabled.
8. Run [**peer**](cmdqueryname=peer+esad-route-compatible) *ipv4-address* **esad-route-compatible** **enable**
   
   
   
   Enable the PE and ASBR to exchange ES-AD routes in the standard format defined in relevant standards.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.