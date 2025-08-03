Configuring Inter-Area Seamless NG MVPN
=======================================

This section describes how to configure inter-area seamless NG MVPN, in which PEs and ABRs establish IBGP peer relationships through BGP LSPs.

#### Usage Scenario

In inter-area seamless NG MVPN, a CE and a PE belong to different ASs, PEs and ABRs belong the same AS. A BGP LSP needs to be established to implement E2E service connectivity.

A PE and an ABR establish an IBGP peer relationship, and ABRs establish and IBGP peer relationship. The local PE and ABR establish an IBGP peer relationship, and the local and remote ABRs establish an IBGP peer relationship, and the remote ABR and PE establish an IBGP peer relationship. The ABRs function as RRs to reflect MVPN routes. [Figure 1](dc_vrp_cfg_ngmvpn_0080.html#EN-US_CONCEPT_0000001270153541__fig_dc_vrp_cfg_ngmvpn_008001) shows inter-area seamless NG MVPN networking.

**Figure 1** Inter-area seamless NG MVPN networking  
![](figure/en-us_image_0000001270193809.png)

#### Pre-configuration Tasks

Before configuring inter-area seamless NG MVPN, complete the following tasks:

* Configure an IGP on the MPLS backbone network to ensure IP connectivity in the AS.
* Configure basic MPLS functions and MPLS LDP for the MPLS backbone network of the AS.
* Establish an IBGP peer relationship between the PE and ABR.
* Establish an IBGP peer relationship between the ABRs.
* [Configure a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) on each PE connected to a CE and [bind interfaces to VPN instances](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Assign an IP address to each CE interface that is connected to a PE.


[Configuring an Automatic mLDP P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0081.html)

Automatic mLDP P2MP tunnels are used to transmit NG MVPN traffic.

[Configuring a Static RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0082.html)

To use a static Rendezvous Point (RP) in a PIM-SM domain, configure the same RP address and same address range of multicast groups that the RP serves on all routers in the PIM-SM domain.

[Configuring Route Reflection on an ABR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0083.html)

Route reflection on an ABR is used to reflect the VPNv4 routes advertised by the PE to other devices in the same AS. As a result, PE does not need to set up BGP peer relationship with other devices, which simplifies configurations.

[Configuring BGP MVPN Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0084.html)

Establish a BGP MVPN peer relationship between devices belonging to the same MVPN, so that the devices can use BGP to exchange BGP A-D and BGP C-multicast routes.

[Configuring a P2MP LSP to Carry Multicast Traffic](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0085.html)

An NG MVPN uses P2MP LSPs to carry multicast traffic. Only mLDP P2MP LSPs are supported.

[(Optional) Configuring Switching Between I-PMSI and S-PMSI Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0021e.html)



[Configuring PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0086.html)

Configuring PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

[Configuring Route Exchange Between PEs and CEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0087.html)

The routing protocol between CE and PE can be BGP, static routing (including default static routes), and IGP.