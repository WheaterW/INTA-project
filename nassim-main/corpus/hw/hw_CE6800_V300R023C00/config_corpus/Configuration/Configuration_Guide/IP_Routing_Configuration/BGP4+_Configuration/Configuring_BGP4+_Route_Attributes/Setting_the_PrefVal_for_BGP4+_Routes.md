Setting the PrefVal for BGP4+ Routes
====================================

Setting the PrefVal for BGP4+ Routes

#### Context

After the PrefVal is set for BGP4+ routes, the route with the largest PrefVal value is selected when multiple routes with the same destination address exist in the BGP4+ routing table.


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
4. Set the PrefVal for all routes learned from a specified peer.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [preferred-value](cmdqueryname=preferred-value) preferredvalue
   ```
   
   
   
   By default, the PrefVal of routes learned from peers is 0.
   
   After the [**peer preferred-value**](cmdqueryname=peer+preferred-value) command is run, all the routes learned from the peer have the same PrefVal.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```