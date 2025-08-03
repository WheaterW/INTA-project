Setting the Default Local\_Pref Attribute for the Local Device
==============================================================

After the Local\_Pref attribute is set for BGP4+ routes, the route with the greatest attribute value is preferred when multiple routes to the same destination exist in the BGP4+ routing table. The preferred value takes precedence over the Local\_Pref attribute.

#### Context

The Local\_Pref attribute is used to determine the optimal route for the traffic that leaves an AS. When a BGP device receives multiple routes that have the same destination address but different next hops from different IBGP peers, the route with the largest Local\_Pref value is selected as the optimal route.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**default local-preference**](cmdqueryname=default+local-preference) *local-preference*
   
   
   
   The default Local\_Pref attribute is set for the local device.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.