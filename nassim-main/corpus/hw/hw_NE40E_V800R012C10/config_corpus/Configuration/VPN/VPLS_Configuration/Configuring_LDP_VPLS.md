Configuring LDP VPLS
====================

Based on MPLS and Ethernet technologies, VPLS is an L2VPN
technology that is used to implement point-to-multipoint VPN networking.
VPLS is better than both the earlier point-to-point L2VPN services
and Layer 3 virtual private network (L3VPN) services requiring carriers
to manage the routing information.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172370092__fig_dc_vrp_vpls_cfg_500301), if
PEs support the usage of LDP as VPLS signaling, you can configure
LDP VPLS.

PEs are fully meshed using PWs and use split horizon
to prevent loops in packet forwarding. A PE forwards packets, including
unicast packets, unknown unicast packets, multicast packets, and broadcast
packets, received from a PW to only the connected CE rather than to
other PEs.

All the PEs need to set up LDP sessions with each
other for signaling negotiation of PWs. Packets from CEs are sent
to the VPLS network through AC interfaces on PEs.

**Figure 1** VPLS network
  
![](images/fig_dc_vrp_vpls_cfg_500301.png)  



#### Pre-configuration Tasks

Before configuring
LDP VPLS, complete the following tasks:

* Configure interface IP addresses of PEs and Ps and configure
  IGP routes.
* Configure LSR IDs, enable MPLS and MPLS LDP, and establish
  LDP sessions.
* (Optional) Set up remote MPLS LDP sessions if PEs are not directly
  connected.
* Enable MPLS L2VPN on PEs.
* Establish tunnels between PEs for data transmission.


[Creating a VSI and Configuring LDP Signaling](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5004.html)

Configuring VSI IDs and peer IP addresses is mandatory for LDP VPLS services. VSI IDs are used to identify VSIs in PW signaling negotiation. Perform the following steps on the endpoint PEs of a PW.

[Binding an AC Interface to a VSI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5005.html)

The view in which an AC interface is bound to a VSI depends on the type of link between the PE and CE.

[(Optional) Configuring Flow Label-based Load Balancing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5074.html)

After flow label-based load balancing is configured for an L2VPN, L2VPN services can be classified by flow label and forwarding paths can be selected based on these flow labels, improving forwarding efficiency.

[(Optional) Configuring VSIs to Ignore AC Status](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5006.html)

If the services running on a legacy network need to switch to a new network, you can configure VSIs to ignore AC status.

[Configuring Sub-interface-based Traffic Suppression](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_traff-supress_cfg_5005_copy.html)

This section describes how to configure sub-interface-based traffic suppression in order to reduce the traffic burden on a network.

[(Optional) Enabling VPLS LDP Fast Switch](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_vpls_cfg_5012_1.html)

In LDP FRR scenarios or scenarios where two LDP LSPs work in load-balancing mode, you can enable VPLS LDP fast switch to accelerate unicast convergence.

[(Optional) Configuring BFD for VPLS PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6057.html)

After a PW is configured for a VPLS using LDP as signaling, BFD can be configured to monitor the primary PW so that traffic can be immediately switched to the secondary PW in case of a primary PW fault.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5008.html)

After configuring LDP VPLS, check information about local VSIs, remote VSIs, VPLS connections, outbound interfaces of VSI PWs, and tunnel policies applied to VSIs.