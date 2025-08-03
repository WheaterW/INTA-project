Configuration Precautions for Timestamp-Refresh
===============================================

Configuration_Precautions_for_Timestamp-Refresh

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Only IPv4 RTP video traffic that complies with SMPTE ST 2022-20 is supported. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| The traffic policies bound to the same timestamp-refresh instance cannot be applied to multiple interfaces. Otherwise, packets are out of order or the timestamp-refresh offset value changes frequently after the timestamp is refreshed. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| During group stream forwarding, the timestamps of all streams in the group must be synchronized. Therefore, ensure that timestamp-refresh is configured for all streams in the group. If the timestamps in the group are different, the receiver cannot assemble the received packets. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| Timestamp-refresh does not support VLANIF or VBDIF. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| The timestamp-refresh function is mutually exclusive with the function of marking the class of service and color of packets matching the traffic policy based on the specified BFD session status. If both the timestamp-refresh and marking of the class of service and color of packets are configured in a level-2 ACL, the timestamp-refresh takes effect first, and the marking of the class of service and color does not take effect. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| In an emergency scenario, artifacts may occur continuously during the period between the time when one device delivers the timestamp-refresh command and the time when the other device delivers the timestamp-refresh command. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |