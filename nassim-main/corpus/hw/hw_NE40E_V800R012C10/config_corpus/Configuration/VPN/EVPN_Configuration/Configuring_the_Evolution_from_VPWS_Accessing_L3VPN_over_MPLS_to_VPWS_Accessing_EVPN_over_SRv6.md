Configuring the Evolution from VPWS Accessing L3VPN over MPLS to VPWS Accessing EVPN over SRv6
==============================================================================================

EVPN over SRv6 is today's mainstream transport solution for 5G services. To prevent live network services from being affected, a new transport solution must be deployed based on these services. When there are a large number of VPWS accessing L3VPN over MPLS services on the live network, you need to evolve VPWS accessing L3VPN over MPLS to VPWS accessing EVPN over SRv6.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0288152680__fig1778318276461), before the evolution is achieved, traditional VPWS services are transmitted from each CSG (CSG1 and CSG2) to ASG1 and ASG2; L3VPN over MPLS services are transmitted from each ASG (ASG1 and ASG2) to RSG1 and RSG2. On ASG1 and ASG2, the approach of L2VE interfaces accessing L3VE interfaces is used to implement the Layer 2 accessing Layer 3 mode. After the evolution is achieved, traditional VPWS services are still transmitted from each CSG (CSG1 and CSG2) to ASG1 and ASG2; EVPN L3VPN over SRv6 services are transmitted from each ASG (ASG1 and ASG2) to RSG1 and RSG2. On ASG1 and ASG2, L2VE interfaces are connected to L3VE interfaces to implement the Layer 2 accessing Layer 3 mode.

RRs are deployed on the network. During the evolution, SRv6-based BGP EVPN peer relationships and MPLS-based VPNv4 or VPNv6 peer relationships exist between RRs and ASGs and between RRs and RSGs. In this case, you need to configure RRs, ASGs, and RSGs to evolve VPWS accessing L3VPN over MPLS to VPWS accessing EVPN over SRv6.

The evolution solution can be implemented in either of the following modes:

* Dual-stack protocol coexistence mode: The core idea of this mode is that during the evolution, priority-based route selection is used to enable ASGs and RSGs to preferentially select SRv6 EVPN routes. Configure a route-policy on the RRs to filter out VPNv4 or VPNv6 routes. After the evolution is complete, delete all BGP VPNv4 or VPNv6 peer relationships.
* Route regeneration mode: The core idea of this mode is that during the evolution, route regeneration is configured on RSGs to regenerate routes received from VPNv4 or VPNv6 peers as EVPN routes and reflect the EVPN routes to the ASGs through RRs. Then, priority-based route selection is performed on the ASGs to preferentially select SRv6 EVPN routes. After the evolution is complete, all BGP VPNv4 or VPNv6 peer relationships are deleted.

**Figure 1** Evolution from VPWS accessing L3VPN over MPLS to VPWS accessing EVPN over SRv6  
![](figure/en-us_image_0288282177.png)

#### Pre-configuration Tasks

Before configuring evolution from VPWS accessing L3VPN over MPLS to VPWS accessing EVPN over SRv6, complete the following tasks:

* Complete the task of [Configuring LDP VPWS](dc_vrp_vpws_cfg_3004.html) between CSGs and ASGs.
* Complete the task of [Configuring a Basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html) or [Configuring a Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html) between the ASGs and RSGs.
* Complete the task of [Configuring EVPN L3VPN over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0252.html), [Configuring EVPN L3VPNv4 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpn_over_srv6-te_policy.html), or [Configuring EVPN L3VPNv6 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpnv6_over_srv6-te_policy.html) between the ASGs and RSGs. The VPN instance used in this task is the same as the traditional L3VPN instance used in the previous task. The difference is that VPN targets need to be set for EVPN routes of the VPN instance in this task.
* [Configure VPWS accessing L3VPN](dc_vrp_l2-l3_cfg_5003.html) on the ASGs.


[Configuring Dual-Stack Protocol-based Evolution](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_dianxinyanjin_02.html)

Configure dual-stack protocol-based evolution so that VPWS accessing L3VPN over MPLS can evolve to VPWS accessing EVPN over SRv6 when IPv4 and IPv6 networks coexist.

[Configuring Route Re-origination-based Evolution](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_dianxinyanjin_03.html)

Configure route re-origination-based evolution to gradually switch traffic to SRv6 EVPN routes, so that VPWS accessing L3VPN over MPLS can evolve to VPWS accessing EVPN over SRv6.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_dianxinyanjin_04.html)

After the evolution from VPWS accessing L3VPN over MPLS to VPWS accessing EVPN over SRv6, you can check EVPN IP prefix route information on the ASGs and RSGs.