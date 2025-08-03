Configuring EVPN VPWS Accessing BRAS (with VRRP Determining the Master/Backup Status)
=====================================================================================

If EVPN VPWS over MPLS or EVPN VPWS over SRv6 in dual-homing single-active mode is deployed on the network and VRRP or VRRP6 is configured on the devices responsible for user access to determine their master/backup status, you need to configure EVPN VPWS accessing BRAS and associate VRRP or VRRP6 with EVPN VPWS to determine the primary/secondary status of EVPN VPWS PWs.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0314538223__fig1291715401904), EVPN VPWS over MPLS or EVPN VPWS over SRv6 in dual-homing single-active mode is deployed between M-AGGs and BNGs, and VRRP4 or VRRP6 is deployed between BNG1 and BNG2 to determine their master/backup status as well as the primary/secondary status of EVPN VPWS PWs. To enable users to access an external network, configure EVPN VPWS accessing BRAS on the BNGs.

**Figure 1** EVPN VPWS accessing BRAS (with VRRP determining the master/backup status)  
![](figure/en-us_image_0314591195.png)

#### Pre-configuration Tasks

Before configuring EVPN VPWS accessing BRAS (with VRRP determining the master/backup status), complete the following tasks:

* Configure [EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html), [EVPN VPWS over SRv6 BE](dc_vrp_srv6_cfg_all_0021_copy.html), or [EVPN VPWS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpws_over_srv6-te_policy_copy.html) between the M-AGGs and BNGs. The single-active mode needs to be configured in the system view or ESI view.
* Configure [multi-device backup for IPv4 user information](../ne/dc_ne_cfg_rui_0004.html) or [multi-device backup for IPv6 user information](../ne/dc_ne_cfg_rui_0020.html) on BNG1 and BNG2. This configuration includes the VRRP or VRRP6 group configuration.


[Creating an L2VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws-bras6_vrrp2.html)

Configure an L2VE interface on each BNG to terminate EVPN VPWS and bind the L2VE interface to a VE group.

[Creating an L3VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws-bras6_vrrp3.html)

Configure an L3VE interface on each BNG for BRAS service access and bind the L3VE interface to a VE group.

[(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws-bras6_vrrp4.html)

If the MAC address of an L2VE or L3VE interface is the same as that of another interface on a BNG, configure a new MAC address for the L2VE or L3VE interface to ensure normal communication.

[Associating an L2VE Interface with an EVPL Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws-bras6_vrrp5.html)

After an L2VE interface is associated with an EVPL instance on a BNG, the L2VE interface can terminate EVPN VPWS.

[Associating an EVPL Instance with VRRP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws-bras6_vrrp6.html)

Associate EVPL instances with VRRP on BNGs, so that EVPN VPWS can determine the primary/secondary status of PWs based on the VRRP or VRRP6 group status.

[Configuring an L3VE Interface as a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws-bras6_vrrp7.html)

Configure the L3VE interface on each BNG as a BAS interface for BRAS access.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws-bras6_vrrp8.html)

After configuring EVPN VPWS accessing BRAS, you can check binding between the VE interfaces and VE group, VRRP or VRRP6 group status, and information about the specified EVPL instance on each BNG.