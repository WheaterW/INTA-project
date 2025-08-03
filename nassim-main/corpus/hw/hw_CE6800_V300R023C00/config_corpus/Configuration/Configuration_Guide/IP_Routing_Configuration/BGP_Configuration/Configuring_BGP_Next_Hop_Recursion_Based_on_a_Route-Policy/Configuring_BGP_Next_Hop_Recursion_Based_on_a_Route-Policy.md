Configuring BGP Next Hop Recursion Based on a Route-Policy
==========================================================

Configuring BGP Next Hop Recursion Based on a Route-Policy

#### Prerequisites

Before configuring BGP next hop recursion based on a route-policy, you have completed the following tasks:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).
* [Configure a route-policy](vrp_route-policy_cfg_0011.html).

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

Before configuring a route-policy, check that all the recursive routes match the route-policy. If not, BGP routes may be unreachable.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Configure BGP next hop recursion based on a route-policy.
   
   
   ```
   [nexthop recursive-lookup](cmdqueryname=nexthop+recursive-lookup+route-policy) route-policy route-policy-name
   ```
   
   By default, BGP next hop recursion based on a route-policy is not configured.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This command does not apply to the routes accepted by directly connected EBGP peers or link-local peers.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *network* [ *mask* | *mask-length* ] command to check detailed information about a specified route in the BGP routing table.