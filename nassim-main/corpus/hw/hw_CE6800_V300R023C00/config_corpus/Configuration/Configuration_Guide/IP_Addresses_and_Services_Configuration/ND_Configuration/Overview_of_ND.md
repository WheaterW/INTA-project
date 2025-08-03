Overview of ND
==============

Overview of ND

#### Definition

The Neighbor Discovery Protocol (NDP) in IPv6 is an enhancement of the Address Resolution Protocol (ARP) and ICMP Router Discovery Protocol (IRDP) in IPv4. It uses ICMPv6 messages to implement functions, such as router discovery, duplicate address detection (DAD), address resolution, and neighbor unreachability detection (NUD).


#### Purpose

If two hosts need to communicate, the sender must know the receiver's MAC address in addition to its network-layer IPv6 address. This is because IPv6 datagrams must be encapsulated with MAC addresses before they can be transmitted over the physical network. NDP is used to map the receiver's IPv6 address to its MAC address.