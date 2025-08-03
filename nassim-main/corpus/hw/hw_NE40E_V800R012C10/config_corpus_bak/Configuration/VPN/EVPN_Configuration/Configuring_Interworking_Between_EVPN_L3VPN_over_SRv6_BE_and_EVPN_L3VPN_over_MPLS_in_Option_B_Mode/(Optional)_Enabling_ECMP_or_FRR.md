(Optional) Enabling ECMP or FRR
===============================

(Optional)_Enabling_ECMP_or_FRR

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The ASBR's system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The EVPN address family is enabled, and its view is displayed.
4. Run [**maximum load-balancing interworking-rib evpn ip-prefix**](cmdqueryname=maximum+load-balancing+interworking-rib+evpn+ip-prefix) *number*
   
   
   
   The maximum number of EVPN Option B routes allowed for load balancing if these routes are optimal routes is configured.
5. Run [**auto-frr**](cmdqueryname=auto-frr)
   
   
   
   Auto FRR is enabled.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the EVPN address family view.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the BGP instance view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.