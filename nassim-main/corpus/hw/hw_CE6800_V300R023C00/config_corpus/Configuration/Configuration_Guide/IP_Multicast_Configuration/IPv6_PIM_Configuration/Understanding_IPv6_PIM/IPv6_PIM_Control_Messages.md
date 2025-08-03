IPv6 PIM Control Messages
=========================

IPv6 PIM devices exchange PIM control messages to implement multicast routing. You are advised to understand IPv6 PIM control messages based on actual scenarios.

IPv6 PIM control messages are encapsulated in IP packets, as shown in [Figure 1](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300501).

**Figure 1** Encapsulation format of an IPv6 PIM control message  
![](figure/en-us_image_0000001589190345.png)  

In the header of an IP packet that contains a PIM message, the protocol type field is set to 103.

The destination address field in the IP header identifies destination receivers of the PIM message. The destination address can be either a unicast address or a multicast address.

#### PIM Control Message Types

All IPv6 PIM control messages use the same header format, as shown in [Figure 2](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300502).

**Figure 2** Header format of an IPv6 PIM control message  
![](figure/en-us_image_0000001589285073.png)

In IPv6 PIM messages, unicast and multicast addresses are encapsulated in encoding formats, for example, group addresses in the Encoded-Group format, source addresses in the Encoded-Source format, and BSR addresses in the Encoded-Unicast format. The length of the address that can be encoded and encapsulated is variable, depending on the supported protocol type.

**Table 1** Fields in a PIM control message
| Field | Length | Description |
| --- | --- | --- |
| Version | 4 bits | IPv6 PIM version. The value is 2. |
| Type | 4 bits | Message type. The options are as follows:  * 0: [Hello](#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) * 1: [Register](#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300503) * 2: [Register-Stop](#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300504) * 3: [Join/Prune](#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300505) * 4: [Bootstrap](#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300506) * 5: [Assert](#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300507) * 9: [Advertisement](#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300510) |
| Reserved | 8 bits | Reserved field. This field is set to 0 when the message is sent and is not processed when the message is received. |
| Checksum | 16 bits | Checksum. |



#### Hello Messages

IPv6 PIM devices periodically exchange Hello messages through all PIM interfaces to discover IPv6 PIM neighbors and maintain neighbor relationships.

In an IP packet that carries a Hello message, the source address is a local interface's address, the destination address is FF02::d, and the TTL value is 1. Hello messages are sent in multicast mode. [Figure 3](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300503) shows the format of a Hello message.

**Figure 3** Hello message format  
![](figure/en-us_image_0000001538765218.png)

Hello messages contain Hello Option fields, whose format is shown in [Figure 4](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300504).

**Figure 4** Hello Option field format  
![](figure/en-us_image_0000001589525081.png)

[Table 2](#EN-US_CONCEPT_0000001589284989__tab_dc_vrp_multicast_feature_300502) shows the fields in a Hello message.

**Table 2** Fields in a Hello message
| Field | Length | Description |
| --- | --- | --- |
| Type | 4 bits | Message type. The value is 0. |
| Option Type | 2 bytes | Parameter type. |
| Option Length | 2 bytes | Length of the Option Value field. |
| Option Value | Variable | Parameter value. |

[Table 3](#EN-US_CONCEPT_0000001589284989__tab_dc_vrp_multicast_feature_300503) describes the valid values of the Option Type field.

**Table 3** Valid values of Option Type
| Option Type | Option Value |
| --- | --- |
| 1 | Holdtime: timeout period during which a neighbor remains in the reachable state. If no Hello message is received within the timeout period, the neighbor is considered unreachable. |
| 2 | The field consists of the following parts:  * LAN Prune Delay: delay in transmitting Prune messages on a shared network segment. * Override Interval: interval for overriding a prune action on a shared network segment. * T: capability of suppressing Join messages. |
| 19 | DR Priority: priority of a device interface, used to run for a DR. The higher the priority, the higher the probability that the interface becomes a DR. |
| 20 | Generation ID: a random number carried in the Hello message, indicating the current neighbor status. If the neighbor status changes, the random number is updated. When a device detects that the Hello messages received from an upstream neighbor contain different Generation IDs, the device determines that the upstream neighbor is down or the status of the upstream neighbor has changed. |
| 21 | State Refresh Capable: interval for refreshing neighbor status. |
| 24 | Address List: PIM interface's secondary address list. |



#### Register Messages

When a multicast source becomes active on an IPv6 PIM-SM network, the corresponding source DR sends a Register message to register with the RP.

In an IP packet that carries a Register message, the source address is the address of a source DR, and the destination address is the RP address. The packet is sent in unicast mode.

[Figure 5](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300505) shows the format of a Register message.

**Figure 5** Register message format  
![](figure/en-us_image_0000001538445510.png)

[Table 4](#EN-US_CONCEPT_0000001589284989__tab_dc_vrp_multicast_feature_300504) describes the fields in a Register message.

**Table 4** Fields in a Register message
| Field | Length | Description |
| --- | --- | --- |
| Type | 4 bits | Message type. The value is 1. |
| B | 1 bit | Border bit. |
| N | 1 bit | Null-Register bit. |
| Reserved2 | 30 bits | Reserved field. This field is set to 0 when the message is sent and is not processed when the message is received. |
| Multicast Data Packet | Variable | Multicast data packet. Upon receipt of a multicast data packet, a source DR encapsulates it in a Register message and sends the message to the RP. After decapsulating the message, the RP learns the (S, G) information of the multicast data packet. |

A multicast source can send data to multiple multicast groups, and therefore the source DR must send Register messages to the RP of each target multicast group. A Register message can carry only one multicast data packet. Therefore, a Register message can carry only one (S, G) entry.

In the register-suppression period, the source DR sends Null-Register messages to notify the RP of the fact that the source is still active. In a Null-Register message, the Multicast Data Packet field contains only the IP header of the multicast data packet, and the header consists of such information as the multicast source address and multicast group address. After the register-suppression times out, the DR re-encapsulates multicast data packets in Register messages.


#### Register-Stop Messages

On an IPv6 PIM-SM network, an RP sends Register-Stop messages to a source DR in the following scenarios:

* Receivers no longer request a multicast group's data through the RP.
* The RP no longer serves a multicast group.
* The multicast data forwarding path has been switched from the RPT to the SPT.

After receiving a Register-Stop message, the source DR stops using Register messages to encapsulate multicast data packets and enters the register-suppression state.

In an IP packet that carries a Register-Stop message, the source address is the RP address, and the destination address is the source DR's address. The packet is sent in unicast mode. [Figure 6](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300506) shows the format of a Register-Stop message.

**Figure 6** Register-Stop message format  
![](figure/en-us_image_0000001589285081.png)

[Table 5](#EN-US_CONCEPT_0000001589284989__tab_dc_vrp_multicast_feature_300505) describes the fields in a Register-Stop message.

**Table 5** Fields in a Register-Stop message
| Field | Length | Description |
| --- | --- | --- |
| Type | 4 bits | Message type. The value is 2. |
| Group Address (Encoded-Group format) | Variable | Multicast group address G. |
| Source Address (Encoded-Unicast format) | Variable | Multicast source address S. |

An RP can serve multiple multicast groups, and a multicast group can receive data from multiple sources. Therefore, an RP may have multiple (S, G) entries registered at the same time.

A Register-Stop message can carry only one (S, G) entry. When an RP sends a Register-Stop message to a source DR, only one (S, G) entry can be deregistered.

After receiving the Register-Stop message carrying an (S, G) entry, the source DR stops encapsulating packets for this (S, G) entry, but it still encapsulates the packets sent from the source S to other multicast groups in Register messages.


#### Join/Prune Messages

A Join/Prune message can contain both Join and Prune information. A Join/Prune message that contains only Join information is called a Join message. A Join/Prune message that contains only Prune information is called a Prune message.

* When an IPv6 PIM device no longer has multicast receivers downstream, it sends a Prune message through its upstream interfaces to instruct the upstream devices to stop forwarding packets to the network segment on which the IPv6 PIM device resides.
* When a receiver starts to require data from an IPv6 PIM-SM network, the receiver DR sends a Join message through the RPF interface pointing to the RP to instruct the upstream neighbor to forward packets to the network segment. The Join message is sent upstream hop by hop to set up an RPT.
* When an RP triggers an SPT switchover, the RP sends a Join message through the RPF interface pointing to the source to instruct the upstream neighbor to forward packets to the network segment. The Join message is sent upstream hop by hop to set up an MDT from the RP to the source.
* When a receiver DR triggers an SPT switchover, the DR sends a Join message through the RPF interface pointing to the source to instruct the upstream neighbor to forward packets to the network segment. The Join message is sent upstream hop by hop to set up an SPT.
* An IPv6 PIM shared network segment may be connected to a downstream interface and multiple upstream interfaces. If an upstream interface sends a Prune message, but other upstream interfaces still require multicast packets, these interfaces that require multicast packets must send Join messages within the override-interval. Otherwise, the downstream interface responsible for forwarding packets on the network segment performs the prune action. On a multicast network, if IPv6 PIM is enabled on user-side interfaces, the PIM DR determines the sending of Join messages. This is because only the PIM DR has an outbound interface list and is eligible to send Join messages.
  
  As shown in [Figure 7](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300509), Port 1 on DeviceA is a downstream interface, and Port 2 on DeviceB and Port 3 on DeviceC are upstream interfaces. If DeviceB sends a Prune message through Port 2, Port 3 of DeviceC and Port 1 of DeviceA will receive this message. If DeviceC still wants to receive the multicast data of the group, DeviceC must send a Join message within the override-interval. This message will notify Port 1 of DeviceA that a downstream device still wants to receive the multicast data. In this case, DeviceA does not perform the prune action.
  
  **Figure 7** Join/Prune messages on a PIM shared network segment  
  ![](figure/en-us_image_0000001538765222.png)

In an IP packet that carries a Join/Prune message, the source address is a local interface's address, the destination address is FF02::d, and the TTL value is 1. The packet is sent in multicast mode. [Figure 8](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300507) shows the format of the message.

**Figure 8** Join/Prune message format  
![](figure/en-us_image_0000001589525089.png)

[Figure 9](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300508) shows the format of the Group J/P Record field.

**Figure 9** Format of the Group J/P Record field  
![](figure/en-us_image_0000001538445514.png)

[Table 6](#EN-US_CONCEPT_0000001589284989__tab_dc_vrp_multicast_feature_300506) describes the fields in a Join/Prune message.

**Table 6** Fields in a Join/Prune message
| Field | Length | Description |
| --- | --- | --- |
| Type | 4 bits | Message type. The value is 3. |
| Upstream Neighbor Address (Encoded-Unicast format) | Variable | Address of the upstream neighbor (address of the downstream interface that performs the Join or Prune action on the device that receives the Join/Prune message). |
| Reserved | 8 bits | Reserved field. |
| Number of Groups(N) | 8 bits | Number of multicast groups contained in the message. |
| Holdtime | 16 bits | Period during which the device that receives a Join/Prune message keeps the corresponding interface in the Join/Prune state. |
| Group Address (Encoded-Group format) | Variable | Multicast group address. |
| Number of Joined Sources | 16 bits | Number of sources whose multicast traffic is requested in a multicast group. |
| Number of Pruned Sources | 16 bits | Number of sources whose multicast traffic is no longer requested in a multicast group. |
| Joined Source Address (Encoded-Source format) | Variable | Address of the source whose multicast traffic is requested. |
| Pruned Source Address (Encoded-Source format) | Variable | Address of the source whose multicast traffic is no longer requested. |



#### Bootstrap Messages

When dynamic RP election is used on a PIM-SM network, candidate-bootstrap routers (C-BSRs) periodically send Bootstrap messages through all PIM interfaces to participate in BSR election. The winner continues to send Bootstrap messages carrying RP-Set information to all PIM devices in the domain.

In an IP packet that carries a Bootstrap message, the source address is a PIM interface's address, the destination address is FF02::d, and the TTL value is 1. The packet is transmitted in multicast mode and is forwarded hop by hop on the PIM-SM network and is flooded on the entire network. [Figure 10](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300510) shows the format of a Bootstrap message.

**Figure 10** Bootstrap message format  
![](figure/en-us_image_0000001589285085.png)

[Figure 11](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300511) shows the format of the Group-RP Record field.

**Figure 11** Format of the Group-RP Record field  
![](figure/en-us_image_0000001538765226.png)

[Table 7](#EN-US_CONCEPT_0000001589284989__tab_dc_vrp_multicast_feature_300507) describes the fields in a Bootstrap message.

**Table 7** Fields in a Bootstrap message
| Field | Length | Description |
| --- | --- | --- |
| Type | 4 bits | Message type. The value is 4. |
| N | 1 bit | If this field is set to 1, Bootstrap message fragments are not forwarded. |
| Reserved | 7 bits | Reserved field. The field is set to 0 when the message is sent and is not processed when the message is received. |
| Fragment Tag | 16 bits | Random number used to distinguish the Bootstrap message. |
| Hash Mask length | 8 bits | Length of the hash mask of a C-BSR. |
| BSR-priority | 8 bits | C-BSR priority. |
| BSR-Address (Encoded-Unicast format) | Variable | C-BSR address. |
| Group Address (Encoded-Group format) | Variable | Multicast group address. |
| RP-Count | 8 bits | Total number of C-RPs that want to serve the group. |
| Frag RP-Cnt | 8 bits | Number of C-RP addresses in the corresponding network segment. For a given multicast group, if the Bootstrap message is fragmented, the Frag RP-Cnt field facilitates RP-Set fragmentation. |
| RP-address (Encoded-Unicast format) | Variable | C-RP address. |
| RP-holdtime | 16 bits | Aging time of the advertisement message sent by a C-RP. |
| RP-Priority | 8 bits | C-RP priority. |

A PIM interface can be configured as a BSR boundary. Multiple BSR boundary interfaces divide the network into different IPv6 PIM-SM domains. Bootstrap messages cannot pass through the BSR boundary.


#### Assert Messages

On a shared network segment, if an IPv6 PIM device receives an (S, G) packet from the downstream interface of an (S, G) or (\*, G) entry, other forwarders exist on the network segment. The device then sends an Assert message through the downstream interface to participate in the forwarder election. The candidates who fail in the election stop forwarding packets through their downstream interfaces.

In an IP packet that carries an Assert message, the source address is a local interface's address, the destination address is FF02::d, and the TTL value is 1. The message is transmitted in multicast mode. [Figure 12](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300512) shows the format of an Assert message.

**Figure 12** Assert message format  
![](figure/en-us_image_0000001589525093.png)

[Table 8](#EN-US_CONCEPT_0000001589284989__tab_dc_vrp_multicast_feature_300508) describes the fields in an Assert message.

**Table 8** Fields in an Assert message
| Field | Length | Description |
| --- | --- | --- |
| Type | 4 bits | Message type. The value is 5. |
| Group Address (Encoded-Group format) | Variable | Multicast group address. |
| Source address (Encoded-Unicast format) | Variable | This field is a multicast source address if the message sender participates in the election of the only forwarder for (S, G) entries and is 0 if the message sender participates in the election of the only forwarder for (\*, G) entries. |
| R | 1 bit | RPT bit. This field is 0 if the message sender participates in the election of the only forwarder for (S, G) entries and is 1 if the message sender participates in the election of the only forwarder for (\*, G) entries. |
| Metric Preference | 31 bits | Priority of the unicast path to the source address.  If the R field is 1, this field indicates the priority of the unicast path to the RP. |
| Metric | 32 bits | Cost of the unicast route to the source address.  If the R field is 1, this field indicates the cost of the unicast path to the RP. |



#### Advertisement Messages

When dynamic RP election is used on a PIM-SM network, the devices that are configured as C-RPs periodically send Advertisement messages to notify the BSR of the range of multicast groups they want to serve.

In an IP packet that carries an Advertisement message, the source address is the C-RP address, and the destination address is the BSR's address. The packet is sent in unicast mode. [Figure 13](#EN-US_CONCEPT_0000001589284989__fig_dc_vrp_multicast_feature_300513) shows the format of an Advertisement message.

**Figure 13** Advertisement message format  
![](figure/en-us_image_0000001538445518.png)

[Table 9](#EN-US_CONCEPT_0000001589284989__tab_dc_vrp_multicast_feature_300511) describes the fields in an Advertisement message.

**Table 9** Fields in an Advertisement message
| Field | Length | Description |
| --- | --- | --- |
| Type | 4 bits | Message type. The value is 8. |
| Prefix-Cnt | 8 bits | Prefix value of the multicast address. |
| Priority | 8 bits | C-RP priority. |
| Holdtime | 16 bits | Aging time of the Advertisement message. |
| RP-Address (Encoded-Unicast format) | Variable | C-RP address. |
| Group Address (Encoded-Group format) | Variable | Multicast group address. |