Configuring Inter-AS VPN Option B (Spanning More Than Two ASs)
==============================================================

In scenarios where a VPN spans more than two ASs, ASBRs need to advertise VPNv4 routes through MP-EBGP.

#### Usage Scenario

If an L3VPN needs to span more than two ASs, you can configure inter-AS VPN Option B (spanning more than two ASs). On the network shown in [Figure 1](dc_vrp_mpls-l3vpn-v4_cfg_0052.html#EN-US_TASK_0172369323__fig_dc_vrp_mpls-l3vpn-v4_cfg_005201), the L3VPN needs to span three ASs to transmit VPN routes.

**Figure 1** Network diagram of inter-AS VPN Option B (spanning more than two ASs)  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_005201.png)

#### Pre-configuration Tasks

Before configuring inter-AS VPN Option B (spanning more than two ASs), complete the following tasks:

* Configure an IGP for the MPLS backbone network of each AS to ensure the IP connectivity of the backbone network in each AS. OSPF or IS-IS is used in most cases. Other protocols can also be used. .
* Configure basic MPLS capabilities and set up LDP LSPs or TE tunnels between MP-IBGP peers on the MPLS backbone network in each AS.
* [Configure a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) on each PE that connects to a CE and [bind the PE interface that connects to the CE to the VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Configure an IP address for the interface connecting a CE to a PE.


[Configuring MP-IBGP Between a PE and an ASBR in the Same AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0053.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between the PE and ASBR.

[Configuring MP-EBGP Between ASBRs in Different ASs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0054.html)

After an MP-EBGP peer relationship is established between ASBRs, an ASBR can advertise the VPNv4 routes of its AS to the other ASBR.

[Configuring MP-IBGP Between ASBRs in the Same AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0055.html)

After the MP-IBGP peer relationship is established between the ASBRs in the same AS, ASBRs can exchange VPNv4 routes.

[Configuring ASBRs Not to Filter VPNv4 Routes Based on VPN Targets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0134.html)

In inter-AS VPN Option B mode, ASBRs do not have VPN instances. If you want ASBRs to keep received VPNv4 routes, configure ASBRs not to filter VPNv4 routes based on VPN targets.

[(Optional) Configuring One-Label-per-Next-Hop Label Distribution on an ASBR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0173.html)

To conserve label resources on an ASBR, configure one-label-per-next-hop label allocation on the ASBR. One-label-per-next-hop label allocation on ASBRs and one-label-per-instance label distribution on PEs must be used together.

[(Optional) Using a Routing Policy to Control VPNv4 Routes on ASBRs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0163.html)

ASBRs can use a routing policy to filter undesired VPNv4 routes.

[Verifying the Configuration of Inter-AS VPN Option B (Spanning More Than Two ASs)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0058.html)

After configuring inter-AS VPN Option B (spanning more than two ASs), you can view the status of all BGP peer relationships and VPNv4 routing information on PEs or ASBRs.