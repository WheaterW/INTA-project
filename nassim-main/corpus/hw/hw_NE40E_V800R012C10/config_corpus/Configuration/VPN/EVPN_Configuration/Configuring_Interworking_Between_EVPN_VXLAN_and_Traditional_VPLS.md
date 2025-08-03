Configuring Interworking Between EVPN VXLAN and Traditional VPLS
================================================================

Configuring Interworking Between EVPN VXLAN and Traditional VPLS

#### Usage Scenario

When a DCN with EVPN VXLAN deployed interworks with an enterprise campus network through MPLS L2VPN, interworking between EVPN VXLAN and traditional VPLS must be deployed.

On the network shown in [Figure 1](#EN-US_TASK_0172370533__fig_dc_vrp_vpls_feature_800301), the EOR switch functions as a DC gateway to access the backbone network through the egress routers PE1 and PE2 on the DCN. PE3, which is the egress router on the campus network, interconnects with PE1 and PE2 through the MPLS VPLS network. VXLAN accessing VPLS is configured on PE1 and PE2 to implement communication between the DCN and campus network.

**Figure 1** Interworking between EVPN VXLAN and traditional VPLS  
![](images/fig_vxlan_vpls_02.png)  


#### Pre-configuration Tasks

Before configuring interworking between EVPN VXLAN and traditional VPLS, complete the following tasks:

* Configure interfaces and IP addresses for the egress device PE3 on the campus network, egress devices PE1 and PE2 on the DCN, and the EOR switch.
* Configure an IGP on PE3, PE1, PE2, and the EOR switch to implement IP connectivity on the backbone network.
* Enable MPLS on PE3, PE1, and PE2. Configure MPLS LDP tunnels between PE3 and PE1 and between PE3 and PE2.
* Configure Layer 2 connections between CEs and PEs.


[Creating VSIs and Configuring PW Connections](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0041.html)

This section describes how to configure MPLS VPLS interconnection between PE1, PE2, and PE3.

[Configuring VXLAN EVPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0042.html)

Before enabling interconnection between PE1, PE2, and the EOR switch, configure basic EVPN and VXLAN functions on PE1 and PE2, and create EVPN instances and NVE interfaces.

[Establishing BGP Peer Relationships](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0043.html)

This section describes how to establish a BGP peer relationship between each of PE1 and PE2 and the EOR switch and configure BGP peers.

[Binding EVPN Instances and VSIs to BDs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0044.html)

To implement interconnection between an enterprise campus network and a DCN, bind an EVPN instance and a VSI to the same BD created on each of PE1 and PE2.

[(Optional) Configuring BFD for VPLS PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0045.html)

Configuring BFD for VPLS PW accelerates PW fault detection, speeding up switching of upper-layer applications.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0046.html)

After configuring interworking between EVPN VXLAN and traditional VPLS, verify the configurations, such as VXLAN tunnel and VPLS tunnel and route configurations.