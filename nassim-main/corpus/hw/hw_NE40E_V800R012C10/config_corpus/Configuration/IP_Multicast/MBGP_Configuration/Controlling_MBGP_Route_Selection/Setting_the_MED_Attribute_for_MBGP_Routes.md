Setting the MED Attribute for MBGP Routes
=========================================

The MED attribute indicates the metric used in IGP. After the MED attribute is set for routes, an EBGP peer can select a route with the smallest MED value for the traffic that enters an AS.

#### Context

The MED serves as the metric used by an IGP. MED determines the optimal route when traffic enters an AS. When an MBGP router obtains multiple routes to the same destination address but with different next hops through EBGP peers, the route with the smallest MED value is selected as the optimal route.


#### Procedure

* Set the default MED value on the local device.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**default med**](cmdqueryname=default+med) *med*
     
     
     
     The default MED value is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable MBGP to compare the MED values of the routes from different ASs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**compare-different-as-med**](cmdqueryname=compare-different-as-med)
     
     
     
     The function to compare the MED values of routes from different ASs is enabled.
     
     
     
     To configure MBGP to compare the MED values of routes from different ASs, run this command.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure MBGP to use the maximum MED value for a route that has no MED value.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**bestroute med-none-as-maximum**](cmdqueryname=bestroute+med-none-as-maximum)
     
     
     
     The maximum MED value is used for a route if the route has no MED value.
     
     
     
     If this command is not configured, MBGP uses 0 as the MED value for a route if the route has no MED value.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Compare the sums of MED multiplied by a MED multiplier and IGP cost multiplied by an IGP cost multiplier.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**bestroute med-plus-igp**](cmdqueryname=bestroute+med-plus-igp) [ **igp-multiplier** *igp-multiplier* | **med-multiplier** *med-multiplier* ]
     
     
     
     The sums of MED multiplied by a MED multiplier and IGP cost multiplied by an IGP cost multiplier are compared.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.