Setting the MED Attribute
=========================

The MED attribute is equal to the metric used in IGP. After the MED attribute is set for routes, an EBGP peer can select a route with the smallest MED value for the traffic that enters an AS.

#### Context

The MED serves as the metric used by an IGP. It is used to determine the optimal route when traffic enters an AS. When a BGP4+ router obtains multiple routes to the same destination address but with different next hops through EBGP peers, the route with the smallest MED value is selected as the optimal route.


#### Procedure

* Set the default MED value on the local device.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**default med**](cmdqueryname=default+med) *med*
     
     
     
     The default MED value is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Compare the MED values of the routes from different ASs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**compare-different-as-med**](cmdqueryname=compare-different-as-med)
     
     
     
     The device is configured to compare MED values of routes from different ASs.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the processing mode for the routes without a MED value.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**bestroute med-none-as-maximum**](cmdqueryname=bestroute+med-none-as-maximum)
     
     
     
     The maximum MED value is used for a route when it has no MED attribute.
     
     If this command is not run, BGP4+ uses 0 as the MED value for a route when it has no MED attribute.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.