IGMPv3
======

IGMPv3 was developed to support the source-specific multicast (SSM) model. IGMPv3 messages can carry multicast source information so that hosts can select a multicast source.

#### IGMPv3 Messages

IGMPv3 differs from IGMPv2 in the following:

* IGMPv3 defines two message types: Query and Report. Unlike IGMPv2, IGMPv3 does not define a Leave message. Group members send Report messages of a specified type to notify multicast devices that they have left a group.
* In addition to General Query and Group-Specific Query messages, IGMPv3 defines a new Query message type: Group-and-Source-Specific Query. A querier sends this message to members in a specific multicast group on a shared network segment, to check whether they want to receive data from specific sources. A Group-and-Source-Specific Query message carries one or more multicast source addresses.
* A Report message contains both the multicast group that a host wants to join and the multicast sources from which the host wants to receive data. IGMPv3 supports source filtering and defines filtering modes INCLUDE and EXCLUDE. Group-source mappings are represented by (G, INCLUDE, (S1, S2...)) or (G, EXCLUDE, (S1, S2...)). The (G, INCLUDE, (S1, S2...)) entry indicates that a host wants to receive data sent from the listed multicast sources to group G. The (G, EXCLUDE, (S1, S2...)) entry indicates that a host wants to receive data sent from all multicast sources except listed ones to group G. If group-source mappings change, hosts add these changes to the Group Record fields in IGMPv3 Report messages and send the messages to the IGMP querier.
* An IGMPv3 Report message can carry multiple multicast groups, whereas an IGMPv1 or IGMPv2 Report message can carry only one multicast group. This greatly reduces the number of IGMPv3 messages.

[Figure 1](#EN-US_CONCEPT_0000001130784226__fig_dc_fd_igmp_100801) shows the format of an IGMPv3 Query message, and [Table 1](#EN-US_CONCEPT_0000001130784226__tab_dc_fd_igmp_100801) describes the fields in this message.

**Figure 1** IGMPv3 Query message format  
![](figure/en-us_image_0000001176743921.png)

**Table 1** Fields in an IGMPv3 Query message
| Field | Description |
| --- | --- |
| Type | Message type. The value is 0x11. |
| Max Response Code | Maximum response time. After receiving a General Query message from an IGMP querier, a member host needs to respond to the message within the maximum response time. |
| Checksum | Checksum. |
| Group Address | Multicast group address. In a General Query message, this field is set to 0. In a Group-Specific Query or Group-and-Source-Specific Query message, the value of this field is the address of the multicast group to be queried. |
| Resv | Reserved field. This field is set to 0 by the sender and is ignored by the receiver. |
| S | When this flag is set to 1, other devices receiving the Query message suppress timer updates. Such a Query message does not suppress the querier election or host-side processing on the devices. |
| QRV | A value other than 0 indicates the robustness variable of the querier. If the value of this field is 0, the robustness variable of the querier is greater than 7. If a device finds that the value of this field in a received Query message is not 0, it sets its robustness variable to this value. If the value of this field is 0, it ignores this field. |
| QQIC | Query interval of an IGMP querier, in seconds. If a non-querier finds that the value of this field in a received Query message is not 0, it sets its query interval to this value. If the value of this field is 0, it ignores this field. |
| Number of Sources | Number of multicast sources in the message. For General Query and Group-Specific Query messages, the value of this field is 0. For a Group-and-Source-Specific Query message, the value of this field is not 0. This number is limited by the MTU of the network over which the message is transmitted. |
| Source Address | Multicast source address. Its quantity is limited by the value of the Number of Sources field. |

[Figure 2](#EN-US_CONCEPT_0000001130784226__fig_dc_fd_igmp_100802) shows the format of an IGMPv3 Report message, and [Table 2](#EN-US_CONCEPT_0000001130784226__tab_dc_fd_igmp_100802) describes the fields in this message.

**Figure 2** IGMPv3 Report message format  
![](figure/en-us_image_0000001176743929.png)

**Table 2** Fields in an IGMPv3 Report message
| Field | Description |
| --- | --- |
| Type | Message type. The value is 0x22. |
| Reserved | Reserved field. This field is set to 0 by the sender and is ignored by the receiver. |
| Checksum | Checksum of an IGMP message. The checksum is 16 bits long. It is the one's complement of the one's complement sum of the whole IGMP message (the entire IP payload). The Checksum field is set to 0 during checksum calculation. The sender must calculate the checksum and insert it into the Checksum field. The receiver must verify the checksum before processing the message. |
| Number of Group Records (M) | Number of group records in the message. |
| Group Record | Group information in the message. [Figure 3](#EN-US_CONCEPT_0000001130784226__fig_dc_fd_igmp_100803) shows the format of the Group Record field, and [Table 3](#EN-US_CONCEPT_0000001130784226__tab_dc_fd_igmp_100803) describes the fields in the Group Record field. |


**Figure 3** Format of the Group Record field  
![](figure/en-us_image_0000001176664011.png)

**Table 3** Fields in the Group Record field
| Field | Description |
| --- | --- |
| Record Type | Group record type:  * Current-State Record: sent by a host in response to a Query message to report its current state. This record type is one of the following two values:   + MODE\_IS\_INCLUDE: indicates that the host wants to receive multicast data sent from the listed source addresses to the group. The message is invalid if the source address list is empty.   + MODE\_IS\_EXCLUDE: indicates that the host does not want to receive multicast data sent from the listed source addresses to the group. * Filter-Mode-Change Record: sent by a host when the filter mode changes. This record type is one of the following two values:   + CHANGE\_TO\_INCLUDE\_MODE: indicates that the filter mode has changed from EXCLUDE to INCLUDE. The host wants to receive multicast data sent from the new sources in the source list to the group. If the specified source list is empty, the host will leave the group.   + CHANGE\_TO\_EXCLUDE\_MODE: indicates that the filter mode has changed from INCLUDE to EXCLUDE. The host rejects multicast data sent from the new sources in the source list to the group. * Source-List-Change Record: sent by a host when the source list changes. This record type is one of the following two values:   + ALLOW\_NEW\_SOURCES: indicates that the source list contains additional sources from which the host wants to receive, for multicast data sent to the group. If the filter mode is INCLUDE, the sources are added to the existing source list. If the filter mode is EXCLUDE, the sources are deleted from the existing blocked source list.   + BLOCK\_OLD\_SOURCES: indicates that the source list contains the sources from which the host no longer wants to receive multicast data sent to the group. If the filter mode is INCLUDE, the sources are deleted from the source list. If the filter mode is EXCLUDE, the sources are added to the source list. |
| Aux Data Len | Auxiliary data length. IGMPv3 Report messages do not contain the Auxiliary Data field and therefore this field is set to 0. |
| Number of Sources (N) | Number of source addresses in this group record. |
| Multicast Address | Multicast group address. |
| Source Address | Multicast source address. |
| Auxiliary Data | Additional information in this group record. This field is reserved for IGMP extensions or later IGMP versions. IGMPv3 Report messages do not contain auxiliary data. |



#### IGMPv3 Working Mechanism

Compared with IGMPv2, IGMPv3 allows hosts to select multicast sources.

**Group-and-source-specific join**

IGMPv3 Report messages have a destination address of 224.0.0.22, which represents all IGMPv3-capable multicast devices on the same network segment. A Report message contains Group Record fields, allowing hosts to specify the multicast sources from which they do or do not want to receive data when joining a multicast group. As shown in [Figure 4](#EN-US_CONCEPT_0000001130784226__fig_01), two multicast sources S1 and S2 send data to multicast group G. The host only wants to receive data sent from S1 to G.

**Figure 4** Group-and-source-specific multicast data flow path  
![](figure/en-us_image_0000001130624474.png)

If IGMPv1 or IGMPv2 is running between the host and the multicast devices, the host cannot select multicast sources when it joins group G. The host receives data from both S1 and S2, regardless of whether it requires the data. If IGMPv3 is used, the host can send an IGMPv3 Report message (G, INCLUDE, (S1)), requesting to receive only the data sent from S1 to G.

**Group-and-source-specific query**

When an IGMP querier receives a Report message with Filter-Mode-Change Records or Source-List-Change Records (such as CHANGE\_TO\_INCLUDE\_MODE and CHANGE\_TO\_EXCLUDE\_MODE), it sends a Group-and-Source-Specific Query message. If a member wants to receive the data from any source in the source list, it sends a Report message. The IGMP querier updates the source list of the corresponding group according to the received Report messages.