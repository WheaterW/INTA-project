Configuration Precautions for IP FPM
====================================

Configuration_Precautions_for_IP_FPM

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| DCPs cannot be deployed on devices that function as PTP (1588v2) clock sources. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In the case of 1588v2 clock synchronization, the master clock source cannot lock the 1588v2 clock. Therefore, the master clock source cannot be used as a DCP. Otherwise, statistics collection is abnormal, and no IP FPM statistics are collected. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| IP FPM does not support GRE tunnel scenarios. In GRE tunnel scenarios, IP FPM statistics are inaccurate. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In an L2VPN scenario, private packets whose Layer 2 headers are not Ethernet headers are not supported and statistics cannot be collected.. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If a third-party device exists on measurement networks, only end-to-end IP FPM can be deployed and hop-by-hop IP FPM measurement results are not available. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In delay measurement, a statistical instance supports at most two InPoint nodes. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| During traffic switching in master/backup RSG scenarios, there is a low probability that the delay statistics collected within the first period are inaccurate. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| For the same VPN or in a native IP scenario, the flow characteristics (including the source IP address, destination IP address, source port, destination port, protocol number, and DSCP) of different measurement instances under the same DCP cannot conflict. For example, the characteristics of one measurement instance cannot include or overlap the characteristics of another. If the characteristics conflict, the measurement result is inaccurate. Please plan the flow granularity for measurement instances. Otherwise, packet loss statistics are inaccurate, and no delay measurement result is available. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| IP FPM multi-path detection:  1. In load balancing mode, the hwIpfpmDcpInstTlpIndexTable and hwIpfpmDcpInstTlpNHIndexTable MIB tables are used to deliver configurations.  2. In non-load balancing mode, the hwIpfpmDcpInstTlpTable and hwIpfpmDcpInstTlpNHTable MIB tables are used to deliver configurations.  Use the corresponding MIB table correctly. Otherwise, the configuration may fail to be delivered. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When configuring IP FPM for one-way delay measurement, you must configure 1588v2 for clock synchronization. Otherwise, the measurement result may be inaccurate. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Some IP FPM configurations cannot be deleted when the device does not have a license or the license trial period is not enabled. The configurations can be deleted only after the license is loaded. To delete all IP FPM configurations, run the undo nqa ipfpm dcp or undo nqa ipfpm mcp command. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |