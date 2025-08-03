Configuring EVPN Carrier's Carrier (BGP Label Distribution)
===========================================================

Configuring_EVPN_Carrier's_Carrier_(BGP_Label_Distribution)

#### Usage Scenario

If a BGP/MPLS IP VPN user is a service provider, who offers BGP/MPLS IP VPN services to its clients, the function of carrier's carrier can be applied. Compared with a basic BGP/MPLS IP VPN, the access of provider carrier CEs to provider carrier PEs is the key to the carrier's carrier model. [Table 1](#EN-US_TASK_0000001214153135__en-us_task_0246668281_table1414188793) describes how carrier's carrier is implemented.

**Table 1** Carrier's carrier solution
| Solution | Solution Between the Level 1 Carrier PE and Level 1 Carrier CE | Solution Between the Level 2 Carrier PE and Level 1 Carrier CE |
| --- | --- | --- |
| Solution 1 | IGP and LDP multi-instance are used to exchange routing information. | Use IGP and LDP to exchange routing information. |
| Solution 2 | Use IBGP to exchange labeled IPv4 VPN routes. | BGP label distribution solution: Establish IBGP peer relationships to establish complete public network tunnels between the PEs of the Level 2 carrier. |
| Use EBGP to exchange labeled IPv4 VPN routes. | LDP label distribution for BGP: No IBGP peer relationship is established. After the Level 2 carrier learns the labeled BGP routes of the public network from the Level 1 carrier's devices, the Level 2 carrier imports the BGP routes to the IGP protocol and triggers LDP to distribute labels for these routes. In this manner, a complete LDP LSP can be established between the PEs of the Level 2 carrier. |


This section describes solution 2, and BGP is used to distribute labels.

Level 1 carrier CEs can access Level 1 carrier PEs in two modes: labeled route mode and labeled address family mode. Determine which mode to use based on actual needs.


#### Pre-configuration Tasks

Before configuring carrier's carrier, complete the following tasks:

* Configure an IGP for the Level 1 carrier's MPLS backbone network to ensure IP connectivity on the backbone network.
* Configure basic MPLS functions and MPLS LDP for the Level 1 carrier's MPLS backbone network.
* Establish EVPN IBGP peer relationships between Level 1 carrier's PEs.
* Configure an IGP for the Level 2 carrier's IP or MPLS network to ensure IP connectivity.
* Configure basic MPLS functions and LDP on the Level 2 carrier network and set up LSPs.


[Configuring Level 1 Carrier CEs Accessing Level 1 Carrier PEs (BGP Label Distribution, Labeled Route Mode)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_csc_0015.html)

If the Level 1 and Level 2 carriers are in different ASs, the Level 1 carrier takes the Level 2 carrier as its VPN user.

[Configuring Level 1 Carrier CEs Accessing Level 1 Carrier PEs (BGP Label Distribution, Labeled Address Family Mode)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_csc_0016.html)

If the Level 1 and Level 2 carriers are in different ASs, the Level 1 carrier takes the Level 2 carrier as its VPN user.

[Configuring Level 2 Carrier CEs to Access Level 2 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_csc_0017.html)

Similar to the configuration of CEs accessing PEs in a basic BGP/MPLS IP VPN scenario, you need to create a VPN instance on Level 2 carrier PEs and configure a routing protocol for these PEs to communicate with CEs.

[Configuring External Route Exchange Between Level 2 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_csc_0018.html)

An MP-BGP peer relationship is established between Level 2 carrier PEs to exchange IPv4 VPN routes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_csc_0019.html)

After carrier's carrier is configured, you can view information about public network routes on Level 1 and Level 2 carriers' PEs and CEs and VPN routes on their PEs.