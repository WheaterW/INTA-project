Understanding AnyFlow
=====================

Understanding AnyFlow

#### AnyFlow Components

An AnyFlow system consists of the AnyFlow Data Exporter (ADE), AnyFlow Data Processor (ADP), and AnyFlow Data Analyzer (ADA).

* ADE: collects service flows, identifies TCP exceptions, and sends collected data to the ADP.
* ADP: processes and analyzes the data sent by the ADE, and exports the analysis results to the ADA.
* ADA: provides a graphical user interface (GUI) for users to intuitively obtain, view, and analyze collected data. For example, iMaster NCE-FabricInsight can function as an ADA.

In actual application scenarios, the ADE and ADP are integrated on a single device. As shown in [Figure 1](#EN-US_CONCEPT_0000001563869841__fig_dc_fd_traffic-analysis_000401), DeviceB functions as both the ADE and ADP to collect traffic statistics and create flow entries in order to detect typical TCP exceptions. When the buffer for flow entries is full or the aging time of flow entries expires, DeviceB exports the flow entries to the ADA in packets. The ADA analyzes the packets and displays the analysis result.

**Figure 1** Network diagram of an AnyFlow system  
![](figure/en-us_image_0000001563869877.png)

#### AnyFlow Working Process

On a device, the intelligent analysis engine of the forwarding chip functions as the ADE, and the chip built in the CPU functions as the ADP. The ADE and ADP collaborate to collect and analyze traffic, detect exceptions, encapsulate statistics into packets in NetStream V9 format, and send these packets to the analyzer. [Figure 2](#EN-US_CONCEPT_0000001563869841__fig41031913165516) shows how AnyFlow works.

**Figure 2** AnyFlow working process  
![](figure/en-us_image_0000001513149874.png)
#### Flow Entry Creation

[Table 1](#EN-US_CONCEPT_0000001563869841__table1359416230237) describes the fields collected for creating flow entries, based on which traffic statistics, path visualization, application access visualization, application-side packet loss awareness for TCP traffic, and TCP exception awareness can be implemented.

**Table 1** Fields collected for creating flow entries
| Field | Description | Application Scenario |
| --- | --- | --- |
| Flow identifier | For TCP, UDP, and VXLAN packets: source IP address, destination IP address, source port number, destination port number, and protocol number.  For RoCEv2 packets: source IP address, destination IP address, and destination queue pair (QP) (used to identify a RoCEv2 flow). | Used to identify a flow. |
| Flow start time | For TCP packets, this field indicates the time when a SYN packet is received.  For UDP and RoCEv2 packets, this field indicates the time when the first packet is received.  For VXLAN packets, the meaning of this field depends on the packets' inner information (TCP, UDP, or RoCEv2) collected by the device. | Used with the flow end time to calculate the flow duration. |
| Flow end time | For TCP packets, this field indicates the time when a FIN packet is received.  For UDP and RoCEv2 packets, this field indicates the time when the last packet is received.  For VXLAN packets, the meaning of this field depends on the packets' inner information (TCP, UDP, or RoCEv2) collected by the device. | Used with the flow start time to calculate the flow duration. |
| Inbound/outbound interface | Inbound and outbound interfaces of a packet. | Used to record traffic paths to implement path visualization. |
| Statistics | Numbers of packets and bytes. | Used for traffic statistics and throughput analysis. |
| TCP SN | Sequence number of the next TCP packet. | Used to detect application-side packet loss for TCP traffic. |
| Anomaly flag | Flag for identifying a TCP packet exception. | Used to identify TCP exceptions, such as TCP reset, TTL change, and packet errors. |

Flow entries are created in two phases:

1. When traffic reaches the device, the intelligent analysis engine module on the forwarding chip processes the traffic as follows:
   1. If the storage space is sufficient, a flow entry is created. When the flow entry is aged out or the reporting interval expires, the flow entry is sent to the chip built in the CPU.
   2. If the storage space is insufficient, a flow entry is created only for SYN/FIN packets and immediately sent to the chip built in the CPU. For non-SYN/FIN packets, no flow entry is created.
2. When the chip built in the CPU receives flow statistics sent by the forwarding chip, it processes them as follows:
   1. If the storage space is sufficient, a flow entry is created. When the flow entry is aged out or the reporting interval expires, the flow entry is sent to the analyzer.
   2. If the storage space is insufficient, a flow entry is created only for SYN/FIN packets and immediately sent to the analyzer. For non-SYN/FIN packets, no flow entry is created, and the analyzer is notified that some packets are discarded.

There are two types of flow tables. One is created on the forwarding chip, which is also called hardware flow table. The other is created on the chip built in the CPU.


#### Flow Entry Export

**Original flow statistics export**

When the flow aging time or reporting interval expires, statistics about each flow are exported to the analyzer. Through original flow statistics export, the analyzer can obtain details about each flow.

**Aggregated flow statistics export**

In aggregated flow statistics export, the chip built in the CPU aggregates the original flows based on aggregation keywords, and exports statistics about the aggregation flows to the analyzer. This export mode greatly reduces bandwidth consumption. Aggregation keywords include the source IP address, destination IP address, destination port number, and protocol type. Only flows whose session status is normal can be aggregated. As shown in [Figure 3](#EN-US_CONCEPT_0000001563869841__fig11760103784916), five original flows in normal session state are aggregated into two flows.

**Figure 3** Aggregation of original flows  
![](figure/en-us_image_0000001512830350.png)

#### Exception Detection

AnyFlow enables the device to use the built-in intelligent analysis engine to proactively analyze TCP exceptions and report the analysis result to the analyzer.

On the network shown in [Figure 4](#EN-US_CONCEPT_0000001563869841__fig1361555192713), the intelligent analysis engine expects a packet with the sequence number of 14100, but actually receives a packet with the sequence number of 15100. After determining that packet loss has occurred, the device proactively reports this exception to the analyzer without the need of analysis on the analyzer, thus reducing the analysis pressure on the analyzer.

**Figure 4** TCP sequence number exception  
![](figure/en-us_image_0000001563750241.png)

AnyFlow detects and reports TCP exceptions to the analyzer for the administrator to predict physical network risks. The following 16 types of TCP exceptions can be detected:

1. DF changing
2. TTL changing
3. Multi-SYN
4. SF anomaly
5. RS anomaly
6. FPU anomaly
7. FA anomaly
8. RA anomaly
9. SFRA anomaly
10. SFRAUP anomaly
11. TCP out-of-range anomaly
12. TCP resent anomaly
13. TCP SYN with data anomaly
14. SYN &FIN are all valid simultaneously
15. Multi-SYN of TCP
16. FIN of TCP