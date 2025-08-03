Configuring Inter-AS NG MVPN Option B
=====================================

This section describes how to configure inter-AS NG MVPN Option B, in which ASBRs use MP-EBGP to advertise labeled VPNv4 routes.

#### Usage Scenario

In inter-AS NG MVPN Option B, ASBRs establish MP-BGP peer relationships and exchange VPN routes. The interfaces that connect the ASBRs do not need to be bound to VPNs. A PE and an ASBR establish an IBGP peer relationship, and two ASBRs establish an EBGP peer relationship. The public network uses non-segmented inter-AS mLDP tunnels to carry multicast VPN traffic. [Figure 1](dc_vrp_cfg_ngmvpn_0024.html#EN-US_TASK_0000001225833436__fig_dc_vrp_cfg_ngmvpn_002401) shows inter-AS NG MVPN Option B networking.

**Figure 1** Inter-AS NG MVPN-Option B  
![](figure/en-us_image_0000001225513876.png)

#### Pre-configuration Tasks

Before configuring inter-AS NG MVPN Option B, complete the following tasks:

* Configure an IGP for the MPLS backbone network of each AS to ensure IP connectivity on each backbone network.
* Configure basic MPLS capabilities for the MPLS backbone network of each AS and establish LDP LSPs between MP-IBGP peers.
* [Configure a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) on each PE connected to a CE and [bind interfaces to VPN instances](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Assign an IP address to each CE interface that is connected to a PE.


[Configuring Global MPLS LDP Functions and Enabling MPLS LDP on Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0026.html)

Global LDP must be enabled on each node before LDP services can be configured in an MPLS domain.

[Configuring an Automatic mLDP P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0027.html)

Automatic mLDP P2MP tunnels can only transmit NG MVPN and multicast VPLS traffic.

[Configuring a Static RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0028.html)

To use a static Rendezvous Point (RP) in a PIM-SM domain, configure the same RP address and same address range of multicast groups that the RP serves on all routers in the PIM-SM domain.

[Configuring MP-IBGP Between a PE and an ASBR in the Same AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0029.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between the PE and ASBR.

[Configuring MP-EBGP Between ASBRs in Different ASs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0030.html)

After an MP-EBGP peer relationship is established between ASBRs, an ASBR can advertise the VPNv4 routes of its AS to the other ASBR.

[Configuring BGP MVPN Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0031.html)

Establish a BGP MVPN peer relationship between PEs belonging to the same MVPN, so that the PEs can use BGP to exchange BGP A-D and BGP C-multicast routes.

[(Optional) Configuring Intra-AS MSDP Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0032.html)

If multiple PIM-SM domains exist in an AS or multiple Rendezvous Points (RPs) serving different multicast groups exist in a PIM-SM domain, configure MSDP peer relationships between RPs (including static RPs and C-RPs).

[Configuring a P2MP LSP to Carry Multicast Traffic](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0033.html)

An NG MVPN uses P2MP LSPs to carry multicast traffic. Only mLDP P2MP LSPs are supported.

[(Optional) Configuring Switching Between I-PMSI and S-PMSI Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0021a.html)



[Configuring PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0034.html)

Configuring PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

[Configuring Route Exchange Between PEs and CEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0025.html)

To enable CEs to communicate, the PEs and CEs must be capable of exchanging routes.