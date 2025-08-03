Configuring Flapping Suppression Involved in BGP4+ Next Hop Recursion
=====================================================================

Flapping suppression involved in next-hop recursion prevents the system from frequently processing changes in routes that recurse to a frequently flapping next hop, thereby reducing system resource consumption and CPU usage.

#### Usage Scenario

If a large number of routes recurse to the same next hop that flaps frequently, the system will be busy processing changes of these routes, which consumes excessive system resources and leads to high CPU usage. To address this problem, configure flapping suppression involved in next-hop recursion.

By default, flapping suppression involved in next-hop recursion is enabled. After flapping suppression involved in BGP4+ next-hop recursion is enabled, a BGP4+ device determines whether to increase, retain, or clear the penalty value by comparing the flapping interval with the configured threshold. When the penalty value exceeds 10, the device suppresses next hop recursion flapping. For example, if the intervals for increasing, retaining, and clearing the penalty value are T1, T2, and T3, respectively, the device calculates the penalty value as follows:

* Increases the penalty value by 1 if the flapping interval is less than T1.
* Retains the penalty value if the flapping interval is greater than or equal to T1, but less than T2.
* Reduces the penalty value by 1 if the flapping interval is greater than or equal to T2, but less than T3.
* Clears the penalty value if the flapping interval is greater than or equal to T3.


#### Pre-configuration Tasks

Before configuring flapping suppression involved in BGP4+ next-hop recursion, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**undo nexthop recursive-lookup restrain disable**](cmdqueryname=undo+nexthop+recursive-lookup+restrain+disable)
   
   
   
   Flapping suppression involved in next-hop recursion is enabled.
   
   If you are not concerned about the system becoming occupied processing route changes and the possible high CPU usage, run the [**nexthop recursive-lookup restrain disable**](cmdqueryname=nexthop+recursive-lookup+restrain+disable) command to disable flapping suppression involved in next-hop recursion.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
6. Run [**nexthop recursive-lookup restrain**](cmdqueryname=nexthop+recursive-lookup+restrain+suppress-interval) **suppress-interval** *add-count-time* **hold-interval** *hold-count-time* **clear-interval** *clear-count-time*
   
   
   
   The intervals are configured for increasing, retaining, and clearing the penalty value for flapping suppression involved in next-hop recursion.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) command to check BGP4+ public network route information.
* Run the [**display bgp vpnv6 routing-table**](cmdqueryname=display+bgp+vpnv6+routing-table) command to check BGP VPNv6 and BGP VPN route information.