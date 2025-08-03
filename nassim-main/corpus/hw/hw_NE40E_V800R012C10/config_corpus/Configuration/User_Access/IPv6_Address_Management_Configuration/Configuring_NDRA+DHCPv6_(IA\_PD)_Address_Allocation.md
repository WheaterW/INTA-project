Configuring NDRA+DHCPv6 (IA\_PD) Address Allocation
===================================================

This section describes how to configure the NE40E to use ND to allocate IPv6 addresses to the WAN interfaces on a CPE and use DHCPv6 (IA\_PD) to allocate prefixes to the CPE when the CPE works in numbered routing mode. The CPE allocates the prefixes to the attached hosts for them to generate IPv6 addresses.

#### Usage Scenario

The CPE sends a DHCPv6 packet carrying only the IA\_PD option to allocate IPv6 prefixes to home LANs; the NE40E uses the PIO option of an RA packet to send the IPv6 prefixes allocated to the WAN interfaces on the CPE to the CPE for it to generate IPv6 addresses.

**Figure 1** Networking diagram of NDRA+DHCPv6 (IA\_PD) address allocation

  
![](figure/en-us_image_0257545077.png)  


The CPE initiates a connection request, and the NE40E uses NDRA to allocate IPv6 addresses to the WAN interfaces on the CPE and uses DHCPv6 (IA\_PD) to allocate prefixes to the CPE and the CPE allocates the prefixes to the attached host for the host to generate IPv6 addresses.


#### Pre-configuration Tasks

Before configuring NDRA+DHCPv6 (IA\_PD) address allocation, complete the following tasks:

Set the CPE working mode to numbered routing.

Enable IPv6 on interfaces.


[Configuring the NE40E Based on Its Role](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0074.html)

This section describes how to configure the NE40E based on its role.

[Configuring the state of Address Allocation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0050.html)

You can configure the address assignment status based on the address assignment mode and access mode.

[Verifying the NDRA+DHCPv6 (IA\_PD) Address Allocation Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0052.html)

After configuring NDRA+DHCPv6 (IA\_PD) address allocation, verify the IPv6 address pool, IPv6 prefix pool, and domain configurations and the usage of the address pool bound to the domain.