Configuring BGP4+ Route Dampening
=================================

Configuring BGP4+ route dampening suppresses unstable BGP4+ routes.

#### Usage Scenario

BGP4+ route dampening suppresses unstable routes and improves network stability. With BGP4+ route dampening, a BGP4+ device does not add any unstable routes to its BGP4+ routing table or advertise them to its BGP4+ peers.

Route instability is mainly reflected by route flapping. When a route flaps, it repeatedly disappears from the routing table and then reappears. BGP4+ is applied to complex networks where routes change frequently. Frequent route flapping consumes bandwidth and CPU resources and even seriously affects network operations. Route dampening prevents the adverse impact of continuous route flapping.

With specified-requirement route dampening, you can use a route-policy to differentiate routes. This allows BGP4+ to apply different route dampening parameters to different routes. You can also configure different route dampening parameters for different nodes of the same route-policy. When route flapping occurs, BGP4+ can use different route dampening parameters to suppress the routes that match the route-policy. For example, on a network, set a long dampening time for routes with a long mask, and set a short dampening time for routes with a short mask (8-bit mask for example).


#### Pre-configuration Tasks

Before configuring BGP4+ route dampening, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Configure BGP4+ route dampening parameters.
   
   
   * Configure EBGP route dampening parameters.
     1. Run the [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast** command to enter the IPv6 unicast address family view, or run the [**ipv6-family**](cmdqueryname=ipv6-family+vpnv6) **vpnv6** command to enter the BGP-VPNv6 address family view.
     2. Run the [**dampening**](cmdqueryname=dampening+route-policy+update-standard) [ *half-life-reach* *reuse* *suppress* *ceiling* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] \* [ **update-standard** ] command to set EBGP route dampening parameters.
   * Configure IBGP route dampening parameters.
     1. Run the [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast** command to enter the IPv6 unicast address family view, or run the [**ipv6-family**](cmdqueryname=ipv6-family+vpnv6) **vpnv6** command to enter the BGP-VPNv6 address family view.
     2. Run the [**dampening ibgp**](cmdqueryname=dampening+ibgp+route-policy+update-standard) [ *half-life-reach* *reuse* *suppress* *ceiling* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] \* [ **update-standard** ] command to set IBGP route dampening parameters.
   
   The value of *suppress* must be greater than that of *reuse* and less than that of *ceiling*.
   
   If the [**dampening**](cmdqueryname=dampening) command is run with a route-policy referenced, BGP4+ applies the route dampening parameters only to the routes that match the route-policy.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp ipv6 routing-table dampened**](cmdqueryname=display+bgp+ipv6+routing-table+dampened) command to check dampened BGP4+ routes.
* Run the [**display bgp ipv6 routing-table dampening parameter**](cmdqueryname=display+bgp+ipv6+routing-table+dampening+parameter) command to check configured BGP4+ route dampening parameters.
* Run the [**display bgp ipv6 routing-table flap-info**](cmdqueryname=display+bgp+ipv6+routing-table+flap-info+regular-expression) [ **regular-expression** *as-regular-expression* | **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | *network-address* [ { *mask* | *mask-length* } [ **longer-match** ] ] ] command to check route flapping statistics.
* Run the [**display bgp vpnv6 routing-table dampening parameter**](cmdqueryname=display+bgp+vpnv6+routing-table+dampening+parameter) command to check configured BGP VPNv6 route dampening parameters.
* Run the [**display bgp vpnv6 routing-table dampened**](cmdqueryname=display+bgp+vpnv6+routing-table+dampened) command to check dampened BGP VPNv6 routes.