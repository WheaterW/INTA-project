Configuring a DHCPv6 Relay Agent on the User Side
=================================================

When independent DHCPv6 servers allocate and manage addresses, the NE40E can be configured as the relay agent to implement redundancy backup and load balancing among the remote DHCPv6 servers.

#### Usage Scenario

When users access the NE40E, the device functions as a DHCPv6 relay agent to forward user address requests to the remote DHCPv6 servers. Configuring multiple DHCPv6 servers is recommended for redundancy backup and load balancing among the remote servers. The DHCPv6 server group must be bound to the remote address pool. This binding shields the interactions between the NE40E and DHCPv6 servers from the client.

**Figure 1** Networking diagram of the NE40E as a DHCPv6 relay agent on user side

  
![](figure/en-us_image_0257545079.png)  




#### Pre-configuration Tasks

The remote DHCPv6 servers have been deployed.


[Configuring a Remote IPv6 Prefix Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0055.html)

When the NE40E functions as a DHCPv6 relay agent, a remote IPv6 prefix pool must be configured to manage the prefixes.

[Configuring DHCPv6 Lease Proxy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0066.html)



[Configuring a Remote IPv6 Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0056.html)

Configuring a remote IPv6 address pool includes binding a prefix pool to the address pool and configuring a preference and route advertisement for the address pool.

[Configuring a DHCPv6 Server Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0014.html)

A DHCPv6 server group needs to be configured only when BAS-side users are assigned IPv6 addresses or prefixes from a remote address pool.

[Associating an Address Pool with a DHCPv6 Server Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0069.html)

Associating an address pool with a DHCPv6 server group is required only when the remote IPv6 address pool is used. 

[Binding a Remote IPv6 Address Pool to a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0077.html)

Users in a domain can obtain addresses from an IPv6 address pool only after the address pool is bound to the domain.

[(Optional) Binding an IPv6 Address Pool to a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0771.html)

When different users go online through the same domain and different IPv6 address segments need to be configured for these users, you can bind an IPv6 address pool to the BAS interface from which the users go online so that the IPv6 address range for the users in the domain can be limited based on the BAS interface.

[(Optional) Configuring a Device to Insert the Option 18 and Option 37 Attributes into the Messages to Be Sent to the DHCPv6 Server](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0164.html)



[(Optional) Parsing Option 64 to Manage User Bandwidth](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_01641.html)

The Router can parse the QoS profile name from the Option 64 field delivered by the DHCP server to manage user bandwidth.

[(Optional) Configuring Lease Management for a Remote Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_01642.html)

The Router supports lease management on addresses in a remote address pool.

[(Optional) Configuring IPv6 Address Pool Isolation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0099.html)

By default, the association between IPv6 address pool isolation and master/slave main control board switchover is enabled. You can enable or disable this function as required.

[(Optional) Disabling BGP from Importing UNRs](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_00060.html)



[(Optional) Locking an IPv6 Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0160a.html)

This section describes how to lock an IPv6 address pool so that the address pool cannot be used to assign IPv6 addresses to new users.

[Verifying the DHCPv6 Relay Agent Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv6_address_cfg_0015.html)

After configuring a DHCPv6 relay agent, verify the DHCPv6 server group configurations, including the DHCP unique identifier (DUID) and the address pool bound to the domain.