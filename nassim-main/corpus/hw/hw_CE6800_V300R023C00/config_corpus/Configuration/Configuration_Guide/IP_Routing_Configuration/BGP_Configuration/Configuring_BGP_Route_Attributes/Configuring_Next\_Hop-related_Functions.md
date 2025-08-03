Configuring Next\_Hop-related Functions
=======================================

Configuring Next\_Hop-related Functions

#### Prerequisites

Before configuring Next\_Hop-related functions, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

Configuring the Next\_Hop-related functions allows for flexible control of BGP route selection.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Configure Next\_Hop-related functions. For details, see [Table 1](#EN-US_TASK_0000001130783872__table29861143141218).
   
   
   
   **Table 1** Configuring Next\_Hop-related functions
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the device to change the next hop of each route to itself when the device advertises them to a specified peer or peer group. | [**peer**](cmdqueryname=peer+next-hop-local) { *ipv4-address* | *group-name* | *peerIpv6Addr* } **next-hop-local** | By default, a device does not change the next hop address of a route learned from an EBGP peer before forwarding the route to IBGP peers. The next hop address of a route advertised by an EBGP peer to this device is the peer address of the EBGP peer. After being forwarded to IBGP peers in the local AS, this route is not active because the next hop is unreachable. To address this issue, configure an ASBR to change the next hop address of a route advertised by an EBGP peer to the ASBR's own IP address before the ASBR advertises the route to an IBGP peer. As an IGP runs within the AS, the next hop of the route is reachable. As such, the route received by the IBGP peer is active.  By default, a device does not change the next-hop address of a route when advertising the route to an IBGP peer.  NOTE:  If BGP load balancing is configured, the local device changes the next hop address of a route to its own address when advertising the route to an IBGP peer or peer group, regardless of whether the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command is run. |
   | Enter the BGP-VPNv4 address family view and configure the device not to change the next hop address of an imported IGP route when advertising the IGP route. | [**peer**](cmdqueryname=peer+next-hop-invariable) { *ipv4-address* | *group-name* } **next-hop-invariable** | By default, a device changes the next hop address of a route imported from an IGP to the address of the local interface connected to a peer when advertising the route to the peer. |
   | Configure the device to recurse routes to next hops based on a specified route-policy. | [**nexthop recursive-lookup**](cmdqueryname=nexthop+recursive-lookup+route-policy) **route-policy** *route-policy-name* | By default, no route-policy is configured for next hop recursion.  After this command is run, the device matches the recursive next hops against the specified route-policy after recursing routes. A route with a recursive next hop that does not match the route-policy will be set to invalid. |
   | Disable the device from changing the next hop address of each route when the device advertises them to a peer in specific scenarios. | [**nexthop third-party**](cmdqueryname=nexthop+third-party) | The specific scenarios include the following:  * A route is learned from a directly connected peer and is to be advertised to a directly connected EBGP peer, the original next hop of the route resides on the same network segment as the local interface that is used to establish the peer relationship with the EBGP peer, and all directly connected interfaces are broadcast interfaces. * A route is locally imported and is to be advertised to a directly connected IBGP or EBGP peer, the recursive next hop of the route resides on the same network segment as the local interface that is used to establish the peer relationship with the IBGP or EBGP peer, and all directly connected interfaces are broadcast interfaces.The default configurations are as follows: * Before advertising a route learned from a directly connected peer to a directly connected EBGP peer, a device changes the next hop address of the route to the IP address of the local interface used to establish the peer relationship with the EBGP peer. * Before advertising a locally imported route to a directly connected IBGP or EBGP peer, the device changes the next hop address of the route to the IP address of the local interface that is used to establish the peer relationship with the IBGP or EBGP peer. |
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```