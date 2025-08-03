Configuring BGP EVPN Soft Reset
===============================

BGP EVPN soft reset allows a device to receive EVPN routes from BGP EVPN peers again.

#### Usage Scenario

BGP EVPN soft reset performs a soft reset on BGP EVPN connections, which triggers BGP EVPN peers to send EVPN routes to a local device without tearing down the BGP EVPN connections and allows the local device to apply a new filtering policy and refresh the BGP EVPN routing table.


#### Pre-configuration Tasks

Before configuring BGP EVPN soft reset, ensure that one of the following EVPN functions has been configured:

* [Configure EVPN VPLS over MPLS (common EVPN instance)](dc_vrp_evpn_cfg_0003.html).
* [Configure EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html).
* [Configure EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html).
* [Configure EVPN L3VPN over MPLS](dc_vrp_evpn_cfg_0038.html).
* [Configure EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html).
* [Configure EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy_copy.html).
* [Configure EVPN VPWS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0021_copy.html).
* [Configure EVPN VPWS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpws_over_srv6-te_policy_copy.html).
* [Configure EVPN L3VPN over SRv6](dc_vrp_evpn_cfg_0152_copy.html).

#### Procedure

* In the user view, run [**refresh bgp evpn**](cmdqueryname=refresh+bgp+evpn) { **all** | *peer-address* | **group** *group-name* } { **export** | **import** }
  
  
  
  BGP EVPN soft reset is configured.

#### Verifying the Configuration

Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command to check the EVPN routing table information after the EVPN soft reset.