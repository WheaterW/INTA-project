IGMPv1
======

IGMPv1 mainly uses the query-report mechanism to manage multicast groups. If there are multiple multicast devices on a network segment, all of them can receive Report messages from hosts. Therefore, only one multicast device needs to be selected to send Query messages. This multicast device is called the IGMP querier. In IGMPv1, Protocol Independent Multicast (PIM) elects a unique assert winner or designated router (DR) as the IGMP querier, which queries group memberships on the local network segment.

#### IGMPv1 Messages

An IGMPv1 message is encapsulated in an IP packet and consists of eight bytes. IGMPv1 defines two types of messages:

* General Query: sent by a querier to all hosts on a shared network to learn which multicast groups have members.
* Report: sent by a host to a querier to request to join a multicast group or respond to a Query message.

[Figure 1](#EN-US_CONCEPT_0000001176743865__fig_dc_fd_igmp_100601) shows the format of an IGMPv1 message, and [Table 1](#EN-US_CONCEPT_0000001176743865__tab_dc_fd_igmp_100601) describes the fields in this message.

**Figure 1** IGMPv1 message format  
![](figure/en-us_image_0000001130624436.png)

**Table 1** Fields in an IGMPv1 message
| Field | Description |
| --- | --- |
| Version | IGMP version. The value is 1. |
| Type | Message type. This field can be set to either of the following values:   * 0x1: General Query message * 0x2: Report message |
| Unused | In IGMPv1, this field is set by the sender to 0 and is ignored by the receiver. |
| Checksum | Checksum. |
| Group Address | Multicast group address. In a General Query message, this field is set to 0. In a Report message, this field is set to the address of the multicast group that the member joins. |



#### IGMPv1 Working Mechanism

On the multicast network shown in [Figure 2](#EN-US_CONCEPT_0000001176743865__fig_03), Source is the multicast source that sends multicast data. DeviceA and DeviceB are connected to three receivers on the same network segment: HostA, HostB, and HostC. DeviceA is the IGMP querier. HostA and HostB want to receive data sent to multicast group G1, and HostC wants to receive data sent to multicast group G2.

**Figure 2** Multicast network  
![](figure/en-us_image_0000001176663985.png)

IGMPv1 involves three mechanisms: multicast group member query mechanism, member join mechanism, and member leave mechanism.

**Multicast group member query mechanism**

As shown in [Figure 3](#EN-US_CONCEPT_0000001176743865__fig_01), the IGMP querier knows which multicast groups have members on the local network segment by querying multicast group members.

**Figure 3** IGMP query and report  
![](figure/en-us_image_0000001130624440.png)

The general query and report process is as follows:

1. The IGMP querier sends a General Query message, with the destination address 224.0.0.1 (indicating all hosts and devices on the same network segment). All group members start a timer when they receive this message.
   
   General Query messages are sent at an interval, which can be configured using a command. HostA and HostB are members of G1. After receiving General Query messages, they start Timer-G1 locally.
2. The group member whose timer expires first sends a Report message for the group.
   
   If Timer-G1 on HostA expires first, HostA sends a Report message with the destination address G1 to the network segment. When HostB, which also wants to join G1, receives the Report message, it stops Timer-G1 and does not send a Report message for G1. This suppresses Report messages, reducing traffic on the network segment.
3. After receiving the Report message from HostA, the IGMP querier checks that G1 has members on the local network segment, and uses a multicast routing protocol to create an (\*, G1) entry, in which \* stands for any multicast source. Once DeviceA receives data sent to G1, it forwards the data to this network segment.

**Member join mechanism**

As shown in [Figure 4](#EN-US_CONCEPT_0000001176743865__fig_02), HostC sends a Report message to the querier to join the multicast group.

**Figure 4** Member join  
![](figure/en-us_image_0000001176743895.png)

HostC joins G2 as follows:

1. HostC proactively sends a Report message for G2 without waiting for a General Query message.
2. After receiving the Report message from HostC, the IGMP querier checks that a member of G2 has connected to the local network segment, and generates an (\*, G2) entry. Once DeviceA receives data sent to G2, it forwards the data to this network segment.

**Member leave mechanism**

IGMPv1 does not define a Leave message. After a host leaves a multicast group, it stops sending Report messages. The processing mechanism varies according to whether other members exist in the multicast group that the host wants to leave. In [Figure 2](#EN-US_CONCEPT_0000001176743865__fig_03):

* If HostA wants to leave G1
  
  When HostA receives a General Query message from the IGMP querier, it does not send a Report message for G1. On the network segment, G1 has another member HostB, which sends a Report message for G1 to the IGMP querier. In this case, the IGMP querier does not know that HostA has left.
* If HostC wants to leave G2
  
  When HostC receives a General Query message from the IGMP querier, it does not send a Report message for G2. Because G2 has no other members on the network segment, the IGMP querier does not receive a Report message for G2. After a certain period (130 seconds by default), the IGMP querier deletes the multicast forwarding entry corresponding to G2.