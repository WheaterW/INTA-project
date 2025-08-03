Configuration Precautions for IOAM
==================================

Configuration Precautions for IOAM

#### Licensing Requirements

IOAM is under license control (CE-LIC-TLM).


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| For the CE6800 Series:  ACL specifications referenced by IOAM  For the CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P:  One IPv4 ACL and one IPv6 ACL can be referenced by IOAM and each ACL can deliver a maximum of 128 rules.  For the CE8800 Series:  ACL specifications referenced by IOAM  For the CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P:  One IPv4 ACL and one IPv6 ACL can be referenced by IOAM and each ACL can deliver a maximum of 128 rules. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| In terms of UDP packets, IOAM can be configured only for those encapsulated in VXLAN packets. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| If the first eight bytes in the payload following the TCP header are the same as the probermarker and the device is a transit or egress node, the first 64 bytes of the payload will be deleted. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| When IP packets enter a VXLAN tunnel, no checksum complement is calculated. This is because the UDP checksum of VXLAN packets is not calculated and is 0 in most cases. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| When IP packets enter a VXLAN tunnel and IOAM is configured for VXLAN packets, the flow is looped back and the required bandwidth doubles. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| If IP packets match both an ACL referenced by IOAM and an ACL referenced by MQC on an ingress node, the forwarding latency on the device doubles. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| The CAR for sending IOAM packets is 1000000 pps. If both IOAM trace/edge-to-edge decapsulation and VXLAN decapsulation are configured, packets are sent in both the upstream and downstream directions. That is, the maximum packet sending rate at each direction is half of the CAR. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| After decapsulating the IOAM-encapsulated VXLAN packets (in direct-export mode), the egress node sends the resulting packets without VXLAN header information to the built-in chip of the CPU. (In Trace/Edge-to-Edge mode, the packets can be reassembled through SCOP, so the packets sent to the built-in chip of the CPU carry VXLAN header information.) | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| If IOAM packets match the host route on the egress node, the IOAM packets are sent to the CPU without being decapsulated. Currently, the control plane cannot parse IOAM packets. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| IOAM and packet loss visualization cannot be configured at the same time. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| When VXLAN decapsulation is performed on the IOAM egress node, the copy-to-CPU service is performed if this service exists. As a result, IOAM information cannot be sent to the CPU. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| IOAM flows do not support services that need to match or parse the content following the Layer 4 header, which include VXLAN path detection and ACLs for matching inner information of VXLAN packets. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| - When both IOAM and VXLAN are configured, the IOAM egress node use the internal loopback interface to remove the IOAM and VXLAN headers from packets. IOAM-encapsulated packets that exceed the CAR value (5 Gbit/s) of the internal loopback interface will be discarded.  - When configuring IOAM, ensure that all the ingress, transit, and egress nodes are configured. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| The probermarker in the IOAM header cannot be modified using commands. If the first eight bytes in the payload of a non-IOAM packet are the same as the probermarker in the IOAM header, a mismatch occurs. This problem can only be resolved by installing a patch. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| An IOAM transit node cannot obtain information, such as the VNI and inner IP address, for hash-based port selection in load balancing scenarios or for ACL matching. By default, the device uses outer packet information for hash-based path selection. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| A maximum of eight hops can be configured. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Because content needs to be added to the packet header, ensure path MTU compatibility.  1. In hop-by-hop direct-export mode, only a 20-byte IOAM header is added to a packet.  2. If data is reported by a termination node:  (1) In trace mode, the packet length is increased by (8 + 12) + 32 x N bytes (N indicates the number of hops).  (2) In edge-to-edge mode, a transit node does not add its metadata to a packet, and only the ingress node adds 32 bytes (8 + 8 + 16) to the packet. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |