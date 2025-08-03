Configuring Inter-AS VPN Option B (ASBR Also Functioning as an RR)
==================================================================

In a scenario in which the backbone network spans two ASs, ASBRs need to advertise VPNv4 routes through MP-EBGP. When multiple PEs exist in the ASs, you can configure an ASBR as an RR to lower configuration complexity.

#### Usage Scenario

In inter-AS VPN Option B mode, if multiple PEs exist in an AS, you can configure an ASBR as an RR to reduce the number of MP-IBGP connections needed between PEs. Configuring an ASBR as an RR will burden the ASBR. Therefore, it is required that a high-performance device be used as the ASBR. On the network shown in [Figure 1](#EN-US_TASK_0172369311__fig7288112053516), ASBR1 is configured as an RR so that PE1 and PE2 do not need to set up an MP-IBGP peer relationship.

**Figure 1** Inter-AS VPN Option B networking (ASBR also functioning as an RR)  
![](figure/en-us_image_0000001430996650.png)

#### Pre-configuration Tasks

Before configuring inter-AS VPN Option B (ASBR also functioning as an RR), complete the following tasks:

* Configure an IGP for the MPLS backbone network of each AS to ensure IP connectivity of the backbone network in each AS.
* Configure MPLS both globally and per interface on each node of the MPLS backbone network in each AS and establish an LDP LSP or TE tunnel between MP-IBGP peers.
* [Configure a VPN instance on each PE](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) and [bind the interface that connects a PE to a CE to the VPN instance on that PE](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Configure an IP address for the interface connecting a CE to a PE.


[Configuring MP-IBGP Between a PE and an ASBR in the Same AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0048.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between the PE and ASBR.

[Configuring MP-EBGP Between ASBRs in Different ASs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0049.html)

After an MP-EBGP peer relationship is established between ASBRs, an ASBR can advertise the VPNv4 routes of its AS to the other ASBR.

[Configuring ASBRs Not to Filter VPNv4 Routes Based on VPN Targets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0133.html)

In inter-AS VPN Option B mode, ASBRs do not have VPN instances. If you want ASBRs to keep received VPNv4 routes, configure ASBRs not to filter VPNv4 routes based on VPN targets.

[(Optional) Using a Routing Policy to Control VPNv4 Routes on ASBRs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0162.html)

ASBRs can use a routing policy to filter undesired VPNv4 routes.

[(Optional) Configuring One-Label-per-Next-Hop Label Distribution on an ASBR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0170.html)

To conserve label resources on an ASBR, configure one-label-per-next-hop label allocation on the ASBR. One-label-per-next-hop label allocation on ASBRs and one-label-per-instance label distribution on PEs must be used together.

[Configuring BGP IPv4 VPN Route Reflection on an ASBR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0050.html)

Route reflection on an ASBR is used to reflect the VPNv4 routes advertised by the PE in the same AS to other PEs. As a result, PEs do not need to set up BGP peer relationships, which simplifies configurations.

[Verifying the Configuration of Inter-AS VPN Option B (ASBR Also Functioning as an RR)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0051.html)

After configuring inter-AS VPN Option B (ASBR also functioning as an RR), check the status of all BGP peer relationships and VPNv4 routing information on PEs or ASBRs.