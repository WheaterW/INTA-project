Configuring a VPLS to Access the Public Network or an L3VPN
===========================================================

This section describes how to configure VPLSs to access the public network or L3VPN. To achieve this, you can implement the VPLS technology on the access network.

#### Applicable Environment

As shown in [Figure 1](#EN-US_TASK_0172370340__fig_dc_vrp_l2-l3_cfg_500801), a user has many scattered sites on the access network of a carrier, and they are connected through Ethernet. These sites are required to interconnect to form an integrated network. In this case, the VPLS can be deployed on the access network to network those sites, and to access the MPLS L3VPN service running on the bearer network. If there are many scattered sites on the access network, deploy the HVPLS on it, as shown in the access network 2 in [Figure 1](#EN-US_TASK_0172370340__fig_dc_vrp_l2-l3_cfg_500801). The network provider edge (NPE) works as provider edge (PE) at upper layer and UPEs as PE at lower layer. Therefore, the logical connections between PEs are reduced.

**Figure 1** Networking diagram of VPLS accessing L3VPN  
![](images/fig_dc_vrp_l2-l3_cfg_500801.png)  


#### Pre-configuration Tasks

Before configuring a VPLS to access an L3VPN, complete the following tasks:

* Connecting the interfaces and configuring their physical parameters so as to make their physical layer Up
* Enabling IGP on the MPLS access network to realize IP connectivity
* Creating full-mesh VPLS between UPEs and NPEs
* Enabling IGP on the MPLS bearer network to realize IP connectivity
* Configuring the basic functions of L3VPN on NPEs


[Creating VE Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5009.html)

This part describes how to configure an L2VE interface that terminates the L2VPN and configure an L3VE interface that access L3VPN, and how to bind the VE interfaces to the relevant VE-Group.

[Creating an L2VE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l3_cfg_5003.html)

This section describes how to configure an L2VE interface for L2VPN termination and bind the L2VE interface to a VE group.

[Creating an L3VE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l3_cfg_5004.html)

This section describes how to configure an L3VE interface for L3VPN access and how to bind the L3VE interface to the corresponding VE group.

[(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l3_cfg_5006.html)

When the MAC address of an L2VE or L3VE interface conflicts with the MAC address of another type of interface, you can change the MAC address of the L2VE or L3VE interface to allow normal communication.

[Binding an L2VE Interface to a VSI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5010.html)

After an L2VE interface is bound to a VSI, the L2VE interface can be considered as an attachment circuit (AC) interface.

[Configuring the Access to the Public Network or an L3VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5011.html)

This section describes how to configure an IP address for an L3VE sub-interface and bind the sub-interface to a VPN for public network or L3VPN access.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5012.html)

After configuring VPLS accessing public network or L3VPN, check the binding relationship between the VE interfaces and VE group and VPLS VSI information.