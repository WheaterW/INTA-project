Configuring Inter-AS VPN Option B (Basic Networking)
====================================================

In scenarios where the backbone network spans two ASs, ASBRs need to advertise VPN IPv4 routes through MP-EBGP.

#### Usage Scenario

If ASBRs can manage VPN routes but there are insufficient interfaces available for the dedicated use of all inter-AS VPNs, you can use inter-AS VPN Option B. This solution eliminates the need to create VPN instances on ASBRs, but requires ASBRs to maintain and advertise VPNv4 routes. In the basic networking of inter-AS VPN Option B, ASBRs cannot play other roles, such as PE and RR roles, and no RR is required in each AS.

On the network shown in [Figure 1](dc_vrp_mpls-l3vpn-v4_cfg_0029.html#EN-US_TASK_0172369288__fig_dc_vrp_mpls-l3vpn-v4_cfg_002902), the connected interfaces between ASBRs do not need to be bound to the VPN. A single-hop MP-EBGP peer relationship is set up between the ASBRs to transmit all inter-AS VPN routes.

**Figure 1** Inter-AS VPN Option B (basic networking)  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_002902.png)

#### Pre-configuration Tasks

Before configuring inter-AS VPN Option B, complete the following tasks:

* Configure an IGP for the MPLS backbone network of each AS to ensure the IP connectivity of the backbone network in each AS.
* Configure basic MPLS capabilities and set up LDP LSPs or TE tunnels between MP-IBGP peers on the MPLS backbone network in each AS.
* [Configure a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) on each PE that connects to a CE and [bind the PE interface that connects to the CE to the VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Configure an IP address for each CE interface that connects to a PE.


[Configuring MP-IBGP Between a PE and an ASBR in the Same AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0030.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between the PE and ASBR.

[Configuring MP-EBGP Between ASBRs in Different ASs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0031.html)

After an MP-EBGP peer relationship is established between ASBRs, an ASBR can advertise the VPNv4 routes of its AS to the other ASBR.

[Configuring ASBRs Not to Filter VPNv4 Routes Based on VPN Targets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0057.html)

In inter-AS VPN Option B mode, ASBRs do not have VPN instances. If you want ASBRs to keep received VPNv4 routes, configure ASBRs not to filter VPNv4 routes based on VPN targets.

[(Optional) Using a Route-Policy to Control VPNv4 Routes on ASBRs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0160.html)

ASBRs can use a route-policy to filter undesired VPNv4 routes.

[Configuring Route Exchange Between a CE and a PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0033.html)

BGP, an IGP, or a static route (including the default route) can run between a CE and a PE. You can choose any of them as required.

[Verifying the Configuration of Inter-AS VPN Option B (Basic Networking)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0034.html)

After configuring inter-AS VPN Option B (basic networking), check the status of all BGP peer relationships and VPNv4 routing information on PEs or ASBRs.