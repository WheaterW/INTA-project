Configuring DHCPv6 (IA\_NA+IA\_PD) Address Allocation
=====================================================

This section describes how to configure the NE40E to use DHCPv6 to allocate IPv6 addresses and prefixes to the WAN interfaces on a CPE when the CPE works in numbered routing mode. The CPE sends the prefixes to the attached hosts for them to generate IPv6 addresses.

#### Usage Scenario

The CPE and NE40E use DHCPv6 to allocate addresses to WAN interfaces and use DHCPv6-PD to allocate IPv6 prefixes to Home LANs. The CPE uses DHCPv6 to obtain IPv6 prefixes from the NE40E and assigns IPv6 addresses to the host. The CPE performs route forwarding when forwarding IPv6 packets.

**Figure 1** Networking diagram of DHCPv6 (IA\_NA+IA\_PD) address allocation  
![](images/fig_dc_ne_ipv6_address_cfg_005401.png)  

The CPE initiates a connection request, and the NE40E uses DHCPv6 (IA\_NA) to allocate IPv6 addresses to the WAN interfaces on the CPE and uses DHCPv6 (IA\_PD) to allocate prefixes to the CPE and the CPE allocates the prefixes to the attached host for the host to generate IPv6 addresses.


#### Pre-configuration Tasks

Before configuring DHCPv6 (IA\_NA+IA\_PD) address allocation, complete the following tasks:

Set the CPE working mode to numbered routing.

Enable IPv6 on interfaces.


[Configuring the NE40E Based on Its Role](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0075.html)

This section describes how to configure the NE40E based on its role.

[Configuring the state of Address Allocation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0060.html)

You can configure the address assignment status based on the address assignment mode and access mode.

[Verifying the DHCPv6 (IA\_NA+IA\_PD) Address Allocation Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0062.html)

After configuring DHCPv6 (IA\_NA+IA\_PD) address allocation, verify the IPv6 address pool, IPv6 prefix pool, and domain configurations and the usage of the address pool bound to the domain.