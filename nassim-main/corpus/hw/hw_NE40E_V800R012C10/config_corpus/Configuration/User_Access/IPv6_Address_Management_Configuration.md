IPv6 Address Management Configuration
=====================================

This section describes how to use IPv6 address management to assign and manage IPv6 addresses for access users.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this feature is supported only by the admin VS.



[Overview of IPv6 Address Management](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0001.html)

IPv6 address management includes configuring a static IPv6 address, receiving an IPv6 address from the RADIUS server, and obtaining an IPv6 address dynamically.

[Configuration Precautions for IPv6 Address Management](../../../../software/nev8r10_vrpv8r16/user/spec/IPv6_Address_Management_limitation.html)



[Configuring a DHCPv6 Relay Agent on the User Side](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0012.html)

When independent DHCPv6 servers allocate and manage addresses, the NE40E can be configured as the relay agent to implement redundancy backup and load balancing among the remote DHCPv6 servers.

[Configuring a Delegating Router](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0071.html)

The NE40E can be configured as a delegating router to allocate and recycle prefixes according to the requests of requesting routers.

[(Optional) Configuring DHCPv6 Service Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0091.html)

Configure transparent transmission of DHCPv6 packets, unicast communication, and two-message exchange between a DHCPv6 client and a DHCPv6 server based on actual network conditions.

[Configuring DHCPv6 (IA\_NA) Address Allocation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0027.html)

This section describes how to configure the NE40E to use DHCPv6 (IA\_NA) to allocate IPv6 addresses when the CPE works in bridging mode.

[Configuring DHCPv6 (IA\_PD) Prefix Allocation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0035.html)

This section describes how to configure the NE40E to allocate prefixes to a CPE when the CPE works in unnumbered routing mode. The CPE allocates the prefixes to the attached host for the host to generate IPv6 addresses.

[Configuring DHCPv6 (IA\_NA+IA\_PD) Address Allocation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0053.html)

This section describes how to configure the NE40E to use DHCPv6 to allocate IPv6 addresses and prefixes to the WAN interfaces on a CPE when the CPE works in numbered routing mode. The CPE sends the prefixes to the attached hosts for them to generate IPv6 addresses.

[Configuring NDRA Address Allocation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0020.html)

This section describes how to configure the NE40E to use ND to allocate IPv6 addresses when the CPE works in bridging mode.

[Configuring NDRA+DHCPv6 (IA\_PD) Address Allocation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0043.html)

This section describes how to configure the NE40E to use ND to allocate IPv6 addresses to the WAN interfaces on a CPE and use DHCPv6 (IA\_PD) to allocate prefixes to the CPE when the CPE works in numbered routing mode. The CPE allocates the prefixes to the attached hosts for them to generate IPv6 addresses.

[Maintaining IPv6 Address Management](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0093.html)



[Configuration Examples for IPv6 Address Management](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0065.html)

This section provides several examples of IPv6 address management. Each configuration example includes the networking requirements, configuration notes, and configuration roadmap.