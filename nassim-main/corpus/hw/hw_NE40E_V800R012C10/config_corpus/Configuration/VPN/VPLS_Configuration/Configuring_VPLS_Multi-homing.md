Configuring VPLS Multi-homing
=============================

In VPLS networking in which a CE is multi-homed to multiple PEs, configuring VPLS multi-homing prevents routing loops between the multi-homed CE and its connected PEs.

#### Usage Scenario

To deliver high-reliability services over a VPLS network, carriers usually dual-home a CE to two PEs through redundant links. While providing link-level protection, the dual-homing mechanism also brings in the risk of routing loops. To prevent loops in multi-homing scenarios, VPLS multi-homing can be deployed on PEs.

A PE assigns a multi-homing site and an MH-ID to each connected CE during VSI configuration. CEs single-homed to the same PE share a default multi-homing site. If a CE is dual-homed to PE1 and PE2, PE1 and PE2 must assign the same MH-ID to the CE. On the network shown in [Figure 1](#EN-US_TASK_0172370200__fig_dc_vrp_vpls_cfg_603601), PE1 assigns a site and MH-ID 1 to CE1. CE2 is dual-homed to PE1 and PE2, which both assign MH-ID 2 to CE2 in addition to assigning a site to CE2. VPLS multi-homing adjusts link priorities based on the AC state (ACS), multi-homing site preference (PREF), and PE's BGP router ID (PE-ID) in descending order of priority to ensure that one access link of a multi-homed CE is in the active state and the other access links are in the blocked state.

**Figure 1** VPLS multi-homing  
![](images/fig_dc_vrp_vpls_cfg_603601.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

VPLS multi-homing described in this document cannot work with VPLS multi-homing defined in the draft-ietf-bess-vpls-multihoming-00 standard.



#### Pre-configuration Tasks

Before configuring VPLS multi-homing, complete the following tasks:

* Configure interface IP addresses and an IGP on PEs and Ps.
* Configure LSR IDs and basic MPLS functions on PEs and Ps.
* Establish tunnels between PEs to transmit service data.


[Configuring BGP Peers to Exchange VPLS Information](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6037.html)

BGP VPLS shares TCP connections with BGP and inherits most BGP configurations. A major difference between BGP and BGP VPLS is that BGP VPLS requires PEs to exchange VPLS information as BGP peers in the L2VPN AD address family view.

[Creating a VPLS Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6038.html)

When configuring VPLS multi-homing, you need to create VSIs, configure BGP signaling, RDs, and VPN targets, and create VPLS connections.

[Binding a Multi-homing Site to an AC Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6039.html)

Configure an AC interface and bind a multi-homing site to the AC interface to implement VPLS multi-homing.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6040.html)

After configuring VPLS multi-homing, check local and remote VSI and VPLS connection information.