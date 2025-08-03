Configuring Inter-AS NG MVPN Option C
=====================================

This section describes how to configure inter-AS NG MVPN Option C, in which PEs in different ASs establish multi-hop EBGP peer relationships to exchange VPNv4 routes.

#### Usage Scenario

In inter-AS NG MVPN Option C, PEs in different ASs establish MP-BGP peer relationships. For example, on the network shown in [Figure 1](dc_vrp_cfg_ngmvpn_0038.html#EN-US_CONCEPT_0000001225833448__fig_dc_vrp_cfg_ngmvpn_003801), PE1 and PE2 establish an EBGP peer relationship to exchange VPN routes, PE1 and ASBR1 establish an IBGP peer relationship, ASBR1 and ASBR2 establish an EBGP peer relationship, and ASBR2 and PE2 establish an IBGP peer relationship. The public network uses non-segmented inter-AS mLDP tunnels to carry multicast VPN traffic. [Figure 1](dc_vrp_cfg_ngmvpn_0038.html#EN-US_CONCEPT_0000001225833448__fig_dc_vrp_cfg_ngmvpn_003801) shows inter-AS NG MVPN Option C networking.

Inter-AS NG MVPN Option C is recommended if each AS needs to exchange a large number of VPN routes with other ASs. This option prevents an ASBR from impeding network expansion. After the local ASBR learns a labeled BGP public network route from the remote ASBR in an AS that is different from the AS of the local ASBR, the local ASBR allocates a label to this route based on the configured policy and advertises the route to the IBGP peer PE that is capable of label processing. A public network LSP is then set up.

**Figure 1** Inter-AS NG MVPN Option C networking  
![](figure/en-us_image_0000001270193977.png)

#### Pre-configuration Tasks

Before configuring inter-AS NG MVPN Option C, complete the following tasks:

* Configure an IGP for the MPLS backbone network of each AS to ensure IP connectivity on each backbone network.
* Configure basic MPLS functions and MPLS LDP for the MPLS backbone network of each AS.
* Establish an IBGP peer relationship between the PE and ASBR in the same AS.
* [Configure a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) on each PE connected to a CE and [bind interfaces to VPN instances](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Assign an IP address to each CE interface that is connected to a PE.


[Configuring Global MPLS LDP Functions and Enabling MPLS LDP on Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0039.html)

Global LDP must be enabled on each node before LDP services can be configured in an MPLS domain.

[Configuring an Automatic mLDP P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0040.html)

Automatic mLDP P2MP tunnels are used to transmit NG MVPN traffic.

[Configuring a Static RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0041.html)

To use a static Rendezvous Point (RP) in a PIM-SM domain, configure the same RP address and same address range of multicast groups that the RP serves on all routers in the PIM-SM domain. You need to configure the RP only if the PIM-SM mode is used on a private network. If the PIM-SSM mode is used, you do not need to configure the RP.

[Configuring MP-IBGP Between a PE and an ASBR in the Same AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0042.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between the PE and ASBR.

[Configuring MP-EBGP for PEs and ASBRs in Different ASs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0043.html)

By introducing extended community attributes into BGP, MP-EBGP can advertise VPNv4 routes between PEs. And after an MP-EBGP peer relationship is established between ASBRs in different ASs, an ASBR can advertise the VPNv4 routes of its AS to the other ASBR.

[Configuring a Routing Policy to Control Label Distribution on ASBRs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0044.html)

Configure a routing policy to control MPLS label allocation for each IPv4 route. The ASBR only allocates labels to the IPv4 routes that match the rules in the policy.

[Configuring BGP MVPN Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0045.html)

Establish a BGP MVPN peer relationship between PEs belonging to the same MVPN so that the PEs can use BGP to exchange BGP A-D and BGP C-multicast routes.

[Configuring a P2MP LSP to Carry Multicast Traffic](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0046.html)

An NG MVPN uses P2MP LSPs to carry multicast traffic. Only mLDP P2MP LSPs are supported.

[(Optional) Configuring Switching Between I-PMSI and S-PMSI Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0021b.html)



[Configuring PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0047.html)

Configuring PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

[Configuring Route Exchange Between PEs and CEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0048.html)

The routing protocol between CE and PE can be BGP, static routing (including default static routes), and IGP.