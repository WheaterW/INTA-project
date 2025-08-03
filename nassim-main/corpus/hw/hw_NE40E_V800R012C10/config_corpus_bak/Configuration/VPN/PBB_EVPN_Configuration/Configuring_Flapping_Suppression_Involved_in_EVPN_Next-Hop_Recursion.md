Configuring Flapping Suppression Involved in EVPN Next-Hop Recursion
====================================================================

Flapping suppression involved in EVPN next-hop recursion prevents the system from processing changes in EVPN routes that recurse to a frequently flapping next hop, thereby reducing system resource consumption and CPU usage.

#### Context

If a large number of EVPN routes recurse to the same next hop that flaps frequently, the system will be busy processing changes in these routes, consuming excessive system resources and leading to high CPU usage. To address this issue, configure flapping suppression involved in EVPN next-hop recursion.

By default, flapping suppression involved in EVPN next-hop recursion is enabled. After flapping suppression involved in EVPN next-hop recursion is enabled, an EVPN device determines whether to increase, retain, or reduce the penalty value by comparing the flapping interval with the configured threshold. When the penalty value exceeds 10, the EVPN device suppresses route recursion to the corresponding next hop. For example, if the intervals for increasing, retaining, and clearing the penalty value are T1, T2, and T3, respectively, the device calculates the penalty value as follows:

* Increases the penalty value by 1 if the flapping interval is less than T1.
* Retains the penalty value if the flapping interval is greater than or equal to T1, but less than T2.
* Reduces the penalty value by 1 if the flapping interval is greater than or equal to T2, but less than T3.
* Clears the penalty value if the flapping interval is greater than or equal to T3.

#### Pre-configuration Tasks

Before configuring flapping suppression involved in EVPN next-hop recursion, complete the following task:

* [Configuring PBB-EVPN](dc_vrp_pbb-evpn_cfg_0001.html)

#### Procedure

* Perform the following configurations in the global EVPN configuration view:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**nexthop recursive-lookup restrain**](cmdqueryname=nexthop+recursive-lookup+restrain) **suppress-interval** *add-count-time* **hold-interval** *hold-count-time* **clear-interval** *clear-count-time* command to configure the intervals for increasing, retaining, and clearing the penalty value for flapping suppression involved in next-hop recursion.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. (Optional) Run the [**evpn**](cmdqueryname=evpn) command to enter the global EVPN configuration view.
  6. (Optional) Run the [**nexthop recursive-lookup restrain disable**](cmdqueryname=nexthop+recursive-lookup+restrain+disable) command to disable flapping suppression involved in EVPN next-hop recursion globally.
     
     
     
     If you do not want to slow down route recursion processing and high CPU usage due to route recursion change processing is not a concern, you can disable flapping suppression involved in next-hop recursion. After this step is performed, flapping suppression involved in next-hop recursion does not take effect for any B-EVPN instance.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Perform the following configurations in the specified EVPN instance view:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**nexthop recursive-lookup restrain**](cmdqueryname=nexthop+recursive-lookup+restrain) **suppress-interval** *add-count-time* **hold-interval** *hold-count-time* **clear-interval** *clear-count-time* command to configure the intervals for increasing, retaining, and clearing the penalty value for flapping suppression involved in next-hop recursion.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. (Optional) Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **b-evpn** command to enter the specified B-EVPN instance view.
  6. (Optional) Run the [**nexthop recursive-lookup restrain disable**](cmdqueryname=nexthop+recursive-lookup+restrain+disable) command to disable flapping suppression involved in EVPN next-hop recursion in the current B-EVPN instance.
     
     
     
     If you do not want to slow down route recursion processing and high CPU usage due to route recursion change processing is not a concern, you can disable flapping suppression involved in next-hop recursion. After this step is performed, flapping suppression involved in next-hop recursion does not take effect for the current B-EVPN instance.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For a B-EVPN instance, flapping suppression involved in next-hop recursion takes effect only when this function is enabled in both the global EVPN configuration view and B-EVPN instance view.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* ] command to check PBB-EVPN routing information.