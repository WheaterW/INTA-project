Configuring EVPN VPWS Accessing L3VPN (with VRRP Determining the Master/Backup Status)
======================================================================================

If EVPN VPWS over MPLS or EVPN VPWS over SRv6 in dual-homing single-active mode is deployed on the network and VRRP or VRRP6 is configured on PEs to determine their master/backup status, you need to configure EVPN VPWS accessing L3VPN and associate VRRP or VRRP6 with EVPN VPWS to determine the primary/secondary status of EVPN VPWS PWs.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001162482723__fig1291715401904), EVPN VPWS over MPLS or EVPN VPWS over SRv6 in dual-homing single-active mode is deployed between M-AGGs and PEs, and VRRP or VRRP6 is deployed between PE1 and PE2 to determine the master/backup status of PEs and primary/secondary status of L3VPN connections. EVPN VPWS accessing L3VPN needs to be configured on PEs.

**Figure 1** EVPN VPWS accessing L3VPN (with VRRP determining the master/backup status)  
![](figure/en-us_image_0000001115882946.png)

#### Pre-configuration Tasks

Before configuring EVPN VPWS accessing L3VPN (with VRRP determining the master/backup status), complete the following tasks:

* Configure [EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html), [EVPN VPWS over SRv6 BE](dc_vrp_srv6_cfg_all_0021_copy.html), or [EVPN VPWS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpws_over_srv6-te_policy_copy.html) between the M-AGGs and PEs. The single-active mode needs to be configured in the system view or ESI view.
* Configure basic L3VPN functions on PEs.


[Creating an L2VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0162.html)

Configure an L2VE interface on each PE to terminate EVPN VPWS and bind the L2VE interface to a VE group.

[Creating an L3VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0163.html)

Configure an L3VE interface used for L3VPN access on each PE and bind the L3VE interface to a VE group.

[Associating an L2VE Interface with an EVPL Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0165.html)

After an L2VE interface is associated with an EVPL instance on a PE, the L2VE interface can terminate EVPN VPWS.

[Associating an EVPL Instance with VRRP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0166.html)

Associate EVPL instances with VRRP on PEs, so that EVPN VPWS can determine the primary/secondary status of PWs based on the VRRP or VRRP6 group status.

[Associating an L3VE Interface with a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0167.html)

Configure an IP address for the L3VE sub-interface on each PE and bind the L3VE sub-interface to the corresponding VPN instance for L3VPN access.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0168.html)

After configuring EVPN VPWS accessing L3VPN, you can check binding between the VE interfaces and VE group, VRRP or VRRP6 group status, and information about the specified EVPL instance on each PE.