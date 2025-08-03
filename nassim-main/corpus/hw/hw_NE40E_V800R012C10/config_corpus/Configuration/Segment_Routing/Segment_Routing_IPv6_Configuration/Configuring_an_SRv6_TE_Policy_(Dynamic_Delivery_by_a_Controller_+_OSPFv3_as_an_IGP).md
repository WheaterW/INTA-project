Configuring an SRv6 TE Policy (Dynamic Delivery by a Controller + OSPFv3 as an IGP)
===================================================================================

SRv6 TE Policy is a tunneling technology developed based on SRv6.

#### Prerequisites

Before configuring an SRv6 TE Policy, complete the following task:

* Configure an IGP to implement network layer connectivity.

#### Context

An SRv6 TE Policy can be manually configured on a forwarder through the CLI or NETCONF. Alternatively, it can be delivered to a forwarder after being dynamically generated through a protocol (such as BGP) on a controller â this mode facilitates network deployment.

The process for a controller to deliver an SRv6 TE Policy is as follows:

1. The controller collects information, such as network topology and SID information, through BGP-LS.
2. The controller and headend forwarder establish an IPv6 SR Policy address family-specific BGP peer relationship.
3. The controller computes an SRv6 TE Policy path based on network topology information and delivers it to the headend forwarder through the BGP peer relationship. The headend then generates an SRv6 TE Policy entry.


[Enabling SRv6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0071c.html)

Other SRv6 TE Policy configurations can be performed only after SRv6 is enabled.

[Configuring TE Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0106a.html)

After receiving TE attributes configured for links, an IGP (IS-IS/OSPFv3) advertises them to a controller through BGP-LS. This enables the controller to adjust links based on the TE attributes during SRv6 TE Policy computation.

[Configuring OSPFv3 Topology Advertisement to BGP-LS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0204.html)

After OSPFv3 topology information is advertised to BGP-LS, BGP-LS reports the topology information to a controller for path planning.

[(Optional) Configuring ORF for the BGP IPv6 SR-Policy Address Family](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0301.html)

When a device advertises BGP IPv6 SR-Policy address family routes to peers, you can configure the outbound route filtering (ORF) function to enable the device to advertise only routes carrying the BGP router IDs of peers. This function helps reduce the network load.

[Configuring BGP Peer Relationships Between the Controller and Forwarder](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0119b.html)

Configuring BGP peer relationships between a controller and a forwarder allows the controller to deliver SRv6 TE Policies to the forwarder. This improves the efficiency of automated SRv6 TE Policy deployment.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0115c.html)

After configuring SRv6 TE Policies, verify the configuration.