Configuration Precautions for IPv6 Basic
========================================

Configuration Precautions for IPv6 Basic

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| IPv6 does not support per-packet load balancing.  Per-flow load balancing is recommended. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the VLANIF interface status is not Down and the outbound interface for Layer 3 forwarding is switched between VLAN member interfaces, the packet loss time depends on the ND entry update or aging time. Therefore, this scenario is not recommended. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If YANG or MIB is used to query IPv6 statistics, IPv6 statistics can be queried only after IPv6 is enabled on an interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |