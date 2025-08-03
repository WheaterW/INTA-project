Configuring BGP4+ Route Recursion to the Default Route
======================================================

In case the next hops of BGP4+ routes are not directly reachable, you can configure BGP4+ route recursion to the default route.

#### Usage Scenario

The next hops of BGP4+ routes may not be directly reachable. In this case, recursion is required so that the BGP4+ routes can be used for traffic forwarding. You can configure whether to allow BGP4+ routes to recurse to the default route.


#### Pre-configuration Tasks

Before configuring BGP4+ route recursion to the default route, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run **[**nexthop recursive-lookup default-route**](cmdqueryname=nexthop+recursive-lookup+default-route)**
   
   
   
   BGP4+ route recursion to the default route is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display current-configuration**](cmdqueryname=display+current-configuration) command in the system view to check whether BGP4+ route recursion to the default route is configured.