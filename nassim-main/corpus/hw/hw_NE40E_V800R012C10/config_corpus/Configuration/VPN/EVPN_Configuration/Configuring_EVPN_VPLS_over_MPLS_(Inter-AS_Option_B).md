Configuring EVPN VPLS over MPLS (Inter-AS Option B)
===================================================

In a scenario in which the backbone network spans two ASs, ASBRs need to advertise BGP-EVPN routes through MP-EBGP.

#### Usage Scenario

If an ASBR can manage BGP-EVPN routes but there are not enough interfaces for all inter-AS EVPNs, EVPN VPLS over MPLS (inter-AS Option B) can be used. This solution requires ASBRs to help maintain and advertise EVPN routes, but these devices do not need to have EVPN instances. In the basic networking of inter-AS EVPN Option B, an ASBR cannot play other roles, such as the PE or RR, and an RR is not required in each AS.

On the network shown [Figure 1](#EN-US_TASK_0172370542__fig_dc_vrp_mpls-l3vpn-v4_cfg_002902), the interfaces connected between ASBRs do not need to be bound to the EVPN. A single-hop MP-EBGP peer relationship is set up between the ASBRs to transmit all inter-AS EVPN route information.

**Figure 1** EVPN VPLS over MPLS (inter-AS Option B) networking  
![](images/fig_evpn_mpls_optionB_01.png)

#### Pre-configuration Tasks

Before configuring EVPN VPLS over MPLS (inter-AS Option B), complete the following tasks:

* Configure an IGP for the MPLS backbone network of each AS to ensure IP connectivity of the backbone network in each AS.
* Configure MPLS and MPLS LDP both globally and per interface on each node of the MPLS backbone network in each AS and establish an LDP LSP or TE tunnel between IBGP peers.
* Configure [an EVPN instance](dc_vrp_evpn_cfg_0004.html) on the PE connected to the CE.
* Configure [the EVPN source address](dc_vrp_evpn_cfg_0012.html) on the PE connected to the CE.
* Configure [binding between the EVPN instance and interface](dc_vrp_evpn_cfg_0005.html) on the PE connected to the CE.
* Configure the IP addresses, through which the CEs access the PEs, on the CEs.


[Configuring MP-IBGP Between a PE and an ASBR in the Same AS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0030.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise EVPN routes between the PE and ASBR.

[Configuring MP-EBGP Between ASBRs in Different ASs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0031.html)

After an MP-EBGP peer relationship is established between ASBRs, an ASBR can advertise the EVPN routes of its AS to the other ASBR.

[Configuring ASBRs Not to Filter EVPN Routes Based on VPN Targets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0032.html)

In inter-AS EVPN Option B mode, ASBRs do not have EVPN instances. If you want ASBRs to keep received EVPN routes, configure ASBRs not to filter EVPN routes based on VPN targets.

[(Optional) Configuring One-Label-per-Next-Hop Label Distribution](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0033.html)

To save label resources on an ASBR, configure one-label-per-next-hop label allocation on the ASBR. One-label-per-next-hop label allocation on ASBRs and one-label-per-instance label distribution on PEs must be used together.

[(Optional) Configuring the Protection Switching Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0035.html)

A protection switching function, such as link or node protection, can be configured to provide high availability for an inter-AS EVPN Option B network.

[(Optional) Configuring BGP-EVPN Route Reflection on an ASBR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0036.html)

When multiple PEs exist in the ASs, you can configure an ASBR as an RR to lower configuration complexity.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0034.html)

After configuring EVPN VPLS over MPLS (inter-AS Option B), verify the status of all BGP peer relationships and EVPN routing information on PEs or ASBRs.