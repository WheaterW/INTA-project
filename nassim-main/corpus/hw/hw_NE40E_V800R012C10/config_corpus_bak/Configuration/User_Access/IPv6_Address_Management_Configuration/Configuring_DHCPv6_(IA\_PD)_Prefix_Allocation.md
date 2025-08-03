Configuring DHCPv6 (IA\_PD) Prefix Allocation
=============================================

This section describes how to configure the NE40E to allocate prefixes to a CPE when the CPE works in unnumbered routing mode. The CPE allocates the prefixes to the attached host for the host to generate IPv6 addresses.

#### Usage Scenario

In DHCPv6 prefix allocation, the IA\_PD option is used to carry IA prefixes.

**Figure 1** Networking diagram of IA\_PD prefix allocation

  
![](figure/en-us_image_0257545108.png)  


The CPE initiates a connection request, and the NE40E uses DHCPv6 (IA\_PD) to allocate prefixes to the CPE and the CPE allocates the prefixes to the attached host for the host to generate IPv6 addresses.


[Configuring the NE40E Based on Its Role](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0073.html)

This section describes how to configure the NE40E based on its role.

[Verifying the DHCPv6 (IA\_PD) Prefix Allocation Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0042.html)

After configuring DHCPv6 (IA\_PD) prefix allocation, verify the IPv6 address pool, IPv6 prefix pool, and domain configurations and the usage of the address pool bound to the domain.