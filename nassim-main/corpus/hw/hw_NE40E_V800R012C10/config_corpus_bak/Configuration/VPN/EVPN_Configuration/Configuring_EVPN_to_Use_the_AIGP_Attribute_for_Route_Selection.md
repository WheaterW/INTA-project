Configuring EVPN to Use the AIGP Attribute for Route Selection
==============================================================

Configuring_EVPN_to_Use_the_AIGP_Attribute_for_Route_Selection

#### Usage Scenario

The Accumulated Interior Gateway Protocol Metric (AIGP) attribute is an optional non-transitive BGP route attribute. The IGP cost accumulates in the AIGP attribute during route transmission. After the AIGP attribute is configured in an AIGP domain, BGP selects routes based on costs in the same manner as IGP, and all devices in the domain forward data along the optimal routes. During BGP route selection, the AIGP attribute is used as follows:

* The preference of a route with the AIGP attribute is higher than that of a route without the AIGP attribute.
* If all routes carry the AIGP attribute, the device selects the route whose AIGP value plus the cost of the IGP route to which the route recurses is smaller.

The AIGP attribute can be added to routes only through routing policies. You can configure an apply clause for a routing policy using the **apply aigp** { [ + | - ]*cost* | **inherit-cost** } command to modify the AIGP value during route import, acceptance, or advertisement by BGP. If no AIGP value is configured, the IGP routes imported by BGP do not carry the AIGP attribute.

After EVPN is configured to use the AIGP attribute for route selection, if BGP LSPs to which routes recurse carry the AIGP attribute, EVPN public and private network routes are selected based on the preceding comparison rules.


#### Pre-configuration Tasks

Before configuring EVPN to use the AIGP attribute for route selection, complete the following tasks:

* [Configure BGP to set an AIGP value based on a route-policy](dc_vrp_bgp_cfg_4101.html).
* [Configure BGP-LS](dc_vrp_bgp_cfg_4098.html).
* EVPN VPLS scenario: [Configuring EVPN VPLS over MPLS (BD EVPN Instance)](dc_vrp_evpn_cfg_0065.html), [Configuring EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html), or [Configuring EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy_copy.html)
* EVPN VPWS scenario: [Configuring EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html), [Configuring EVPN VPWS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0021_copy.html), or [Configuring EVPN VPWS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpws_over_srv6-te_policy_copy.html)
* EVPN L3VPN scenario: [Configuring EVPN L3VPN over MPLS](dc_vrp_evpn_cfg_0038.html), [Configuring EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html), or [Configuring EVPN L3VPNv4 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpn_over_srv6-te_policy_copy.html)


#### Procedure

* Configure a device to use the AIGP attribute for route selection in an EVPN VPLS scenario.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to enter the BD EVPN instance view.
  3. Run the [**bestroute nexthop-resolved aigp**](cmdqueryname=bestroute+nexthop-resolved+aigp) command to allow EVPN private network routes to participate in route selection based on the AIGP attributes of the corresponding BGP LSPs.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a device to use the AIGP attribute for route selection in an EVPN VPWS scenario.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws** command to enter the VPWS EVPN instance view.
  3. Run the [**bestroute nexthop-resolved aigp**](cmdqueryname=bestroute+nexthop-resolved+aigp) command to allow EVPN private network routes to participate in route selection based on the AIGP attributes of the corresponding BGP LSPs.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a device to use the AIGP attribute for route selection in an EVPN L3VPN scenario.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP EVPN address family view.
  4. Run the [**bestroute nexthop-resolved aigp**](cmdqueryname=bestroute+nexthop-resolved+aigp) command to allow EVPN public network routes to participate in route selection based on the AIGP attributes of the corresponding BGP LSPs.
  5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* ] command to check that BGP EVPN route information contains **resolving-AIGP** information.