Configuring NG MVPN Option C in Inter-AS Seamless MPLS Scenarios
================================================================

This section describes how to configure NG MVPN Option C in an inter-AS seamless MPLS scenario, in which inter-PEs establish EBGP peer relationships over inter-AS BGP LSPs.

#### Usage Scenario

In NG MVPN Option C in an inter-AS seamless MPLS scenario, the access and aggregation layers belong to one AS, and the core layer belongs to another AS. An inter-AS BGP LSP is established to implement E2E service connectivity.

Inter-AS PEs establish MP-BGP peer relationships. For example, on the network shown in [Figure 1](dc_vrp_cfg_ngmvpn_0060.html#EN-US_CONCEPT_0000001225673364__fig_dc_vrp_cfg_ngmvpn_006001), PE1 and PE2 establish an EBGP peer relationship to exchange VPN routes. The local and remote PEs establish an MP-EBGP peer relationship. The local PE and ABR establish an IBGP peer relationship, the ABR and local ASBR establish an IBGP peer relationship, the local and remote ASBRs establish an EBGP peer relationship, and the remote ASBR and PE establish an IBGP peer relationship to exchange routes. [Figure 1](dc_vrp_cfg_ngmvpn_0060.html#EN-US_CONCEPT_0000001225673364__fig_dc_vrp_cfg_ngmvpn_006001) shows NG MVPN Option C networking in an inter-AS seamless MPLS scenario.

**Figure 1** NG MVPN Option C networking in an inter-AS seamless MPLS scenario  
![](figure/en-us_image_0000001270153621.png)

#### Pre-configuration Tasks

Before configuring NG MVPN Option C in an inter-AS seamless MPLS scenario, complete the following tasks:

* Configure an IGP for the MPLS backbone network of each AS to ensure IP connectivity on each backbone network.
* Configure basic MPLS functions and MPLS LDP for the MPLS backbone network of each AS.
* Establish an IBGP peer relationship between the PE and ABR/ASBR in the same AS.
* Establish an IBGP peer relationship between the ABR and ASBR.
* Establish an EBGP peer relationship between the local and remote ASBRs.
* [Configure a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) on each PE connected to a CE and [bind interfaces to VPN instances](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Assign an IP address to each CE interface that is connected to a PE.


[Configuring Global MPLS LDP Functions and Enabling MPLS LDP on Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0061.html)

Global LDP must be enabled on each node before LDP services can be configured in an MPLS domain.

[Configuring an Automatic mLDP P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0062.html)

Automatic mLDP P2MP tunnels are used to transmit NG MVPN traffic.

[Configuring a Static RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0063.html)

To use a static Rendezvous Point (RP) in a PIM-SM domain, configure the same RP address and same address range of multicast groups that the RP serves on all routers in the PIM-SM domain.

[Configuring MP-IBGP Among PEs, ABRs, and ASBRs in the Same AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0064.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes among the PEs, ABRs, and ASBRs.

[Configuring MP-EBGP for PEs and ASBRs in Different ASs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0065.html)

By introducing extended community attributes into BGP, MP-EBGP can advertise VPNv4 routes between PEs. After an MP-EBGP peer relationship is established between ASBRs in Different ASs, an ASBR can advertise the VPNv4 routes of its AS to the other ASBR.

[Configuring a Routing Policy to Control Label Distribution](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0066.html)

Configure a routing policy to control MPLS label allocation for each IPv4 route. The ASBR only allocates label to the routes that match the rules in the policy. The routing policy used for peer ASBR needs to be configured on PE and ABR.

[Configuring Route Reflection on an ABR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0067.html)

Route reflection on an ABR is used to reflect the VPNv4 routes advertised by the PE or ASBR to other devices in the same AS. As a result, PE does not need to set up BGP peer relationship with ASBR, which simplifies configurations.

[Configuring BGP MVPN Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0068.html)

Establish a BGP MVPN peer relationship between devices belonging to the same MVPN, so that the devices can use BGP to exchange BGP A-D and BGP C-multicast routes.

[Configuring a P2MP LSP to Carry Multicast Traffic](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0069.html)

An NG MVPN uses P2MP LSPs to carry multicast traffic. Only mLDP P2MP LSPs are supported.

[(Optional) Configuring Switching Between I-PMSI and S-PMSI Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0021d.html)



[Configuring PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0070.html)

Configuring PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.