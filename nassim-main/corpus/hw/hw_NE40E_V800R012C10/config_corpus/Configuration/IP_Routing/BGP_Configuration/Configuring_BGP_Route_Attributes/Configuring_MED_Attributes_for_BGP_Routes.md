Configuring MED Attributes for BGP Routes
=========================================

The MED attribute is equivalent to the metric used by an IGP. The MED attribute determines the optimal route for the traffic entering an AS.

#### Context

If the Router running BGP obtains multiple routes from different EBGP peers and these routes have the same destination but different next hops, the Router selects the route with the smallest MED value when other conditions are the same.


#### Procedure

* Set the default MED value on a device.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**default med**](cmdqueryname=default+med) *med*
     
     
     
     A default MED value is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**default med**](cmdqueryname=default+med) command is valid only for routes imported using the [**import-route**](cmdqueryname=import-route) command and summary BGP routes on the local Router.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device to compare the MED values of the routes from different ASs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**compare-different-as-med**](cmdqueryname=compare-different-as-med)
     
     
     
     The MED values of routes from different ASs are compared.
     
     By default, the BGP device compares the MED values of only routes from different peers in the same AS. To configure the device to compare the MED values of the routes from different ASs, run this command.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the deterministic-MED function.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**deterministic-med**](cmdqueryname=deterministic-med)
     
     
     
     The deterministic-MED function is enabled.
     
     
     
     If the deterministic-MED function is not enabled and the device receives multiple routes with the same prefix from different ASs, the route selection result is related to the sequence in which the routes are received. After the deterministic-MED function is enabled, these routes are first grouped based on the leftmost AS number in the AS\_Path attribute. Routes with the same leftmost AS number are grouped together and compared, and an optimal route is selected in the group. The optimal route in this group is then compared with the optimal routes from other groups to determine the final optimal route. With the deterministic-MED function, the route selection result is independent of the sequence in which the routes are received.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the processing mode when the MED value is lost.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**bestroute med-none-as-maximum**](cmdqueryname=bestroute+med-none-as-maximum)
     
     
     
     The maximum MED value is used as the MED when a route carries no MED.
     
     If the [**bestroute med-none-as-maximum**](cmdqueryname=bestroute+med-none-as-maximum) command is not run and a route carries no MED, 0 is used as the MED value of the route.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device to compare the MED values of routes in a confederation.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**bestroute med-confederation**](cmdqueryname=bestroute+med-confederation)
     
     
     
     The MED values of routes in a confederation are compared.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device to compare the sums of MED values multiplied by a MED multiplier and IGP metrics multiplied by an IGP metric multiplier for different routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**bestroute med-plus-igp**](cmdqueryname=bestroute+med-plus-igp+igp-multiplier+med-multiplier) [ **igp-multiplier** *igp-multiplier* | **med-multiplier** *med-multiplier* ]
     
     
     
     The sums of MED multiplied by a MED multiplier and IGP cost multiplied by an IGP cost multiplier are compared.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable BGP to remove the MED attribute from the imported routes that are locally leaked and are to be advertised to a specified peer after an export route-policy in which the [**apply cost-type**](cmdqueryname=apply+cost-type) command is run is applied to routes to be advertised to the peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**local-cross-routing non-med**](cmdqueryname=local-cross-routing+non-med)
     
     
     
     BGP is configured to remove the MED attribute from the imported routes that are locally leaked and are to be advertised to a specified peer after an export route-policy in which the [**apply cost-type**](cmdqueryname=apply+cost-type) command is run is applied to routes to be advertised to the peer.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.