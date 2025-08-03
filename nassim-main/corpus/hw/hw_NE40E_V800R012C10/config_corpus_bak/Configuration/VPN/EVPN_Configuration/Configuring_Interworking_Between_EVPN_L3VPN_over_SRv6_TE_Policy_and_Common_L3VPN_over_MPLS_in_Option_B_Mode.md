Configuring Interworking Between EVPN L3VPN over SRv6 TE Policy and Common L3VPN over MPLS in Option B Mode
===========================================================================================================

During network evolution, EVPN L3VPN over SRv6 TE Policy and common L3VPN over MPLS may coexist. To allow these two types of networks to communicate, perform this task.

#### Usage Scenario

EVPN L3VPN is deployed on the SRv6 network, and traditional VPN is deployed on the traditional MPLS network (metro network). These two types of networks need to communicate in Option B mode.

**Figure 1** Interworking between EVPN L3VPN over SRv6 TE Policy and L3VPN over MPLS in Option B mode  
![](figure/en-us_image_0000001232368971.png)

#### Pre-configuration Tasks

Before configuring interworking between EVPN L3VPN over SRv6 TE Policy and L3VPN over MPLS in Option B mode, complete the following tasks:

* Configure basic MPLS functions on PE2 and the ASBR.
* Configure an IGP on PE1, PE2, and the ASBR to ensure route reachability.

* Configure [EVPN L3VPN over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpn_over_srv6-te_policy_copy.html) or [EVPN L3VPNv6 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpnv6_over_srv6-te_policy_copy.html) on the network where PE1 and the ASBR reside.
* Configure a basic BGP/MPLS IP VPN or BGP/MPLS IPv6 VPN on the network where PE2 and the ASBR reside. For details, see [Configuring a Basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html) or [Configuring a Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html).


[Configuring Route Import Across Address Families](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0180.html)

In the BGP VPNv4/v6 address family, import remote EVPN IP prefix routes to generate VPNv4/v6 routes. In the EVPN address family, import remote VPNv4/v6 routes to generate EVPN IP prefix routes. Apply for SIDs in one-SID-per-route or one-SID-per-next-hop mode, so that traffic can be exchanged between the EVPN side and VPNv4/v6 side.

[Configuring a Tunnel Selector](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0182.html)

EVPN public network routes recurse to IP tunnels based on next hops by default. To enable EVPN public network routes to recurse to SRv6 TE Policy next hops, deploy a tunnel selector for route matching.

[(Optional) Enabling ECMP or FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0183.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0184.html)

After configuring EVPN L3VPN over SRv6 TE Policy and L3VPN over MPLS to interwork in Option B mode, check information about all BGP peer relationships, EVPN routes on PEs or ASBRs, and BGP VPNv4/v6 routes on PEs or ASBRs.