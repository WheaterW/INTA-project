Configuring BGP Route Dampening
===============================

BGP route dampening can be configured to suppress unstable routes.

#### Usage Scenario

Route instability is mainly reflected by route flapping. A route is considered to be flapping when it repeatedly appears and then disappears in the routing table. BGP is generally applied to complex networks where routes change frequently. Frequent route flapping consumes lots of bandwidth and CPU resources and even seriously affects network operations.

BGP route dampening can deal with frequent route flapping. It uses a penalty value to measure route stability. When a route flaps, it is assigned a penalty value. Later, each time the route flaps, its penalty value increases by a specific value. If the penalty value of a route exceeds the pre-defined threshold, the route will not be advertised until the penalty value of the route reduces to the reuse threshold.


#### Pre-configuration Tasks

Before configuring BGP route dampening, complete the following task:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Configuring BGP route dampening parameters
   
   
   * Configure EBGP route dampening parameters.
     1. Run the [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast** command to enter the IPv4 unicast address family view.
     2. Run the [**dampening**](cmdqueryname=dampening+route-policy+update-standard) [ *half-life-reach* *reuse* *suppress* *ceiling* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] \* [ **update-standard** ] command to set the EBGP route dampening parameters.
   * Configure IBGP route dampening parameters.
     1. Run the [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast** command to enter the IPv4 unicast address family view.
     2. Run the [**dampening ibgp**](cmdqueryname=dampening+ibgp+route-policy+update-standard) [ *half-life-reach* *reuse* *suppress* *ceiling* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] \* [ **update-standard** ] command to set IBGP route dampening parameters.
   
   When you configure BGP route dampening, the values of *reuse*, *suppress*, and *ceiling* must meet the following condition: *reuse* < *suppress* < *ceiling*.
   
   If the [**dampening**](cmdqueryname=dampening) command is run with a route-policy or route-filter referenced, BGP applies the route dampening parameters only to the matched routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp routing-table flap-info**](cmdqueryname=display+bgp+routing-table+flap-info+regular-expression) [ **regular-expression** *as-regular-expression* | **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | *network-address* [ { *mask* | *mask-length* } [ **longer-match** ] ] ] command to check route flapping statistics.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+time-range) **time-range** *start-time* *end-time* command to check information about the routes that flap within a specified period.
* Run the [**display bgp routing-table dampened**](cmdqueryname=display+bgp+routing-table+dampened) command to check dampened BGP routes.
* Run the [**display bgp routing-table dampening parameter**](cmdqueryname=display+bgp+routing-table+dampening+parameter) command to check configured BGP route dampening parameters.