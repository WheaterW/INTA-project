Configuring Carrier's Carrier in the Labeled-Unicast Address Family (BGP Label Distribution Solution)
=====================================================================================================

In carrier's carrier networking, the user of the carrier providing BGP/MPLS IP VPN services is also a carrier that provides BGP/MPLS IP VPN services. This section describes how to use the labeled-unicast address family (also known as the BGP-labeled or BGP-labeled-VPN instance IPv4 address family) to configure inter-AS BGP LSPs for carrier's carrier.

#### Usage Scenario

If a BGP/MPLS IP VPN user is a service provider, who offers BGP/MPLS IP VPN services to its clients, the function of carrier's carrier can be applied.

Two solutions can be adopted to realize carrier's carrier:

* BGP label distribution: An IBGP peer relationship is established between a Level 1 carrier CE and a Level 2 carrier PE to establish a complete public network tunnel between the Level 2 carrier PEs.
* LDP label distribution for BGP: No IBGP peer relationship is established between a Level 1 carrier CE and a Level 2 carrier PE. After learning labeled BGP routes of the public network from the Level 1 carrier, the Level 2 carrier can import these BGP routes to the IGP routing table and use LDP to distribute labels for these routes. In this manner, a complete LDP LSP can be established between Level 2 carrier PEs.

This section describes the BGP label distribution solution. In this solution, a BGP peer relationship is established in a BGP-labeled address family or BGP-labeled-VPN instance IPv4 address family so that the BGP peers can advertise BGP-labeled routes to each other, allowing BGP LSPs to be set up between the BGP peers.


#### Pre-configuration Tasks

Before configuring the carrier's carrier, complete the following tasks:

* Configure an IGP for the Level 1 carrier's MPLS backbone network to implement the IP connectivity of the backbone network.
* Configure basic MPLS functions and MPLS LDP for the Level 1 carrier's MPLS backbone network.
* Establish an MP-IBGP connection between Level 1 carrier PEs.
* Configure an IGP for the Level 2 carrier's IP network or MPLS network to implement IP connectivity.
* Configure basic MPLS functions and MPLS LDP for the network of the Level 2 carrier and establish LSPs if the Level 2 carrier provides BGP/MPLS IP VPN services.


[Configuring a Level 1 Carrier CE to Access Level 1 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2048.html)

When the Level 1 carrier and Level 2 carrier are in different ASs, the Level 1 carrier takes the Level 2 carrier as its VPN user.

[Configuring a Level 2 Carrier CE to Access a Level 2 Carrier PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2049.html)

In the Level 2 carrier networking, for the CE's access to a PE, you need to create a VPN instance on the Level 2 PE and configure a routing protocol between the PE and CE, the configuration of which is similar to the configuration in the basic BGP/MPLS IP VPN.

[Configuring External Route Exchanges Between Level 2 Carrier's PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2050.html)

An MP-BGP peer relationship is established between PEs of the Level 2 carrier to exchange IPv4 VPN routes.

[Verifying the Configuration of Carrier's Carrier in an Independent Labeled Address Family (Solution 1)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2051.html)

After configuring carrier's carrier, you can view information about public network routes on PEs and CEs of carriers with different levels, and VPN routes on the PEs.