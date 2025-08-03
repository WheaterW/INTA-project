Setting a PrefVal for BGP Routes
================================

After PrefVals are set for routes, the route with the largest PrefVal is preferred when multiple routes to the same destination exist in the BGP routing table.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+preferred-value) { *group-name* | *ipv4-address* } [**preferred-value**](cmdqueryname=peer+preferred-value) *preferredvalue*
   
   
   
   A PrefVal is set for all the routes learned from a specified peer.
   
   
   
   After the [**peer preferred-value**](cmdqueryname=peer+preferred-value) command is run, all the routes learned from a peer have the same PrefVal.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.