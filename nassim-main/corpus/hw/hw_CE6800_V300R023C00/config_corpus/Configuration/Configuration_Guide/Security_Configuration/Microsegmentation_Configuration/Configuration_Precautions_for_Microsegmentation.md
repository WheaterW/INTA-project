Configuration Precautions for Microsegmentation
===============================================

Configuration Precautions for Microsegmentation

#### Licensing Requirements

Microsegmentation is not under license control.


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
| \* For traffic that re-enters the tunnel on the termination device, microsegmentation enforces the policy.  \* When traffic enters a tunnel on a non-VXLAN termination device, microsegmentation does not enforce policies. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Microsegmentation conflicts with MQC-based VXLAN reserved field re-marking. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Microsegmentation conflicts with INOF and NPCC and cannot be configured together. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| When microsegmentation and MQC conflict, MQC takes effect preferentially. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| \* If the GBP classifier contains the Layer 4 port number field, the GBP classifier does not take effect on non-first TCP/UDP fragments. The default action is to allow non-first TCP/UDP fragments to pass through.  \* The default group behavior and default intra-group behavior do not take effect on non-initial fragmented packets. The default action is to allow non-initial fragmented packets to pass through.  \* The unknown packet policy takes effect on fragmented packets.  \* You are advised to adjust the network MTU to prevent packet fragmentation. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| \* In inter-VPN communication scenarios, the source VPN is used to query the destination EPG.  \* Add members of the destination IP address and source VPN to the destination EPG. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| \* For basic Layer 3 forwarding traffic, if the source and destination IP addresses match the group member rule, the traffic is counted.  \* If the inner source and destination IP addresses of VXLAN passerby packets match the group member rule, the packets are counted.  \* Microsegmentation grouping policies take effect only for packets forwarded at Layer 3 on the VXLAN overlay network. Microsegmentation policy statistics can be used to assist statistics collection. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| \* The destination group statistics do not include the traffic with unknown source groups.  \* The source group statistics include the traffic with unknown destination groups. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |