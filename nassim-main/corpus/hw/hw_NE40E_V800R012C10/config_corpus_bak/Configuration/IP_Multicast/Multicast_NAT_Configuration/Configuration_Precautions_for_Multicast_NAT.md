Configuration Precautions for Multicast NAT
===========================================

Configuration_Precautions_for_Multicast_NAT

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| In multicast NAT and 2022-7 switching scenarios, NTP clock synchronization is not supported, and only PTP clock synchronization is supported. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In the group flow switching scenario, when the group contains 2022-6 flows for clean switching, the clean switching effect is not ensured. That is, no interlacing, artifact, or packet loss occurs in the intermediate process. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If the outbound interface of a multicast NAT leaf node is deployed on a non-enhanced TM board or a non-enhanced TM subcard and downstream TM replication is configured on the board, the channelized rate limit function of multicast NAT cannot be ensured. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Multicast NAT does not support port extension. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K-B |
| IGMP interconnection of multicast NAT does not support the active/standby switchover of the control board.  In the active/standby switchover scenario, the tool on the NMS side cannot passively detect the active/standby switchover operation on the host side. As a result, the connection is interrupted, affecting the sending and receiving of IGMP packets. The tool on the OSS side needs to periodically query the connection status and reconnect to the NE. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Multicast NAT and trunk member binding are mutually exclusive. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Multicast NAT and portswitch on Layer 2 interfaces are mutually exclusive. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the multicast NAT 2022-7 feature is used for switchover, the delay difference between the incoming stream and outgoing stream cannot exceed 1/4 of the frame length. Otherwise, the switchover effect cannot be ensured. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the multicast NAT 2022-7 feature is used for switchover, the frame rates and sampling rates of the incoming and outgoing streams must be the same. Otherwise, the switchover effect cannot be ensured. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In the SMPTE 2022-7 seamless protection switching scenario, the class-A receiver constraint specified in SMPTE 2022-7 must be met (that is, the delay difference between the active and standby paths must be less than 10 ms). Otherwise, the switching effect cannot be ensured. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In multicast NAT 2022-7 switching scenarios, when the CPU usage is high, the switching point calculation and switching behavior processing are affected. As a result, the net switching effect and response time of multicast NAT cannot be ensured. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |