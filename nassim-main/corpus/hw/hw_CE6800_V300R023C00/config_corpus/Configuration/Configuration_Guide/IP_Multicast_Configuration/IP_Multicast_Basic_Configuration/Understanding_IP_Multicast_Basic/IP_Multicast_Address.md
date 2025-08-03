IP Multicast Address
====================

Network-layer multicast using IP multicast addresses is required to enable multicast sources and group members to communicate. Additionally, link-layer multicast that uses multicast MAC addresses is required to enable multicast data to be correctly transmitted on the local physical network. The destination address of multicast data is a group with unknown members but not a specific receiver. Therefore, IP multicast addresses must be mapped to multicast MAC addresses.

#### IPv4 Multicast Address

The Internet Assigned Numbers Authority (IANA) allocates Class D addresses to IPv4 multicast. An IPv4 address is 32 bits long, and the first four bits of a Class D address is 1110. The address ranges from 224.0.0.0 to 239.255.255.255. [Table 1](#EN-US_CONCEPT_0000001176741511__tab_01) describes the ranges and meanings of IPv4 multicast addresses.

**Table 1** Ranges and meanings of IPv4 multicast addresses
| Address Range | Meaning |
| --- | --- |
| 224.0.0.0 to 224.0.0.255 | Permanent group address range. This is an IP address range reserved by the IANA for a routing protocol, also called a reserved group address range. It identifies a group of network devices and is used for scenarios such as routing and topology lookup, but not for multicast forwarding. [Table 2](#EN-US_CONCEPT_0000001176741511__tab_02) describes common permanent group addresses. |
| 224.0.1.0 to 231.255.255.255  233.0.0.0 to 238.255.255.255 | ASM group address range, which is valid on the entire network.  NOTE:  224.0.1.39 and 224.0.1.40 are reserved addresses and are not recommended. |
| 232.0.0.0 to 232.255.255.255 | Default SSM group address range, which is valid on the entire network. |
| 239.0.0.0 to 239.255.255.255 | Local administrative group address range, which is valid only in the local administrative domain. Different administrative domains can use the same local administrative group address. |


**Table 2** List of common permanent group addresses
| Permanent Group Address | Meaning |
| --- | --- |
| 224.0.0.0 | Not allocated |
| 224.0.0.1 | Address (similar to a broadcast address) of all the hosts and multicast devices on a network segment |
| 224.0.0.2 | All multicast devices' address |
| 224.0.0.3 | Not allocated |
| 224.0.0.4 | Distance Vector Multicast Routing Protocol (DVMRP) router's address |
| 224.0.0.5 | Open Shortest Path First (OSPF) router's address |
| 224.0.0.6 | OSPF designated router's address |
| 224.0.0.7 | Shared tree (ST) router's address |
| 224.0.0.8 | ST host's address |
| 224.0.0.9 | Routing Information Protocol version 2 (RIP-2) router's address |
| 224.0.0.11 | Mobile agents' address |
| 224.0.0.12 | Dynamic Host Configuration Protocol (DHCP) server's or relay agent's address |
| 224.0.0.13 | All Protocol Independent Multicast (PIM) routers' address |
| 224.0.0.14 | Address used for Resource Reservation Protocol (RSVP) encapsulation |
| 224.0.0.15 | All core-based tree (CBT) routers' address |
| 224.0.0.16 | Specified Subnetwork Bandwidth Management (SBM) device's address |
| 224.0.0.17 | All SBMs' address |
| 224.0.0.18 | Virtual Router Redundancy Protocol (VRRP) address |
| 224.0.0.22 | Address of all routers enabled with Internet Group Management Protocol, Version 3 (IGMPv3) |
| 224.0.0.19 to 224.0.0.21  224.0.0.23 to 224.0.0.255 | Not specified |



#### IPv4 Multicast MAC Address

When IPv4 unicast messages are transmitted on an Ethernet network, they use receiver MAC addresses as destination MAC addresses. However, the destination of a multicast data message is a group with unknown members but not a specific receiver. Therefore, multicast data messages must use IPv4 multicast MAC addresses, which are link-layer addresses mapped from IPv4 multicast addresses.

As defined by the IANA, the 24 most significant bits of an IPv4 multicast MAC address are 0x01005e, the 25th bit is 0, and the 23 least significant bits are the same as the 23 least significant bits of an IPv4 multicast address, as shown in [Figure 1](#EN-US_CONCEPT_0000001176741511__fig_03).

**Figure 1** Mapping between an IPv4 multicast address and an IPv4 multicast MAC address  
![](figure/en-us_image_0000001176741517.png)  

The four most significant bits of an IPv4 multicast address are fixed at 1110, mapping the 25 most significant bits of a multicast MAC address. Among the last 28 bits, only 23 bits are mapped to a MAC address, and 5 bits are lost. As a result, 32 IPv4 multicast addresses are mapped to the same MAC address.