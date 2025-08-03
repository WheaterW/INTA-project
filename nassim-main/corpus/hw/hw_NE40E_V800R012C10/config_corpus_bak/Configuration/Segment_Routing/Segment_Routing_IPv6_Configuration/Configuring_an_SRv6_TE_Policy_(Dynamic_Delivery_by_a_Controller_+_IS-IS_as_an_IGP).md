Configuring an SRv6 TE Policy (Dynamic Delivery by a Controller + IS-IS as an IGP)
==================================================================================

SRv6 TE Policy is a tunneling technology developed based on SRv6.

#### Pre-configuration Tasks

Before configuring an SRv6 TE Policy, complete the following task:

* Configure an IGP to implement network layer connectivity.

#### Context

An SRv6 TE Policy can be manually configured on a forwarder through the CLI or NETCONF. Alternatively, it can be delivered to a forwarder after being dynamically generated through a protocol (such as BGP) on a controller â this mode facilitates network deployment.

The process for a controller to deliver an SRv6 TE Policy is as follows:

1. The controller collects information, such as network topology and SID information, through BGP-LS.
2. The controller and headend forwarder establish an IPv6 SR Policy address family-specific BGP peer relationship.
3. The controller computes an SRv6 TE Policy path based on network topology information and delivers it to the headend forwarder through the BGP peer relationship. The headend then generates an SRv6 TE Policy entry.


[Enabling SRv6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0071a.html)

Other SRv6 TE Policy configurations can be performed only after SRv6 is enabled.

[Configuring SRv6 SIDs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0117.html)

The headend can orchestrate network paths only if SIDs are allocated to adjacencies and nodes on the network.

[Configuring TE Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0106.html)

After receiving TE attributes configured for links, an IGP (IS-IS/OSPFv3) advertises them to a controller through BGP-LS. This enables the controller to adjust links based on the TE attributes during SRv6 TE Policy computation.

[Configuring IS-IS Topology Advertisement to BGP-LS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0118.html)

After IS-IS topology information is advertised to BGP-LS, BGP-LS reports the topology information to a controller for path planning.

[(Optional) Configuring ORF for the BGP IPv6 SR-Policy Address Family](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0305.html)

When a device advertises BGP IPv6 SR-Policy address family routes to peers, you can configure the outbound route filtering (ORF) function to enable the device to advertise only routes carrying the BGP router IDs of peers. This function helps reduce the network load.

[Configuring BGP Peer Relationships Between the Controller and Forwarder](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0119.html)

Configuring BGP peer relationships between a controller and a forwarder allows the controller to deliver SRv6 TE Policies to the forwarder. This improves the efficiency of automated SRv6 TE Policy deployment.

[Configuring SRv6 TE Policy Status Advertisement to BGP-LS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0100.html)

Configure a forwarder to advertise SRv6 TE Policy status to BGP-LS. BGP-LS can then advertise the status to peers.

[Verifying the SRv6 TE Policy Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0122.html)

After configuring SRv6 TE Policies, verify the configuration.