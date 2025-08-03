Setting the PrefVal for BGP Routes
==================================

Setting the PrefVal for BGP Routes

#### Prerequisites

Before setting the PrefVal for BGP routes, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

After the PrefVal is set for BGP routes, the route with the largest PrefVal value is selected when multiple routes with the same destination address exist in the BGP routing table.


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
4. Set the PrefVal for all the routes learned from a specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { group-name | ipv4-address | peerIpv6Addr } [preferred-value](cmdqueryname=preferred-value) preferredvalue
   ```
   
   By default, the PrefVal of routes learned from a peer is 0.
   
   After the [**peer preferred-value**](cmdqueryname=peer+preferred-value) command is run, all routes learned from the specified peer have the same PrefVal value.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```