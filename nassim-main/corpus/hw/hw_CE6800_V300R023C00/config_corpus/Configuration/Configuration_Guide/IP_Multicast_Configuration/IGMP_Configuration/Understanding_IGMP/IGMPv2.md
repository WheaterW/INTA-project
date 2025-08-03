IGMPv2
======

The working mechanism of IGMPv2 is similar to that of IGMPv1, and a major difference between them is that IGMPv2 adds the querier election and member leave mechanisms. IGMPv2 enables an IGMP querier to promptly know the groups that have no members on the network segment, updating group memberships quickly and reducing redundant multicast traffic on the network.

#### IGMPv2 Messages

IGMPv2 differs from IGMPv1 in the following:

* In addition to General Query and Report messages, IGMPv2 defines two new messages:
  + Leave message: sent by a host to notify the querier that it has left a multicast group.
  + Group-Specific Query message: sent by a querier to a specified multicast group on the shared network segment to check whether the group has members.
* IGMPv2 also improves the format of a General Query message by adding the Max Response Time field. The value of this field can be configured using a command to control the response speed of members to Query messages.

[Figure 1](#EN-US_CONCEPT_0000001176663975__fig_dc_fd_igmp_100701) shows the format of an IGMPv2 message, and [Table 1](#EN-US_CONCEPT_0000001176663975__tab_dc_fd_igmp_100701) describes the fields in this message.

**Figure 1** IGMPv2 message format  
![](figure/en-us_image_0000001130624468.png)

**Table 1** Fields in an IGMPv2 message
| Field | Description |
| --- | --- |
| Type | Message type. This field can be set to any of the following values:   * 0x11: Query message. IGMPv2 Query messages include General Query and Group-Specific Query messages. * 0x12: IGMPv1 Report message. * 0x16: IGMPv2 Report message. * 0x17: Leave message. |
| Max Response Time | Maximum response time. After receiving a General Query message from an IGMP querier, a member host needs to respond to the message within the maximum response time. This field is valid only in IGMP Query messages. |
| Checksum | Checksum. |
| Group Address | Multicast group address.   * In a General Query message, this field is set to 0. * In a Group-Specific Query message, the value of this field is the address of the multicast group to be queried. * In a Report or Leave message, the value of this field is the address of the multicast group that a host wants to join or leave. |



#### IGMPv2 Working Mechanism

Compared with IGMPv1, IGMPv2 adds the querier election and member leave mechanisms.

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001176663975__fig15519328504), DeviceA and DeviceB connect to the network segment with three receivers: HostA, HostB, and HostC. HostA and HostB want to receive data sent to multicast group G1, and HostC wants to receive data sent to multicast group G2.**Figure 2** Multicast network  
![](figure/en-us_image_0000001130624458.png)

The following describes the querier election and member leave mechanisms.

**Querier election mechanism**

As shown in [Figure 3](#EN-US_CONCEPT_0000001176663975__fig_01), IGMPv2 uses an independent querier election mechanism. If multiple multicast devices are available on a shared network segment, the device with the smallest IP address is elected as the querier.

**Figure 3** Querier election  
![](figure/en-us_image_0000001176664007.png)

In IGMPv2, the querier election process is as follows:

1. In the initial state, all IGMPv2 multicast devices (DeviceA and DeviceB) consider themselves queriers and send General Query messages to all hosts and multicast devices on the local network segment. After DeviceA and DeviceB receive a General Query message from each other, they compare the source IP address of the message with their own interface addresses. This ensures that the multicast device with the smallest IP address becomes the querier, and the other multicast devices become non-queriers. As shown in [Figure 3](#EN-US_CONCEPT_0000001176663975__fig_01), the interface address of DeviceA is smaller than that of DeviceB. Therefore, DeviceA is elected as the querier, and DeviceB is elected as the non-querier.
2. The IGMP querier (DeviceA) sends General Query messages to all hosts and other multicast devices on the local network segment, whereas the non-querier (DeviceB) no longer sends General Query messages.
   
   DeviceB starts the other querier present timer. If DeviceB receives a Query message from the querier before the timer expires, it resets the timer; otherwise, it considers the original querier invalid and triggers querier election.

**Member leave mechanism**

As shown in [Figure 4](#EN-US_CONCEPT_0000001176663975__fig_02), in IGMPv2, when a member leaves a multicast group, it proactively sends a Leave message to the querier to notify that it has left the multicast group.

**Figure 4** Member leave  
![](figure/en-us_image_0000001130624466.png)

HostA leaves G1 as follows:

1. HostA sends a Leave message for G1 to all multicast devices on the local network segment. The destination address of the Leave message is 224.0.0.2.
2. After receiving the Leave message, the querier sends a Group-Specific Query message for G1. The sending interval and count are configurable, and the default values are 1 second and twice. In addition, the querier starts Timer-Membership (its length is the sending interval multiplied by the sending count).
3. Assume that G1 has other members (such as HostB) on the network segment. After receiving Group-Specific Query messages from the querier, these members immediately send Report messages for G1. The querier continues maintaining the membership of G1 after receiving the Report messages. If G1 has no other members on the network segment, the querier does not receive any Report message for G1. When Timer-Membership expires, the querier deletes the (\*, G1) entry. Thereafter, if the querier receives multicast data sent to G1, it does not forward the data downstream.