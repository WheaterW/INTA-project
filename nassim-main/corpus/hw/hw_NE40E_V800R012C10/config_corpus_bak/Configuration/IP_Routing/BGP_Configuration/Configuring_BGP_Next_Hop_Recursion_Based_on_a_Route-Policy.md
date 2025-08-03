Configuring BGP Next Hop Recursion Based on a Route-Policy
==========================================================

Configuring BGP next hop recursion based on a route-policy prevents traffic loss if routes changes.

#### Usage Scenario

When BGP routes change, BGP needs to perform route recursion on the BGP routes with indirect next hops. If no route-policies are configured to filter the routes on which a BGP route with an indirect next hop depends for recursion, the BGP route may recurse to an incorrect route, which may cause traffic loss. To address this problem, configure BGP next hop recursion based on a route-policy. If no routes match the route-policy, the BGP route with an indirect next hop is considered unreachable. In this situation, incorrect route recursion and traffic loss are prevented.


#### Pre-configuration Tasks

Before configuring BGP next hop recursion based on a route-policy, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).
* [Configure a route-policy](dc_vrp_route-policy_cfg_0007.html).

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Ensure that all desirable recursive routes match the routing policy. Otherwise, BGP routes may be considered unreachable, unable to guide traffic forwarding.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**nexthop recursive-lookup**](cmdqueryname=nexthop+recursive-lookup+route-policy) { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
   
   
   
   BGP next hop recursion based on a route-policy or route-filter is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The command does not apply to the routes received from directly connected EBGP peers or LinkLocal peers.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *network* [ *mask* | *mask-length* ] command to check detailed information about a specified route in the BGP routing table.