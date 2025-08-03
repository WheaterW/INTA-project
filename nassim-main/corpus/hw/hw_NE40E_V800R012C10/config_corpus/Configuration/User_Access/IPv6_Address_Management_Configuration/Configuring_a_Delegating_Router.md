Configuring a Delegating Router
===============================

The NE40E can be configured as a delegating router to allocate and recycle prefixes according to the requests of requesting routers.

#### Usage Scenario

DHCPv6 PD is used to manage and configure IPv6 network segments.

On an IPv4 network, the NE40E uses DHCPv4 to allocate IPv4 addresses to the CPE; the CPE allocates private IPv4 addresses to home users and forwards IPv4 packets through NAT.

On an IPv6 network, all users can obtain global unicast addresses. The CPE uses DHCPv6 PD to obtain the prefixes from the NE40E and allocates IPv6 addresses to the hosts. The CPE performs route forwarding when forwarding IPv6 packets.

**Figure 1** Networking diagram of the NE40E as a delegating router

  
![](figure/en-us_image_0257545110.png)  




#### Pre-configuration Tasks

Before configuring the NE40E as a delegating router, enable IPv6 on interfaces.


[Configuring a DHCPv6 Server DUID](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0010.html)

A DHCPv6 client uses a DHCP unique identifier (DUID) to identify the DHCPv6 server when the client communicates with the server.

[Configure an IPv6 Delegation Prefix Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0037.html)

When the NE40E functions as a delegating router, an IPv6 delegation prefix pool must be configured to manage prefixes.

[Configuring an IPv6 Delegation Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0038.html)

Configuring an IPv6 delegation address pool includes binding a prefix pool to the address pool and configuring a preference and other services (such as a DNS or DNS suffix) for the address pool.

[Binding an IPv6 Delegation Address Pool to a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0078.html)

After an IPv6 delegation address pool is bound to a domain, users in the domain can be assigned prefixes from the address pool.

[(Optional) Binding an IPv6 Address Pool to a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_00781.html)

When different users go online through the same domain and different IPv6 address segments need to be configured for these users, you can bind an IPv6 address pool to the BAS interface from which the users go online so that the IPv6 address range for the users in the domain can be limited based on the BAS interface.

[(Optional) Locking an IPv6 Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0160b.html)

This section describes how to lock an IPv6 address pool so that the address pool cannot be used to assign IPv6 addresses to new users.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0080.html)

After configuring a delegating router, you can view the configurations of IPv6 address pool, the prefix pool, and statistics about the DHCPv6 server.