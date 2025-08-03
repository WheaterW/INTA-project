Configuring an Intra-AS NG MVPN
===============================

An NG MVPN allows IP multicast services to run on BGP/MPLS IP VPNs, ensuring reliability, security, and efficiency of IP multicast services.

#### Usage Scenario

Multicast services, such as IPTV services, video conferences, and real-time multi-player online games, are increasingly used in daily life. These services are transmitted over service bearer networks that need to:

* Forward multicast traffic smoothly even during traffic congestion.
* Detect network faults in a timely manner and quickly switch traffic from faulty links to normal links.
* Ensure multicast traffic security in real time.

To solve multicast service issues related to traffic congestion, transmission reliability, and data security, deploy an NG MVPN on the service provider's backbone network. [Figure 1](#EN-US_TASK_0000001225673436__fig_dc_vrp_cfg_ngmvpn_000401) shows the basic NG MVPN model.**Figure 1** Typical NG MVPN application  
![](figure/en-us_image_0000001225833720.png)


#### Pre-configuration Tasks

Before configuring an intra-AS NG MVPN, complete the following tasks:

* [Configure basic BGP/MPLS IP VPN functions](dc_vrp_mpls-l3vpn-v4_cfg_0154.html)
* [Configure an automatic mLDP P2MP tunnel](dc_vrp_ldp-p2p_cfg_0062.html) on the root, branch, and leaf nodes, if the NG MVPN needs to use mLDP P2MP LSPs.
* [Configure an automatic P2MP TE tunnel](dc_vrp_te-p2p_cfg_0133.html) on the root, branch, and leaf nodes, if the NG MVPN needs to use RSVP-TE P2MP LSPs.


[Configuring BGP MVPN Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0006.html)

Establish a BGP MVPN peer relationship between PEs belonging to the same MVPN so that the PEs can use BGP to exchange BGP A-D and BGP C-multicast routes.

[Configuring a P2MP LSP to Carry Multicast Traffic](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0007.html)

An NG MVPN uses P2MP LSPs to carry multicast traffic. You can configure either RSVP-TE P2MP or mLDP P2MP LSPs.

[Configuring PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0008.html)

Configuring PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

[(Optional) Configuring IGMP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0009.html)

Configuring IGMP on the interfaces connecting a multicast device to a user network segment allows the device to manage multicast group members on the network segment.

[(Optional) Configuring Switching Between I-PMSI and S-PMSI Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0021.html)



[(Optional) Configuring NG MVPN ORF](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0035.html)

If NG MVPN outbound route filtering (ORF) is enabled in the BGP-MVPN address family, a BGP speaker filters the routes to be advertised to a peer by matching the local export route target (ERT) against the import route target (IRT) of the peer so that the peer receives only desired routes. In this way, NG MVPN ORF reduces network load.

[Verifying the Intra-AS NG MVPN Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0010.html)

After configuring an intra-AS NG MVPN, verify the BGP MVPN peer relationships, I-PMSI tunnels, and VPN instance PIM routing table information.