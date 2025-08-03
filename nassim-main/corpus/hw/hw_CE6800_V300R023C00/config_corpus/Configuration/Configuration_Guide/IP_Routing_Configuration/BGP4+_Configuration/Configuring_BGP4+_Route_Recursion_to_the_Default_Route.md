Configuring BGP4+ Route Recursion to the Default Route
======================================================

Configuring BGP4+ Route Recursion to the Default Route

#### Prerequisites

Before configuring BGP4+ route recursion to the default route, you have completed the following task:

* [Configuring Basic BGP4+ Functions](vrp_bgp6_cfg_0006.html)

#### Context

The next hops of BGP4+ routes may not be directly reachable. In this case, recursion is required so that the BGP4+ routes can be used for traffic forwarding. You can configure whether to allow BGP4+ routes to recurse to the default route.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Configure BGP4+ route recursion to the default route.
   
   
   ```
   [nexthop recursive-lookup default-route](cmdqueryname=nexthop+recursive-lookup+default-route)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring BGP4+ route recursion to the default route, check the configuration.

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **bgp** **|** **include** **nexthop recursive-lookup default-route** command to check whether BGP4+ route recursion to the default route is configured.