Setting a PrefVal for BGP4+ Routes
==================================

After a PrefVal is set for BGP4+ routes, the route with the greatest value is preferred when multiple routes to the same destination exist in the BGP4+ routing table.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**preferred-value**](cmdqueryname=preferred-value) *preferredvalue*
   
   
   
   A PrefVal is set for all the routes learned from a specified peer.
   
   
   
   After the [**peer preferred-value**](cmdqueryname=peer+preferred-value) command is run, all the routes learned from a specified peer have the same PrefVal.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.