Configuring BGP4+ to Advertise Default Routes to Peers or Peer Groups
=====================================================================

A device sends a default route with the local address as the next hop address to the specified peer for load balancing, regardless of whether there are default routes in the local routing table. This greatly reduces the number of routes on the network.

#### Context

Default routes can be used on networks that have the following characteristics:

* There are multiple EBGP peers, and each peer can receive full Internet routes.
* There are multiple Route Reflectors (RRs), and each RR can receive full Internet routes.

When load balancing is not performed on the network, a BGP4+ peer receives at most one copy of active full Internet routes. After load balancing is performed on the network, the number of active routes received by the BGP4+ peer doubles, which causes the number of routes on the network to sharply increase. In this case, you can configure the local device to advertise only default routes to its BGP4+ peer and use default routes for load balancing, which can greatly reduce the number of routes on the network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**default-route-advertise**](cmdqueryname=default-route-advertise+route-policy+conditional-route-match-all) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] [ **conditional-route-match-all** { *ipv6-address1* *ipv6-mask-length1* } &<1-4> | **conditional-route-match-any** { *ipv6-address2* *ipv6-mask-length2* } &<1-4> ]
   
   
   
   The device is configured to send the default route to the specified peer or peer group.
   
   
   
   If **route-policy** *route-policy-name* or **route-filter** *route-filter-name* is set, the BGP device changes attributes of the default route accordingly.
   
   * If **conditional-route-match-all** { *ipv6-address1* *ipv6-mask-length1* } &<1-4> is specified, the device advertises the default route only if all the routes matching the specified conditions exist in the local IPv6 routing table.
   * If **conditional-route-match-any** { *ipv6-address2* *ipv6-mask-length2* } &<1-4> is specified, the device advertises the default route if any route matching a specified condition exists in the local IPv6 routing table.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**peer default-route-advertise**](cmdqueryname=peer+default-route-advertise) command is run on a device, the device advertises a default route (with its local address as the next-hop address) to the specified peer, regardless of whether there is a default route in the local routing table.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.