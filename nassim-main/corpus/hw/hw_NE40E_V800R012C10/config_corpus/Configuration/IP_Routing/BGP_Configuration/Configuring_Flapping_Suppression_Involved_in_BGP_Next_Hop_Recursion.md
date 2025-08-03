Configuring Flapping Suppression Involved in BGP Next Hop Recursion
===================================================================

Flapping suppression involved in next-hop recursion prevents the system from frequently processing changes in routes that recurse to a frequently flapping next hop, thereby reducing system resource consumption and CPU usage.

#### Usage Scenario

If a large number of routes recurse to the same next hop that flaps frequently, the system will be busy processing changes of these routes, which consumes excessive system resources and leads to high CPU usage. To address this problem, configure flapping suppression involved in next-hop recursion.

By default, flapping suppression involved in next-hop recursion is enabled. After this function is enabled, BGP calculates the penalty value that starts from 0 by comparing the flapping interval with configured intervals if next hop flapping occurs. When the penalty value exceeds 10, BGP suppresses route recursion to the corresponding next hop. For example, if the intervals for increasing, retaining, and clearing the penalty value are T1, T2, and T3, respectively, BGP calculates the penalty value as follows:

* Increases the penalty value by 1 if the flapping interval is less than T1.
* Retains the penalty value if the flapping interval is greater than or equal to T1, but less than T2.
* Reduces the penalty value by 1 if the flapping interval is greater than or equal to T2, but less than T3.
* Clears the penalty value if the flapping interval is greater than or equal to T3.


#### Pre-configuration tasks

Before configuring flapping suppression involved in BGP next-hop recursion, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**undo nexthop recursive-lookup restrain disable**](cmdqueryname=undo+nexthop+recursive-lookup+restrain+disable)
   
   
   
   Flapping suppression involved in next hop recursion is enabled.
   
   
   
   If you do not want to slow down route recursion processing and high CPU usage due to route recursion change processing is not a concern, you can disable flapping suppression involved in next-hop recursion using the [**nexthop recursive-lookup restrain disable**](cmdqueryname=nexthop+recursive-lookup+restrain+disable) command.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
6. Run [**nexthop recursive-lookup restrain**](cmdqueryname=nexthop+recursive-lookup+restrain+suppress-interval) **suppress-interval** *add-count-time* **hold-interval** *hold-count-time* **clear-interval** *clear-count-time*
   
   
   
   The intervals are configured for increasing, retaining, and clearing the penalty value for flapping suppression involved in next hop recursion.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) command to check BGP public network route information.
* Run the [**display bgp vpnv4 routing-table**](cmdqueryname=display+bgp+vpnv4+routing-table) command to check BGP VPNv4 and BGP VPN route information.