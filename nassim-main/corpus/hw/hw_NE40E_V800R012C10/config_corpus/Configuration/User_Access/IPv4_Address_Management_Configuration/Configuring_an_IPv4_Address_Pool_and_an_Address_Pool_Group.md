Configuring an IPv4 Address Pool and an Address Pool Group
==========================================================

After an IPv4 address pool is configured, users can obtain IPv4 addresses from the IPv4 address pool.

#### Usage Scenario

A BAS-side address pool needs to be configured to assign IP addresses to access users. If the NE40E needs to allocate IP addresses to users, you must configure a local address pool on the NE40E, as shown in [Figure 1](#EN-US_TASK_0172373765__fig_dc_ne_ipv4_address_cfg_004903); if a DHCPv4 or BOOTP server needs to allocate IP addresses to users, you must configure a remote address pool on the NE40E, as shown in [Figure 2](#EN-US_TASK_0172373765__fig_dc_ne_ipv4_address_cfg_004904).

**Figure 1** Networking diagram for address assignment from the local address pool

  
![](figure/en-us_image_0257534281.png "Click to enlarge")  



**Figure 2** Networking diagram for address assignment from the remote address pool

  
![](figure/en-us_image_0257534282.png "Click to enlarge")  




#### Pre-configuration Tasks

Before configuring a remote address pool, [configure the DHCPv4 server](dc_ne_ipv4_address_cfg_0033.html).


[Configuring an Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0050.html)



[(Optional) Configuring IPv4 Address Reservation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_00501.html)



[(Optional) Configuring Static IP Address Binding](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0051.html)

The IP address pool configured for static address binding contains special IP addresses, which are assigned to servers in need of fixed IP addresses or users with particular requirements.

[(Optional) Configuring DNS Services for the DHCPv4 Client](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0052.html)

You can configure DNS server parameters for the DHCPv4 client. This allows the DHCPv4 client to automatically obtain DNS services automatically. Then, users can use easy-to-memorize domain names rather than complicated IP addresses.

[(Optional) Configuring NetBIOS Services for DHCPv4 Clients](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0053.html)

You can configure NetBIOS services for DHCPv4 clients to enable users to obtain NetBIOS services automatically. Then, users can use easy-to-memorize hostnames rather than complicated IP addresses.

[(Optional) Configuring SIP Services for the DHCPv4 Client](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0068.html)

You can configure SIP services for the DHCPv4 client on a DHCPv4 server to implement multimedia communication, such as multimedia conferencing, Internet calls, distance education, and distance medical treatment.

[(Optional) Configuring DHCPv4 User-Defined Options](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0054.html)

You can configure DHCPv4 user-defined options to provide more control information and parameters for clients.

[(Optional) Configuring Address Pool Protection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0055.html)

Configuring address pool protection includes locking an address pool, disabling IP addresses, and reclaiming IP addresses in special scenarios.

[(Optional) Configuring IPv4 Address Pool Isolation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0099.html)

By default, the association between IPv4 address pool isolation and master/slave main control board switchover is enabled. You can enable or disable this function as required.

[(Optional) Configuring a Constant Index for an IPv4 Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0237.html)

By default, IPv4 address pools do not support constant indexes. Instead, their indexes change after a device restart. After a device restart, the NMS loses all IPv4 address pool statistics and can no longer monitor these address pools. This problem can be solved by configuring constant indexes for the address pools.

[(Optional) Allocating IP Addresses Based on Option 60](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0171.html)

When there is no relay device between a DHCP client and a DHCP server, the DHCP server allocates different network segments and VPN addresses based on Option 60 carried in user packets.

[(Optional) Locking an IP Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0260.html)

This section describes how to lock an IP address pool so that the address pool cannot be used to assign IP addresses to new users.

[Configuring an Address Pool Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0153.html)

An address pool group is a set of address pools sharing specified attributes. An address pool group simplifies configuration in some situations.

[Specifying an IPv4 Address Pool for a Domain and a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0117.html)

Users in a domain can obtain addresses from an IPv4 address pool only after the pool is specified for the domain.

[(Optional) Configuring the Thresholds for Public IP Address Pool Usage in a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0004.html)

This section describes how to configure the upper and lower thresholds for public IP address pool usage in a domain to calculate pool usage status, which is sent to a Remote Authentication Dial-In User Service (RADIUS) server.

[(Optional) Configuring IPv4 Address Pool Route Leaking](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_00041.html)

This section describes how to configure a VPN import policy for address pool subnet routes in order to achieve VPN-based automatic IPv4 address pool route leaking.

[(Optional) Disabling BGP from Importing UNRs](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_00060.html)



[Verifying the Configuration of IPv4 Address Pools and Address Pool Groups](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0057.html)

After configuring IPv4 address pools or pool groups, verify the configurations of all IP address pools or pool groups. You can also verify the configurations of a specified IP address pool or pool group.