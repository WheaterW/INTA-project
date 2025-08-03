Configuring Clean Switching of Multicast Streams in Multicast Groups
====================================================================

To translate the source IP addresses, destination IP addresses, and UDP port numbers of multiple input multicast streams in multicast groups, configure clean switching for the multicast streams.

#### Usage Scenario

In multicast applications, you may need to translate the characteristics of input multicast streams to match output devices and application scenarios. For example, you need to output one multicast stream to multiple terminals. You can configure multicast NAT to meet this need. If you need to translate the characteristics of multiple input multicast streams at the same time, you can place the input multicast streams in an input multicast group and configure clean switching for the multicast streams.


#### Pre-configuration Tasks

None


[Enabling Multicast NAT Globally](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0008_a.html)

Before configuring multicast NAT, you must enable multicast NAT globally. Otherwise, the multicast NAT configuration cannot take effect.

[Creating a Multicast NAT Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0009_a.html)

In multicast NAT, input and output multicast streams are associated through a multicast NAT instance. This section describes how to create a multicast NAT instance.

[Creating a Multicast NAT Instance Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0021.html)

In multicast NAT, input and output multicast streams are associated through a multicast NAT instance. If multiple input multicast streams need to be switched at the same time, create a multicast NAT instance group and add the multicast streams to the multicast NAT instance group.

[Configuring Traffic Policies](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0026.html)

To implement multicast NAT, you must configure traffic policies to match input multicast streams.

[Applying a Traffic Policy on an Inbound Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0011_a.html)

A traffic policy can be applied on an inbound interface of multicast streams to match the packet header information of input multicast streams.

[Configuring Multicast NAT on an Outbound Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0012_a.html)

This section describes how to configure multicast NAT on an outbound interface of multicast streams and specify a source IP address, destination IP address, and destination port number for post-translation multicast streams.

[Creating a Multicast NAT Outbound Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0022.html)

In multicast NAT, input and output multicast streams are associated through a multicast NAT instance. If multiple input multicast streams need to be switched at the same time, create a multicast NAT instance group, add the multicast streams to the multicast NAT instance group, create a multicast NAT outbound group, add output multicast streams to the group, and then bind the multicast NAT outbound group to the multicast NAT instance group.

[Binding a Multicast NAT Outbound Group to a Multicast NAT Instance Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0023.html)

This section describes how to bind a multicast NAT outbound group to a multicast NAT instance group.

[Verifying the Multicast NAT Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_multicast_cfg_0017_a.html)

After configuring multicast NAT, verify the configuration.