Configuration Precautions for iQCN
==================================

Configuration Precautions for iQCN

#### Licensing Requirements

iQCN is under license control (CE-LIC-AFRD).


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
| 1. The iQCN function applies to downlink interfaces of leaf nodes in storage scenarios (many-to-one Incast traffic causes severe congestion). This function does not need to be configured on spine nodes.  2. The iQCN function can be enabled on downlink physical interfaces of devices. This function cannot be enabled on interfaces in a PFC uplink interface group and physical member interfaces of peer-link interfaces.  3. When the iQCN function is enabled globally, a maximum of two member interfaces can be configured for an M-LAG ID, and a maximum of two member interfaces can be added to an Eth-Trunk interface.  4. When the number of used iQCN flow entries is less than 1024, CNPs can be sent for compensation in a timely manner. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |