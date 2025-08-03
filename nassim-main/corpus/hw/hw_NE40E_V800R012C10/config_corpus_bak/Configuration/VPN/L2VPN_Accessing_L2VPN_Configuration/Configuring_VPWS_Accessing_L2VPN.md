Configuring VPWS Accessing L2VPN
================================

This section describes how to configure VPWS accessing L2VPN. To achieve this, VPWS needs to be deployed on the access network.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001199088905__fig_dc_vrp_l2-l3_cfg_500301), if a user needs to access an MPLS L2VPN on a carrier's bearer network through an MPLS L2VPN on the carrier's access network, VPWS can be deployed on the carrier's access network to allow the user to access the target MPLS L2VPN through a virtual private line.

**Figure 1** VPWS accessing L2VPN  
![](figure/en-us_image_0000001199048811.png)

#### Pre-configuration Tasks

Before configuring LDP VPWS accessing L2VPN, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the interfaces are up.
* Enable an IGP on the MPLS access network for IP connectivity.
* Enable MPLS L2VPN on UPEs and NPEs.
* Create L2VPN tunnels between UPEs and NPEs.
* For LDP PWs: create LDP sessions between UPEs and NPEs. (If the UPEs and NPEs are not directly connected, set up remote LDP sessions between them.)
* For BGP PWs: create BGP sessions between UPEs and NPEs.
* Enable an IGP on the MPLS bearer network for IP connectivity.
* Configure basic L2VPN functions on NPEs.


[Creating a VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5004.html)

This section describes how to configure an L2VE interface that terminates L2VPN and an L3VE interface that provides access to L2VPN, and how to bind the VE interfaces to the corresponding VE group.

[Creating an L2VE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l2_cfg_5001.html)

This section describes how to configure an L2VE interface for L2VPN termination and bind the L2VE interface to a VE group.

[Creating an L3VE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l2_cfg_5002.html)

This section describes how to configure an L3VE interface to access an L2VPN and bind the L3VE interface to a VE group.

[(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2-l2_cfg_5005.html)

When the MAC address of an L2VE or L3VE interface conflicts with the MAC address of another type of interface, you can change the MAC address of the L2VE or L3VE interface to allow normal communication.

[Associating an L2VE Interface with a VPWS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5005.html)

This section describes how to associate an L2VE interface with a VPWS, specifically, how to configure a VPWS connection on an L2VE sub-interface to provide L2VPN functions.

[(Optional) Configuring PW APS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5027.html)

This section describes how to configure PW APS, so that an active/standby PW switchover can be performed if a PW fails.

[Configuring Access to L2VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5006.html)

This section describes how to configure an IP address for an L3VE sub-interface and bind the sub-interface to a VPN to implement access to L2VPN.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5007.html)

After configuring VPWS accessing L2VPN, check the binding between the VE interfaces and VE group and information about the LDP VPWS connection.