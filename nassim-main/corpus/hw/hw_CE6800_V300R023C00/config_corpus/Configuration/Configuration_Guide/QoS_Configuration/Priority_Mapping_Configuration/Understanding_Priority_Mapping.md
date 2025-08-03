Understanding Priority Mapping
==============================

Understanding Priority Mapping

#### External Priority Fields

Certain fields in the packet header or frame header record QoS information so that network devices can provide differentiated services. These fields include:

* Precedence field
  
  As defined in RFC 791, the 8-bit Type of Service (ToS) field in an IP packet header contains a 3-bit IP precedence field. [Figure 1](#EN-US_CONCEPT_0000001564109785__fig_dc_fd_qos_000501) shows the format of the precedence field in an IP packet.
  
  **Figure 1** IP Precedence/DSCP field  
  ![](figure/en-us_image_0000001564109797.png "Click to enlarge")
  
  Bits 0 to 2 constitute the precedence field, representing values 7, 6, 5, 4, 3, 2, 1 and 0, listed in descending order of priority. The highest-priority values (7 and 6) are reserved for routing and network control communication updates. User-level applications can use only priority values 0 to 5.
  
  In addition to the precedence field, a ToS field contains the following sub-fields:
  
  + Bit D indicates the delay. The value 0 represents a normal delay, and value 1 represents a short delay.
  + Bit T indicates the throughput. The value 0 represents a normal throughput, and value 1 represents a high throughput.
  + Bit R indicates the reliability. The value 0 represents normal reliability, and value 1 represents high reliability.
  
  Bits 6 and 7 represent the Explicit Congestion Notification (ECN) field.
* DSCP field
  
  The ToS field in IP packets was defined in RFC 1349, with bit C (monetary cost) added. Following that, the IETF DiffServ Working Group redefined bits 0 to 5 of a ToS field as the DSCP field in RFC 2474. In RFC 2474, the field name is changed from ToS to differentiated service (DS). [Figure 1](#EN-US_CONCEPT_0000001564109785__fig_dc_fd_qos_000501) shows the DSCP field in packets.
  
  In the DS field, the first six bits (bits 0 to 5) are the DS CodePoint (DSCP) and the last two bits (bits 6 and 7) are reserved. Additionally, the first three bits (bits 0 to 2) are the Class Selector CodePoint (CSCP), which represents the DSCP type. A DS node selects a PHB based on the DSCP value.
* 802.1p value in an Ethernet frame header
  
  Layer 2 devices exchange VLAN frames. As defined in IEEE 802.1Q, the PRI field (802.1p value, also known as CoS) in the Ethernet frame header identifies the QoS requirement. [Figure 2](#EN-US_CONCEPT_0000001564109785__fig_dc_fd_qos_000502) shows the format of the 802.1p value in an Ethernet frame header.
  
  **Figure 2** 802.1p value in an Ethernet frame header  
  ![](figure/en-us_image_0000001512830178.png)
  
  The 802.1Q header contains a 3-bit PRI field and a 1-bit CFI field. The PRI field defines eight service priority values 7, 6, 5, 4, 3, 2, 1, and 0, listed in descending order of priority. The CFI field defines the drop priority of packets.

#### Implementation

In [Figure 3](#EN-US_CONCEPT_0000001564109785__fig_dc_cfg_qos_034501_dc), voice, video, and data traffic from Host1, Host2, and Host3 traverses DeviceA and DeviceB to reach the network. As voice, video, and data services have priorities in descending order, the device needs to provide differentiated QoS services based on their priorities.

Packets carry different precedence fields depending on the network type. For example, packets carry the 802.1p value on a Layer 2 network and the DSCP value on a Layer 3 network. When packets enter a device, the device maps their external priorities to internal priorities and drop priorities, and provides differentiated QoS services for the packets according to their internal priorities and drop priorities. When packets leave the device, the device maps the internal priorities and drop priorities to external priorities so that the network can provide corresponding QoS services based on the external priorities of the packets.

**Figure 3** Implementation of priority mapping  
![](figure/en-us_image_0000001643855614.png)
The implementation of priority mapping is described as follows:

1. On DeviceA, configure traffic policies in the inbound direction to re-mark priorities of voice, video, and data packets into different 802.1p values.
2. On DeviceB, map 802.1p values to internal and drop priorities in the inbound direction to provide differentiated QoS services for packets based on the internal and drop priorities.
3. On DeviceB, map the internal and drop priorities to the corresponding DSCP values in the outbound direction so that the Layer 3 network can provide differentiated QoS services for the three types of services based on the DSCP values.