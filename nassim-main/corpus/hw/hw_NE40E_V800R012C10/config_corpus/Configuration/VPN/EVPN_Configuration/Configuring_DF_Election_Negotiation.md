Configuring DF Election Negotiation
===================================

This section describes how to configure DF election negotiation.

#### Usage Scenario

After DF election negotiation is configured on a PE, if the DF election algorithm configured on the PE does not match that on the remote PE, the DF election algorithm on the PE is rolled back to the default DF election algorithm.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In EVPN VPLS scenarios, DF election algorithms are rolled back to the interface- or VLAN-based election algorithm based on the configuration. In EVPN VPWS scenarios, DF election algorithms are rolled back to the interface- or service ID-based election algorithm based on the configuration.
* In scenarios where E-Trunk, VRRP, or PW status is used to determine the master/backup status of devices, DF election negotiation is not affected.


#### Pre-configuration Tasks

Before configuring DF election negotiation, complete one of the following tasks:

* [Configure EVPN VPLS over MPLS (common EVPN instance)](dc_vrp_evpn_cfg_0003.html).
* [Configure EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html).
* [Configure EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html).
* [Configure EVPN VPWS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0021_copy.html).
* [Configure EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn**](cmdqueryname=evpn)
   
   
   
   The global EVPN configuration view is displayed.
3. Run [**df-election extcommunity-check enable**](cmdqueryname=df-election+extcommunity-check+enable)
   
   
   
   DF election negotiation is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After DF election negotiation is configured, you can run the [**display evpn**](cmdqueryname=display+evpn) **vpn-instance** **name** *vpn-instance-name* **df result** **esi** *esi* command to check whether **DF Election Type** is **Preference-based**.