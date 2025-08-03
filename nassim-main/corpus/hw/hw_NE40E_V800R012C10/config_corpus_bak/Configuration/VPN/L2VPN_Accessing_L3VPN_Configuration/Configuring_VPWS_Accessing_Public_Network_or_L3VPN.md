Configuring VPWS Accessing Public Network or L3VPN
==================================================

This section describes how to configure VPWS accessing public network or L3VPN, specifically, how to deploy VPWS on the access network.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172370327__fig_dc_vrp_l2-l3_cfg_500301), if a user needs to access an MPLS L3VPN on a carrier's transport network (or the public network) through an MPLS L2VPN on the carrier's access network, VPWS can be deployed on the carrier's access network to facilitate such access through a virtual private line.

**Figure 1** VPWS accessing L3VPN networking  
![](images/fig_dc_vrp_l2-l3_cfg_500301.png)

#### Pre-configuration Tasks

Before configuring VPWS accessing L3VPN, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is up.
* Configure an IGP on the MPLS access network for IP connectivity.
* Enable MPLS L2VPN on UPEs and NPEs.
* Create L2VPN tunnels between UPEs and NPEs.
* For LDP PWs: Create LDP sessions between UPEs and NPEs. If the UPEs and NPEs are not directly connected, establish remote LDP sessions between them.
* For BGP PWs: Create BGP sessions between UPEs and NPEs.
* Configure an IGP on the MPLS transport network for IP connectivity.
* Configure basic L3VPN functions on NPEs.


[Creating VE Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5004.html)

This section describes how to configure an L2VE interface for L2VPN termination and an L3VE interface for L3VPN access and bind the two VE interfaces to the corresponding VE group.

[Creating an L2VE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l3_cfg_5001.html)

This section describes how to configure an L2VE interface for L2VPN termination and bind the L2VE interface to a VE group.

[Creating an L3VE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l3_cfg_5002.html)

This section describes how to configure an L3VE interface for L3VPN access and how to bind the L3VE interface to the corresponding VE group.

[(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l3_cfg_5005.html)

When the MAC address of an L2VE or L3VE interface conflicts with the MAC address of another type of interface, you can change the MAC address of the L2VE or L3VE interface to allow normal communication.

[Associating an L2VE Interface with a VPWS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5005.html)

This section describes how to associate an L2VE interface with a VPWS, specifically, how to configure a VPWS connection on an L2VE sub-interface to provide L2VPN functions.

[(Optional) Configuring PW APS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5027.html)

This section describes how to configure PW APS, so that an active/standby PW switchover can be performed if a PW fails.

[Configuring Public Network or L3VPN Access](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5006.html)

This section describes how to configure an IP address for an L3VE sub-interface and bind the sub-interface to a VPN for public network or L3VPN access.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5007.html)

After configuring VPWS accessing public network or L3VPN, check the binding relationship between VE interfaces and the VE group and VPWS connection information.