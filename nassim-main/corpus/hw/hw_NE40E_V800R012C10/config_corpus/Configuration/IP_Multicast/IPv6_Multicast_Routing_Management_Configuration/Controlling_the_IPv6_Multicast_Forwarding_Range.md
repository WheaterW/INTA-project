Controlling the IPv6 Multicast Forwarding Range
===============================================

Multicast data for each multicast group on an IPv6 network needs to be transmitted in a certain range. You can control the IPv6 multicast forwarding range by setting a minimum TTL value for IPv6 multicast packets or an IPv6 multicast forwarding boundary.

#### Usage Scenario

Multicast data for each multicast group on an IPv6 network needs to be transmitted in a certain range. The NE40E supports the following methods for controlling the IPv6 multicast forwarding range:

* Configure an IPv6 multicast forwarding boundary on an interface to form a closed multicast forwarding area. After an interface is configured with a forwarding boundary for a specific group, the interface does not forward or receive any IPv6 multicast packet for this group.
* Set a minimum TTL value for IPv6 multicast packets to restrict the transmission distance of IPv6 multicast packets. The interface forwards only the IPv6 multicast packets with the TTL value being greater than or equal to the minimum TTL value. If the TTL value of a packet is smaller than the minimum TTL value, the interface discards the packet.

#### Pre-configuration Tasks

Before controlling the IPv6 multicast forwarding range, complete the following tasks:

* Configure an IPv6 unicast routing protocol to ensure that IPv6 unicast routes are reachable.
* Configure basic IPv6 multicast functions.


[Setting a Minimum TTL Value for IPv6 Multicast Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_ipv6_cfg_0008.html)

Multicast data for each multicast group on an IPv6 network needs to be transmitted in a certain range. You can control the IPv6 multicast forwarding range by setting a minimum TTL value for IPv6 multicast packets.

[Configuring an IPv6 Multicast Forwarding Boundary](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_ipv6_cfg_0009.html)

After an interface is configured with a forwarding boundary for a specific group, the interface does not forward or receive any IPv6 multicast packet for this group.