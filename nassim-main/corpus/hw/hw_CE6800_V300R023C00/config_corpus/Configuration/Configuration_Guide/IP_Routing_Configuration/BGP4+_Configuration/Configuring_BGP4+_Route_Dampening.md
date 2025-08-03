Configuring BGP4+ Route Dampening
=================================

Configuring BGP4+ Route Dampening

#### Prerequisites

Before configuring BGP4+ route dampening, you have completed the following task:

* [Configure basic BGP4+ functions.](vrp_bgp6_cfg_0006.html)

#### Context

BGP4+ route dampening is designed to suppress unstable routes and improve network stability. With this function enabled, a BGP4+ device does not add any unstable routes to its BGP4+ routing table or advertise them to its BGP4+ peers.

A primary cause of route instability is route flapping, which occurs when a route repeatedly appears and disappears in the routing table. BGP4+ is typically used in complex networks where routes change frequently. Frequent route flapping consumes lots of bandwidth and CPU resources and even seriously affects network operations. To prevent the impact of frequent route flapping, BGP4+ uses route dampening to suppress unstable routes.

BGP4+ route dampening uses different dampening parameters to suppress different routes based on a specified route-policy. In addition, you can also configure different route dampening parameters for different nodes of the same route-policy. In this way, BGP4+ can use different route dampening parameters when route flapping occurs to suppress the routes that match the route-policy. For example, on real-world networks, a long dampening period of time is set for routes with a long mask, whereas a short dampening period of time is set for routes with a short mask (for example, an 8-bit mask).


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
4. Set BGP4+ route dampening parameters.
   
   
   ```
   [dampening](cmdqueryname=dampening+route-policy+update-standard) [ half-life-reach reuse suppress ceiling | route-policy route-policy-name ] * [ update-standard ]
   [dampening ibgp](cmdqueryname=dampening+ibgp+route-policy+update-standard) [ half-life-reach reuse suppress ceiling | route-policy route-policy-name ] * [ update-standard ]
   ```
   
   The values of *reuse*, *suppress*, and *ceiling* must meet the following condition: *reuse* < *suppress* < *ceiling*.
   
   If the [**dampening**](cmdqueryname=dampening) command is run with a route-policy referenced, BGP4+ applies the route dampening parameters only to the routes that match the route-policy.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp ipv6 routing-table dampened**](cmdqueryname=display+bgp+ipv6+routing-table+dampened) command to check dampened BGP4+ routes.
* Run the [**display bgp ipv6 routing-table dampening parameter**](cmdqueryname=display+bgp+ipv6+routing-table+dampening+parameter) command to check BGP4+ route dampening parameters.
* Run the [**display bgp ipv6 routing-table flap-info**](cmdqueryname=display+bgp+ipv6+routing-table+flap-info+regular-expression) [ **regular-expression** *as-regular-expression* | **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | *network-address* [ { *mask* | *mask-length* } [ **longer-match** ] ] ] command to check BGP4+ route flapping statistics.