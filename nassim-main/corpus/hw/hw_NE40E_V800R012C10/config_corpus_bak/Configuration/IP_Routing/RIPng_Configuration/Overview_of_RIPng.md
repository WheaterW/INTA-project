Overview of RIPng
=================

RIPng protocol can implement the interworking of small
and medium-sized networks.

#### Definition

RIP next generation (RIPng) is an extension to RIP version 2 (RIP-2)
on IPv6 networks. Most RIP concepts apply to RIPng.

RIPng is
a distance-vector routing protocol, which measures the distance (metric
or cost) to the destination host by the hop count. In RIPng, the hop
count from a device to its directly connected network is 0, and the
hop count from a device to a network that is reachable through another
device is 1. When the hop count is equal to or exceeds 16, the destination
network or host is defined as unreachable.

To be applied on
IPv6 networks, RIPng makes the following changes to RIP:

* UDP port number: RIPng uses UDP port number 521 to send and
  receive routing information.
* Multicast address: RIPng uses FF02::9 as the link-local multicast
  address of a RIPng device.
* Prefix length: RIPng uses a 128-bit (the mask length) prefix
  in the destination address.
* Next hop address: RIPng uses a 128-bit IPv6 address.
* Source address: RIPng uses link-local address FE80::/10 as
  the source address to send RIPng Update packets.

#### Purpose

RIPng is an extension to RIP for support of IPv6.