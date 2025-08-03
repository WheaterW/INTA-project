Configuring Inter-AS VPN Option B (ASBR Also Functioning as a PE)
=================================================================

In a scenario in which the backbone network spans two ASs,
ASBRs need to advertise VPNv4 routes through MP-EBGP and ASBRs also
need to function as PEs.

#### Usage Scenario

If an ASBR can manage VPN
routes and the ASBR also functions as a PE for CE access, you can
configure inter-AS VPN Option B (ASBR also functioning as a PE). This
mode requires ASBRs to help to maintain and advertise not only the
VPNv4 routes of its own VPN instances but also the VPNv4 routes of
other VPN instances.


#### Pre-configuration Tasks

Before configuring
inter-AS VPN Option B (ASBR also functioning as a PE), complete the
following tasks:

* Configure an IGP for the MPLS backbone network of each AS to
  ensure IP connectivity of the backbone network in each AS.
* Configure MPLS both globally and per interface on each node
  of the MPLS backbone network in each AS and establish an LDP LSP or
  TE tunnel between MP-IBGP peers.
* [Configure a VPN instance on each PE](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) and [bind the interface that connects
  a PE to a CE to the VPN instance on that PE](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Configure an IP address for the interface connecting a CE to
  a PE.


[Configuring MP-IBGP Between a PE and an ASBR in the Same AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0036.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between the PE and ASBR.

[Configuring MP-EBGP Between ASBRs in Different ASs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0037.html)

After an MP-EBGP peer relationship is established between ASBRs, ASBRs can exchange VPNv4 routes.

[Configuring ASBRs Not to Filter VPNv4 Routes Based on VPN Targets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0132.html)

In inter-AS VPN Option B mode, ASBRs do not have VPN instances. If you want ASBRs to keep received VPNv4 routes, configure ASBRs not to filter VPNv4 routes based on VPN targets.

[(Optional) Using a Routing Policy to Control VPNv4 Routes on ASBRs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0161.html)

ASBRs can use a routing policy to filter undesired VPNv4 routes.

[(Optional) Configuring One-Label-per-Next-Hop Label Distribution on an ASBR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0171.html)

To conserve label resources on an ASBR, configure one-label-per-next-hop label allocation on the ASBR. One-label-per-next-hop label allocation on ASBRs and one-label-per-instance label distribution on PEs must be used together.

[Configuring a VPN Instance on an ASBR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0038.html)

If an ASBR also functions as a PE, you need to configure a VPN instance enabled with the IPv4 address family on the ASBR to manage VPN routes.

[Configuring Route Exchange Between a CE and an ASBR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0039.html)

The configuration of route exchange between a CE and an ASBR is similar to the configuration of route exchange between a CE and a PE on a basic BGP/MPLS IP VPN.

[Configuring Route Exchange Between a CE and a PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0040.html)

BGP, an IGP, or a static route (including the default route) can run between a CE and a PE. You can choose any of them as required.

[Verifying the Configuration of Inter-AS VPN Option B (ASBR Also Functioning as a PE)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0041.html)

After configuring inter-AS VPN Option B (ASBR also functioning as a PE), check the status of all BGP peer relationships and VPNv4 routing information on PEs or ASBRs.