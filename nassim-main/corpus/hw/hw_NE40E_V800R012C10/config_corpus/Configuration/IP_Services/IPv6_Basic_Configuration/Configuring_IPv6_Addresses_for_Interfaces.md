Configuring IPv6 Addresses for Interfaces
=========================================

Assigning IPv6 addresses to a network device enables the device to communicate with other devices on the network.

#### Usage Scenario

IPv6 addresses must be configured for Router interfaces so that the Routers can communicate with IPv6 devices.

Link-local addresses are used in neighbor discovery and in the communication between nodes on the local link during stateless address autoconfiguration. The packets with link-local addresses as source or destination addresses are only forwarded on the local link.

Link-local addresses can be automatically generated or manually configured.

* After the IPv6 function is enabled on an interface, the system automatically generates a link-local address for the interface.
* The link-local address that is manually configured must be valid (usually with the FE80::/10 prefix).

Link-local addresses are used for the communication between link-local nodes. It means that link-local addresses are usually used for the communication between protocols, and are not directly related to the communication between users. Therefore, automatic generation of link-local addresses is recommended.

Global unicast addresses, equivalent to public IPv4 addresses, are used for data forwarding on a public network and are necessary for the communication between users.

EUI-64 addresses function the same as global unicast addresses. The difference is that only the network bits need to be specified for an EUI-64 address, and the host bits are derived from the interface MAC address; for a global unicast address, all the 128 bits must be specified. You must note that the prefix length of the network bits of an EUI-64 address cannot be more than 64 bits.

Both or either of EUI-64 addresses and global unicast addresses can be configured on an interface for communications. The addresses that are configured on the same interface, however, must belong to different network segments.

IPv6 addresses are classified as unicast, multicast, or anycast addresses.

* Multicast address: assigned to a group of interfaces that belong to different nodes and is similar to an IPv4 multicast address. A packet destined for a multicast address is delivered to all the interfaces identified by that address.
* Anycast address: assigned to a group of interfaces that generally belong to different nodes. A packet destined for an anycast address is delivered to only one of the member interfaces, typically the nearest to the sender based on the distance vector in the interface group identified by the anycast address. Currently, anycast addresses are applicable to a few scenarios. In typical applications, anycast addresses are used by a large number of 6to4 relay routers in a 6to4 tunnel to enhance the network expandability.

#### Pre-configuration Tasks

Before configuring IPv6 addresses for interfaces, complete the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is Up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is Up.


[Enabling IPv6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0004.html)

You can perform IPv6-related configurations on an interface only when IPv6 is enabled in the interface view.

[Configuring a Link-local Address for an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0005.html)

Link-local addresses are used in neighbor discovery and in the communication between nodes on the local link during stateless address autoconfiguration. Link-local addresses are valid only on local links, meaning that packets with link-local addresses as source or destination addresses are not forwarded to other links.

[Configuring a Global Unicast Address for an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0006.html)

Global unicast addresses function the same as public IPv4 addresses. They are used for links whose route prefixes can be aggregated, reducing the number of routing entries.

[Configuring an IPv6 Anycast Address for an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_2000.html)

An anycast address is used to identify a group of interfaces.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0007.html)

After configuring IPv6 addresses, verify the configuration.