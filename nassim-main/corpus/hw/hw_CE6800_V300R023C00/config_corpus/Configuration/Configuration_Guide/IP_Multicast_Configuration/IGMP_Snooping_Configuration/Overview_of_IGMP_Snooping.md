Overview of IGMP Snooping
=========================

Overview of IGMP Snooping

#### Definition

Internet Group Management Protocol (IGMP) snooping is a basic Layer 2 multicast function. It optimizes multicast traffic forwarding and implements multicast data forwarding and control on Layer 2 devices.

![](../public_sys-resources/note_3.0-en-us.png) 

When both Layer 2 and Layer 3 multicast services are running on a device, it is recommended that the Layer 2 multicast configuration be the same as the Layer 3 multicast configuration. Otherwise, Layer 2 multicast inherits the Layer 3 multicast configuration, causing the Layer 2 multicast configuration to become invalid.



#### Purpose

In most cases, multicast messages must pass through Layer 2 switching devices, especially on a Layer 2 switching network. [Figure 1](#EN-US_CONCEPT_0000001130622116__fig8606326171418) shows multicast message forwarding before and after IGMP snooping is deployed on DeviceB, which is an Ethernet Layer 2 device. DeviceB is connected to DeviceA through interface10, and is also connected to some users. Among these users, UserA and UserB are members of a multicast group and send IGMP Report messages to join the group. When DeviceA receives traffic for this multicast group, it forwards the traffic to the switching network, which then forwards the traffic to UserA and UserB. The Layer 2 DeviceB, however, floods unicast frames with an unknown destination MAC address, multicast frames, or broadcast frames received in a VLAN in the same VLAN by default. Assuming that interface1, interface2, and interface3 belong to the same VLAN, DeviceB forwards such frames through all these interfaces. As a result, in addition to members of the multicast group, the traffic is sent to UserC, which is not a member of the multicast group, wasting network bandwidth and decreasing device performance.

After IGMP snooping is deployed on DeviceB, DeviceB parses the IGMP Report messages sent by UserA and UserB before forwarding them to DeviceA. DeviceB then associates the multicast group address with interface1 and interface2 to create Layer 2 forwarding entries. In this case, DeviceB forwards the multicast traffic received from DeviceA through interface1 and interface2 according to entries in the Layer 2 forwarding table. In this case, the multicast traffic is not sent to UserC, which is not a member of the multicast group. This demonstrates how IGMP snooping enables DeviceB to forward multicast traffic only through interfaces that connect to multicast receivers. In conclusion:

* If IGMP snooping is not enabled, DeviceB broadcasts multicast data at the data link layer.
* If IGMP snooping is enabled, DeviceB does not broadcast multicast data at the data link layer. Instead, it determines the forwarding interfaces (connected to multicast receivers) according to entries in the Layer 2 multicast forwarding table and then forwards multicast traffic only through the forwarding interfaces (interface1 and interface2 in this example). This ensures that the multicast traffic is not forwarded to users who do not request it.

**Figure 1** Multicast traffic forwarding before and after IGMP snooping is deployed on a Layer 2 device  
![](figure/en-us_image_0000001130622140.png)

#### Benefits

IGMP snooping implements on-demand multicast data forwarding at the data link layer and offers the following benefits:

* Reduces network bandwidth consumption.
* Improves multicast data security.
* Reduces the performance pressure of upstream Layer 3 devices.
* Helps ensure the service quality of users.