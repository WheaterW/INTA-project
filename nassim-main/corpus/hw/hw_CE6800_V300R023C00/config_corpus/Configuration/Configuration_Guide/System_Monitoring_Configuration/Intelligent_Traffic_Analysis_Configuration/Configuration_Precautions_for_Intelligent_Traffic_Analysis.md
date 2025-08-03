Configuration Precautions for Intelligent Traffic Analysis
==========================================================

Configuration Precautions for Intelligent Traffic Analysis

#### Licensing Requirements

Intelligent traffic analysis is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-LL-56F (low latency mode) |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| - After the packet truncation function is configured for mirrored packets, intelligent traffic analysis processes truncated packets. If the truncation length is set to a small value, the function may be abnormal. For common IPv4 packets, the truncated length must be no less than 64 bytes. For common IPv6 packets, the truncated length must be no less than 96 bytes. For VXLAN IPv4 packets, the truncated length must be no less than 128 bytes. For VXLAN IPv6 packets, the truncated length must be no less than 160 bytes.  - If the packet truncation function is not configured for mirrored packets, intelligent traffic analysis processes truncated packets. By default, 256 bytes are truncated.  - If the packet truncation function is not configured for mirrored packets and intelligent traffic analysis and mirroring are performed for IPv4 UDP flows in the outbound direction, 256 bytes may be truncated for mirrored packets. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| On the live network, link redundancy may exist in scenarios such as M-LAG, ECMP, or inter-board transmission. In these scenarios, bidirectional TCP flows are forwarded through different boards, and the device exports unidirectional flow entries. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| 1. Packets matching ACL rules configured in defense functions, such as filters or attack source tracing, are discarded, and these packets cannot be obtained for analysis.  2. Packets discarded by a traffic policy cannot be obtained for analysis.  3. When both intelligent traffic analysis and forwarded packet capture are configured, intelligent traffic analysis takes effect. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-LL-56F (low latency mode)  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Assume that a device functions as a VXLAN termination node, and intelligent traffic analysis for UDP flows is configured on the device to match only IP addresses. If VXLAN-encapsulated packets that meet the matching rule pass through the device, the device incorrectly matches the traffic and creates flow entries based on the inner packet information. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Intelligent traffic analysis does not support path changes caused by link switchover, dynamic load balancing, or per-packet load balancing when the related flow entries are still valid. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |