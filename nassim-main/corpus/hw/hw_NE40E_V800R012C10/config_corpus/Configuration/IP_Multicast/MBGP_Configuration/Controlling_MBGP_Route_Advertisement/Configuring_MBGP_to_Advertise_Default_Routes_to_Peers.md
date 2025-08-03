Configuring MBGP to Advertise Default Routes to Peers
=====================================================

A device sends a default route with the local address as the next hop address to the specified peer for load balancing, regardless of whether there are default routes in the local routing table. This greatly reduces the number of routes on the network.

#### Context

Default routes can be used on networks that have the following characteristics:

* There are multiple EBGP peers, and each peer can receive full Internet routes.
* There are multiple Route Reflectors (RRs), and each RR can receive full Internet routes.

When load balancing is not performed on a network, an MBGP peer receives at most one copy of active full Internet routes. After load balancing is performed on the network, the number of active routes received by the MBGP peer doubles, which causes the number of routes on the network to sharply increase. In this case, you can configure the local device to advertise only default routes to its MBGP peer and use default routes for load balancing, which can greatly reduce the number of routes on the network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
4. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } [**default-route-advertise**](cmdqueryname=default-route-advertise) [ **route-policy** *route-policy-name* ]
   
   
   
   Default routes are advertised to an MBGP peer or peer group.
   
   
   
   * *group-name*: specifies the name of an MBGP peer group.
   * *peer-address*: specifies the IP address of a remote MBGP peer.
   * **route-policy** *route-policy-name*: specifies a routing policy to control which routes are advertised.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.