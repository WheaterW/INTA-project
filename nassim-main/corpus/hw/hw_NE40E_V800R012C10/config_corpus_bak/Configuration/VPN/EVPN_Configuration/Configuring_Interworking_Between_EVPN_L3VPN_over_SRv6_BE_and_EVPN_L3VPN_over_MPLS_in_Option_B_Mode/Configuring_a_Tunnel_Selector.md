Configuring a Tunnel Selector
=============================

EVPN public network routes recurse to IP tunnels based on next hops by default. To enable EVPN public network routes to recurse to SRv6 BE tunnels based on next hops, deploy a tunnel selector for route matching.

#### Context

By default, EVPN public network routes recurse to IP tunnels based on next hops.

If EVPN L3VPN over SRv6 BE interworks with EVPN L3VPN over MPLS in Option B mode, EVPN public network routes on ASBRs need to recurse to SRv6 BE tunnels.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The ASBR's system view is displayed.
2. Run [**tunnel-selector**](cmdqueryname=tunnel-selector) *name* *matchMode* **node** *node*
   
   
   
   A tunnel selector is created, and its view is displayed.
3. Run [**apply segment-routing ipv6**](cmdqueryname=apply+segment-routing+ipv6) **best-effort**
   
   
   
   The function to recurse routes to SRv6 BE tunnels based on SID attributes is enabled.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the tunnel selector view.
5. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
7. Run [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name*
   
   
   
   The tunnel selector is applied.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the BGP-EVPN address family view.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the BGP address family view.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.