Configuring Carrier's Carrier
=============================

In the networking of carrier's carrier, the Level 2 carrier provides BGP/MPLS IPv6 VPN services for its users.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_CONCEPT_0172369657__fig1902052195316), if the BGP/MPLS IPv6 VPN users are also service providers, who provide BGP/MPLS IPv6 VPN services for their customers, you can use the carrier's carrier configuration.

In this situation:

* The Level 1 carrier network is the IPv4 network.
* The Level 2 carrier network is the IPv4 network.
* The users of the Level 2 carrier network are the IPv6 network.

**Figure 1** Carrier's carrier networking  
![](figure/en-us_image_0236500415.png)

#### Pre-configuration Tasks

Before configuring the carrier's carrier, complete the following tasks:

* Configure an IGP for the Level 1 carrier's MPLS backbone network to implement the IP connectivity of the backbone network.
* Configure the basic MPLS capacity and the LDP for the Level 1 carrier's MPLS backbone network and establish the LSP.
* Establish the MP-IBGP connection between the Level 1 carrier PEs.
* Configure an IGP for the Level 2 carrier's IP network or MPLS network to the IP connectivity.
* Configure the basic MPLS capacity and LDP for the Level 2 carrier network and establish the LSP if the Level 2 carrier provides the BGP/MPLS IPv6 VPN services.


[Configuring Level 1 Carrier CE to Access the Level 1 Carrier PE (Intra-AS)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2105.html)

If the Level 1 carrier and the Level 2 carrier are in the same AS, the Level 1 carrier takes the Level 2 carrier as its VPN user. The configuration of carrier's carrier is similar to the configuration of CE accessing PE in the basic BGP/MPLS IP VPN.

[Configuring Level 1 Carrier CE to Access Level 1 Carrier PE (Inter-AS)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2106.html)

If the Level 1 carrier and the Level 2 carrier are in different ASs, the Level 1 carrier takes the Level 2 carrier as its VPN user, and the configuration of carrier's carrier is similar to the configuration of CE accessing PE in the basic BGP/MPLS IP VPN.

[Configuring the Level 2 Carrier's Customer to Access the Level 2 Carrier PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2108.html)

The Level 2 carrier provides IPv6 VPN services for its users, and the configuration of the Level 2 carrier is similar to the configuration of CE accessing PE in the basic BGP/MPLS IPv6 VPN.

[Configuring External Route Exchanges Between Level 2 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2107.html)

This section describes how to configure the MP-BGP peer relationship between PEs to exchange VPNv6 routes.

[Checking the Configurations of Carrier's Carrier](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2109.html)

After carrier's carrier is configured, you can view information about public network routes and VPN routes on PEs and CEs of the Level 2 carrier and Level 1 carrier.