Configuring VPLS Accessing L2VPN
================================

This section describes how to configure VPLS accessing L2VPN. To achieve this, VPLS needs to be deployed on the access network.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0000001153011020__fig_dc_vrp_l2-l3_cfg_500801), a user has multiple dispersed sites that connect to a carrier's access network through Ethernet. These sites need to communicate with each other to form a continuous network. To meet this requirement, deploy VPLS on the carrier's access network for these sites to communicate and to access MPLS L2VPN services on the carrier's bearer network. If too many dispersed sites are connected to the access network, deploy HVPLS on the access network. As shown in [Figure 1](#EN-US_TASK_0000001153011020__fig_dc_vrp_l2-l3_cfg_500801), on access network 2, network provider edges (NPEs) function as upper-layer PEs, and underlayer provider edges (UPEs) function as lower-layer PEs. In this manner, the logical connections between PEs are reduced.

**Figure 1** VPLS accessing L2VPN  
![](figure/en-us_image_0000001200293307.png)

#### Pre-configuration Tasks

Before configuring VPLS accessing L2VPN, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the interfaces are up.
* Enable an IGP on the MPLS access network for IP connectivity.
* Create full-mesh VPLS between UPEs and NPEs
* Enable an IGP on the MPLS bearer network for IP connectivity.
* Configure basic L2VPN functions on NPEs.


[Creating a VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5004_copy1.html)

This section describes how to configure an L2VE interface that terminates L2VPN and an L3VE interface that provides access to L2VPN, and how to bind the VE interfaces to the corresponding VE group.

[Creating an L2VE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l2_cfg_5003.html)

This section describes how to configure an L2VE interface for L2VPN termination and bind the L2VE interface to a VE group.

[Creating an L3VE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l2_cfg_5004.html)

This section describes how to configure an L3VE interface to access an L2VPN and bind the L3VE interface to a VE group.

[(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l2_cfg_5006.html)

When the MAC address of an L2VE or L3VE interface conflicts with the MAC address of another type of interface, you can change the MAC address of the L2VE or L3VE interface to allow normal communication.

[Binding an L2VE Interface to a VSI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5010.html)

After an L2VE interface is bound to a VSI, the L2VE interface can be considered as an attachment circuit (AC) interface.

[Configuring Access to L2VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5006_copy.html)

This section describes how to configure an IP address for an L3VE sub-interface and bind the sub-interface to a VPN to implement access to L2VPN.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5012.html)

After configuring VPLS accessing L2VPN, you can view the binding between the VE interfaces and VE group, and information about VPLS VSIs.