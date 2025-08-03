Configuring EVPN Recursion Suppression in Case of Next Hop Flapping
===================================================================

EVPN recursion suppression in case of next hop flapping prevents the system from processing changes in EVPN routes that recurse to a frequently flapping next hop, thereby reducing system resource consumption and CPU usage.

#### Usage Scenario

If a large number of EVPN routes recurse to the same next hop that flaps frequently, the system will be busy processing changes in these routes, consuming excessive system resources and leading to high CPU usage. To address this issue, configure EVPN recursion suppression in case of next hop flapping.

By default, EVPN recursion suppression in case of next hop flapping is enabled. After EVPN recursion suppression in case of next hop flapping is enabled, an EVPN device determines whether to increase, retain, or reduce the penalty value by comparing the flapping interval with the configured threshold. When the penalty value exceeds 10, the EVPN device suppresses route recursion to the corresponding next hop. For example, if the intervals for increasing, retaining, and clearing the penalty value are T1, T2, and T3, respectively, the device calculates the penalty value as follows:

* Increases the penalty value by 1 if the flapping interval is less than T1.
* Retains the penalty value if the flapping interval is greater than or equal to T1, but less than T2.
* Reduces the penalty value by 1 if the flapping interval is greater than or equal to T2, but less than T3.
* Clears the penalty value if the flapping interval is greater than or equal to T3.

#### Pre-configuration Tasks

Before configuring EVPN recursion suppression in case of next hop flapping, complete one of the following tasks:

* [Configure EVPN VPLS over MPLS (common EVPN instance)](dc_vrp_evpn_cfg_0003.html).
* [Configure EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html).
* [Configure EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html).
* [Configure EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html).
* [Configure EVPN VPWS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0021_copy.html).

#### Procedure

* Perform the following configurations in the global EVPN configuration view:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**nexthop recursive-lookup restrain**](cmdqueryname=nexthop+recursive-lookup+restrain) **suppress-interval** *add-count-time* **hold-interval** *hold-count-time* **clear-interval** *clear-count-time* command to configure the intervals for increasing, retaining, and clearing the penalty value for recursion suppression in case of next hop flapping.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. (Optional) Run the [**evpn**](cmdqueryname=evpn) command to enter the global EVPN configuration view.
  6. (Optional) Run the [**nexthop recursive-lookup restrain disable**](cmdqueryname=nexthop+recursive-lookup+restrain+disable) command to disable EVPN recursion in case of next hop flapping globally.
     
     
     
     If you do not want to slow down route recursion processing and high CPU usage due to route recursion change processing is not a concern, you can disable recursion suppression in case of next hop flapping. After this step is performed, recursion suppression in case of next hop flapping does not take effect for any EVPN instance.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Perform the following configurations in the specified EVPN instance view:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**nexthop recursive-lookup restrain**](cmdqueryname=nexthop+recursive-lookup+restrain) **suppress-interval** *add-count-time* **hold-interval** *hold-count-time* **clear-interval** *clear-count-time* command to configure the intervals for increasing, retaining, and clearing the penalty value for recursion suppression in case of next hop flapping.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. (Optional) Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* [ **bd-mode** | **vpws** ] command to enter the view of the EVPN instance with the specified name and mode.
  6. (Optional) Run the [**nexthop recursive-lookup restrain disable**](cmdqueryname=nexthop+recursive-lookup+restrain+disable) command to disable EVPN recursion suppression in case of next hop flapping in the current EVPN instance.
     
     
     
     If you do not want to slow down route recursion processing and high CPU usage due to route recursion change processing is not a concern, you can disable recursion suppression in case of next hop flapping. After this step is performed, recursion suppression in case of next hop flapping does not take effect for the current EVPN instance.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For an EVPN instance, EVPN recursion suppression in case of next hop flapping takes effect only when this function is enabled in both the global EVPN configuration view and EVPN instance view.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* ] command to check BGP EVPN route information.