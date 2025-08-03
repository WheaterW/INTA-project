Configuration Precautions for AnyFlow
=====================================

Configuration Precautions for AnyFlow

#### Licensing Requirements

AnyFlow is under license control (CE-LIC-AFV).


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
| The outbound interface recorded in a flow entry is the outbound interface in the first packet of the corresponding flow. The outbound interface will not be updated before the flow entry is aged out even if the outbound interface in packets of this flow changes. After the flow entry is aged out, the outbound interface will be updated in a new flow entry. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| When the resource mode is set to IPv4, a small number of IPv6 flow tables exist. When the resource mode is set to IPv6, a small number of IPv4 flow tables exist. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| To prevent packet statistics from being repeatedly sent to the analyzer, the device does not create AnyFlow entries for packets received from peer-link interfaces. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| When an ACL is used to filter packets based on RoCEv2 qpair information, if there are VXLAN packets with inner RoCEv2 packets and the VNI carried in the VXLAN packets is the same as the configured qpair information, the packets incorrectly match the ACL and flow entries are created. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| When a flow entry is created for packets forwarded at Layer 3, the flow entry does not contain VLAN information. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| When flow entries are created for VXLAN or RoCEv2 packets, the flow entries do not contain VLAN or VPN information. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| In a VXLAN scenario, the hardware flow table statistics contain only the inner IP address but not the VTEP IP address. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Users cannot delete specified flow entries from the hardware. The flow entries on the hardware can be deleted only through the aging mechanism of the hardware. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| After the IPv4 and IPv6 flow table specifications are adjusted, the device needs to be restarted for the adjustment to take effect. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |