Configuring an L2VPN to Access Multiple L2VPNs Through Sub-interfaces for VLAN Tag Termination
==============================================================================================

Configure an L2VPN to access multiple L2VPNs through L3VE sub-interfaces.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0000001204798491__fig_dc_vrp_l2-l3_cfg_501801) and [Figure 2](#EN-US_TASK_0000001204798491__fig_dc_vrp_l2-l3_cfg_501802), multiple types of services, such as data, voice, and video, are transmitted on a user network. The sub-interface for VLAN tag termination transmits different VLAN tags to different MPLS L2VPNs on the carrier's bearer network through the L2VPN on the access network. This helps the carrier to allocate network resources based on service types on the bearer network, effectively utilize network resources, and provide differentiated QoS for different types of services.

If the L3VE sub-interface receives single-tagged service data packets from the UPE, configure the L3VE sub-interface as a sub-interface for dot1q VLAN tag termination to access the L2VPN.

If the L3VE sub-interface receives double-tagged service data packets from the UPE, configure the L3VE sub-interface as a sub-interface for QinQ VLAN tag termination to access L2VPN.

**Figure 1** Typical networking of an L2VPN accessing multiple L2VPNs through sub-interfaces for dot1q VLAN tag termination  
![](figure/en-us_image_0000001158759982.png)
**Figure 2** Typical networking of an L2VPN accessing multiple L2VPNs through sub-interfaces for QinQ VLAN tag termination  
![](figure/en-us_image_0000001204559963.png)

#### Pre-configuration Tasks

To configure an L2VPN to access multiple L2VPNs through sub-interfaces for VLAN tag termination, complete the following tasks:

* Connect interfaces and set parameters for the interfaces to ensure that the physical-layer status of the interfaces is up.
* Enable IGP on the MPLS access network to realize IP connectivity.
* Create VPLS or VLL between UPEs and NPEs.
* Configure an IGP on the MPLS bearer network to realize IP connectivity.
* Configure basic L2VPN functions on NPEs.

#### Configuration Procedures

| Configuring an L2VPN to Access Multiple L2VPNs Through Dot1q Sub-interfaces for VLAN Tag Termination | Configuring an L2VPN to Access Multiple L2VPNs Through QinQ Sub-interfaces for VLAN Tag Termination |
| --- | --- |
| Creating a VE Interface | |
| Binding an L2VE Interface to a VPWS or VSI | |
| Creating an L3VE Sub-interface for Dot1q VLAN Tag Termination and Connecting It to an L2VPN | Creating an L3VE Sub-interface for QinQ VLAN Tag Termination and Connecting It to an L2VPN |



[Creating a VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5004_copy2.html)

This section describes how to configure an L2VE interface that terminates L2VPN and an L3VE interface that provides access to L2VPN, and how to bind the VE interfaces to the corresponding VE group.

[Binding an L2VE Interface to a VPWS or VSI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5020.html)

This section describes how to configure an L2VE interface to terminate L2VPN.

[Creating an L3VE Sub-interface for Dot1q VLAN Tag Termination and Connecting It to an L2VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5021.html)

If one tag is carried by a user packet from a UPE, configure the L3VE sub-interface as a sub-interface for dot1q VLAN tag termination for access to L2VPN.

[Creating an L3VE Sub-interface for QinQ VLAN Tag Termination and Connecting It to an L2VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5022.html)

If an L3VE sub-interface receives double-tagged service packets from a UPE, configure the L3VE sub-interface as a sub-interface for QinQ VLAN tag termination to access L2VPN.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l2_cfg_5023.html)

After an L2VPN accesses multiple L2VPNs through sub-interfaces for VLAN tag termination, you can view the binding between the VE interfaces and VE group, and termination information on VE sub-interfaces.