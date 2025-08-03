(Optional) Enabling ECMP or FRR
===============================

(Optional)_Enabling_ECMP_or_FRR

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the ASBR is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The EVPN address family is enabled, and its view is displayed.
4. Run [**maximum load-balancing interworking-rib evpn ip-prefix**](cmdqueryname=maximum+load-balancing+interworking-rib+evpn+ip-prefix) *number*
   
   
   
   The maximum number of EVPN Option B routes allowed for load balancing if these routes are optimal routes is configured.
5. Run [**auto-frr**](cmdqueryname=auto-frr)
   
   
   
   Auto FRR is enabled.
6. Run [**bestroute nexthop-recursive-priority srv6-te-policy**](cmdqueryname=bestroute+nexthop-recursive-priority+srv6-te-policy)
   
   
   
   The device is enabled to compare the types of SRv6 tunnels to which routes recurse based on next hops during route selection. The routes that recurse to SRv6 TE Policies based on next hops take precedence over those that recurse to SRv6 BE tunnels based on next hops or recurse to common IPv6 next hops.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the EVPN address family view.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the BGP instance view.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.