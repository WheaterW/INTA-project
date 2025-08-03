IPv6 Address
============

IPv6 Address

#### IPv6 Address Format

A 128-bit IPv6 address has two formats:

* X:X:X:X:X:X:X:X
  
  + An IPv6 address in this format is written as eight groups of four hexadecimal digits (0 to 9, A to F), each group separated by a colon (:). Each "X" represents a group of hexadecimal digits. An IPv6 address example is as follows:
    
    2001:db8:130F:0000:0000:09C0:876A:130B
    
    For convenience, leading zeros of each group can be omitted. Therefore, the preceding address can be written as:
    
    2001:db8:130F:0:0:9C0:876A:130B
  + Any number of consecutive groups of 0s can be replaced with two colons (::). Therefore, the given example can be written as:
    
    2001:db8:130F::9C0:876A:130B
    
    An IPv6 address can contain only one double-colon substitution. Multiple occurrences of double-colon substitutions lead to ambiguity.
* X:X:X:X:X:X:d.d.d.d
  
  IPv4-mapped IPv6 address: The format of an IPv4-mapped IPv6 address is 0:0:0:0:0:FFFF:IPv4-address. IPv4-mapped IPv6 addresses are used to represent IPv4 node addresses as IPv6 addresses.
  
  "X:X:X:X:X:X" represents the high-order six groups of digits, with each "X" standing for 16 bits, which are represented by hexadecimal digits. "d.d.d.d" represents the low-order four groups of digits, with each "d" standing for 8 bits, which are represented by decimal digits. "d.d.d.d" is a standard IPv4 address.

#### IPv6 Address Structure

An IPv6 address is composed of two parts:

* Network prefix: equivalent to the network ID of an IPv4 address, which is of *n* bits.
* Interface ID: equivalent to the host ID of an IPv4 address, which is of (128 - *n*) bits.

[Figure 1](#EN-US_CONCEPT_0000001130781936__fig_dc_vrp_ipv6_feature_000401) illustrates the structure of the address 2001:DB8:6101:1::E0:F726:4E58 /64.

**Figure 1** Structure of the address 2001:DB8:6101:1::E0:F726:4E58 /64  
![](figure/en-us_image_0000001130781956.png)

#### IPv6 Address Classification

IPv6 addresses have three types.

* Unicast address: identifies a single network interface and is similar to an IPv4 unicast address. A packet destined for a unicast address is transmitted to the unique interface identified by this address.
  
  A global unicast address cannot be the same as its network prefix, because this type of address is a subnet-router anycast address reserved for a device. However, this rule does not apply to an IPv6 address with a 127-bit network prefix.
* Anycast address: identifies a group of interfaces, which usually belong to different nodes. A packet destined for an anycast address is transmitted to only one of the interfaces, that is, the nearest one according to distance as defined by the routing protocol.
  
  Application scenario: When a mobile host communicates with the mobile agent on the home subnet, it uses the anycast address of the subnet's routing device.
  
  Address specifications: Anycast addresses do not have independent address space. They can use the format of any unicast address. Syntax is required to differentiate an anycast address from a unicast address.
  
  As IPv6 defines, an IPv6 address with the interface identifier of all 0s is a subnet-router anycast address. As shown in [Figure 2](#EN-US_CONCEPT_0000001130781936__fig_dc_vrp_ipv6_feature_000403), the subnet prefix is an IPv6 unicast address prefix which is specified during configuration of an IPv6 unicast address.
  
  **Figure 2** Format of a subnet-router anycast address  
  ![](figure/en-us_image_0000001176661715.png)  
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  An anycast address is not necessarily a subnet-router anycast address and can also be a global unicast address.
* Multicast address: assigned to a set of interfaces that belong to different nodes and is similar to an IPv4 multicast address. A packet destined for a multicast address is transmitted to all the interfaces identified by this address.
  
  IPv6 addresses do not include broadcast addresses. In IPv6, multicast addresses can provide the functions of broadcast addresses.

Unicast addresses can be classified into the types listed in [Table 1](#EN-US_CONCEPT_0000001130781936__tab_dc_vrp_ipv6_feature_000401).

**Table 1** IPv6 unicast address types
| Address Type | Binary Prefix | IPv6 Prefix Identifier |
| --- | --- | --- |
| Link-local unicast address | 1111111010 | FE80::/10 |
| Unique local unicast address | 1111110 | FC00::/7 |
| Loopback address | 00...1 (128 bits) | ::1/128 |
| Unspecified address | 00...0 (128 bits) | ::/128 |
| Global unicast address | Others | - |

Each unicast address type is described as follows:

* Link-local unicast address: used in the neighbor discovery protocol and in the communication between nodes on the local link during stateless address autoconfiguration. The packet with the link-local unicast address as the source or destination address is only forwarded on the local link. The link-local unicast address can be automatically configured on an Ethernet interface using the link-local prefix FE80::/10 (1111 1110 10) and an EUI-64 interface ID (the 48-bit MAC address of an interface can be converted into a 64-bit interface ID according to IEEE EUI-64).
* Unique local unicast address: identifies a single site and has a globally unique prefix. Sites use unique local unicast addresses to establish private connections, without incurring address conflicts. Even if routes destined for unique local unicast addresses leak, the routes do not conflict with Internet routes. Upper-layer applications use unique local unicast addresses as global unicast addresses.
* Loopback address: is 0:0:0:0:0:0:0:1 or ::1 and not assigned to any interface. Similar to the IPv4 loopback address 127.0.0.1, the IPv6 loopback address indicates that a node sends IPv6 packets to itself.
* Unspecified address (::): can neither be assigned to any node nor function as a destination address. The unspecified address can be used in the Source Address field of the IPv6 packet sent by an initializing host before it has learned its own address. During DAD, the Source Address field of an NS message is an unspecified address.
* Global unicast address: equivalent to an IPv4 public address. Global unicast addresses are used on links that can be aggregated, and are provided to Internet service providers (ISPs). The structure of global unicast addresses enables route prefix aggregation, which maximizes the number of global routing entries. A global unicast address consists of a 48-bit route prefix managed by carriers, a 16-bit subnet ID managed by local nodes, and a 64-bit interface ID. Unless otherwise specified, global unicast addresses include site-local unicast addresses.

#### Interface ID in the IEEE EUI-64 Format

The 64-bit interface ID in an IPv6 address identifies a unique interface on a link. This address is derived from the link-layer address (such as a MAC address) of the interface. The 64-bit IPv6 interface ID is translated from a 48-bit MAC address by inserting a hexadecimal number into the MAC address, and then setting the U/L bit (the leftmost seventh bit) to 1.

If an interface has been configured with a MAC address, an EUI-64 address is generated based on the MAC address of the interface, with FFFE added in the middle.

If an interface has not been configured with a MAC address, an EUI-64 address is generated based on the following rules:

* The EUI-64 address of a Layer 3 physical interface or sub-interface is generated based on the MAC address of the physical interface, with the last two bytes following the interface index added in the middle.
* For a loopback or tunnel interface, an EUI-64 address is generated based on the MAC address of the interface, with the last two bytes following the interface index added in the middle.
* For an Eth-Trunk interface and its sub-interfaces or VLANIF interface, an EUI-64 address is generated based on the MAC address of the interface, with FFFE added in the middle.

Taking the insertion of a hexadecimal number FFFE (1111 1111 1111 1110) into the middle of a MAC address as an example, see [Figure 3](#EN-US_CONCEPT_0000001130781936__fig_dc_vrp_ipv6_feature_000402) for the detailed conversion procedure.

**Figure 3** Translation from a MAC address to an EUI-64 address  
![](figure/en-us_image_0000001130781954.png)