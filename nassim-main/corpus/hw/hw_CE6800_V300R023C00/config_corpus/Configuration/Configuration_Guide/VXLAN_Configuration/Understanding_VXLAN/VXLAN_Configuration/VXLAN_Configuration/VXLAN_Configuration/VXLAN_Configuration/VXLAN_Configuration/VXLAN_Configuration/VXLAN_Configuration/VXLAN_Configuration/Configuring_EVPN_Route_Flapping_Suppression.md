Configuring EVPN Route Flapping Suppression
===========================================

Configuring EVPN Route Flapping Suppression

#### Prerequisites

Before configuring EVPN route flapping suppression, complete one of the following tasks:

* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1066.html)

#### Context

Route flapping is a major symptom of EVPN route instability. When an EVPN route flaps, it repeatedly disappears from the routing table and then reappears. EVPN route flapping consumes lots of bandwidth and CPU resources and even affects the normal network operation in extreme cases.

EVPN supports EVPN route flapping suppression through route dampening, which uses a penalty value to reflect the stability of an EVPN route. When an EVPN route flaps, it is assigned a penalty value. A greater number of flapping times indicates a larger penalty value. If the penalty value exceeds the preset threshold, the EVPN route is not advertised. When the penalty value decreases to the reuse threshold after a period of time, the EVPN route is re-advertised.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BGP, and enter the BGP or BGP multi-instance view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number [ instance instance-name ]
   ```
3. Enter the BGP-EVPN address family view or BGP multi-instance EVPN address family view.
   
   
   ```
   [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
   ```
4. Enable EVPN route dampening and set route dampening parameters.
   
   
   * Enable EBGP EVPN route dampening and set route dampening parameters.
     ```
     [dampening](cmdqueryname=dampening) [ half-life-reach reuse suppress ceiling | [ route-policy route-policy-name ] ]* [ update-standard ]
     ```
   * Enable IBGP EVPN route dampening and set route dampening parameters.
     ```
     [dampening](cmdqueryname=dampening) ibgp [ half-life-reach reuse suppress ceiling | [ route-policy route-policy-name ] ]* [ update-standard ]
     ```
   
   
   
   By default, the value is 15 minutes for *half-life-reach*, 750 for *reuse*, 2000 for *suppress*, and 16000 for *ceiling*.
   
   The *reuse*, *suppress*, and *ceiling* values must meet the following requirement: *reuse* value < *suppress* value < *ceiling* value.
   
   After a route-policy is specified, EVPN can use different route dampening parameters to suppress different routes.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp**](cmdqueryname=display+bgp+evpn+all+routing-table+dampening+parameter) [ **instance** *instance-name* ] **evpn all routing-table dampening parameter** command to check the set route dampening parameters.
* Run the [**display bgp**](cmdqueryname=display+bgp+evpn+routing-table+flap-info) [ **instance** *instance-name* ] **evpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **flap-info** [ **mac-route** | **prefix-route** ] command to check statistics about EVPN route flapping.
* Run the [**display bgp**](cmdqueryname=display+bgp+evpn+routing-table+dampened) [ **instance** *instance-name* ] **evpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** [ **mac-route** | **prefix-route** ] **dampened** command to check dampened EVPN routes.
* Run the [**display bgp**](cmdqueryname=display+bgp+evpn+routing-table+dampened) [ **instance** *instance-name* ] **evpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **statistics** **dampened** command to check statistics about dampened EVPN routes.

#### Follow-up Procedure

To clear the dampening information about EVPN routes and release suppressed EVPN routes, run either of the following commands as needed:

* [**reset bgp**](cmdqueryname=reset+bgp+evpn+dampening) [ **instance** *instance-name* ] **evpn dampening**
* [**reset bgp**](cmdqueryname=reset+bgp+evpn+dampening) [ **instance** *instance-name* ] **evpn dampening** { **mac-route** | **prefix-route** } *prefix*

To clear statistics about EVPN route flapping, run any of the following commands as needed:

* [**reset bgp**](cmdqueryname=reset+bgp+evpn+flap-info) [ **instance** *instance-name* ] **evpn flap-info**
* [**reset bgp**](cmdqueryname=reset+bgp+evpn+flap-info) [ **instance** *instance-name* ] **evpn flap-info** { **mac-route** | **prefix-route** } *prefix*
* [**reset bgp**](cmdqueryname=reset+bgp+evpn+flap-info) [ **instance** *instance-name* ] **evpn** { *ip-address* | *peerIpv6Addr* } **flap-info**

![](../public_sys-resources/note_3.0-en-us.png) 

Cleared information cannot be restored. Exercise caution when performing this operation.