Configuring BGP Route Recursion to the Default Route
====================================================

When the next hop of a BGP route is not directly reachable, you can configure BGP route recursion to the default route.

#### Usage Scenario

The next hops of BGP routes may not be directly reachable. In this case, recursion is required so that the BGP routes can be used for traffic forwarding. You can configure whether to allow BGP routes to recurse to the default route.


#### Pre-configuration Tasks

Before configuring BGP route recursion to the default route, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family unicast**](cmdqueryname=ipv4-family+unicast)
   
   
   
   The BGP-IPv4 unicast address family view is displayed.
4. Run [**nexthop recursive-lookup default-route**](cmdqueryname=nexthop+recursive-lookup+default-route)
   
   
   
   BGP route recursion to the default route is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display current-configuration**](cmdqueryname=display+current-configuration) command in the system view to check whether BGP route recursion to the default route is configured.