Configuring Basic NAT64 Functions
=================================

This section describes how to configure basic NAT64 functions.

#### Usage Scenario

Basic NAT64 functions are prerequisites for NAT64 configurations, including enhanced NAT64 configurations. The configuration of basic NAT64 functions includes the following operations:

* A NAT64 IPv6 prefix is configured. The destination address of IPv6 service data packets sent to a NAT64 Carrier Grade NAT (CGN) device is an IPv6 address, regardless of whether the packets are sent to the IPv4 or IPv6 network. To differentiate IPv4 and IPv6 packets, the NAT64 CGN device processes the packets based on the IPv6 prefix.
* Create NAT64 instances. The creation of NAT64 instances is the basis of NAT64 configuration because NAT64 instances are used in many subsequent configurations.
* Configure a NAT64 address pool. A NAT64 address pool is essential to the implementation of NAT64. When IPv6 user data packets are sent to a NAT64 CGN device, an IPv4 address must be allocated from the NAT64 address pool to the packets so that the packets are transmitted over an IPv4 network.


#### Pre-configuration Tasks

Before you configure basic NAT64 functions, complete the following tasks:

* Install a NAT64 license.
* Ensure that service boards have been installed and working properly.
* Configure data link layer protocol parameters and IP addresses for interfaces so that the data link layer protocol on each interface can go Up.
* (Optional) Configure a NAT64 device to properly interwork with a RADIUS server.


[Binding a Service Board to a NAT64 Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0007.html)

This section describes how to bind a service board to a NAT64 instance. A NAT64 instance is a logical carrier that implements NAT64 functions.

[Configuring a NAT64 Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0008.html)

You can create a NAT64 address pool and assign available public IPv4 address segments to a specified NAT64 instance to translate between private IPv6 addresses and public IPv4 addresses.

[Configuring a NAT64 IPv6 Prefix](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0006.html)

A device identifies a network type based on a NAT64 prefix and sends each type of packet to a DNS64 server for processing.

[(Optional) Configuring a Port Allocation Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0009_m2k.html)

Configuring a port allocation mode helps manage port resources.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0010.html)

After basic NAT64 functions are configured, you can verify the basic NAT64 configuration.