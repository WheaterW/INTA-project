Overview of RIPng
=================

Routing Information Protocol next generation (RIPng) implements interworking between small- and medium-sized IPv6 networks.

#### Definition

RIPng is an extension of RIP version 2 (RIP-2) on IPv6 networks. As such, most RIP concepts apply to RIPng.

RIPng is a routing protocol based on the Distance Vector (D-V) algorithm and measures the distance (metric or cost) to the destination host by hop count. RIPng defines that the hop count from a device to its directly connected network is 0, and the hop count from a device to a network that is reachable through one device is 1, further incrementing in this manner. When the hop count reaches 16, the destination network or host is defined as unreachable.

RIPng is derived from RIP and applies to IPv6 networks. Unlike RIP, RIPng has the following characteristics:

* UDP port number: RIPng uses UDP port 521 (RIP-2 uses UDP port 520) to send and receive routing information.
* Multicast address: FF02::9 is used as the link-local multicast address of a RIPng device.
* Prefix length: The prefix length (mask length) of a destination address is 128 bits.
* Next-hop address: A next-hop address is a 128-bit IPv6 address.
* Source address: The link-local address FE80::/10 is used as the source address for sending RIPng Update messages.

#### Purpose

RIPng is an extension of RIP for support of IPv6.