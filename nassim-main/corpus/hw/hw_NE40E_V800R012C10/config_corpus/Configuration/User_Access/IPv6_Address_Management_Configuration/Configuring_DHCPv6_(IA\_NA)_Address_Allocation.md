Configuring DHCPv6 (IA\_NA) Address Allocation
==============================================

This section describes how to configure the NE40E to use DHCPv6 (IA\_NA) to allocate IPv6 addresses when the CPE works in bridging mode.

#### Usage Scenario

In DHCPv6 (IA\_NA) address allocation mode, IA\_NA options are used to carry IA addresses to be allocated.

**Figure 1** Networking diagram of DHCPv6 (IA\_NA) address allocation

  
![](figure/en-us_image_0257545075.png)  


The host initiates a connection request and the CPE transparently forwards the connection request packet. The NE40E uses DHCPv6 (IA\_NA) to allocate IPv6 addresses to the host.


[Configuring the NE40E Based on Its Role](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0031.html)

This section describes how to configure the NE40E based on its role.

[Configuring the Address Assignment Status](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0024.html)

You can configure the address assignment status based on the address assignment mode and access mode.

[Verifying the DHCPv6 (IA\_NA) Address Allocation Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0034.html)

After configuring DHCPv6 address allocation, verify the IPv6 address pool, IPv6 prefix pool, and domain configurations and the usage of the address pool bound to the domain.