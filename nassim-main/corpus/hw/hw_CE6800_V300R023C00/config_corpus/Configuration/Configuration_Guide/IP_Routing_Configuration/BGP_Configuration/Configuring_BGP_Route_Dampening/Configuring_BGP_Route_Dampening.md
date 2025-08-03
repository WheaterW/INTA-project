Configuring BGP Route Dampening
===============================

Configuring BGP Route Dampening

#### Prerequisites

Before configuring BGP route dampening, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Context

The main cause of route instability is route flapping, whereby a route repeatedly appears and disappears in the routing table. BGP is generally applied to complex networks where routes change frequently. Frequent route flapping consumes extensive bandwidth and CPU resources and can even seriously impact network operations.

BGP route dampening prevents frequent route flapping by using a penalty value to measure route stability. When a route flaps, it is assigned a penalty; the more it flaps, the more penalties accumulate. If the penalty value of a route exceeds the pre-defined threshold, the route will not be advertised until the penalty value reduces to the reuse threshold.


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
4. Configure BGP route dampening parameters.
   
   
   ```
   [dampening](cmdqueryname=dampening+route-policy+update-standard) [ half-life-reach reuse suppress ceiling | route-policy route-policy-name ] * [ update-standard ]
   [dampening ibgp](cmdqueryname=dampening+ibgp+route-policy+update-standard) [ half-life-reach reuse suppress ceiling | route-policy route-policy-name ] * [ update-standard ]
   ```
   
   The values of *reuse*, *suppress*, and *ceiling* must meet the following condition: *reuse* < *suppress* < *ceiling*.
   
   If the [**dampening**](cmdqueryname=dampening) command is run with a route-policy referenced, BGP applies the route dampening parameters only to the routes that match the route-policy.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp routing-table flap-info**](cmdqueryname=display+bgp+routing-table+flap-info+regular-expression) [ **regular-expression** *as-regular-expression* | **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | *network-address* [ { *mask* | *mask-length* } [ **longer-match** ] ] ] command to check route flapping statistics.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) **time-range** *start-time* *end-time* command to view the routes that flap within a specified period.
* Run the [**display bgp routing-table dampened**](cmdqueryname=display+bgp+routing-table+dampened) command to check dampened BGP routes.
* Run the [**display bgp routing-table dampening parameter**](cmdqueryname=display+bgp+routing-table+dampening+parameter) command to check configured BGP route dampening parameters.