Re-marking
==========

Re-marking

#### Precedence Fields

In order for devices to provide differentiated services, certain fields in the packet header or frame header are used to record QoS information. These fields include:

* **802.1p value in an Ethernet frame header**
  
  Layer 2 devices communicate by exchanging Ethernet frames. In the Ethernet frame header, the PRI field (802.1p value, also called CoS) is used to identify the QoS requirements, as defined in IEEE 802.1Q. [Figure 1](#EN-US_CONCEPT_0000001512836358__fig_dc_fd_qos_000502) shows the format of the 802.1p value in an Ethernet frame header.
  
  **Figure 1** 802.1p value in an Ethernet frame header  
  ![](figure/en-us_image_0000001513155898.png)
  
  As shown in the figure, the 802.1Q header contains a 3-bit PRI field and a 1-bit CFI field. The PRI field defines eight service priority values 7, 6, 5, 4, 3, 2, 1, and 0, listed in descending order of priority. The CFI field defines the drop priority of packets.
* **Precedence field in an IP packet**
  
  As defined in RFC 791, the 8-bit Type of Service (ToS) field in an IP packet header contains a 3-bit IP precedence field. [Figure 2](#EN-US_CONCEPT_0000001512836358__fig_dc_fd_qos_000501) shows the format of the precedence field in an IP packet.
  
  **Figure 2** IP precedence in the DSCP field  
  ![](figure/en-us_image_0000001512836378.png "Click to enlarge")
  
  Bits 0 to 2 represent the precedence field, representing values 7, 6, 5, 4, 3, 2, 1 and 0, listed in descending order of priority. The highest-priority values (7 and 6) are reserved for routing and network control communication updates. User-level applications can use only priority values 0 to 5.
  
  In addition to the precedence field, a ToS field contains the following sub-fields:
  
  + Bit D indicates the delay. The value 0 represents a normal delay and the value 1 represents a short delay.
  + Bit T indicates the throughput. The value 0 represents a normal throughput and the value 1 represents a high throughput.
  + Bit R indicates the reliability. The value 0 represents normal reliability and the value 1 represents high reliability.
  
  Bits 6 and 7 constitute the Explicit Congestion Notification (ECN) field.
* **DSCP field in an IP packet**
  
  The ToS field in IP packets was defined in RFC 1349, with bit C (monetary cost) added. Following that, the IETF DiffServ Working Group redefined bits 0 to 5 of a ToS field as the DS CodePoint (DSCP) field in RFC 2474. In RFC 2474, the field name is changed from ToS to differentiated service (DS). [Figure 2](#EN-US_CONCEPT_0000001512836358__fig_dc_fd_qos_000501) shows the DSCP field in an IP packet.
  
  In the DS field, the first six bits (bits 0 to 5) are the DSCP and the last two bits (bits 6 and 7) are reserved. The first three bits (0 to 2) are the Class Selector CodePoint (CSCP), which represents the DSCP type. A DS node selects a Per-Hop Behavior (PHB) based on the DSCP value.

#### Packet Re-marking

Packet re-marking involves setting the preceding QoS-related packet fields and redefining the scheduling and transmission modes of packets. Currently, the device supports the following packet re-marking modes:

* Re-marking 802.1p values of VLAN packets
* Re-marking DSCP values of IP packets
* Re-marking internal priorities of packets
* Re-marking local IDs
* Re-marking reserved VXLAN fields