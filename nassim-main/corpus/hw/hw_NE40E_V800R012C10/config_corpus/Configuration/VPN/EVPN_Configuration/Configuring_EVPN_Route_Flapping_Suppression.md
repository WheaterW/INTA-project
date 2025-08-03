Configuring EVPN Route Flapping Suppression
===========================================

Configuring EVPN route flapping suppression helps mitigate the impact of EVPN route instability on running services.

#### Usage Scenario

Route flapping is a major symptom of EVPN route instability. When an EVPN route flaps, it repeatedly disappears from the routing table and then reappears. EVPN route flapping consumes lots of bandwidth and CPU resources and even affects the normal network operation in extreme cases.

EVPN supports EVPN route flapping suppression through route dampening, which uses a penalty value to reflect the stability of an EVPN route. When an EVPN route flaps, it is assigned a penalty value. A greater number of flapping times indicates a larger penalty value. If the penalty value exceeds the preset threshold, the EVPN route is not advertised. When the penalty value decreases to the reuse threshold after a period of time, the EVPN route is re-advertised.


#### Pre-configuration Tasks

Before configuring EVPN route flapping suppression, complete one of the following tasks:

* [Configure EVPN VPLS over MPLS (common EVPN instance)](dc_vrp_evpn_cfg_0003.html).
* [Configure EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html).
* [Configure EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html).
* [Configure EVPN VPWS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0021_copy.html).
* [Configure EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html).
* [Configure an EVPN route-policy](dc_vrp_evpn_cfg_0150.html)

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP EVPN address family view.
4. Enable EVPN route dampening and set route dampening parameters.
   * Run the [**dampening**](cmdqueryname=dampening) [ *half-life-reach* *reuse suppress* *ceiling* | [ **route-policy** *route-policy-name* ] ] \* [ **update-standard** ] command to enable EBGP EVPN route dampening and set route dampening parameters.
   * Run the [**dampening**](cmdqueryname=dampening) **ibgp** [ *half-life-reach* *reuse suppress* *ceiling* | [ **route-policy** *route-policy-name* ] ] \* [ **update-standard** ] command to enable IBGP EVPN route dampening and set route dampening parameters.
   
   
   
   The *reuse*, *suppress*, and *ceiling* values must meet the following requirement: *reuse* value < *suppress* value < *ceiling* value.
   
   After a route-policy is specified, EVPN can use different route dampening parameters to suppress different routes.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, perform the following operations to verify it:

* Run the [**display bgp evpn all routing-table dampening parameter**](cmdqueryname=display+bgp+evpn+all+routing-table+dampening+parameter) command to check the set EVPN route dampening parameters.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **flap-info** [ **mac-route** | **prefix-route** ] command to check statistics about BGP EVPN route flapping.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** [ **mac-route** | **prefix-route** ] **dampened** command to check dampened routes.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **statistics** **dampened** command to check statistics about dampened EVPN routes.

#### Follow-up Procedure

To clear the dampening information about EVPN routes and release suppressed EVPN routes, run either of the following commands as needed:

* [**reset bgp evpn dampening**](cmdqueryname=reset+bgp+evpn+dampening)
* [**reset bgp evpn dampening**](cmdqueryname=reset+bgp+evpn+dampening) { **mac-route** | **prefix-route** } *prefix*

To clear statistics about EVPN route flapping, run any of the following commands as needed:

* [**reset bgp evpn flap-info**](cmdqueryname=reset+bgp+evpn+flap-info)
* [**reset bgp evpn flap-info**](cmdqueryname=reset+bgp+evpn+flap-info) { **mac-route** | **prefix-route** } *prefix*
* [**reset bgp evpn**](cmdqueryname=reset+bgp+evpn) { *ip-address* | *peerIpv6Addr* } **flap-info**