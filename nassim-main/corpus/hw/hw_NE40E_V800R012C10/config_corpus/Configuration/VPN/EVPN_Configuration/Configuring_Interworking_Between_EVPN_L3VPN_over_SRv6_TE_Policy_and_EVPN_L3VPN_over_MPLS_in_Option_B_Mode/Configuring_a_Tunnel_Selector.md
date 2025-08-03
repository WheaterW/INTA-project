Configuring a Tunnel Selector
=============================

EVPN public network routes recurse to IP tunnels based on next hops by default. To enable EVPN public network routes to recurse to SRv6 TE Policies based on next hops, deploy a tunnel selector for route matching.

#### Context

By default, EVPN public network routes recurse to IP tunnels based on next hops.

If EVPN L3VPN over SRv6 TE Policy interworks with EVPN L3VPN over MPLS in Option B mode, EVPN public network routes on ASBRs need to recurse to SRv6 TE Policies based on next hops.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the ASBR is displayed.
2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
   
   
   
   A tunnel policy is created, and its view is displayed.
3. Run [**tunnel select-seq ipv6**](cmdqueryname=tunnel+select-seq+ipv6) **srv6-te-policy** **load-balance-number** *loadBalanceNumber*
   
   
   
   The type of tunnel to be selected and the maximum number of tunnels that can participate in load balancing are configured.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the tunnel policy view.
5. Run [**tunnel-selector**](cmdqueryname=tunnel-selector) *name* *matchMode* **node** *node*
   
   
   
   A tunnel selector is created, and its view is displayed.
6. Run [**apply tunnel-policy**](cmdqueryname=apply+tunnel-policy) *tunnel-policy-name*
   
   
   
   A tunnel policy is applied to routes.
7. Run [**apply segment-routing ipv6**](cmdqueryname=apply+segment-routing+ipv6) **traffic-engineer**
   
   
   
   The function to recurse routes to SRv6 TE Policy next hops based on SID attributes is enabled.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the tunnel selector view.
9. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
10. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
    
    
    
    The BGP-EVPN address family view is displayed.
11. Run [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name*
    
    
    
    The tunnel selector is applied.
12. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the BGP-EVPN address family view.
13. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the BGP address family view.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.