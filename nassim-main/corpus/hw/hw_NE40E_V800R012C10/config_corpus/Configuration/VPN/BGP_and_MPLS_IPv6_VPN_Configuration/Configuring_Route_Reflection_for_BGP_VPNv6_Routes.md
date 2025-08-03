Configuring Route Reflection for BGP VPNv6 Routes
=================================================

Using a BGP VPNv6 RR can reduce the number of MP-IBGP connections between PEs. The RR not only reduces the burden on PEs, but also facilitates network maintenance and management.

#### Usage Scenario

A BGP speaker does not advertise the routes learned from an IBGP peer to other IBGP peers. To enable a PE to advertise the routes of the VPN that the PE accesses to the BGP-VPNv6 peers in the same AS with the PE so that the PE can directly exchange IPv6 VPN routing information with the peers, the PE must establish IBGP connections with all these peers. In other words, MP-IBGP peers must be fully meshed. If there are n PEs (including ASBRs) in an AS, n x (n â 1)/2 MP-IBGP peer relationships need to be established. A large number of IBGP peers consume a great number of network resources.

To resolve this issue, use an RR to reflect routes. In an AS, one device serves as an RR to reflect VPNv6 routes; the other PEs and ASBRs serve as RR clients. An RR can be a P, PE, ASBR, or other type of device.


#### Pre-configuration Tasks

Before configuring route reflection to optimize the VPN backbone layer, complete the following tasks:

* Configure a routing protocol on the MPLS backbone network for IP connectivity.
* Establish LSPs or MPLS TE tunnels between the RR and all PEs serving as clients.
* Configure the extended community attribute if a reflection policy needs to be applied to VPNv6 routes.


[Configuring a Client PE to Establish an MP-IBGP Peer Relationship with the RR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2015.html)

You can configure a PE to establish an MP-IBGP peer relationship with an RR so that the PE can receive VPNv6 routes reflected by the RR.

[Configuring an RR to Establish MP-IBGP Peer Relationships with All Client PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2016.html)

You can configure an RR to establish MP-IBGP connections with all its client PEs to reflect VPNv6 routes.

[Establishing Route Reflection for BGP VPNv6 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2017.html)

This section describes how to configure route reflection for BGP VPNv6 routes so that the RR can reflect the VPNv6 routes received from a client PE to other client PEs.

[Verifying the Configuration of Route Reflection for BGP VPNv6 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2018.html)

After configuring route reflection for BGP VPNv6 routes, check information about VPNv6 peers and VPNv6 routes on the RR or its client PEs.