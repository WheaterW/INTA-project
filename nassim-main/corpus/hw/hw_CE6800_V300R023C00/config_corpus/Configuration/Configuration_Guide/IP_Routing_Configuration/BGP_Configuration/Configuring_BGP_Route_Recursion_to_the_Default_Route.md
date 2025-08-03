Configuring BGP Route Recursion to the Default Route
====================================================

Configuring BGP Route Recursion to the Default Route

#### Prerequisites

Before configuring BGP route recursion to the default route, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

The next hops of BGP routes may not be directly reachable. In this case, recursion is required so that the BGP routes can be used for traffic forwarding. You can configure whether to allow BGP routes to recurse to the default route.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Configure BGP route recursion to the default route.
   
   
   ```
   [nexthop recursive-lookup default-route](cmdqueryname=nexthop+recursive-lookup+default-route)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring BGP route recursion to the default route, check the configuration.

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration+configuration+bgp+%7C+include) **configuration** **bgp** **|** **include** **nexthop recursive-lookup default-route** command to check whether BGP route recursion to the default route is configured.