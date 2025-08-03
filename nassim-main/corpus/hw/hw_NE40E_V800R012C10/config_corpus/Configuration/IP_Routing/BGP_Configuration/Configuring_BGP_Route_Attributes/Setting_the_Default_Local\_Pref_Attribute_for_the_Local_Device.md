Setting the Default Local\_Pref Attribute for the Local Device
==============================================================

The function of the Local\_Pref attribute is similar to that of the preferred value. The priority of the Local\_Pref attribute, however, is lower than that of the preferred value.

#### Context

The Local\_Pref attribute is used to determine the optimal route for the traffic that leaves an AS. When a BGP device receives multiple routes that have the same destination address but different next hops from different IBGP peers, the route with the largest Local\_Pref value is selected as the optimal route.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**default local-preference**](cmdqueryname=default+local-preference) *local-preference*
   
   
   
   The default Local\_Pref value is set for the local device.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.