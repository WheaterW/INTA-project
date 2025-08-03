Configuration Precautions for NPCC
==================================

Configuration Precautions for NPCC

#### Licensing Requirements

NPCC is under license control (CE-LIC-NPCC).


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
| 1. NPCC and dynamic load balancing are mutually exclusive.  2. NPCC and iQCN are mutually exclusive.  3. In versions earlier than V300R022C00, NPCC does not support IPv6.  4. NPCC does not support VXLAN.  5. After NPCC is enabled on an interface, the RoCEv2 packets that pass through the queues that are not enabled with NPCC are also counted in the RoCEv2 flow table maintained by NPCC.  6. When traffic on an interface matches both MQC and NPCC functions, the MQC function takes effect preferentially.  7. When traffic on an interface matches both the packet capture and NPCC functions, the packet capture function takes effect preferentially.  8. When traffic matches both the iNOF zone isolation function and NPCC, the iNOF zone isolation function takes effect preferentially.  9. For a flow with the specified source IP address, destination IP address, and source QP, a maximum of 16 interfaces can proactively send CNPs at the same time.  10. NPCC does not support M-LAG.  11. For a flow with the specific source IP address, destination IP address, and source QP, after the flow is switched to another interface, the interface statistics in the flow table age in 3s to 6s.  For the CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P: | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |