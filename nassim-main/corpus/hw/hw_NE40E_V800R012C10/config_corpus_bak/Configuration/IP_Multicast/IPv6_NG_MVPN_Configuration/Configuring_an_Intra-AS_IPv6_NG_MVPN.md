Configuring an Intra-AS IPv6 NG MVPN
====================================

An IPv6 NG MVPN allows IP multicast services to run on BGP/MPLS IP VPNs, ensuring reliability, security, and efficiency of IP multicast services.

#### Usage Scenario

Multicast services, such as IPTV services, video conferences, and real-time multi-player online games, are increasingly used in daily life. These services are transmitted over service bearer networks that need to:

* Forward multicast traffic smoothly even during traffic congestion.
* Detect network faults in a timely manner and quickly switch traffic from faulty links to normal links.
* Ensure multicast traffic security in real time.

To solve multicast service issues related to traffic congestion, transmission reliability, and data security, deploy an IPv6 NG MVPN on the service provider's backbone network. [Figure 1](#EN-US_TASK_0172367562__fig_dc_vrp_cfg_ngmvpn_020401) shows the basic IPv6 NG MVPN model.**Figure 1** Typical NG MVPN application  
![](images/fig_dc_vrp_cfg_ngmvpn_020401.png)


#### Pre-configuration Tasks

Before configuring an intra-AS NG MVPN, complete the following tasks:

* [Configure basic BGP/MPLS IP VPN functions](dc_vrp_mpls-l3vpn-v4_cfg_0154.html)
* [Configure automatic mLDP P2MP LSPs](dc_vrp_ldp-p2p_cfg_0062.html) on the root, branch, and leaf nodes, if the NG MVPN needs to use mLDP P2MP LSPs.
* [Configure automatic P2MP TE tunnels](dc_vrp_te-p2p_cfg_0133.html) on the root, branch, and leaf nodes, if the NG MVPN needs to use RSVP-TE P2MP LSPs.


[Configuring BGP MVPN Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0206.html)

Establish a BGP MVPN peer relationship between PEs belonging to the same MVPN so that the PEs can use BGP to exchange BGP A-D and BGP C-multicast routes.

[Configuring a P2MP LSP to Carry Multicast Traffic](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0207.html)

An NG MVPN uses P2MP LSPs to carry multicast traffic. You can configure either RSVP-TE P2MP or mLDP P2MP LSPs.

[Configuring IPv6 PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0208.html)

Configuring IPv6 PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

[(Optional) Configuring MLD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0209.html)

Configuring MLD on the interfaces connecting a multicast device to a user network segment allows the device to manage multicast group members on the network segment.

[(Optional) Configuring Switching Between I-PMSI and S-PMSI Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0210.html)



[Verifying the Configuration of an Intra-AS NG MVPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0211.html)

After configuring an intra-AS IPv6 NG MVPN, verify the BGP MVPN peer relationships, I-PMSI tunnels, and VPN instance PIM routing table information.