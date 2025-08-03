Intelligent Traffic Analysis for TCP Flows
==========================================

TCP is a connection-oriented, highly reliable protocol. For this reason, 90% of services in a data center are transmitted over TCP. With so many services being TCP-based, a TCP-related fault will have a huge impact on the network. Therefore, the intelligent traffic analysis function is implemented for TCP flows.

When packets in both directions of a specified TCP flow pass through the same device, the intelligent traffic analysis module of the device matches packets of the TCP flow based on ACL rules on the inbound interfaces of the device, and creates a flow table for the matched TCP packets for in-depth analysis. In this way, it is possible to obtain high-precision information such as the packet loss rate, latency, and status of the TCP flow.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support intelligent traffic analysis for TCP flows.


#### Basic Concepts

TCP provides connection-oriented and reliable delivery of a stream of bytes between applications. To ensure the receiver is aware of any packet loss, the sender specifies a sequence number for each TCP packet. This also ensures that the receiver is able to reorder the packets into the correct sequence. After successfully receiving a packet, the receiver sends an acknowledgment (ACK) packet to the sender. If the sender does not receive any ACK packet within a specified RTT, it considers that the sent data packet was lost and retransmits the packet. [Figure 1](#EN-US_CONCEPT_0000001563892933__fig088212108481) shows the format of a TCP packet.

**Figure 1** Format of a TCP packet  
![](figure/en-us_image_0000001512693836.png)

The main fields in a TCP header are described as follows:

* Source Port and Destination Port are both 16 bits long. Source Port and Destination Port are key values for creating a TCP flow table when intelligent traffic analysis for TCP flows is enabled.
* Sequence Number specifies the sequence number of a sent packet. This field is 32 bits long.
  + If the SYN flag is set to 1, a client is attempting to establish a TCP connection with a server. In this case, Sequence Number is the initial sequence number of a TCP packet.
  + If the SYN flag is set to 0, a TCP connection has been established between a client and a server. In this case, the Sequence Number field specifies the sequence number of the first byte in the TCP packet sent from the client, which is the initial sequence number plus 1.
* Acknowledgment Number is 32 bits long. This field is valid only when the ACK flag is set to 1. Sequence Number and Acknowledgment Number are important parameters used in intelligent traffic analysis for matching TCP packets sent and received along different paths.
* Flags are important for analyzing the TCP flow status.
  + URG: The value 1 indicates a high-priority data packet and that the Urgent Pointer field is significant.
  + ACK: The value 1 indicates that the Acknowledgment Number field is significant.
  + PSH: The value 1 indicates the push function that asks the receiver to push the buffered data to the application layer without waiting for the buffer to be full.
  + RST: The value 1 indicates a major error. In this case, the TCP connection may need to be reset.
  + SYN: The value 1 indicates that a client and a server are establishing a TCP connection and sequence numbers are synchronized.
  + FIN: The value 1 indicates that the packet is the last to be sent from the sender. This field is used when the TCP connection is to be torn down.
* Urgent Pointer is 16 bits long. This field specifies an offset from the relative sequence number indicating the last urgent data byte and is significant only when URG is set to 1.

#### TCP Flow Matching

* **Flow matching on the TDE**
  
  The administrator configures a service flow to be detected on the TDE and delivers an ACL rule to match the service flow. The TDE mirrors and sends matched packets to the TAP. The ACL rules that are not supported cannot be delivered, preventing the TAP from receiving corresponding service flows.
* **Flow matching on the TAP**
  
  After intelligent traffic analysis for TCP flows is enabled, the TAP creates flow tables for received service flows and analyzes the flows. If the TAP cannot process the packets sent by the TDE, for example, the TAP does not support the packet type or the number of received packets exceeds the processing capability of the TAP, the TAP discards the packets.

#### TCP Flow Analysis

Intelligent traffic analysis collects and analyzes packet statistics based on flows. After receiving matched TCP packets, the TAP creates a flow table based on 5-tuple information in the packets. The TAP then collects statistics on certain key fields in the flow table, and analyzes the statistical results to obtain high-precision service flow information to determine the flow's characteristics.

The statistics in a flow table are continuously collected within the flow lifetime and can be viewed on the device. In addition, after the flow is aged out, the statistical results are exported to the TDA for further display and analysis.

* **Flow table creation based on 5-tuple information**
  
  Currently, intelligent traffic analysis for TCP flows supports flow table creation based on 5-tuple information in TCP packets. The 5-tuple information uniquely identifies a session, for example: 192.168.1.1, 10000, TCP, 172.16.1.1, and 80. This 5-tuple indicates that the terminal with the IP address 192.168.1.1 and using port number 10000 establishes a TCP connection with the terminal with the IP address 172.16.1.1 and using port number 80.
  
  [Table 1](#EN-US_CONCEPT_0000001563892933__tab_dc_fd_traffic-analysis_000501) lists the five key values in 5-tuple information for creating a TCP flow table.
  
  **Table 1** Key values in 5-tuple information for creating a TCP flow table
  | Key Value | Description |
  | --- | --- |
  | ClientPort | Specifies the port number of a client that sends and receives TCP flows. |
  | ClientIP | Specifies the IP address of a client that sends and receives TCP flows. Currently, only IPv4 addresses are supported.  + For a flow table created based on SYN packets, the SIP is the source IP address of the SYN packets. + For a flow table created based on TCP intermediate data packets, the SIP is the source IP address of the first packet received by the TAP. |
  | ServerPort | Specifies the port number of a server that sends and receives TCP flows. |
  | ServerIP | Specifies the IP address of a server that sends and receives TCP flows. Currently, only IPv4 addresses are supported. |
  | Protocol | Specifies the TCP protocol. |
* **Flow table characteristics**
  
  After a TCP flow table is created based on 5-tuple information, the TAP collects statistics on fields in the flow table and analyzes characteristics of the flow.
  
  [Table 2](#EN-US_CONCEPT_0000001563892933__tab_dc_fd_traffic-analysis_000502) lists the TCP traffic characteristics that can be analyzed by the TAP.
  
  **Table 2** TCP traffic characteristics that can be analyzed by the TAP
  | Characteristic | Description |
  | --- | --- |
  | Number of discarded packets | The TAP can collect the following statistics on packets transmitted in both directions: + Total number of discarded packets + Number of packets discarded on the upstream device |
  | Latency | The TAP can calculate the smoothed RTT for packets transmitted in both directions, which is accurate to the nearest nanosecond. |
  | Number of packets | The TAP can count the number of packets transmitted in each direction. |
  | Flow status | The TAP can analyze the TCP flow status in the current flow table. The flow status can be one of the following:  + SYN status + SYN + ACK status + ACK status + TCP connection establishment status + TCP connection termination status |
  | Flow table creation time | The TAP can collect statistics on the time when a TCP flow table is created. |
  | Inbound interface of packets | The TAP can identify the inbound interfaces of packets transmitted in both directions. |

#### TCP Flow Table Export

Intelligent traffic analysis for TCP flows allows users to view TCP flow characteristics analyzed by the TAP. In addition, flow tables need to be exported to the TDA for visualized and user-friendly display of analysis results. Currently, only the iMaster NCE-FabricInsight can be used as the TDA, which consists of the FabricInsight collector and FabricInsight analyzer.

[Figure 2](#EN-US_CONCEPT_0000001563892933__fig3599161025517) shows the process of exporting TCP flow tables. The intelligent traffic analysis flow tables that contain flow analysis results are first stored on the device. When a flow table meets the aging conditions, the device sends the flow table to the FabricInsight collector, which then summarizes the content and sends it to the FabricInsight analyzer for final processing and display of flow characteristics.

**Figure 2** Exporting TCP flow tables  
![](figure/en-us_image_0000001563773329.png)

An intelligent traffic analysis flow table is exported to the FabricInsight collector only when the flow table meets aging conditions or the aging time expires. The device supports three aging modes for TCP flow tables: active flow aging, inactive flow aging, and FIN- or RST-based aging. When multiple aging modes are configured on the device, a flow table is aged out as soon as it meets any aging condition.

* **Active flow aging**
  
  When active flow aging is configured, a flow is collected within a specified period, starting from the time that its first packet is sampled. When this specified period is reached, the device exports analysis information about the flow to the TDA. This aging mode is enabled by default and suitable for analyzing flows that span a relatively long period of time.
* **Inactive flow aging**
  
  When inactive flow aging is configured, if no record is added to the flow table of a specified flow (as determined by the number of collected packets) within the inactive flow aging time, the device exports records of this flow to the TDA and deletes the records.
  
  Inactive flow aging clears unnecessary entries so that the device can fully leverage statistics entries. This aging mode is enabled by default and suitable for analyzing flows that span a relatively short period of time. The device exports flow statistics as soon as the flow stops, saving memory.
* **FIN- or RST-based aging**
  
  When FIN- or RST-based aging is configured, the TCP connection for a flow is disconnected if a FIN or RST packet is added to the flow. The device can then immediately export the existing statistics in the flow table and delete the flow records to save space in the flow table.
  
  This aging mode is disabled by default.

In practice, the TAP uses the NetStream V9 template to define the statistical fields in an intelligent traffic analysis flow table. When a flow table meets aging conditions, instead of directly exporting the flow table to the FabricInsight collector, the TAP adds the statistical fields in the flow table to the NetStream V9 template for encapsulation. The forwarding chip then sends the encapsulated packets to the FabricInsight collector based on routing entries.

[Figure 3](#EN-US_CONCEPT_0000001563892933__fig157301351112510) shows the format of an exported packet in the intelligent traffic analysis system. Such a packet is encapsulated based on UDP, and includes the NetStream packet header in the NetStream V9 format as well as one or more intelligent traffic analysis results. In addition, because intelligent traffic analysis for TCP flows needs to be used together with the Layer 3 remote flow mirroring function, the source IP address of the exported packets in the intelligent traffic analysis system must be set to the IP address of the mirrored device in Layer 3 remote flow mirroring.

**Figure 3** Format of an exported packet in the intelligent traffic analysis system  
![](figure/en-us_image_0000001563773333.png)

After receiving the exported packets from the intelligent traffic analysis system, the FabricInsight collector summarizes the characteristics of service flows based on packet information such as source addresses, and sends the characteristics to the FabricInsight analyzer for graphical display.

Specifically, for TCP packets sent and received along different paths, FabricInsight summarizes the characteristics in the flow tables containing unidirectional packet information (unidirectional flow table for short) based on the exported packets, and finally obtains complete characteristics of the TCP flow.


#### Analysis of TCP Packets Sent and Received Along Different Paths

In scenarios such as M-LAG and ECMP, packets in the same TCP flow may be sent and received along different paths. In these scenarios, after the intelligent traffic analysis module samples and sends TCP packets that match ACL rules to the TAP, the TAP creates a unidirectional TCP flow table based on the first packet. When the TAP receives TCP packets in the same direction again, the TAP takes different actions based on whether reverse-direction information about the packets exists in the flow table.

* If reverse-direction information exists in the flow table, the response packet to the first packet also passes through the local device. In this case, the TAP considers that packets in the flow are sent and received along the same path and will age out the flow table normally.
* If no reverse-direction information exists in the flow table, the TAP considers that packets in the flow are sent and received along different paths and triggers the unidirectional flow table creation mechanism:
  1. The TAP identifies the sequence number or acknowledgment number in the collected TCP packets.
  2. If the sequence number is within the range configured by the administrator, the TAP creates a TCP flow entry that contains unidirectional information about each TCP packet with the sequence number in this range.
  3. After creating a unidirectional flow table for each packet, the TAP sends the flow table to the FabricInsight collector in real time, without waiting for the flow table to meet aging conditions. The FabricInsight collector then summarizes and sends characteristics of the TCP flow to the FabricInsight analyzer for graphical display.

Link failures or route switching may cause the link on which a TCP flow is transmitted to change. This can cause the flow table to be exported in one of two ways:

* Bidirectional traffic changes from using different paths to using the same path:
  
  The TAP exports the unidirectional flow table of each packet before the current active flow aging timer expires. When the next active flow aging timer starts, the TAP exports the flow table containing bidirectional information (bidirectional flow table for short) about the TCP flow.
* Bidirectional traffic changes from using the same path to using different paths:
  
  The TAP exports and ages bidirectional flow tables normally until no traffic of the same flow is sent. FabricInsight determines that a path switching event occurs when no information about a characteristic is added to the flow table or interface information in the flow table is changed.