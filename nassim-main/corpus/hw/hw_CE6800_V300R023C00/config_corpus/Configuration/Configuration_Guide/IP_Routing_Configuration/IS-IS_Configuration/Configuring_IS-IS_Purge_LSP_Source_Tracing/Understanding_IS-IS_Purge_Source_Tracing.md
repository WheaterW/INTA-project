Understanding IS-IS Purge Source Tracing
========================================

Understanding IS-IS Purge Source Tracing

#### Context

If network-wide IS-IS LSP deletion causes network instability, source tracing must be implemented as soon as possible to locate and isolate the fault source. However, IS-IS itself does not support source tracing. A conventional solution is to isolate nodes one by one until the fault source is located, but the process is complex and time-consuming and may compromise network services. To address this problem, enable IS-IS purge source tracing.

IS-IS purge source tracing is a Huawei proprietary protocol.


#### Related Concepts

PS-PDU: packets that carry information about the node that floods IS-IS purge LSPs.

CAP-PDU: packets used to negotiate the IS-IS purge source tracing capability between IS-IS neighbors.

IS-IS purge source tracing port: UDP port number used to send and receive IS-IS purge source tracing packets. This UDP port number is configurable.


#### Fundamentals

IS-IS purge LSPs do not carry source information. If a device fails on the network, a large number of purge LSPs are flooded. Without a source tracing mechanism, nodes need to be isolated one by one until the faulty node is located, which is labor-intensive and time-consuming. IS-IS purge LSPs will trigger route flapping on the network, or even routes become unavailable. In this case, the device that flooded the purge LSPs needs to be located and isolated immediately.

A solution that can meet the following requirements is required:

1. Information about the source that flooded the purge LSPs can be obtained when network routes are unreachable.

2. The method used to obtain source information must apply to all devices on the network and support incremental deployment, without compromising routing capabilities.

For requirement 1, IS-IS purge source tracing uses UDP to send and receive source tracing packets. These packets carry IS-IS LSP information purged by the faulty device and are flooded hop by hop along the IS-IS neighbor topology. After IS-IS purge source tracing packets are flooded, you can log in to any device that supports IS-IS purge source tracing to view information about the device that flooded the purge LSPs. This helps to speed up fault locating.

For requirement 2, IS-IS purge source tracing forwards packets along UDP channels that are independent of the channels used to transmit IS-IS packets. In addition, source tracing does not affect the devices with the related UDP port disabled.


#### Capability Negotiation

Source tracing packets are transmitted over UDP. Devices listen for the UDP port and use it to send and receive source tracing packets. If a source tracing-capable device sends source tracing packets to a device that is source tracing-incapable, the former may be incorrectly identified as an attacker. Therefore, the source tracing capability needs to be negotiated between devices so that source tracing packets are exchanged between only source tracing-capable devices. In addition, source tracing capability negotiation is also required to enable a source tracing-capable device to send source tracing information on behalf of a source tracing-incapable device.

Source tracing capability negotiation depends on IS-IS neighbor relationships. Specifically, after an IS-IS neighbor relationship is established, the local device initiates source tracing capability negotiation based on the IP address of the neighbor.


#### PS-PDU Generation

If a fault source purges an LSP, it generates and floods a PS-PDU to all its source tracing neighbors.

If a device receives a purge LSP from a source tracing-incapable neighbor, the device generates and floods a PS-PDU to all its neighbors. If a device receives the same purge LSP (with the same LSP ID and sequence number) from more than one source tracing-incapable neighbor, the device generates only one PS-PDU.

PS-PDU flooding is similar to IS-IS LSP flooding.


#### Security Concern

A UDP port is used to send and receive source tracing packets. Therefore, the security of the port must be taken into consideration.

The source tracing protocol inevitably increases packet receiving and sending workload and intensifies bandwidth pressure. To minimize its impact on other protocols, the number of source tracing packets must be controlled.

**Authentication**: Source tracing is embedded in the IGP, inherits existing configuration parameters of the IGP, and uses authentication parameters of the IGP to authenticate packets.

**Generalized TTL security mechanism (GTSM)**: GTSM is a security mechanism that checks whether the time to live (TTL) value in each received IP packet header is within a pre-defined range.

Source tracing packets can only be flooded as far as one hop. Therefore, GTSM can be used to check such packets by default. When a device sends a packet, it sets the TTL of the packet to 255. If the TTL is not 254 when the packet is received, the packet will be discarded.

**CPU-CAR**: The NP module on a device can check and control the packets to be sent to the CPU for processing, preventing the CPU from being overloaded by a large number of packets that are sent to the CPU.

The source tracing protocol needs to apply for an independent CAR channel and has small CAR values configured.


#### Typical Scenarios

**Scenario where all nodes support source tracing**

Assume that all nodes on the network support source tracing and DeviceA is the fault source. In this scenario, the fault source can be accurately located. [Figure 1](#EN-US_CONCEPT_0000001176743797__fig_dc_vrp_isis_feature_003902) shows the networking.

**Figure 1** Scenario where all nodes support source tracing  
![](figure/en-us_image_0000001176743837.png)

When DeviceA purges an IGP packet, it floods a source tracing packet that carries DeviceA information and brief information about the IGP packet. Then the source tracing packet is flooded on the network hop by hop. After the fault occurs, maintenance personnel can log in to any node on the network to locate DeviceA, which keeps sending purge LSPs, and isolate DeviceA from the network.

**Scenario where source tracing-incapable nodes are not isolated from source tracing-capable nodes**

Assume that all devices except DeviceC support source tracing and DeviceA is the fault source. In this scenario, PS-PDUs can be flooded on the entire network, and the fault source can be accurately located. [Figure 2](#EN-US_CONCEPT_0000001176743797__fig_dc_vrp_ospf_feature_003903) shows the networking.

**Figure 2** Scenario where source tracing-incapable nodes are not isolated from source tracing-capable nodes  
![](figure/en-us_image_0000001130784178.png)

When DeviceA purges an LSP, it generates a PS-PDU that carries its information and the purged LSP and sends the purge LSP and PS-PDU to DeviceB. When DeviceB and DeviceE negotiate the source tracing capability with DeviceC, they find that DeviceC does not support source tracing. After DeviceB receives the PS-PDU from DeviceA, DeviceB sends the packet to DeviceD, but not to DeviceC. After receiving the purge LSP from DeviceC, DeviceE finds that DeviceC does not support source tracing and then generates a PS-PDU which carries information about the advertisement source (DeviceE), purge source (DeviceC), and the purged LSP, and floods the PS-PDU on the network.

After the fault occurs, maintenance personnel can log in to any node on the network except DeviceC to locate the faulty node. Two possible faulty nodes can be located in this case: DeviceA and DeviceC, and they both sends the same purge LSP. In this case, DeviceA takes precedence over DeviceC when the maintenance personnel determine the most probable fault source. After DeviceA is isolated, the network recovers, ruling out the possibility that DeviceC is the fault source.

**Scenario where source tracing-incapable nodes are isolated from source tracing-capable nodes**

Assume that all devices except DeviceC and DeviceD support source tracing and DeviceA is the fault source. In this scenario, PS-PDUs cannot be flooded on the entire network. The fault source locating is complicated. [Figure 3](#EN-US_CONCEPT_0000001176743797__fig_dc_vrp_ospf_feature_003904) shows the networking.

**Figure 3** Scenario where source tracing-incapable nodes are isolated from source tracing-capable nodes  
![](figure/en-us_image_0000001176663925.png)

When DeviceA purges an LSP, it generates a PS-PDU that carries its information and the purged LSP and sends the purge LSP and PS-PDU to DeviceB. However, the PS-PDU can only reach DeviceB because DeviceC and DeviceD do not support IS-IS purge source tracing.

During source tracing capability negotiation, DeviceE and DeviceF find that DeviceC and DeviceD do not support source tracing, respectively. After receiving the purge LSP from DeviceC, DeviceE generates and floods a PS-PDU on behalf of DeviceC. Similarly, after receiving the purge LSP from DeviceD, DeviceF generates and floods a PS-PDU on behalf of DeviceD.

After the fault occurs, maintenance personnel can locate the fault source (DeviceA) directly if they log in to DeviceA or DeviceB. After DeviceA is isolated, the network recovers. However, if the personnel log in to DeviceE, DeviceF, DeviceG, or DeviceH, they will find that DeviceE claims DeviceC to be the fault source and DeviceF claims DeviceD to be the fault source. If the personnel then log in to DeviceC or DeviceD, they will find that the purge LSP was sent by DeviceB, and was not generated by DeviceC or DeviceD. If the personnel then log in to DeviceB, they will determine that DeviceA is the fault source. After DeviceA is isolated, the network recovers.