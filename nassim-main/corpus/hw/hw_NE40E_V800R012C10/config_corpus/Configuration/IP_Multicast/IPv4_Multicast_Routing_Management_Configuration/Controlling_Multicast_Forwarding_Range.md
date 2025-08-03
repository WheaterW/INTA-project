Controlling Multicast Forwarding Range
======================================

Multicast data for each multicast group on a network needs to be transmitted in a certain range. You can control the multicast forwarding range by setting a minimum TTL value for multicast packets or a multicast forwarding boundary.

#### Usage Scenario

Multicast data for each multicast group on a network needs to be transmitted in a specific range. The NE40E supports the following methods for controlling multicast forwarding range:

* Configure a multicast forwarding boundary on an interface to form a closed multicast forwarding area. After an interface is configured with a forwarding boundary for a specific group, the interface does not forward or receive any multicast packet for this group.
* Set a minimum TTL value for multicast packets on an interface to restrict the transmission distance of multicast packets. The interface forwards only the multicast packets (including packets generated on the local device) with the TTL value being greater than or equal to the minimum TTL value. If the TTL value of a packet is smaller than the minimum TTL value, the interface discards the packet.

#### Pre-configuration Tasks

Before controlling the multicast forwarding range, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* Configure basic multicast functions.


[Adjusting the Minimum TTL Value for Multicast Forwarding](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0086.html)

Multicast information of each multicast group on a network should be transmitted within a specific range. Therefore, setting the minimum TTL value for multicast forwarding is necessary for limiting the multicast data forwarding scope.

[Configuring the Multicast Forwarding Boundary](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2173.html)

When an interface of a multicast device is configured with a forwarding boundary for a specified group, the forwarding scope of multicast packets is restricted.