Configuring Multicast NAT
=========================

To translate the source IP address, destination IP address, and UDP port number of input multicast streams, configure multicast NAT.

#### Usage Scenario

In multicast applications, you may need to translate the characteristics of input multicast streams to match output devices and application scenarios. For example, you need to output one multicast stream to multiple terminals. You can configure multicast NAT to meet this need.


#### Pre-configuration Tasks

None


[Enabling Multicast NAT Globally](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0008.html)

Before configuring multicast NAT, you must enable multicast NAT globally. Otherwise, the multicast NAT configuration cannot take effect.

[Creating a Multicast NAT Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0009.html)

In multicast NAT, input and output multicast streams are associated through a multicast NAT instance. This section describes how to create a multicast NAT instance.

[Configuring Traffic Policies](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0025.html)

To implement multicast NAT, you must configure traffic policies to match input multicast streams.

[Applying a Traffic Policy on an Inbound Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0011.html)

A traffic policy can be applied on an inbound interface of multicast streams to match the packet header information of input multicast streams.

[Configuring Multicast NAT on an Outbound Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0012.html)

This section describes how to configure multicast NAT on an outbound interface of multicast streams and specify a source IP address, destination IP address, and destination port number for post-translation multicast streams.

[Binding Output Multicast Streams to a Multicast Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0013.html)

This section describes how to bind output multicast streams to a multicast instance.

[(Optional) Disabling TTL Decrease by 1](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0014.html)

This section describes how to disable TTL decrease by 1.

[Verifying the Multicast NAT Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0017.html)

After configuring multicast NAT, verify the configuration.