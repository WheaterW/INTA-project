Configuring an L2VPN to Access Multiple L3VPNs Through Sub-interfaces for VLAN Tag Termination
==============================================================================================

This section describes how to configure an L2VPN to access L3VPNs through the L3VE sub-interface in QinQ or Dot1q termination mode. To be specific, you can configure the L3VE sub-interface to terminate user packets of different inner VLAN tags, and then these packets can be sent to different L3VPNs.

#### Applicable Environment

As shown in [Figure 1](#EN-US_TASK_0172370352__fig_dc_vrp_l2-l3_cfg_501801) and [Figure 2](#EN-US_TASK_0172370352__fig_dc_vrp_l2-l3_cfg_501802), different services, such as data, voice, and video, are running on a user network. By adding different VLAN tags to different service packets, sub-interfaces for Dot1q or QinQ VLAN tag termination forward these packets from the L2VPN to different MPLS L3VPNs on the bearer network. In this manner, operators can fully utilize the network resources by allocating different network resources to different services and provide different QoS guarantees for differentiated services.

If an L3VE sub-interface receives single-tagged service data packets from the UPE, configure the L3VE sub-interface as a sub-interface for Dot1q VLAN tag termination to access the L3VPN.

If an L3VE sub-interface receives double-tagged service data packets from the UPE, configure the L3VE sub-interface as a sub-interface for QinQ VLAN tag termination to access the L3VPN.

**Figure 1** Typical networking of the access of an L2VPN to multiple L3VPNs through sub-interfaces for Dot1q VLAN tag termination  
![](images/fig_dc_vrp_l2-l3_cfg_501801.png)  

**Figure 2** Typical networking of the access of an L2VPN to multiple L3VPNs through sub-interfaces for QinQ VLAN tag termination  
![](images/fig_dc_vrp_l2-l3_cfg_501802.png)  


#### Pre-configuration Tasks

To configure an L2VPN to access multiple L3VPNs through sub-interfaces for VLAN tag termination, complete the following tasks:

* Connecting the interfaces and configuring their physical parameters so as to make their physical layer Up
* Enabling IGP on the MPLS access network to realize IP connectivity
* Creating VPLS or VLL between UPEs and NPEs
* Enabling IGP on the MPLS bearer network to realize IP connectivity
* Configuring the basic functions of L3VPN on NPEs

#### Configuration Procedures

| Configure an L2VPN to Access Multiple L3VPNs Through Sub-Interfaces for Dot1q VLAN Tag Termination | Configure an L2VPN to Access L3VPNs Through Sub-Interfaces for QinQ Termination |
| --- | --- |
| Creating VE Interfaces | |
| Binding the L2VE to VPWS or VSI | |
| Creating the L3VE Sub-interface Terminated by Dot1q | Creating the L3VE Sub-interface Terminated by QinQ |



[Creating VE Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5019.html)

This section describes how to configure an L2VE interface for L2VPN termination and an L3VE interface for L3VPN access and bind the two VE interfaces to the corresponding VE group.

[Binding the L2VE to VPWS or VSI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5020.html)

This part describes how to configure an L2VE interface that terminates the L2VPN.

[Creating an L3VE Sub-interface for Dot1q VLAN Tag Termination and Binding the Sub-interface to an L3VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5021.html)

If an L3VE sub-interface receives single-tagged service data packets from the UPE, configure the L3VE sub-interface as a dot1q VLAN tag termination sub-interface for L3VPN access.

[Creating the L3VE Sub-interface Terminated by QinQ](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5022.html)

If an L3VE sub-interface receives double-tagged service data packets from the UPE, configure the L3VE sub-interface as a sub-interface for QinQ VLAN tag termination to access the L3VPN.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2-l3_cfg_5023.html)

After an L2VPN accesses multiple L3VPNs through VLAN tag termination sub-interfaces, you can view the binding relationships between the VE interfaces and VE group as well as termination information on VE sub-interfaces.