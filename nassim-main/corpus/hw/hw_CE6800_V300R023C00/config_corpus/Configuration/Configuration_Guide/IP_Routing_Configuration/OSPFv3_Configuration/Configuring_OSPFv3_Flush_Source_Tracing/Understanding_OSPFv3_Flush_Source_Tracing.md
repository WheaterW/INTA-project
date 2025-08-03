Understanding OSPFv3 Flush Source Tracing
=========================================

Understanding OSPFv3 Flush Source Tracing

#### Context

If network-wide OSPFv3 LSA flush causes network instability, source tracing must be implemented as soon as possible to locate and isolate the fault source. However, OSPFv3 itself does not support source tracing. A conventional solution is to isolate nodes one by one until the fault source is located, but the process is complex and time-consuming and may compromise network services. To solve the preceding problem, OSPFv3 introduces a proprietary protocol, namely, the source tracing protocol. This protocol supports the flooding of flush source information. When the preceding problem occurs, you can quickly query the flush source information on any device on the network to quickly locate the fault source.


#### Related Concepts

**Source tracing**

The source tracing protocol provides a flush source tracing mechanism to locate the device that flushes an OSPFv3 LSA. This feature has the following characteristics:

* Uses a new UDP port. Source tracing packets are carried by UDP packets, and the UDP packets carry the OSPFv3 LSAs flushed by the current device and are flooded hop by hop based on the OSPFv3 topology.
* Depends on OSPFv3 neighbors for flooding and forwards packets along UDP channels, which are independent of the channels used to transmit OSPFv3 packets. Therefore, this protocol facilitates incremental deployment. In addition, source tracing does not affect the devices with the related UDP port disabled.
* Supports query of the node that flushed LSAs on any device that supports this feature after source tracing packets are flooded on the network, which speeds up fault locating and faulty node isolation by maintenance personnel.

**Flush**

Network-wide OSPFv3 LSAs are deleted.

**PS-Hello packets**

Packets used to negotiate the OSPFv3 flush source tracing capability between OSPFv3 neighbors.

**PS-LSA**

When a device flushes an OSPFv3 LSA, it generates a PS-LSA carrying information about the device and brief information about the OSPFv3 LSA.

**PS-LSU packets**

OSPFv3 flush source tracing packets that carry PS-LSAs.

**PS-LSU ACK packets**

Acknowledgment packets used to enhance the reliability of OSPFv3 flush source tracing packets.

**OSPFv3 flush source tracing port**

ID of the UDP port that receives and sends OSPFv3 flush source tracing packets. The ID is configurable.


#### Fundamentals

The implementation of OSPFv3 flush source tracing is as follows:

1. Source tracing capability negotiation
   
   After an OSPFv3 neighbor relationship is established between two devices, they need to negotiate the source tracing capability through PS-Hello packets.
2. PS-LSA generation and flooding
   
   When a device flushes an OSPFv3 LSA, it generates a PS-LSA carrying information about the device and brief information about the OSPFv3 LSA, adds the PS-LSA to a PS-LSU packet, and floods the PS-LSU packet to source tracing-capable neighbors, which helps other devices locate the fault source and perform isolation.

![](../public_sys-resources/note_3.0-en-us.png) 

Only router-LSAs, network-LSAs, and inter-area-router-LSAs can be flushed. Therefore, a device generates a PS-LSA only when it flushes a router-LSA, network-LSA, or inter-area-router-LSA.




#### Source Tracing Capability Negotiation

The source tracing protocol uses UDP to carry source tracing packets and listens to the UDP port, which is used to receive source tracing packets. If a source tracing-capable Huawei device sends source tracing packets to a source tracing-incapable Huawei device or non-Huawei device, the source tracing-capable Huawei device may be incorrectly identified as an attacker. Therefore, the source tracing capability needs to be negotiated between the devices. In addition, the source tracing-capable device needs to send source tracing information on behalf of the source tracing-incapable device, which also requires negotiation.

Source tracing capability negotiation depends on OSPFv3 neighbor relationships. Specifically, after an OSPFv3 neighbor relationship is established, the local device initiates source tracing capability negotiation. [Figure 1](#EN-US_CONCEPT_0000001176662801__fig_dc_vrp_ospf_feature_202301) shows the negotiation process.

**Figure 1** Source tracing capability negotiation  
![](figure/en-us_image_0000001130623384.png)

**Table 1** Source tracing capability negotiation
| Whether Source Tracing Is Supported | Source Tracing Capability Negotiation Process |
| --- | --- |
| DeviceA and DeviceB both support source tracing. | 1. DeviceA sends a PS-Hello packet to notify its source tracing capability. 2. Upon reception of the PS-Hello packet, DeviceB sets the source tracing field for DeviceA and replies with an ACK packet to notify its source tracing capability to DeviceA. 3. Upon reception of the ACK packet, DeviceA sets the source tracing field for DeviceB, and does not retransmit the PS-Hello packet. |
| DeviceA supports source tracing, but DeviceB does not. | 1. DeviceA sends a PS-Hello packet to notify its source tracing capability. 2. DeviceA fails to receive an ACK packet from DeviceB within 10s and retransmits the PS-Hello packet. A maximum of two retransmissions are allowed. After DeviceA fails to receive an ACK packet from DeviceB after two retransmissions, DeviceA considers that DeviceB does not support source tracing. |
| DeviceA and DeviceB both support source tracing, but source tracing is disabled from DeviceB. | 1. After source tracing is disabled from DeviceB, DeviceB sends a PS-Hello packet to notify its source tracing incapability to DeviceA. 2. Upon reception of the PS-Hello packet from DeviceB, DeviceA replies with an ACK packet that carries the source tracing capability. 3. Upon reception of the ACK packet from DeviceA, DeviceB considers the capability negotiation complete and disables the UDP port. |
| DeviceA does not support source tracing, and source tracing is disabled from DeviceB. | 1. After source tracing is disabled from DeviceB, DeviceB sends a PS-Hello packet to notify its source tracing incapability. 2. DeviceB fails to receive an ACK packet within 10s and retransmits the PS-Hello packet. A maximum of two retransmissions are allowed. After two retransmissions, DeviceB considers the capability negotiation complete and disables the UDP port. |



#### PS-LSA Generation and Flooding

PS-LSA: carries information about the node that flushed OSPFv3 LSAs.

* If a device flushes an LSA, it generates and floods a PS-LSA to source tracing-capable neighbors.
* If a device receives a flush LSA from a source tracing-incapable neighbor, the device generates and floods a PS-LSA to source tracing-capable neighbors. If a device receives the same flush LSA (with the same LSID and sequence number) from more than one source tracing-incapable neighbor, the device generates only one PS-LSA.
* If a device flushes a router-LSA, network-LSA, or inter-area-router-LSA, it generates a PS-LSA, adds the PS-LSA to a PS-LSU packet, and floods the PS-LSU packet to all source tracing-capable neighbors.

**Figure 2** PS-LSA generation rules  
![](figure/en-us_image_0000001176662931.png)

**PS-LSA generation rules**

* When DeviceA flushes a router-LSA, network-LSA, or inter-area-router-LSA, it generates a PS-LSA in which the **Flush Router** field is its router ID and the **Neighbor Router** field is 0, and adds the PS-LSA to the queue where packets are to be sent to all source tracing-capable neighbors.
* After DeviceA receives the flush LSA from source tracing-incapable DeviceB, DeviceA generates a PS-LSA in which the **Flush Router** field is its router ID and the **Neighbor Router** field is the router ID of DeviceB, and adds the PS-LSA to the queue where packets are to be sent to all source tracing-capable neighbors.
* After DeviceA receives the flush LSA from DeviceB, followed by the same flush LSA sent by DeviceC, DeviceA generates a PS-LSA in which the **Flush Router** field is its router ID and the **Neighbor Router** field is the router ID of DeviceB, and adds the PS-LSA to the queue where packets are to be sent to all source tracing-capable neighbors. No PS-LSA is generated in response to the flush LSA received from DeviceC.

**PS-LSU packet sending rules**

* During neighbor relationship establishment, a device initializes the sequence number of the PS-LSU packet of the neighbor. When the device replies with a PS-LSU packet, it adds the sequence number of the PS-LSU packet of the neighbor. During PS-LSU packet retransmission, the sequence number remains unchanged. After the device receives a PS-LSU ACK packet with the same sequence number, it increases the sequence number of the neighbor's PS-LSU packet by 1.
* The neighbor manages the PS-LSA sending queue. When a PS-LSA is added to the queue which was empty, the neighbor starts a timer. After the timer expires, the neighbor adds the PS-LSA to a PS-LSU packet, sends the packet to its neighbor, and starts another timer to wait for a PS-LSU ACK packet.
* After the PS-LSU ACK timer expires, the PS-LSU packet is retransmitted.
* When the device receives a PS-LSU ACK packet with a sequence number same as that in the neighbor record, the device clears PS-LSAs from the neighbor queue, and sends another PS-LSU packet after the timer expires.
  + If the sequence number of a received PS-LSU ACK packet is less than that in the neighbor record, the device ignores the packet.
  + If the sequence number of a received PS-LSU ACK packet is greater than that in the neighbor record, the device discards the packet.

![](../public_sys-resources/note_3.0-en-us.png) 

PS-LSU packet sending is independent among neighbors.

**PS-LSU packet receiving rules**

* When a device receives a PS-LSU packet from a neighbor, the neighbor records the sequence number of the packet and replies with a PS-LSU ACK packet.
* When the device receives a PS-LSU packet with the sequence number the same as that in the neighbor record, the device discards the PS-LSU packet.
* After the device parses a PS-LSU packet, it adds the PS-LSA in the packet to its LSDB. The device also checks whether the PS-LSA is newer than the corresponding PS-LSA in its LSDB.
  + If the received PS-LSA is newer, the device floods it to other neighbors.
  + If the received PS-LSA is the same as the corresponding local one, the device does not process the received PS-LSA.
  + If the received PS-LSA is older, the device floods the corresponding local one to the neighbor.
* If the device receives a PS-LSU packet from a neighbor and the neighbor does not support source tracing, the device modifies the neighbor status as source tracing capable.

#### Source Tracing Security

The source tracing protocol uses a UDP port to receive and send source tracing packets. Therefore, the security of the port must be taken into consideration.

The source tracing protocol inevitably increases packet receiving and sending workload and intensifies bandwidth pressure. To minimize its impact on other protocols, the number of source tracing packets must be controlled.

The following security measures are available:

**Table 2** Security Measures for Source Tracing
| Security Measures for Source Tracing | Fundamentals |
| --- | --- |
| Authentication | Source tracing is embedded in OSPFv3, inherits existing OSPFv3 configuration parameters, and uses OSPFv3 authentication parameters to authenticate packets. |
| GTSM | GTSM is a security mechanism that checks whether the time to live (TTL) value in each received IP packet header is within a pre-defined range. Source tracing packets can only be flooded as far as one hop. Therefore, GTSM can be used to check such packets by default.  * When a device sends a packet, it sets the TTL of the packet to 255. * If the TTL is not 254 when the packet is received, the packet will be discarded. |
| CPU-CAR | The device can check and control the packets to be sent to the CPU for processing, preventing the CPU from being overloaded by a large number of packets that are sent to the CPU. The source tracing protocol needs to apply for an independent CAR channel and has small CAR values configured. |



#### Typical Scenarios

**Scenario where all nodes support source tracing**

Assume that all nodes on the network support source tracing and DeviceA is the fault source. In this scenario, the fault source can be accurately located. [Figure 3](#EN-US_CONCEPT_0000001176662801__fig_dc_vrp_ospf_feature_202302) shows the networking.

**Figure 3** Scenario where all nodes support source tracing  
![](figure/en-us_image_0000001176742839.png)

When DeviceA flushes an OSPFv3 LSA, it generates a PS-LSA that carries DeviceA information and brief information about the flush LSA and floods the PS-LSA. After the fault occurs, maintenance personnel can log in to any node on the network to locate DeviceA, which keeps sending flush LSAs, and isolate DeviceA from the network.

**Scenario where source tracing-incapable nodes are not isolated from source tracing-capable nodes**

All nodes on the network except DeviceC support source tracing, and DeviceA is the fault source. In this case, the PS-LSA can be flooded on the entire network, and the fault source can be accurately located. [Figure 4](#EN-US_CONCEPT_0000001176662801__fig8882636306) shows the networking.

**Figure 4** Scenario where source tracing-incapable nodes are not isolated from source tracing-capable nodes  
![](figure/en-us_image_0000001130623392.png)

When DeviceA flushes an OSPFv3 LSA, it generates a PS-LSA that carries DeviceA information and brief information about the flush LSA and floods the PS-LSA. When DeviceB and DeviceE negotiate the source tracing capability with DeviceC, they find that DeviceC does not support source tracing. Therefore, after DeviceB receives the PS-LSA from DeviceA, DeviceB sends the PS-LSA to DeviceD, but not to DeviceC. Device A sends a flush LSA to Device B. When Device C sends the flush LSA to Device E, Device E finds that Device C does not support source tracing, helps Device C generate a PS-LSA that carries information about the advertisement source (Device E) and flush source (Device C), and flushed OSPFv3 LSA, and floods the PS-LSA on the entire network.

After the fault occurs, maintenance personnel can log in to any device on the network except DeviceC to locate the faulty node. Two possible faulty nodes can be located in this case: DeviceA and DeviceC, and they both send the same flush LSA. In this case, DeviceA takes precedence over DeviceC when the maintenance personnel determine the most possible faulty source. After DeviceA is isolated from the network, the network recovers.

**Scenario where source tracing-incapable nodes are isolated from source tracing-capable nodes**

All nodes on the network except DeviceC and DeviceD support source tracing, and DeviceA is the fault source. In this case, the PS-LSA cannot be flooded on the entire network. The fault source locating is complicated. [Figure 5](#EN-US_CONCEPT_0000001176662801__fig764319173016) shows the networking.

**Figure 5** Scenario where source tracing-incapable nodes are isolated from source tracing-capable nodes  
![](figure/en-us_image_0000001130623396.png)

When DeviceA flushes an OSPFv3 LSA, it generates a PS-LSA that carries DeviceA information and brief information about the flush LSA and floods the PS-LSA. However, the PS-LSA sent by DeviceA can reach only DeviceB because DeviceC and DeviceD do not support source tracing.

During source tracing capability negotiation, DeviceE finds that DeviceC does not support source tracing, and DeviceF finds that DeviceD does not support source tracing. After DeviceE receives the flush LSA from DeviceC, DeviceE generates and floods a PS-LSA on behalf of DeviceC. Similarly, after DeviceF receives the flush LSA from DeviceD, DeviceF generates and floods a PS-LSA on behalf of DeviceD.

After the fault occurs:

* If maintenance personnel log in to DeviceA or DeviceB, the personnel can locate the fault source (DeviceA) directly. After DeviceA is isolated, the network recovers.
* If the maintenance personnel log in to DeviceE, DeviceF, DeviceG, or DeviceH, the personnel will find that DeviceE claims DeviceC to be the fault source of the OSPFv3 flush LSA and DeviceF claims DeviceD to be the fault source of the OSPFv3 flush LSA.
* If the maintenance personnel log in to DeviceC and DeviceD, the personnel will find that the flush LSA was initiated by DeviceB, not generated by DeviceC or DeviceD.
* If the maintenance personnel log in to DeviceB, the personnel will find that DeviceA is the fault source, and isolate DeviceA. After DeviceA is isolated, the network recovers.