Introduction to MLDv2
=====================

MLDv1 messages carry only multicast group information â they do not carry multicast source information. As such, MLDv1 hosts can only select the groups they want to join and cannot select the multicast sources from which they want to receive multicast data. MLDv2 resolves this problem by allowing hosts to select both multicast groups and multicast sources. Unlike MLDv1 Multicast Listener Report messages that carry information about only one multicast group, MLDv2 Multicast Listener Report messages can carry information about multiple multicast groups. This significantly reduces the number of messages transmitted between hosts and a querier.

#### MLDv2 Messages

Compared with MLDv1 messages, MLDv2 messages have the following changes:

* MLDv2 defines two message types: Query messages and Multicast Listener Report messages. In MLDv2, no Multicast Listener Done message is defined. Instead, group members send a specified type of Report message to notify multicast devices that they are leaving a group.
* In addition to General Query and Multicast Address Specific Query messages, MLDv2 defines a new Query message type: Multicast Address and Source Specific Query. A querier sends this message to members in a specific multicast group on a shared network segment to check whether the members want to receive data from specific sources. A Multicast Address and Source Specific Query message carries one or more multicast source addresses.
* A Multicast Listener Report message contains both the multicast group that a host wants to join and the multicast sources from which the host wants to receive data. MLDv2 supports source filtering and defines filtering modes INCLUDE and EXCLUDE. Group-source mappings are represented by (G, INCLUDE, (S1, S2...)) or (G, EXCLUDE, (S1, S2...)). The (G, INCLUDE, (S1, S2...)) entry indicates that a host wants to receive data sent from the listed multicast sources to group G. The (G, EXCLUDE, (S1, S2...)) entry indicates that a host wants to receive data sent from all multicast sources (except the listed ones) to group G. If group-source mappings change, hosts add these changes to the Multicast Address Record fields in MLDv2 Multicast Listener Report messages and send the messages to the MLD querier.

[Figure 1](#EN-US_CONCEPT_0000001589496149__fig14752143817291) shows the format of an MLDv2 Query message, and [Table 1](#EN-US_CONCEPT_0000001589496149__tab_01) describes the fields in this message.

**Figure 1** Format of an MLDv2 Query message  
![](images/fig_dc_fd_mld_100601.png)

**Table 1** Fields in an MLDv2 Query message
| Field | Description |
| --- | --- |
| Type | Message type. In MLDv2 Query messages, this field is set to 130. MLDv2 Query messages include General Query, Multicast Address Specific Query, and Multicast Address and Source Specific Query messages. |
| Code | This field is set by the sender to 0 and is ignored by the receiver. |
| Checksum | Standard ICMPv6 checksum. It covers the entire MLD message plus a pseudo header of IPv6 header fields. The Checksum field is set to 0 during checksum calculation. The receiver must verify the checksum before processing the message. |
| Maximum Response Code | Maximum response time. After receiving a General Query message from an MLD querier, a member host needs to respond to the message within the maximum response time. This field is valid only in MLD Query messages. |
| Reserved | Reserved field. This field is set by the sender to 0 and is ignored by the receiver. |
| Multicast Address | Multicast group address. In a General Query message, this field is set to 0. In a Multicast Address Specific Query or Multicast Address and Source Specific Query message, the value of this field is the address of the multicast group to be queried. |
| Resv | Reserved field. This field is set to 0 by the sender and is ignored by the receiver. |
| S | When this flag is set to 1, other devices receiving the Query message suppress timer updates. Such a Query message does not suppress the querier election or host-side processing on the devices. |
| QRV | A value other than 0 indicates the robustness variable of the querier (the value 0 indicates that the robustness variable of the querier is greater than 7). If a device finds that the value of this field in a received Query message is not 0, it sets its robustness variable to this value. If the value of this field is 0, it ignores this field. |
| QQIC | Query interval code of an MLD querier, in seconds. If a non-querier finds that the value of this field in a received Query message is not 0, it sets its query interval to this value. If the value of this field is 0, it ignores this field. |
| Number of Sources | Number of multicast sources in the message. For General Query and Multicast Address Specific Query messages, the value of this field is 0. For a Multicast Address and Source Specific Query message, the value of this field is not 0. This number is limited by the MTU of the network over which the message is transmitted. |
| Source Address | Multicast source address. Its quantity is limited by the value of the Number of Sources field. |

[Figure 2](#EN-US_CONCEPT_0000001589496149__fig07531738162911) shows the format of an MLDv2 Multicast Listener Report message, and [Table 2](#EN-US_CONCEPT_0000001589496149__tab_02) describes the fields in this message.

**Figure 2** Format of an MLDv2 Multicast Listener Report message  
![](images/fig_dc_fd_mld_100602.png)

**Table 2** Fields in an MLDv2 Multicast Listener Report message
| Field | Description |
| --- | --- |
| Type | Message type. In MLDv2 Multicast Listener Report messages, this field is set to 143. |
| Reserved | Reserved field. This field is set to 0 by the sender and is ignored by the receiver. |
| Checksum | Standard ICMPv6 checksum. It covers the entire MLD message plus a pseudo header of IPv6 header fields. The Checksum field is set to 0 during checksum calculation. The receiver must verify the checksum before processing the message. |
| Nr of Mcast Address Records | Number of multicast address records in the message. |
| Multicast Address Record | Multicast address record. [Figure 3](#EN-US_CONCEPT_0000001589496149__fig_03) shows the format of this field, and [Table 3](#EN-US_CONCEPT_0000001589496149__tab_03) describes the fields in this field. |


**Figure 3** Format of the Multicast Address Record field  
![](images/fig_dc_fd_mld_100603.png)

**Table 3** Fields in the Multicast Address Record field
| Field | Description |
| --- | --- |
| Record Type | Multicast address record type:  * Current-State Record: sent by a host to report its current state after receiving a Query message. This record type is one of the following two values:   + MODE\_IS\_INCLUDE: indicates that the host wants to receive multicast data sent from the listed source addresses to the group. The message is invalid if the source address list is empty.   + MODE\_IS\_EXCLUDE: indicates that the host does not want to receive multicast data sent from the listed source addresses to the group. * Filter-Mode-Change Record: sent by a host when the filter mode changes. This record type is one of the following two values:   + CHANGE\_TO\_INCLUDE\_MODE: indicates that the filter mode has changed from EXCLUDE to INCLUDE. The host wants to receive multicast data sent from the new sources in the source list to the group. If the specified source list is empty, the host will leave the multicast group.   + CHANGE\_TO\_EXCLUDE\_MODE: indicates that the filter mode has changed from INCLUDE to EXCLUDE. The host rejects multicast data sent from the new sources in the source list to the group. * Source-List-Change Record: sent by a host when the source list changes. This record type is one of the following two values:   + ALLOW\_NEW\_SOURCES: indicates that the source list contains additional sources from which the host wants to receive multicast data sent to the group. If the filter mode is INCLUDE, the sources are added to the existing source list. If the filter mode is EXCLUDE, the sources are deleted from the blocked source list.   + BLOCK\_OLD\_SOURCES: indicates that the source list contains the sources from which the host no longer wants to receive multicast data sent to the group. If the filter mode is INCLUDE, the sources are deleted from the source list. If the filter mode is EXCLUDE, the sources are added to the source list. |
| Aux Data Len | Auxiliary data length. MLDv2 Multicast Listener Report messages do not contain the Auxiliary Data field and therefore this field is set to 0. |
| Number of Sources | Number of source addresses in this group record. |
| Multicast Address | Multicast group address. |
| Sources Address | Multicast source address. |
| Auxiliary Data | Additional information in this address group record. MLDv2 Multicast Listener Report messages do not contain auxiliary data. |



#### MLDv2 Working Mechanism

Unlike MLDv1, MLDv2 allows hosts to select multicast sources.

**Group-and-source-specific join**

MLDv2 Multicast Listener Report messages have a destination address FF02::16, which represents all MLDv2-capable devices on the same network segment. A Multicast Listener Report message contains Multicast Address Record fields, allowing hosts to specify the multicast sources from which they do or do not want to receive data when joining a multicast group. As shown in [Figure 4](#EN-US_CONCEPT_0000001589496149__fig_04), two multicast sources S1 and S2 send data to multicast group G. The host only wants to receive data sent from S1 to G.

**Figure 4** Group-and-source-specific multicast data flow path  
![](images/fig_dc_fd_mld_100604.png)

If MLDv1 is running on the host, the host cannot select multicast sources when it joins group G. In this case, the host receives data from both S1 and S2, regardless of whether it requires the data. If MLDv2 is running on the host, the host can choose to receive only data from S1 using either of the following methods:

* Method 1: The host sends an MLDv2 Multicast Listener Report (G, INCLUDE, (S1)), requesting to receive only the data sent from S1 to G.
* Method 2: The host sends an MLDv2 Multicast Listener Report (G, EXCLUDE, (S2)), notifying the upstream router that it does not want to receive data from S2. In this case, only data sent from S1 is forwarded to the host.

**Group-and-source-specific query**

When an MLD querier receives a Multicast Listener Report message with Filter-Mode-Change Records or Source-List-Change Records (such as CHANGE\_TO\_INCLUDE\_MODE and CHANGE\_TO\_EXCLUDE\_MODE), it sends a Multicast Address and Source Specific Query message. If a member wants to receive the data from any source in the source list, it sends a Multicast Listener Report message. The MLD querier updates the source list of the corresponding group according to the received Multicast Listener Report message.