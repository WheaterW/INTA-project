Setting the Local\_Pref Attribute for MBGP Routes
=================================================

The Local\_Pref attribute has the same function as the preferred value of a route. If both of them are configured for an MBGP route, the preferred value takes precedence over the Local\_Pref attribute.

#### Context

The Local\_Pref attribute determines the optimal route for the traffic that leaves an AS. If an MBGP device obtains multiple routes from different IBGP peers and these routes have different next hops to the same destination, the MBGP device will select the route with the largest Local\_Pref value.

Perform the following steps on the Router that is configured as an MBGP peer:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is optional.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
4. Run [**default local-preference**](cmdqueryname=default+local-preference) *preference-value*
   
   
   
   The Local\_Pref attribute is set for the local device.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.