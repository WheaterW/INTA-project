Configuring EVPN VPWS over MPLS Accessing BRAS (VRRP Determining the Master/Backup Status Not Used)
===================================================================================================

If EVPN VPWS over MPLS is used to carry E-Line services on a network, configure EVPN VPWS over MPLS accessing BRAS on each device that provides access for users.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0286123731__fig202803358290), EVPN VPWS over MPLS is deployed between M-AGGs and BNGs to carry E-Line services. To allow users to access an external network, configure EVPN VPWS over MPLS accessing BRAS on the BNGs.

**Figure 1** Networking diagram for EVPN VPWS over MPLS accessing BRAS  
![](figure/en-us_image_0286124440.png)

#### Pre-configuration Tasks

Before configuring EVPN VPWS over MPLS accessing BRAS, complete the following tasks:

On the M-AGGs and BNGs: [Configuring EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html)


[Creating an L2VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws_over_mpls_bras1.html)

Configure an L2VE interface on each BNG to terminate EVPN VPWS and bind the L2VE interface to a VE group.

[Creating an L3VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws_over_mpls_bras2.html)

Configure an L3VE interface on each BNG for BRAS service access and bind the L3VE interface to a VE group.

[(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws_over_mpls_bras3.html)

If the MAC address of an L2VE or L3VE interface is the same as that of another interface on a BNG, configure a new MAC address for the L2VE or L3VE interface to ensure normal communication.

[Associating an L2VE Interface with an EVPL Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws_over_mpls_bras4.html)

After an L2VE interface is associated with an EVPL instance on a BNG, E-Line services can be terminated on the L2VE interface.

[Configuring an L3VE Interface as a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws_over_mpls_bras5.html)

Configure the L3VE interface on each BNG as a BAS interface for BRAS access.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpws_over_mpls_bras6.html)

After configuring EVPN VPWS over MPLS accessing BRAS, check the binding relationships between the VE interfaces and VE group and information about the specified EVPL instance on each BNG.