Understanding Static MLD Snooping
=================================

Understanding Static MLD Snooping

#### Context

Multicast data can be transmitted to user terminals in either dynamic or static multicast mode over an IP bearer network. [Table 1](#EN-US_CONCEPT_0000001321630870__table250121274716) compares the two modes.

**Table 1** Comparison between the dynamic and static multicast modes
| Mode | Description | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Dynamic multicast mode | A device receives and delivers a multicast group's traffic only after receiving the first join request from the group. The device stops receiving the traffic after the last member leaves the group. | Network traffic is always minimized, saving network resources and bandwidth. | Users may experience a network delay when joining a new multicast group. |
| Static multicast mode | Multicast forwarding entries are configured for each multicast group on a device. A multicast group's data is delivered to the device, regardless of whether users request the data from this device. | Because multicast routes are fixed, multicast paths always exist, regardless of whether there is multicast data. This means that group switching is fast, ensuring good user experience.  Multicast source and group ranges are easy to manage because multicast paths are relatively stable.  The delay in first data forwarding is short because no dynamic multicast routing process is involved. | Each device on a multicast data transmission path must be manually configured, involving a heavy configuration workload.  Multicast forwarding paths may be sub-optimal because downstream and upstream ports need to be manually specified on each device.  When the network topology or unicast routes change, static multicast paths may need to be reconfigured. This involves a heavy configuration and management workload.  Multicast routes exist even when no multicast data needs to be forwarded. This wastes network resources and creates high bandwidth requirements. |

A Layer 2 multicast forwarding table can be dynamically built using MLD snooping or be manually configured. Choose whether to use the dynamic or static multicast mode depending on the required network quality level and service types.

If hosts require data of a specific multicast group from a router port for an extended period of time and network bandwidth is sufficient, static Layer 2 multicast can be deployed to implement stable multicast data transmission within a network range.


#### Related Concepts

Static router ports or member ports are used in static Layer 2 multicast.

* Static router ports are used to receive multicast traffic steadily.
* Static member ports are used to send data of a specified multicast group address steadily.

#### Benefits

After static Layer 2 multicast is deployed on a device, the device does not age out its multicast entries, ensuring that users can steadily receive specified multicast group data. It offers the following benefits:

* Simplified management
* Reduced network delays
* Improved information security by preventing unregistered users from receiving data and protocol messages