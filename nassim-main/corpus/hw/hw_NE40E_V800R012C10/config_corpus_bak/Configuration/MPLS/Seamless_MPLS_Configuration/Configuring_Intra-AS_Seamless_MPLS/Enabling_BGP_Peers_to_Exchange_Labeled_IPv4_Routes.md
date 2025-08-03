Enabling BGP Peers to Exchange Labeled IPv4 Routes
==================================================

In the seamless MPLS networking, before an E2E BGP LSP is established, BGP peers must be able to exchange labeled IPv4 routes with each other.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer+label-route-capability+check-tunnel-reachable) { *ipv4-address* | *group-name* } **label-route-capability** [ **check-tunnel-reachable** ]
   
   
   
   The ability to exchange labeled IPv4 routes with a BGP peer is enabled.
   
   * If the **check-tunnel-reachable** is configured, a local device advertises an IPv4 unicast route to its peer if a tunnel between the local and remote devices is unreachable and advertises a labeled IPv4 route if the tunnel is reachable. This parameter helps prevent a data forwarding failure when an MP-IBGP peer relationship between the CSG and MASG is established but an LSP over the peer relationship fails to be established.
   * If the **check-tunnel-reachable** parameter is not configured, the local device advertises a labeled IPv4 route, regardless of whether a tunnel between the local and remote devices is unreachable.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.