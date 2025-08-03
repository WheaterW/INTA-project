Intelligent Traffic Analysis for UDP Flows
==========================================

Unlike TCP, UDP is a connectionless transport layer protocol that has poor reliability. However, UDP is simpler than TCP and features fewer control options, less latency, and higher data transmission efficiency. Therefore, UDP is suitable for applications that do not require high reliability or that can ensure reliability by themselves, for example, DNS, TFTP, and SNMP. UDP is widely used on data center networks. The intelligent traffic analysis function for UDP flows enables the device to match the received UDP packets based on ACL rules and send the matched packets to the TAP for analysis. The TAP then sends the analysis result to the TDA for further analysis and graphical display.

#### Basic Concepts

UDP is a connectionless transport layer protocol that provides a simple and unreliable message service for transaction-oriented services. UDP does not provide any fragmentation, reassembly, or sorting mechanism for data packets. For this reason, after a packet is sent, UDP cannot guarantee that the packet arrives at the destination securely or completely. [Figure 1](#EN-US_CONCEPT_0000001512853436__fig088212108481) shows the format of a UDP packet. From the figure, it can be seen that the UDP packet is very simple, which gives UDP the advantages of low resource consumption and fast processing. Such advantages make UDP an ideal choice for applications that have high requirements on transmission efficiency but not data integrity, such as audio and multimedia applications. Just like TCP packets, UDP packets are encapsulated in IP packets during transmission on the network.

**Figure 1** Format of a UDP packet  
![](figure/en-us_image_0000001564013213.png)

The main fields in a UDP packet are described as follows:

* A UDP packet consists of a UDP header and UDP data. The UDP header consists of 4 fields, each of which is 2 bytes:
  + Source Port and Destination Port identify the ports of the sender and receiver.
  + The Length field specifies the length in bytes of the UDP packet. The minimum length is 8 bytes, which is the length of the UDP header.
  + The Checksum field is used for error-checking during UDP packet transmission. A UDP packet is discarded if an error is found.
* An IP header is encapsulated at the front of the UDP packet:
  + The Protocol field specifies the number of the protocol used in the data portion of an IP packet, so that the IP layer of the destination host can know the process to which the packet is to be sent (different protocols are processed by different processes). The numbers of different protocols are as follows: TCP: 6; UDP: 17; ICMP: 1.
  + The Identification field uniquely identifies an IP packet sent by the host. The value is typically incremented by 1 each time a packet is sent. An IP packet may be fragmented if the length of the packet exceeds the maximum transmission unit (MTU) value allowed by the transport network. The value of Identification is replicated to the Identification field of each fragment. In this way, the destination assembles fragments with the same Identification value into the original IP packet. For a UDP flow, the Identification value representing the sequence number of a UDP packet is incremented by 1 each time the host sends a UDP packet. The size of the Identification field is 16 bits. Therefore, the sequence numbers of UDP packets in a UDP flow are in the range from 0 to 65535.

#### UDP Flow Matching

* **Flow matching on the TDE**
  
  When the intelligent traffic analysis module collects UDP traffic on inbound interfaces of a device, the device matches the received UDP traffic based on the delivered ACL rules. The device mirrors and sends the matched UDP packets to the TAP. The ACL rules that are not supported cannot be delivered, preventing the TAP from receiving corresponding service flows.
* **Flow matching on the TAP**
  
  After intelligent traffic analysis for UDP flows is enabled, the TAP creates flow tables for received service flows and analyzes the flows. If the TAP cannot process the packets sent by the TDE, for example, the TAP does not support the packet type or the number of received packets exceeds the processing capability of the TAP, the TAP discards the packets.

#### UDP Flow Analysis

In contrast to intelligent traffic analysis for TCP flows, intelligent traffic analysis for UDP flows performs flow table creation and analysis on a per-block basis. The Identification field determines the sequence number of a UDP packet. Based on these sequence numbers, UDP packets in a UDP flow are grouped into multiple blocks. By default, the intelligent traffic analysis module sets the number of blocks to 256. That is, a UDP flow is divided into 256 blocks. Since the sequence number of UDP packets ranges from 0 to 65535, UDP packets numbered from 0 to 255 belong to the first block, as shown in [Figure 2](#EN-US_CONCEPT_0000001512853436__fig1689115112216).

**Figure 2** UDP block division  
![](figure/en-us_image_0000001563892953.png)

After receiving a matched UDP flow, the TAP analyzes all UDP packets in the first UDP block and creates a flow table based on key values such as 5-tuple information in the packets. The TAP then collects statistics on some key fields in the flow table based on UDP packets in subsequent blocks sent from the TDE, and analyzes the statistical results to obtain characteristics of the flow.

* **Flow table creation based on 5-tuple information**
  
  Intelligent traffic analysis for UDP flows supports flow table creation based on 5-tuple information in UDP packets. The 5-tuple information uniquely identifies a UDP session. [Table 1](#EN-US_CONCEPT_0000001512853436__tab_dc_fd_traffic-analysis_000501) lists the five key values in 5-tuple information for creating a UDP flow table.
  
  **Table 1** Key values in 5-tuple information for creating a UDP flow table
  | Key Value | Description |
  | --- | --- |
  | SPORT | Specifies the source port number of a UDP flow. |
  | SIP | Specifies the source IP address of a UDP flow. Currently, only IPv4 addresses are supported. |
  | DPORT | Specifies the destination port number of a UDP flow. |
  | DIP | Specifies the destination IP address of a UDP flow. Currently, only IPv4 addresses are supported. |
  | Protocol | Specifies the UDP protocol. |
* **Flow table characteristics**
  
  After creating an intelligent traffic analysis flow table based on the first UDP block, the TAP collects statistics on fields in the flow table based on UDP packets in subsequent blocks and analyzes the characteristics of the flow. Note that intelligent traffic analysis for UDP flows does not require packets to be sent and received along the same path. The UDP flow table created by the TAP contains only unidirectional information of the UDP flow. Characteristics of the sent and received packets in the UDP flow can be obtained after the TDA summarizes all the received flow analysis results.
  
  [Table 2](#EN-US_CONCEPT_0000001512853436__tab_dc_fd_traffic-analysis_000502) lists the UDP traffic characteristics that can be analyzed by the TAP.
  
  **Table 2** UDP traffic characteristics that can be analyzed by the TAP
  | Characteristic | Description |
  | --- | --- |
  | Number of packets | The TAP can count the number of UDP packets in each block. The TDA summarizes packet quantity statistics and compares the number of UDP packets in each block of the same UDP flow to determine whether packet loss occurs. |
  | Size of packets | The TAP can count the number of bytes of UDP packets in a block. |
  | Timestamp | The TAP can collect statistics on timestamps of blocks. For the same UDP flow, the timestamp increases with the block ID. After the TDA summarizes timestamp statistics, it can obtain the latency of the UDP flow. |
  | Path | The TAP can collect statistics about inbound interfaces of UDP packets and sends the statistics to the TDA. After intelligent traffic analysis for UDP flows is configured on the entire network, you can view the actual path of the UDP flow on the TDA.  NOTE:  The intelligent traffic analysis function for UDP flows must be configured on the entire network to monitor the paths of UDP flows on the network. |
  | Flow table creation time | The TAP can collect statistics on the time when a UDP flow table is created. |

#### UDP Flow Export

After creating a flow table based on UDP packets sent from the TDE, the TAP exports the flow table that contains the flow analysis result to the specified TDA for further processing and graphical display of the flow information. The UDP flow table export process is similar to the TCP flow table export process. For details, see [TCP Flow Table Export](galaxy_traffic-analysis_cfg_0005.html#EN-US_CONCEPT_0000001563892933__section105033210299).

Note that UDP flow analysis results are periodically sent to the TDA on a per-block basis when a UDP flow is continuously received. The details are as follows:

1. Because the flow table is created based on the first UDP block, the flow analysis result of the first UDP block is not immediately sent to the TDA. Instead, the TAP continues to analyze the second UDP block.
2. When receiving the third UDP block, the TAP sends the flow analysis result of the first UDP block to the TDA.
3. When receiving the fourth block, the TAP sends the flow analysis result of the second UDP block to the TDA.

The TAP repeats this process until inactive flow aging of the flow table is triggered as follows: When the inactive time (the time from when the last UDP packet is received to the current time) of the UDP flow exceeds the configured inactive flow aging time, the device considers that the UDP flow is inactive (the flow is interrupted). In this case, the device forcibly sends the current flow table to the TDA and deletes it. This process is called inactive flow aging.