Configuring Inter-AS IPv6 VPN Option B
======================================

In the scenario where the backbone network spans two ASs, ASBRs need to advertise VPNv6 routes through MP-EBGP.

#### Usage Scenario

If an ASBR can manage VPN routes but there are not enough interfaces for all inter-AS VPNs, inter-AS VPN Option B can be used. Inter-AS VPN Option B requires ASBRs to help to maintain and advertise VPNv6 routes and you need not create VPN instances on the ASBRs.

On the network shown in [Figure 1](#EN-US_TASK_0172369631__fig_dc_vrp_mpls-l3vpn-v6_cfg_205101), the interfaces connected between ASBRs do not need to be bound to the VPN. A single-hop MP-EBGP peer relationship is set up between the ASBRs to transmit all inter-AS VPN routing information.

**Figure 1** Schematic diagram for inter-AS IPv6 VPN Option B
  
![](images/fig_dc_vrp_mpls-l3vpn-v6_cfg_205101.png)

#### Pre-configuration Tasks

Before configuring inter-AS VPN Option B, complete the following tasks:

* Configure an IGP for the MPLS backbone network of each AS to ensure IP connectivity of the backbone network within an AS.
* Configure the basic MPLS functions for the MPLS backbone network of each AS and establish an LDP LSP or TE tunnel between MP-IBGP peers.
* [Configure a VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2058.html) on the PE connected to the CE and [binding interfaces to the VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2059.html).
* Configure an IPv6 address for the interface connecting the CE to the PE.


[Configuring MP-IBGP Between a PE and an ASBR in the Same AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2052.html)

By importing extended community attributes to BGP, MP-IBGP can advertise VPNv6 routes between the PE and the ASBR.

[Configuring MP-EBGP Between ASBRs in Different ASs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2053.html)

After the MP-EBGP peer relationship is established between ASBRs, an ASBR can advertise the VPNv6 routes of its AS to the other ASBR.

[Controlling the Learning and Advertising of VPN Routes on ASBR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2054.html)

An ASBR can either save partial VPNv6 routes by filtering VPN targets through a routing policy or save all VPNv6 routes.

[(Optional) Configuring One-Label-per-Next-Hop Label Distribution on an ASBR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2099.html)

To conserve label resources on an ASBR, configure one-label-per-next-hop label allocation on the ASBR. One-label-per-next-hop label allocation on ASBRs and one-label-per-instance label distribution on PEs must be used together.

[Configuring Route Exchange Between a CE and a PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2055.html)

BGP, the static route (including the default route), or IGP can run between a CE and a PE. You can choose any of them as required.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2056.html)

After configuring inter-AS IPv6 VPN Option B, you can view the status of all BGP peer relationships and VPNv6 routing information on PEs or ASBRs.