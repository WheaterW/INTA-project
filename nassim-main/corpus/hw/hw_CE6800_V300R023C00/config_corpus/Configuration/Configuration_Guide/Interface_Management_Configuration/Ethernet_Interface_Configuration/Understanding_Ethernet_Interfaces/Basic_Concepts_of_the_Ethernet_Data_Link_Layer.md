Basic Concepts of the Ethernet Data Link Layer
==============================================

Basic Concepts of the Ethernet Data Link Layer

#### Hierarchical Structure of the Ethernet Data Link Layer

In Ethernet, the following access modes are used according to the duplex mode:

* CSMA/CD is used in half-duplex mode.
* Data is sent and received directly in full-duplex mode without having to detect if the line is idle.

The duplex mode, either half or full, is a physical layer concept, whereas the access mode, varying with the duplex mode, is a data link layer concept. The two layers are related on the Ethernet.

Because of this relationship, a specific data link layer is required for different operation modes at the physical layer. This causes some issues for the design and application of the Ethernet.

To address this issue, some organizations and vendors have proposed dividing the data link layer into two sub-layers: logical link control (LLC) and media access control (MAC). In this case, different physical layers correspond to different MAC sub-layers, and the LLC sub-layer becomes totally independent, as shown in [Figure 1](#EN-US_CONCEPT_0000001513040942__fig_dc_vrp_ethernet_feature_000501).

**Figure 1** Hierarchical structure of the Ethernet data link layer  
![](figure/en-us_image_0000001512681790.png)  


#### MAC Sub-layer

The MAC sub-layer is responsible for the following:

* Accessing physical links
  
  The MAC sub-layer is associated with the physical layer so that different MAC sub-layers provide access to different physical layers.
  
  Ethernet has two types of MAC sub-layers:
  
  + Half-duplex MAC: provides access to the physical layer in half-duplex mode.
  + Full-duplex MAC: provides access to the physical layer in full-duplex mode.
  
  The two types of MAC sub-layers are integrated in a network adapter. After the network adapter is initialized, auto-negotiation is performed to choose an operation mode, and according to which, a MAC sub-layer is chosen.
* Identifying stations at the data link layer
  
  The MAC sub-layer reserves MAC addresses to uniquely identify stations at the data link layer.
* Transmitting data at the data link layer
  
  After receiving data from the LLC sub-layer, the MAC sub-layer adds MAC addresses and control information to the data before transmitting it to the physical link. In this process, the MAC sub-layer provides functions such as the check function.
  
  Data transmission at the data link layer is as follows:
  
  1. The upper layer delivers data to the MAC sub-layer.
  2. The MAC sub-layer stores the data in a buffer.
  3. The MAC sub-layer adds the destination and source MAC addresses to the data and calculates the length of the data frame to form an Ethernet frame.
  4. The Ethernet frame is sent to the peer according to the destination MAC address.
  5. The peer compares the destination MAC address with entries in the MAC address table.
     
     + If there is a matching entry, the frame is accepted.
     + If there is no matching entry, the frame is discarded.


#### Ethernet Frame Structure

Ethernet II and IEEE 802.3 frames are the most common frames on a LAN. In TCP/IP, the Ethernet II frame format is defined in RFC 894, and the IEEE 802.3 frame format is defined in RFC 1042. Currently, the Ethernet II (also called Ethernet DIX) frame format is more widely used. Compared with IEEE 802.3, Ethernet II is more suitable for transmitting a large amount of data. However, Ethernet II lacks control over the data link layer, and is therefore unsuitable for transmitting data that requires strict control.

**Ethernet II Frames**

Ethernet II frames are the most common types of frames and are generally used by the IP protocol. [Figure 2](#EN-US_CONCEPT_0000001513040942__fig_dc_vrp_ethernet_feature_000502) shows the Ethernet II frame format.

**Figure 2** Ethernet II frame format  
![](figure/en-us_image_0000001563880941.png)

[Table 1](#EN-US_CONCEPT_0000001513040942__table1098519115572) describes the fields in an Ethernet II frame.

**Table 1** Fields in an Ethernet II frame
| Field | Length | Description |
| --- | --- | --- |
| DMAC | 6 bytes | DMAC: destination MAC address, which specifies the receiver of the frame. |
| SMAC | 6 bytes | SMAC: source MAC address, which specifies the sender of the frame. |
| Type | 2 bytes | The 2-byte Type field identifies the upper layer protocol in the Data field. The receiver can interpret the meaning of the Data field according to the Type field.  Multiple protocols can coexist on a LAN. The hexadecimal values in the Type field of an Ethernet II frame specify these protocols.   * 0800 indicates IP. * 0806 indicates the Address Resolution Protocol (ARP). * 0835 indicates the Reverse Address Resolution Protocol (RARP). * 8137 indicates Internetwork Packet Exchange (IPx) and Sequenced Packet Exchange (SPx). |
| Data | 46 bytes to 1500 bytes | The minimum length of the Data field is 46 bytes, ensuring that the frame is at least 64 bytes. A 46-byte Data field is required even if a station transmits 1 byte of data.  If the length of this field is less than 46 bytes, 0s are used for padding.  The maximum length of the Data field is 1500 bytes. |
| CRC | 4 bytes | CRC: The cyclic redundancy check (CRC) field provides an error detection mechanism.  Each sending device calculates a CRC code from the DMAC, SMAC, Type, and Data fields. The CRC code is then filled into the 4-byte CRC field. |

**IEEE 802.3 frame**

[Figure 3](#EN-US_CONCEPT_0000001513040942__fig_dc_vrp_ethernet_feature_000503) shows the IEEE 802.3 frame format.

**Figure 3** IEEE 802.3 frame format  
![](figure/en-us_image_0000001564121053.png)

The format of an IEEE 802.3 frame is similar to that of an Ethernet II frame. In an IEEE 802.3 frame, however, the Type field is changed to the Length field, and the LLC field and SNAP field occupy 8 bytes of the Data field. [Table 2](#EN-US_CONCEPT_0000001513040942__table123313271122) describes the fields in an IEEE 802.3 frame.

**Table 2** Fields in an IEEE 802.3 frame
| Field | Description |
| --- | --- |
| Length | Specifies the number of bytes of the Data field. |
| LLC | Consists of three sub-fields: Destination Service Access Point (DSAP), Source Service Access Point (SSAP), and Control. |
| SNAP | Consists of the Org Code field and Type field. Three bytes of the Org Code field are all 0s. The Type field functions the same as that in Ethernet II frames. |


![](public_sys-resources/note_3.0-en-us.png) 

For descriptions of other fields, see Ethernet II frames.

According to the values of DSAP and SSAP, an IEEE 802.3 frame can be as follows:

* If DSAP and SSAP are both 0xff, the IEEE 802.3 frame becomes a NetWare-Ethernet frame carrying NetWare data.
* If DSAP and SSAP are both 0xaa, the IEEE 802.3 frame becomes an Ethernet\_SNAP frame.
  
  An Ethernet\_SNAP frame can be used for multi-protocol transmission. Therefore, SNAP can be considered as an extension of the Ethernet protocol and allows vendors to invent their own Ethernet transmission protocols.
  
  The Ethernet\_SNAP standard is defined by IEEE 802.1 to help ensure compatibility between the operations of an IEEE 802.3 LAN and Ethernet.
* Other values of DSAP and SSAP indicate pure IEEE 802.3 frames.

#### LLC Sub-layer

As described, the MAC sub-layer supports both IEEE 802.3 and Ethernet II frames. In the latter, the Type field identifies the upper layer protocol. In this case, the LLC sub-layer is not needed, and only the MAC sub-layer is required.

In an IEEE 802.3 frame, useful features are defined at the LLC sub-layer in addition to the traditional services of the data link layer. These features are specified by the sub-fields of DSAP, SSAP, and Control.

For example, the LLC sub-layer supports the following types of P2P data transmission services:

* Connectionless service. Currently implemented by Ethernet.
* Connection-oriented service. Specifically, a connection is set up before data is transmitted, thereby ensuring reliability.
* Connectionless service with data acknowledgment. Specifically, a connection is not required before data transmission. However, an acknowledgment mechanism is adopted to improve reliability.

The following is an example to describe SSAP and DSAP applications. Assuming that terminals A and B use connection-oriented services, data is transmitted through the following process:

1. A sends a frame to B to request a connection.
2. After receiving the frame, if B has enough resources, it returns an acknowledgment message that contains a SAP. The SAP identifies the connection required by A.
3. After receiving the acknowledgment message, A knows that B has set up a local connection between them. After creating a SAP, A sends a message containing the SAP to B. The connection is then set up.
4. The LLC sub-layer of A encapsulates the data to be transmitted into a frame. The DSAP field is filled in with the SAP sent by B, and the SSAP field is filled in with that created by A. The LLC sub-layer of A then transfers the data to its MAC sub-layer.
5. The MAC sub-layer of A adds the MAC address and Length fields to the frame, before transferring it to the data link layer.
6. After receiving the frame at the MAC sub-layer of B, the MAC sub-layer transfers the frame to the LLC sub-layer, which identifies the connection that the frame belongs to according to the DSAP field.
7. After checking and acknowledging the frame based on the connection type, the LLC sub-layer of B transfers the frame to the upper layer.
8. After data transmission is complete, A sends B a frame, instructing B to cancel the connection. At this time, the communication ends.