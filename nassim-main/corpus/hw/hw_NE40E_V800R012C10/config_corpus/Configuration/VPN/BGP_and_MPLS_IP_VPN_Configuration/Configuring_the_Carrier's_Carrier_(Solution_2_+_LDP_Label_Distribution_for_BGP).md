Configuring the Carrier's Carrier (Solution 2 + LDP Label Distribution for BGP)
===============================================================================

After LDP LSPs are established for labeled BGP routes of the public network, IBGP peer relationships do not need to be established within the Level 2 carrier network, and the Level 2 carrier can provide BGP/MPLS IP VPN services.

#### Usage Scenario

If a BGP/MPLS IP VPN user is a service provider, who offers BGP/MPLS IP VPN services to its clients, the function of carrier's carrier can be applied. Compared with a basic BGP/MPLS IP VPN, the access of provider carrier CEs to provider carrier PEs is the key to the carrier's carrier model. [Table 1](#EN-US_TASK_0246668287__en-us_task_0246668281_table1414188793) describes how carrier's carrier is implemented.

**Table 1** Carrier's carrier solution
| Solution | Solution Between the Level 1 Carrier PE and Level 1 Carrier CE | Solution Between the Level 2 Carrier PE and Level 1 Carrier CE |
| --- | --- | --- |
| Solution 1 | IGP and LDP multi-instance are used to exchange routing information. | Use IGP and LDP to exchange routing information. |
| Solution 2 | Use IBGP to exchange labeled IPv4 VPN routes. | BGP label distribution solution: Establish IBGP peer relationships to establish complete public network tunnels between the PEs of the Level 2 carrier. |
| Use EBGP to exchange labeled IPv4 VPN routes. | LDP label distribution for BGP: No IBGP peer relationship is established. After the Level 2 carrier learns the labeled BGP routes of the public network from the Level 1 carrier's devices, the Level 2 carrier imports the BGP routes to the IGP protocol and triggers LDP to distribute labels for these routes. In this manner, a complete LDP LSP can be established between the PEs of the Level 2 carrier. |


This section describes solution 2, and LDP is used to distribute labels for BGP.


#### Pre-configuration Tasks

Before configuring the carrier's carrier, complete the following tasks:

* Configure an IGP for the Level 1 carrier's MPLS backbone network to implement the IP connectivity of the backbone network.
* Configure basic MPLS functions and MPLS LDP for the MPLS backbone network of the Level 1 carrier.
* Establish an MP-IBGP connection between the Level 1 carrier PEs.
* Configure an IGP for the Level 2 carrier's IP network or MPLS network to implement IP connectivity.
* Configure basic MPLS functions and LDP on the Level 2 carrier network and set up LSPs.


[Configuring a Level 1 Carrier CE to Access Level 1 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2036a.html)

When the Level 1 carrier and Level 2 carrier are in different ASs, the Level 2 carrier functions as the VPN user of the Level 1 carrier, the same as the CE of the PE in the basic BGP/MPLS IP VPN.

[Configuring a Level 2 Carrier CE to Access a Level 2 Carrier PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2037a.html)

In the Level 2 carrier networking, for the CE's access to a PE, you need to create a VPN instance on the Level 2 PE and configure a routing protocol between the PE and CE, the configuration of which is similar to the configuration in the basic BGP/MPLS IP VPN.

[Configuring External Route Exchanges Between Level 2 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2038a.html)

An MP-BGP peer relationship is established between Level 2 carrier PEs to exchange IPv4 VPN routes.

[Importing BGP routes to the IGP Routing Table](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2039a.html)

To enable LDP to allocate labels for BGP, you need first import BGP routes into the IGP routing table.

[Configuring LDP to Distribute Labels for the Labeled BGP Routes of the Public Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2040a.html)

By allocating labels for labeled BGP routes, you can establish LDP LSPs for labeled BGP routes in the Level 2 carrier's network.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2041a.html)

After configuring carrier's carrier, you can check information about public network routes on PEs and CEs of Level 1 and Level 2 carriers, VPN routes on the PEs, and LDP LSPs.