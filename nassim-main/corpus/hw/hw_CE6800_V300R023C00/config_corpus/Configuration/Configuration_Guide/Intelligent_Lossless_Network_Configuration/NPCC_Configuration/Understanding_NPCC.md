Understanding NPCC
==================

Understanding NPCC

#### RoCEv2 Packet Format

NPCC takes effect only on RoCEv2 packets, which are encapsulated based on UDP. [Figure 1](#EN-US_CONCEPT_0000001512680458__fig4958336487) shows the format of an RoCEv2 packet.**Figure 1** RoCEv2 packet format  
![](figure/en-us_image_0000001563759965.png)

* Ethernet Header: contains the source and destination MAC addresses.
* IP Header: contains the source and destination IP addresses.
* UDP Header: contains the source and destination port numbers. The destination port number is 4791.
* InfiniBand Base Transport Header: indicates the header field of the InfiniBand transport layer, including key information of the RoCEv2 packet. For details about the main fields involved in the NPCC function, see [Table 1](#EN-US_CONCEPT_0000001512680458__table45490246526).
* InfiniBand Payload: indicates the message payload.

**Table 1** Some fields in the InfiniBand Base Transport Header
| Field | Description |
| --- | --- |
| Opcode | RoCEv2 packet type, which can be:  * Communication Management (ConnectMsg): The packet is used to set up an RoCEv2 connection. * Send: The sender does not control where the receiver stores data. * Write: The address, key, and length of the data to be written by the receiver are specified in the packet. * Read: The address, key, and length of the data to be read by the receiver are specified in the packet. * Acknowledge (ACK): The packet is used by the receiver to respond to the sender.  RoCEv2 packets of the Send, Write, and Read types are also called data packets. |
| Dest QP | Destination Queue Pair, which is used to identify an RoCEv2 flow. |




#### NPCC Implementation

**Figure 2** NPCC implementation  
![](figure/en-us_image_0000001563879617.png)

[Figure 2](#EN-US_CONCEPT_0000001512680458__fig0810227163617) shows how NPCC is implemented.

1. Maintaining an RoCEv2 flow table and obtaining path information
   
   An NPCC-enabled port on a forwarding device replicates the RoCEv2 ACK packet and data packet passing through it and sends them to the CPU.
   
   1. The forwarding device creates an RoCEv2 flow table based on the source IP address, destination IP address, and QP information in the ACK packet.
   2. The forwarding device updates the Target Port (TP) information (port index information) in the flow table according to the data packet, and associates the flow table with the NPCC-enabled port.
   
   The forwarding device repeats these operations to continuously maintain the RoCEv2 flow table, based on which it can obtain the address information and forwarding path of each RoCEv2 flow.
2. Detecting the congestion status of a lossless queue and calculating the number of CNPs
   
   The forwarding device detects the length (buffer usage) of an NPCC-enabled lossless queue on the NPCC-enabled port and intelligently calculates the number of CNPs to be sent based on the lossless queue's congestion status.
   
   * If the queue length increases: When the queue is shallow, the forwarding device sends a small number of CNPs to prevent incorrect determination of the congestion status. When the queue is deep, the forwarding device sends a large number of CNPs to quickly relieve queue congestion and reduce the forwarding latency.
   * If the queue length decreases: When the queue is shallow, the forwarding device does not send CNPs, preventing the throughput from decreasing due to excess rate reduction. When the queue is deep, the forwarding device sends a small number of CNPs to relieve queue congestion while maintaining the highest-possible throughput and lowest-possible latency.
   * If the queue has a sudden low jitter: The forwarding device considers that a microburst has occurred and therefore does not send CNPs, preventing excess rate reduction.
3. Constructing and forwarding CNPs
   
   The forwarding device constructs CNPs based on address information in the RoCEv2 flow table (the number of CNPs is calculated based on the congestion status in Step 2). It then proactively sends the CNPs to the receiver. After receiving the CNPs, the receiver reduces the rate at which it sends RoCEv2 packets.