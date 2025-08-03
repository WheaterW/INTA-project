Configuring Next\_Hop-related Functions
=======================================

Configuring Next\_Hop-related Functions

#### Context

The Next\_Hop attribute of BGP4+ differs from that of an IGP, as the former is not necessarily the IPv6 address of a neighboring device. Configuring the Next\_Hop-related functions allows for flexible control of BGP4+ route selection.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Configure Next\_Hop-related functions. For details, see [Table 1](#EN-US_TASK_0000001176741867__table29861143141218).
   
   
   
   **Table 1** Configuring Next\_Hop-related functions
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the device to change the next hop of each route to itself when the device advertises them to a specified IBGP peer or peer group. | [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* | *ipv4-address* } [**next-hop-local**](cmdqueryname=next-hop-local) | To ensure that an IBGP peer can find the correct next hop, you can configure the local device to use its own address as the next-hop address of each route when the local device advertises routes to the IBGP peer.  By default, a device does not change the next-hop address of a route when advertising the route to an IBGP peer.  NOTE:  If BGP4+ load balancing is configured on a device, the device changes the next hop address of a route to its own IP address when advertising the route to IBGP peers or peer groups, regardless of whether the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command is run. |
   | Configure the device to recurse routes to next hops based on a specified route-policy. | [**nexthop recursive-lookup**](cmdqueryname=nexthop+recursive-lookup+route-policy) **route-policy** *route-policy-name* | By default, no route-policy is configured for next hop recursion.  After this command is run, the device matches the recursive next hops against the specified route-policy after recursing routes. A route with a recursive next hop that does not match the route-policy will be set to invalid. |
   | Configure the device not to change the next hop address of a route when advertising the route to a peer in a specific scenario. This ensures that traffic is transmitted along the optimal path. | [**nexthop third-party**](cmdqueryname=nexthop+third-party) | The specific scenarios include the following:  * The route is learned from a directly connected peer and is to be advertised to a directly connected EBGP peer, the original next hop of the route resides on the same network segment as the local interface that is used to establish the BGP4+ peer relationship with the EBGP peer, and directly connected interfaces are broadcast interfaces. * The route is locally imported and is to be advertised to a directly connected IBGP or EBGP peer, the next hop to which the route recurses resides on the same network segment as the local interface that is used to establish the BGP4+ peer relationship with the IBGP or EBGP peer, and directly connected interfaces are broadcast interfaces. |
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```