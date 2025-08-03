Configuring the Carrier's Carrier (Solution 1)
==============================================

Configuring the Carrier's Carrier (Solution 1)

#### Usage Scenario

If a BGP/MPLS IP VPN user is a service provider, who offers BGP/MPLS IP VPN services to its clients, the function of carrier's carrier can be applied. Compared with a basic BGP/MPLS IP VPN, the access of provider carrier CEs to provider carrier PEs is the key to the carrier's carrier model. [Table 1](#EN-US_TASK_0246668281__table1414188793) describes how carrier's carrier is implemented.

**Table 1** Carrier's carrier solution
| Solution | Solution Between the Level 1 Carrier PE and Level 1 Carrier CE | Solution Between the Level 2 Carrier PE and Level 1 Carrier CE |
| --- | --- | --- |
| Solution 1 | IGP and LDP multi-instance are used to exchange routing information. | Use IGP and LDP to exchange routing information. |
| Solution 2 | Use IBGP to exchange labeled IPv4 VPN routes. | BGP label distribution solution: Establish IBGP peer relationships to establish complete public network tunnels between the PEs of the Level 2 carrier. |
| Use EBGP to exchange labeled IPv4 VPN routes. | LDP label distribution for BGP: No IBGP peer relationship is established. After the Level 2 carrier learns the labeled BGP routes of the public network from the Level 1 carrier's devices, the Level 2 carrier imports the BGP routes to the IGP protocol and triggers LDP to distribute labels for these routes. In this manner, a complete LDP LSP can be established between the PEs of the Level 2 carrier. |


This section describes solution 1, that is, the LDP multi-instance solution.


#### Pre-configuration Tasks

Before configuring the carrier's carrier, complete the following tasks:

* Configure IGP on the Level 1 carrier's MPLS backbone network for IP connectivity on the network.
* Configure basic MPLS functions and MPLS LDP for the Level 1 carrier's MPLS backbone network.
* Establish an MP-IBGP connection between the Level 1 carrier PEs.
* Configure IGP on the Level 2 carrier's IP network or MPLS network for IP connectivity.
* Configure basic MPLS functions and LDP on the Level 2 carrier network and set up LSPs.


[Configuring the Level 1 Carrier CE to Access the Level 1 Carrier PE (Using LDP Multi-Instance)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2030a.html)

When the Level 1 carrier and Level 2 carrier are in the same AS, the Level 1 carrier takes the Level 2 carrier as its VPN user.

[Configuring a Level 2 Carrier CE to Access a Level 2 Carrier PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2032a.html)

In the Level 2 carrier networking, for the CE's access to a PE, you need to create a VPN instance on the Level 2 PE and configure a routing protocol between the PE and CE, the configuration of which is similar to the configuration in the basic BGP/MPLS IP VPN.

[Configuring the External Route Exchange Between Level 2 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2033a.html)

An MP-BGP peer relationship is established between Level 2 carrier PEs to exchange IPv4 VPN routes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2034a.html)

After carrier's carrier is configured, you can check information about public network routes and VPN routes on PEs and CEs of the Level 2 carrier and Level 1 carrier.