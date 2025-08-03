Enabling BGP Peers to Exchange Labeled IPv4 Routes
==================================================

In the inter-AS seamless MPLS+HVPN networking, before an E2E BGP LSP is established between an AGG and MASG, these two BGP peers must be able to exchange labeled IPv4 routes with each other.

#### Procedure

* Perform the following steps on each AGG and MASG:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer+label-route-capability) { *ipv4-address* | *group-name* } **label-route-capability**
     
     
     
     The ability to exchange labeled IPv4 routes between devices in the local AS is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on each AGG ASBR and core ASBR:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connected to the peer ASBR is displayed.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     An IP address is assigned to the interface.
  4. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**peer**](cmdqueryname=peer+label-route-capability+check-tunnel-reachable) { *ipv4-address* | *group-name* } **label-route-capability** [ **check-tunnel-reachable** ]
     
     
     
     The ability to exchange labeled IPv4 routes between BGP peers, including the peer ASBR and the devices in the local AS, is enabled.
     
     + If the **check-tunnel-reachable** is configured, a local device advertises an IPv4 unicast route to its peer if a tunnel between the local and remote devices is unreachable and advertises a labeled IPv4 route if the tunnel is reachable. This parameter helps prevent a data forwarding failure when an MP-EBGP peer relationship between the CSG and MASG is established but an LSP over the peer relationship fails to be established.
     + If the **check-tunnel-reachable** parameter is not configured, the local device advertises a labeled IPv4 route, regardless of whether a tunnel between the local and remote devices is unreachable.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.