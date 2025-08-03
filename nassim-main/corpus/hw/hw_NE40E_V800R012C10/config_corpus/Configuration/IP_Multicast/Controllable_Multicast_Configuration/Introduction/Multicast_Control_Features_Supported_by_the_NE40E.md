Multicast Control Features Supported by the NE40E
=================================================

This section describes implementation mechanism of controllable multicast and the functions of multicast list, multicast profile, and multicast replication.

#### Implementation

The Router provides an AAA-based controllable multicast mechanism. By applying a multicast profile in an AAA domain, carriers can control the multicast rights of users.


#### Multicast Program List

A multicast program list matches one or more multicast addresses. For example, 224.1.1.1/30 indicates four multicast addresses: 224.1.1.0, 224.1.1.1, 224.1.1.2, and 224.1.1.3. These multicast addresses are channels or programs of the IPTV service.


#### Multicast Profile

The multicast profile is a frame that defines the multicast rights of users. A multicast profile is a collection of a series of multicast program lists. One multicast profile may contain several multicast program lists, and one multicast program list may be contained in several multicast profiles.

The rights of all the multicast users are controlled by multicast profiles. Each user has a profile. The Router checks the following profiles one by one to determine the profile matching a user (the latter profile overwrites the previous profile):

* Profile used by the home domain of a user
* Profile delivered by the RADIUS server
* Profile used at the access interface of a user

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The RADIUS server delivers only the names of the profiles.
* For the configurations on the RADIUS server, refer to the configuration guides of the servers. You need to configure two servers on the Router only.


#### Multicast Copy

Generally, the Router replicates a copy of multicast traffic of a multicast group to each physical interface only. Then the Layer 2 device replicates the multicast traffic to each member in the multicast group.

In most cases, a BAS interface connects to multiple users. To reduce the traffic replication workload, the Router supports the following multicast traffic replication modes:

* Replication by session
* Replication by multicast VLAN
* Replication by interface + VLAN
* Replication by interface

If the Router's downstream Layer 2 device does not provide IGMP snooping for user identification, configure multicast replication by session on the Router's interface connected to the downstream Layer 2 device. After the configuration is complete, the Router directly copies multicast packets to each user session.

Because the Router's downstream Layer 2 device cannot parse PPPoE sessions, you must configure multicast replication by session on the Router's interface for PPPoE users.

If multiple IPoX users order the same program from the same VLAN on an interface and IGMP snooping is enabled on the NE40E's downstream Layer 2 device, configure multicast replication by interface + VLAN to reduce the NE40E's copy burden. After the configuration is complete, the NE40E copies only one multicast packet to this interface. The interface copies the packet to its directly connected Layer 2 device. The downstream Layer 2 device then copies the packet to the IPoX users.