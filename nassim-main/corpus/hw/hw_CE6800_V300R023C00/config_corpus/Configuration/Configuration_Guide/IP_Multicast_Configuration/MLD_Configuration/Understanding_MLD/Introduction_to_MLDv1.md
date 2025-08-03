Introduction to MLDv1
=====================

The working mechanism of MLDv1 is the same as that of IGMPv2. MLDv1 defines querier election, general query and report, member join, and member leave mechanisms.

The MLD querier periodically sends a General Query message to all hosts and multicast devices on the local network segment and maintains memberships based on Multicast Listener Report messages from the hosts. When receiving a Multicast Listener Done message, the MLD querier sends a Multicast Address Specific Query message to check whether the group has other members in the network segment. If the MLD querier does not receive any Multicast Listener Report message for the group within a specified period, it no longer maintains the membership of the group. The MLD querier determines whether to forward multicast data packets to the network segment based on memberships.

#### MLDv1 Messages

MLDv1 defines the following messages:

* General Query: sent by a querier to all hosts and devices on a shared network to learn which multicast groups have members.
* Multicast Address Specific Query: sent by a querier to a specified multicast group on the shared network segment to check whether the group has members.
* Multicast Listener Report: sent by a host to a querier to request to join a multicast group or respond to a Query message.
* Multicast Listener Done: sent by a host to notify the querier that it has left a multicast group.

To simplify the description, the preceding message types are referred to simply as "Query," "Report," and "Done."

[Figure 1](#EN-US_CONCEPT_0000001589256121__fig_06) shows the format of an MLDv1 message, and [Table 1](#EN-US_CONCEPT_0000001589256121__tab_01) describes the fields in this message.

**Figure 1** Format of an MLDv1 message  
![](images/fig_dc_fd_mld_100506.png)

**Table 1** Fields in an MLDv1 message
| Field | Description |
| --- | --- |
| Type | Message type. This field can be set to any of the following values:   * 130: Query message. MLDv1 Query messages include General Query and Multicast Address Specific Query messages. * 131: Multicast Listener Report message. * 132: Multicast Listener Done message. |
| Code | This field is set by the sender to 0 and is ignored by the receiver. |
| Checksum | Standard ICMPv6 checksum. It covers the entire MLD message plus a pseudo header of IPv6 header fields. The Checksum field is set to 0 during checksum calculation. The receiver must verify the checksum before processing the message. |
| Maximum Response Delay | Maximum response time. After receiving a General Query message from an MLD querier, a member host needs to respond to the message within the maximum response time. This field is valid only in MLD Query messages. |
| Reserved | Reserved field. This field is set by the sender to 0 and is ignored by the receiver. |
| Multicast Address | Multicast group address.   * In a General Query message, this field is set to 0. * In a Multicast Address Specific Query message, the value of this field is the IPv6 address of the multicast group to be queried. * In a Multicast Listener Report or Done message, the value of this field is the IPv6 address of the multicast group that a host wants to join or leave. |



#### MLDv1 Working Mechanism

On the IPv6 multicast network shown in [Figure 2](#EN-US_CONCEPT_0000001589256121__fig1796543214713), DeviceA and DeviceB connect to the network segment with three receivers: HostA, HostB, and HostC. HostA and HostB want to receive data sent to multicast group G1, and HostC wants to receive data sent to multicast group G2.**Figure 2** IPv6 PIM network  
![](images/fig_dc_fd_mld_100501.png)

MLDv1 defines querier election, general query and report, member join, and member leave mechanisms.

**Querier election mechanism**

On a network segment with multiple IPv6 multicast devices, all these devices can receive Multicast Listener Report messages from hosts. Therefore, only one multicast device needs to be selected to send Query messages. This multicast device is called the MLD querier.

**Figure 3** Querier election  
![](images/fig_dc_fd_mld_100502.png)

As shown in [Figure 3](#EN-US_CONCEPT_0000001589256121__fig1020617238513), the querier election process is as follows:

1. In the initial state, all MLD multicast devices (DeviceA and DeviceB) consider themselves queriers and send General Query messages to all hosts and multicast devices on the local network segment. After multicast devices receive a General Query message from each other, they compare the source IPv6 address of the message with their own interface addresses. The multicast device with the smallest IPv6 address becomes the querier, and the other multicast devices become non-queriers.
   
   As shown in [Figure 3](#EN-US_CONCEPT_0000001589256121__fig1020617238513), the interface address of DeviceA is smaller than that of DeviceB, meaning that DeviceA is elected as the querier, and DeviceB is elected as the non-querier.
2. The MLD querier (DeviceA) sends General Query messages to all hosts and other multicast devices on the local network segment, whereas the non-querier (DeviceB) no longer sends General Query messages.
   
   DeviceB starts the Other Querier Present timer. If DeviceB receives a Query message from the querier before the timer expires, it resets the timer; otherwise, it considers the original querier invalid and triggers querier election.

**General query and report mechanism**

By sending General Query messages and receiving Multicast Listener Report messages, an MLD querier learns which multicast groups have members on the local network segment.

**Figure 4** General query and report  
![](images/fig_dc_fd_mld_100503.png)

As shown in [Figure 4](#EN-US_CONCEPT_0000001589256121__fig_03), the general query and report process is as follows:

1. The MLD querier sends a General Query message, with destination address FF02::1 (indicating all hosts and devices on the same network segment). All group members start a timer when they receive this message.
   
   General Query messages are sent at an interval, which can be set using a command. By default, they are sent every 125 seconds. HostA and HostB are members of G1 and start Timer-G1 locally. By default, the value of the timer ranges from 0 to 10 seconds.
2. The group member whose timer expires first sends a Multicast Listener Report message for the group.
   
   If Timer-G1 on HostA expires first, HostA sends a Multicast Listener Report message with the destination address G1 to the network segment. When HostB receives the Multicast Listener Report message, it stops Timer-G1 and does not send a Multicast Listener Report message for G1. This suppresses Multicast Listener Report messages, reducing the number of MLD messages on the network segment.
3. After receiving the Multicast Listener Report message from HostA, the MLD querier checks that G1 has members on the local network segment. The querier then uses an IPv6 multicast routing protocol to create an (\*, G1) entry, in which \* stands for any IPv6 multicast source. Once the querier receives data sent to G1, it forwards the data to this network segment.

**Member join mechanism**

When a host on the shared network segment wants to join a multicast group, it sends a Multicast Listener Report message to an MLD querier without waiting for a General Query message.

**Figure 5** Member join  
![](images/fig_dc_fd_mld_100504.png)

As shown in [Figure 5](#EN-US_CONCEPT_0000001589256121__fig_04), the IPv6 host HostC joins multicast group G2 through the following process:

1. HostC proactively sends a Multicast Listener Report message for G2 without waiting for a General Query message.
2. After receiving the Multicast Listener Report message from HostC, the MLD querier checks that a member of G2 has connected to the local network segment. The querier then generates an (\*, G2) entry. Once the querier receives data sent to G2, it forwards the data to this network segment.

**Member leave mechanism**

This mechanism enables an MLD querier to quickly discover which groups have no members on the network segment so that group memberships can be quickly updated and redundant multicast traffic reduced on the network.

**Figure 6** Member leave  
![](images/fig_dc_fd_mld_100505.png)

As shown in [Figure 6](#EN-US_CONCEPT_0000001589256121__fig_05), the IPv6 host HostA leaves multicast group G1 through the following process:

1. HostA sends a Multicast Listener Done message for G1 to all multicast devices on the local network segment. The destination address of the message is FF02::2.
2. After receiving the Multicast Listener Done message, the querier sends a Multicast Address Specific Query message for G1. The sending interval and count are configurable (the default values are 1 second and twice, respectively). In addition, the querier starts Timer-Membership (its length is the sending interval multiplied by the sending count).
3. G1 has the other member (HostB) on the network segment. After receiving a Multicast Address Specific Query message from the querier, this member immediately sends a Multicast Listener Report message for G1. The querier continues maintaining the membership of G1 after receiving the Multicast Listener Report message.
   
   If G1 has no other members on the network segment, the querier does not receive any Multicast Listener Report message for G1. When Timer-Membership expires, the querier deletes the (\*, G1) entry. Thereafter, if the querier receives multicast data sent to G1, it does not forward the data downstream.