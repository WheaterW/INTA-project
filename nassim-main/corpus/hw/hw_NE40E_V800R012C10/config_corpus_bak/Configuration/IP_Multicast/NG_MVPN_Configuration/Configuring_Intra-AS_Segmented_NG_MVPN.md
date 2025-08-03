Configuring Intra-AS Segmented NG MVPN
======================================

To ensure successful multicast data transmission on a network where areas use different types of MPLS protocols for tunnel establishment, configure segmented next generation multicast virtual private network (NG MVPN), improving the transmission reliability, security, and efficiency for IP multicast services.

#### Usage Scenario

Generally, successful multicast data transmission on a non-segmented NG MVPN requires areas to use the same type of MPLS protocol to establish tunnels. If the areas use different types of MPLS protocols, configure segmented NG MVPN to meet the multicast data transmission requirement.

Deploying segmented NG MVPN on a carrier's backbone network can resolve the issues related to multicast traffic congestion, transmission reliability, and data security. [Figure 1](#EN-US_TASK_0000001270433417__fig_dc_vrp_cfg_ngmvpn_009001) shows a basic model of segmented NG MVPN. **Figure 1** Segmented NG MVPN  
![](figure/en-us_image_0000001225513776.png)


#### Pre-configuration Tasks

Before configuring intra-AS segmented NG MVPN, complete the following tasks:

* [Configure basic BGP/MPLS IP VPN functions.](dc_vrp_mpls-l3vpn-v4_cfg_0154.html)
* If point-to-multipoint (P2MP) Multipoint Extensions for LDP (mLDP) tunnels need to be used, [configure automatic P2MP mLDP tunnel establishment](dc_vrp_ldp-p2p_cfg_0062.html) on the root, intermediate, and leaf nodes of each expected tunnel.
* If P2MP Resource Reservation Protocol-Traffic Engineering (RSVP-TE) tunnels need to be used, [configure automatic P2MP TE tunnel establishment](dc_vrp_te-p2p_cfg_0133.html) on the root, intermediate, and leaf nodes of each expected tunnel.


[Configuring Route Reflection on an ABR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0099.html)

Route reflection on an ABR is used to reflect the VPNv4 routes advertised by the PE to other devices in the same AS.

[Establishing BGP MVPN Peer Relationships](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0091.html)

Establish BGP multicast virtual private network (MVPN) peer relationships, allowing provider edges (PEs) on the same MVPN to exchange Auto-Discovery (A-D) and C-multicast routes through BGP.

[Configuring P2MP Tunnels to Carry Multicast Traffic](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0093.html)

NG MVPN uses P2MP tunnels to carry multicast traffic. You can configure P2MP mLDP or RSVP-TE tunnels as needed.

[Configuring the Support for Segmented Tunnels in an AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0092.html)

To ensure successful transmission of multicast traffic among intra-AS areas that use different types of MPLS protocols for tunnel establishment, configure the support for segmented tunnels in the AS.

[(Optional) Configuring Switching Between I-PMSI and S-PMSI Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0021g.html)



[Configuring PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0095.html)

Configure PIM for a VPN, so that multicast VPN routing tables can be created to guide multicast data forwarding.

[(Optional) Configuring IGMP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0096.html)

Enable the Internet Group Management Protocol (IGMP) on a multicast device's interface that is connected to users, implementing multicast group member management on the local network.

[Verifying the Configuration of Intra-AS Segmented NG MVPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ngmvpn_0097.html)

After configuring intra-AS segmented NG MVPN, verify information about BGP MVPN peer relationships, I-PMSI tunnels, and VPN instances' PIM routing tables on PEs.