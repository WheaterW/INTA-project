Configuring Carrier's Carrier in the Labeled-Unicast Address Family (BGP Label Distribution Using LDP)
======================================================================================================

After LDP LSPs are established for labeled public network BGP routes, the Level 2 carrier can provide BGP/MPLS IP VPN services without the need to establish IBGP peer relationships within its network. This section describes how to use the labeled-unicast address family (also known as the BGP-labeled or BGP-labeled-VPN instance IPv4 address family) to configure inter-AS BGP LSPs for carrier's carrier.

#### Usage Scenario

If a BGP/MPLS IP VPN user is a service provider, who offers BGP/MPLS IP VPN services to its clients, the function of carrier's carrier can be applied.

Two solutions can be adopted to realize carrier's carrier:

* BGP label distribution: An IBGP peer relationship is established between a Level 1 carrier CE and a Level 2 carrier PE to establish a complete public network tunnel between the Level 2 carrier PEs.
* LDP label distribution for BGP: No IBGP peer relationship is established between a Level 1 carrier CE and a Level 2 carrier PE. After learning labeled BGP routes of the public network from the Level 1 carrier, the Level 2 carrier can import these BGP routes to the IGP routing table and use LDP to distribute labels for these routes. In this manner, a complete LDP LSP can be established between Level 2 carrier PEs.

This section describes how LDP distributes labels for BGP. In this solution, a BGP peer relationship is established in a BGP-labeled address family or BGP-labeled-VPN instance IPv4 address family so that the BGP peers can advertise BGP-labeled routes to each other, allowing BGP LSPs to be set up between the BGP peers.


#### Pre-configuration Tasks

Before configuring the carrier's carrier, complete the following tasks:

* Configure an IGP for the Level 1 carrier's MPLS backbone network to implement the IP connectivity of the backbone network.
* Configure basic MPLS functions and MPLS LDP for the Level 1 carrier's MPLS backbone network.
* Establish an MP-IBGP connection between Level 1 carrier PEs.
* Configure an IGP for the Level 2 carrier's IP network or MPLS network to implement IP connectivity.
* Configure basic MPLS functions and MPLS LDP for the network of the Level 2 carrier and establish LSPs if the Level 2 carrier provides BGP/MPLS IP VPN services.


[Configuring a Level 1 Carrier CE to Access Level 1 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2053.html)

When Level 1 and Level 2 carriers are in different ASs, the Level 2 carrier functions as the VPN user of the Level 1 carrier, the scenario of which is the same as that the CE's access to the PE in the basic BGP/MPLS IP VPN.

[Configuring the Level 2 Carrier's Clients to Access the Level 2 Carrier's PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2054.html)

In the Level 2 carrier networking, for the CE's access to a PE, you need to create a VPN instance on the Level 2 PE and configure a routing protocol between the PE and CE, the configuration of which is similar to the configuration in the basic BGP/MPLS IP VPN.

[Configuring External Route Exchanges Between Level 2 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2055.html)

The MP-BGP peer relationship is established between PEs of the Level 2 carrier to exchange IPv4 VPN routes.

[Importing BGP routes to the IGP Routing Table](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2056.html)

To enable LDP to allocate labels for BGP, you need first import BGP routes to the relevant IGP routing table.

[Configuring LDP to Distribute Labels for the Labeled BGP Routes of the Public Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2057.html)

By allocating labels for labeled BGP routes, you can establish LDP LSPs for labeled BGP routes in the Level 2 carrier' network.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2058.html)

After configuring carrier's carrier, you can check information about public network routes on PEs and CEs of Level 1 and Level 2 carriers, VPN routes on the PEs, and LDP LSPs.