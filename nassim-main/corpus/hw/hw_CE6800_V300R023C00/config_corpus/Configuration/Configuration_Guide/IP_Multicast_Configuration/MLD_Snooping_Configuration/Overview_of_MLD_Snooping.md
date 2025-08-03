Overview of MLD Snooping
========================

Overview of MLD Snooping

#### Definition

Multicast listener discovery (MLD) snooping is a basic IPv6 Layer 2 multicast function. It optimizes multicast traffic forwarding on Layer 2 devices and implements multicast data forwarding and control on Layer 2 devices.

![](../public_sys-resources/note_3.0-en-us.png) 

When both Layer 2 and Layer 3 multicast services are running on a device, it is recommended that the Layer 2 multicast configuration be the same as the Layer 3 multicast configuration. Otherwise, Layer 2 multicast inherits the Layer 3 multicast configuration, causing the Layer 2 multicast configuration to become invalid.



#### Purpose

In most cases, multicast messages must pass through Layer 2 switching devices, especially on a Layer 2 switching network. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001372911321__fig8606326171418), DeviceB is not configured with MLD snooping. DeviceB is connected to DeviceA through interface 10. User A and User B send MLD Report messages to the network, requesting to join a multicast group. When DeviceA receives traffic for this multicast group, it forwards the traffic to the switching network, which then forwards the traffic to UserA and UserB. The Layer 2 DeviceB, however, floods unicast frames with an unknown destination MAC address, multicast frames, or broadcast frames received in a VLAN in the same VLAN by default. Assuming that interface1, interface2, and interface3 belong to the same VLAN, DeviceB forwards such frames through all these interfaces. As a result, in addition to members of the multicast group, the traffic is sent to UserC, which is not a member of the multicast group, wasting network bandwidth and decreasing device performance.

After MLD snooping is deployed on DeviceB, DeviceB parses the MLD Report messages sent by UserA and UserB before forwarding them to DeviceA. DeviceB then associates the multicast group address with interface1 and interface2 to create Layer 2 forwarding entries. In this case, DeviceB forwards the multicast traffic received from DeviceA through interface1 and interface2 according to entries in the Layer 2 forwarding table. In this case, the multicast traffic is not sent to UserC, which is not a member of the multicast group. This demonstrates how MLD snooping enables DeviceB to forward multicast traffic only through interfaces that connect to multicast receivers. In conclusion:

* If MLD snooping is not enabled, DeviceB broadcasts multicast data at the data link layer.
* If MLD snooping is enabled, DeviceB does not broadcast multicast data at the data link layer. Instead, it determines the forwarding interfaces (connected to multicast receivers) according to entries in the Layer 2 multicast forwarding table and then forwards multicast traffic only through the forwarding interfaces (interface1 and interface2 in this example). This ensures that the multicast traffic is not forwarded to users who do not request it.

**Figure 1** Multicast traffic forwarding before and after MLD snooping is deployed on a Layer 2 device  
![](figure/en-us_image_0000001495707389.png)

#### Benefits

MLD snooping implements on-demand multicast data forwarding at the data link layer and offers the following benefits:

* Reduces network bandwidth consumption.
* Improves multicast data security.
* Reduces the performance pressure of upstream Layer 3 devices.
* Helps ensure the service quality of users.