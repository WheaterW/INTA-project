Understanding IOAM
==================

Understanding IOAM

#### System Components

The IOAM network consists of two parts: data collection module and data analysis module, as shown in [Figure 1](#EN-US_CONCEPT_0000001563758401__fig8843033122013). The data collection module includes three nodes: the encapsulation, transit, and decapsulation nodes, which collect the running data of network nodes and forward packets. The data analysis module mainly consists of an analyzer, which analyzes the collected data to monitor the network.

**Figure 1** IOAM network system  
![](figure/en-us_image_0000001563758477.png "Click to enlarge")

#### IOAM Fundamentals

For the data collection module, three data collection modes are available: trace mode, edge-to-edge mode, and direct-export mode. The following describes the functions of the encapsulation, transit, and decapsulation nodes on the IOAM network in each of these modes.

1. Trace mode
   
   On the network shown in [Figure 2](#EN-US_CONCEPT_0000001563758401__fig8282825173511), the encapsulation, transit, and decapsulation nodes perform the following functions.
   
   **Figure 2** Packet forwarding on an IOAM network in trace mode (TCP packets are used as an example)  
   ![](figure/en-us_image_0000001512678978.png "Click to enlarge")
   * Encapsulation node: samples service packets sent by Host1, encapsulates the packets with IOAM headers and its own metadata (MD), and then forwards the resulting IOAM packets.
   * Transit node: receives IOAM packets from the encapsulation node, adds its own MD into the packets, and then forwards the packets. This node is mainly used in hop-by-hop analysis scenarios to obtain information of the inbound and outbound interfaces, forwarding delay, timestamp, queue depth, and time to live (TTL) of traffic. As the number of hops that packets traverse increases, so does the packet headers, requiring high forwarding performance.
   * Decapsulation node: adds its own MD to received IOAM packets, copies the packet headers without the payload, encapsulates the copied packet headers into packets in NetStream V9 format, and sends the packets to the analyzer. Additionally, the decapsulation node removes IOAM information from the received IOAM packets, and then forwards the packets to Host2.![](public_sys-resources/note_3.0-en-us.png) 
   
   An IOAM packet can be encapsulated with a maximum of eight layers of MD on an IOAM network in trace mode.
2. Edge-to-edge mode
   
   [Figure 3](#EN-US_CONCEPT_0000001563758401__fig5178542124310) shows packet forwarding on an IOAM network in edge-to-edge mode.
   
   **Figure 3** Packet forwarding on an IOAM network in edge-to-edge mode (TCP packets are used as an example)  
   ![](figure/en-us_image_0000001513158122.png "Click to enlarge")
   * Encapsulation node: samples service packets sent by Host1, encapsulates the packets with IOAM headers and its own MD, and then forwards the resulting IOAM packets.
   * Transit node: forwards the IOAM packets received from the encapsulation node without adding its own MD to the packets. This node is mainly used in E2E analysis scenarios to obtain the forwarding delay of service traffic on the entire network. As the transit node does not add its MD to the packets, the length of packet headers does not increase significantly. Therefore, in this mode, there are no high requirements on the device forwarding performance.
   * Decapsulation node: adds its own MD to received IOAM packets, copies the packet headers without the payload, encapsulates the copied packet headers into packets in NetStream V9 format, and sends the packets to the analyzer. Additionally, the decapsulation node removes IOAM information from the received IOAM packets, and then forwards the packets to Host2.![](public_sys-resources/note_3.0-en-us.png) 
   
   On an IOAM network in edge-to-edge mode, transit nodes are optional.
3. Direct-export mode
   
   [Figure 4](#EN-US_CONCEPT_0000001563758401__fig1347974523613) shows packet forwarding on an IOAM network in direct-export mode.
   
   **Figure 4** Packet forwarding on an IOAM network in direct-export mode (TCP packets are used as an example)  
   ![](figure/en-us_image_0000001563998389.png "Click to enlarge")
   * Encapsulation node: samples service packets sent by Host1 and encapsulates the packets with IOAM headers. The node then copies the packet headers, adds its own MD to the copied packet headers, encapsulates the copied packet headers into packets in NetStream V9 format, and sends the packets to the analyzer. The original IOAM packets are then forwarded.
   * Transit node: copies the headers of received IOAM packets, adds its MD to the copied packet headers, encapsulates the copied packet headers into packets in NetStream V9 format, and sends the packets to the analyzer. The original IOAM packets are then forwarded.
   * Decapsulation node: copies the headers of received IOAM packets, adds its MD to the copied packet headers, encapsulates the copied packet headers into packets in NetStream V9 format, and sends the packets to the analyzer. Additionally, the decapsulation node removes IOAM information from the received IOAM packets, and then forwards the packets to Host2.

#### Packet Format

Currently, TCP and VXLAN packets can be sampled on an IOAM network. You can configure an advanced ACL on the encapsulation node to specify a packet sampling rule. For TCP packets, the device matches original packet headers based on the ACL sampling rule, and adds the IOAM header and IOAM MD following the TCP header. For VXLAN packets, the device matches the inner TCP or UDP packet header based on the ACL packet sampling rule, and adds the IOAM header and IOAM MD following the outer UDP header. [Figure 5](#EN-US_CONCEPT_0000001563758401__fig463413917569) shows IOAM encapsulation in different types of packets.

**Figure 5** IOAM encapsulation in different types of packets  
![](figure/en-us_image_0000001563998381.png "Click to enlarge")

1. IOAM header format
   
   An IOAM header consists of the probermarker, IOAM SHIM header, and IOAM option header, as shown in [Figure 6](#EN-US_CONCEPT_0000001563758401__fig114276792815). The probermarker is a 64-bit IOAM header that identifies an IOAM packet. The 32-bit IOAM SHIM header specifies the data collection mode. The 64-bit IOAM option header specifies the MD options in different data encapsulation modes.
   
   **Figure 6** IOAM header format  
   ![](figure/en-us_image_0000001512678998.png "Click to enlarge")
   
   **Table 1** Description of probermarker
   | Field | Length | Description |
   | --- | --- | --- |
   | Probermarker | 64 bits | Identifies an IOAM packet, which is invariably 0xAABBCCDDDDCCBBAA. |
   
   
   **Table 2** Description of fields in the IOAM SHIM header
   | Field | Length | Description |
   | --- | --- | --- |
   | IOAM Type | 8 bits | Data collection mode of an IOAM packet, which can be trace or edge-to-edge. |
   | IOAM HDR Len | 8 bits | Length of the IOAM header, in units of 4 bytes. |
   | Reserved | 16 bits | Reserved field. |
   
   
   **Table 3** Description of fields in the IOAM option header (in trace or direct-export mode)
   | Field | Length | Description |
   | --- | --- | --- |
   | Namespace ID | 16 bits | Namespace ID of a node. |
   | Node Len | 5 bits | Length of the MD added by a node, in units of 4 bytes. |
   | Flags | 4 bits | Bit0 Overflow (O-bit): most significant bit. If the **Remaining Len** value is less than the **Node Len** value, no MD is added.  Bit1 Loopback (L-bit): loopback mode, which is currently not configurable.  Bit2 Active (A-bit): whether a packet is sent by the CPU, which is currently not configurable.  Bit3 Immediate Export (I-bit): indicates that each IOAM-capable node immediately exports IOAM data fields to the analyzer.  When Bit3 is set to 1, the direct-export mode is used. |
   | Remaining Len | 7 bits | Length of the MD that can be added, in units of 4 bytes. |
   | IOAM-Trace-Type | 24 bits | Trace mode flag, which is invariably 0xFA1001. |
   | Reserved | 8 bits | Reserved, with all the bits being 0. |
   
   
   **Table 4** Description of fields in the IOAM option header (in edge-to-edge mode)
   | Field | Length | Description |
   | --- | --- | --- |
   | Namespace ID | 16 bits | Namespace ID of a node. |
   | IOAM-Edge-to-Edge-Type | 16 bits | Edge-to-edge mode flag, which is invariably 0xB000. |
2. IOAM MD formats
   
   The MD collected varies according to the data collection modes, as shown in [Figure 7](#EN-US_CONCEPT_0000001563758401__fig159002401497). In trace and direct-export modes, the MD contains information of the inbound and outbound interfaces, forwarding delay, timestamp, and queue depth of a node. In edge-to-edge mode, the MD contains the sequence number and the timestamp when a packet enters the device.
   
   **Figure 7** IOAM MD formats  
   ![](figure/en-us_image_0000001513158134.png "Click to enlarge")
   
   **Table 5** Description of fields in the IOAM MD (in trace or direct-export mode)
   | Field | Length | Description |
   | --- | --- | --- |
   | HopLimit | 8 bits | Hop count limit. |
   | Device ID | 24 bits | Device ID. |
   | Ingress Port ID | 16 bits | Inbound interface ID. |
   | Egress Port ID | 16 bits | Outbound interface ID. |
   | In TimeStamp | 64 bits | Timestamp when a packet enters the device. |
   | Forwarding Delay | 32 bits | Forwarding delay. |
   | Queue Depth | 32 bits | Queue depth. |
   | Buffer | 32 bits | Buffer. |
   | Checksum Complement | 32 bits | Checksum complement of the IOAM header. |
   
   
   **Table 6** Description of fields in the IOAM MD (in edge-to-edge mode)
   | Field | Length | Description |
   | --- | --- | --- |
   | Sequence | 64 bits | Sequence number of an IOAM packet. |
   | In TimeStamp | 64 bits | Timestamp when a packet enters the device. |