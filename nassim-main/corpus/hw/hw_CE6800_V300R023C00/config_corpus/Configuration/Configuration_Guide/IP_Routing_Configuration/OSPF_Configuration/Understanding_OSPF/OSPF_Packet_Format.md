OSPF Packet Format
==================

OSPF packets are encapsulated into IP packets, and the OSPF protocol number is 89. OSPF packets are classified into Hello packets, DD packets, LSR packets, LSU packets, and LSAck packets.

* [Hello packet](#EN-US_CONCEPT_0000001130783220__section_02)
* [DD packet](#EN-US_CONCEPT_0000001130783220__section_03)
* [LSR packet](#EN-US_CONCEPT_0000001130783220__section_04)
* [LSU packet](#EN-US_CONCEPT_0000001130783220__section_05)
* [LSAck packet](#EN-US_CONCEPT_0000001130783220__section_06)

#### Packet Header Format

All five types of OSPF packets have the same packet header format, and the header of each type of packet is 24 bytes long. [Figure 1](#EN-US_CONCEPT_0000001130783220__fig_dc_vrp_ospf_feature_003601) shows an OSPF packet header.

**Figure 1** Packet header format  
![](figure/en-us_image_0000001176663057.png)

**Table 1** OSPF packet header fields
| Field | Length | Description |
| --- | --- | --- |
| Version | 8 bits | OSPF version number. For OSPFv2, the value is 2. |
| Type | 8 bits | OSPF packet type. The values are as follows:   * 1: Hello packet * 2: DD packet * 3: LSR packet * 4: LSU packet * 5: LSAck packet |
| Packet length | 16 bits | Length of the OSPF packet with the packet header, in bytes. |
| Router ID | 32 bits | ID of the device that sends the OSPF packet. |
| Area ID | 32 bits | ID of the area to which the device that sends the OSPF packet belongs. |
| Checksum | 16 bits | Checksum of the OSPF packet, excluding the Authentication field. |
| AuType | 16 bits | Authentication type. The values are as follows:   * 0: non-authentication * 1: simple authentication * 2: ciphertext authentication  NOTE:  The MD5 algorithm is insecure and poses security risks. |
| Authentication | 64 bits | This field has different meanings for different AuType values:   * 0: This field is not defined. * 1: This field defines password information. * 2: This field contains the key ID, MD5 authentication data length, and sequence number. |


![](../public_sys-resources/note_3.0-en-us.png) 

MD5 authentication data is added after an OSPF packet and is not included in the Authentication field.



#### Hello Packet

Hello packets are commonly used packets, which are periodically sent by OSPF interfaces to establish and maintain neighbor relationships. A Hello packet includes information about the DR, backup designated router (BDR), timers, and known neighbors. [Figure 2](#EN-US_CONCEPT_0000001130783220__fig_dc_vrp_ospf_feature_003602) shows the format of a Hello packet.

**Figure 2** Format of a Hello packet  
![](figure/en-us_image_0000001176663055.png)

**Table 2** Hello packet fields
| Field | Length | Description |
| --- | --- | --- |
| Network Mask | 32 bits | Mask of the network on which the interface that sends the Hello packet resides. |
| HelloInterval | 16 bits | Interval at which Hello packets are sent. |
| Options | 8 bits | Optional OSPF capabilities:   * E: AS-external-LSAs can be flooded. * N/P: Type 7 LSAs can be processed. * DC: Demand circuits can be processed. |
| Rtr Pri | 8 bits | DR priority. The default value is 1.  NOTE:  If the DR priority of a device interface is set to 0, the interface cannot participate in a DR or BDR election. |
| RouterDeadInterval | 32 bits | Dead interval. If a device does not receive any Hello packets from its neighbors within a specified dead interval, the neighbors are considered to be down. |
| Designated Router | 32 bits | Interface address of the DR. |
| Backup Designated Router | 32 bits | Interface address of the BDR. |
| Neighbor | 32 bits | Router ID of a neighbor. |

[Table 3](#EN-US_CONCEPT_0000001130783220__tab_dc_vrp_ospf_feature_003603) lists the address types, interval types, and default intervals used when Hello packets are transmitted on different networks.

**Table 3** Hello packet characteristics for various network types
| Network Type | Address Type | Interval Type | Default Interval |
| --- | --- | --- | --- |
| Broadcast | Multicast address | HelloInterval | 10 seconds for HelloInterval |
| NBMA | Unicast address | * HelloInterval is used by the DR, BDR, and any device that can become a DR. * PollInterval is used if neighbors go down, and HelloInterval is used in other cases. | 30 seconds for HelloInterval  120 seconds for PollInterval |
| P2P | Multicast address | HelloInterval | 10 seconds for HelloInterval |
| P2MP | Multicast address | HelloInterval | 30 seconds for HelloInterval |


![](../public_sys-resources/note_3.0-en-us.png) 

To establish neighbor relationships between devices on the same network segment, set the same HelloInterval, PollInterval, and RouterDeadInterval values for the devices. PollInterval applies only to NBMA networks.



#### DD Packet

During adjacency initialization between two devices, DD packets are used to describe their LSDBs for synchronization. A DD packet contains the header of each LSA in an LSDB. An LSA header uniquely identifies an LSA, and occupies only a small portion of the LSA, which reduces the amount of traffic transmitted between devices. In addition, a neighbor can use the LSA header to check whether it already has the LSA. When two devices exchange DD packets, one functions as the master, and the other as the slave. The master defines a start sequence number and increments it by one each time it sends a DD packet. After the slave receives a DD packet, it uses the sequence number carried in the DD packet for acknowledgment.

[Figure 3](#EN-US_CONCEPT_0000001130783220__fig_dc_vrp_ospf_feature_003603) shows the format of a DD packet.

**Figure 3** Format of a DD packet  
![](figure/en-us_image_0000001176663063.png)

**Table 4** DD packet fields
| Field | Length | Description |
| --- | --- | --- |
| Interface MTU | 16 bits | Maximum size of an IP packet that an interface can send without fragmenting the packet. |
| Options | 8 bits | Optional OSPF capabilities:   * E: AS-external-LSAs can be flooded. * N/P: Type 7 LSAs can be processed. * DC: Demand circuits can be processed. |
| I | 1 bit | If the DD packet is the first among multiple consecutive DD packets sent by a device, this field is set to 1. Otherwise, this field is set to 0. |
| M (More) | 1 bit | If the DD packet is the last among multiple consecutive DD packets sent by a device, this field is set to 0. Otherwise, this field is set to 1. |
| M/S (Master/Slave) | 1 bit | When two OSPF devices exchange DD packets, they negotiate a master/slave relationship. The device with a larger router ID becomes the master. If this field is set to 1, the DD packet is sent by the master. |
| DD sequence number | 32 bits | Sequence number of the DD packet. The master and slave use sequence numbers to check the reliability and integrity of DD packets. |
| LSA Headers | - | LSA header information included in the DD packet. |



#### LSR Packet

After two devices exchange DD packets, they then send LSR packets to request each other's LSAs for update. These LSR packets contain the summaries of the requested LSAs. [Figure 4](#EN-US_CONCEPT_0000001130783220__fig_dc_vrp_ospf_feature_003604) shows the format of an LSR packet.

**Figure 4** Format of an LSR packet  
![](figure/en-us_image_0000001130623514.png)

**Table 5** LSR packet fields
| Field | Length | Description |
| --- | --- | --- |
| LS type | 32 bits | Type of the LSA. |
| Link State ID | 32 bits | This field, together with the LS type field, uniquely identifies each LSA in an OSPF area. |
| Advertising Router | 32 bits | Router ID of the device that generates the LSA. |


![](../public_sys-resources/note_3.0-en-us.png) 

The LS type, Link State ID, and Advertising Router fields can uniquely identify an LSA. If two LSAs have the same LS type, Link State ID, and Advertising Router fields, the two LSAs are considered to be the same, with one being old and the other being new. In this case, a device uses the LS sequence number, LS checksum, and LS age fields to determine which LSA is newer.



#### LSU Packet

A device uses an LSU packet to transmit LSAs requested by its neighbors or to flood its own updated LSAs. The LSU packet contains all LSAs involved. For multicast and broadcast networks, LSU packets are multicast to flood LSAs. To ensure reliable LSA flooding, a device uses an LSAck packet to acknowledge the LSAs contained in an LSU packet that is received from a neighbor. If an LSA fails to be acknowledged, the device retransmits the LSA to the neighbor. [Figure 5](#EN-US_CONCEPT_0000001130783220__fig_dc_vrp_ospf_feature_003605) shows the format of an LSU packet.

**Figure 5** Format of an LSU packet  
![](figure/en-us_image_0000001130623516.png)

**Table 6** LSU packet field
| Field | Length | Description |
| --- | --- | --- |
| Number of LSAs | 32 bits | Number of LSAs contained in the LSU packet |



#### LSAck Packet

A device uses an LSAck packet to acknowledge the LSAs contained in a received LSU packet. The LSAs can be acknowledged using LSA headers. LSAck packets can be transmitted in unicast or multicast mode, and the transmission mode is determined by the link type. [Figure 6](#EN-US_CONCEPT_0000001130783220__fig_dc_vrp_ospf_feature_003606) shows the format of an LSAck packet.

**Figure 6** Format of an LSAck packet  
![](figure/en-us_image_0000001176663065.png)

**Table 7** LSAck packet field
| Field | Length | Description |
| --- | --- | --- |
| LSAs Headers | Determined by the header length of the LSA to be acknowledged. | This field is used to acknowledge an LSA. |