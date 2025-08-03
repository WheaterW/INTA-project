Configuration Precautions for IPv4 user-side multicast
======================================================

Configuration_Precautions_for_IPv4_user-side_multicast

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The following multicast scenarios are not supported in VE interface access scenarios:  1. Multicast shaping is not supported.  2. Multicast CAC is supported at the user level, not at the interface level.  3. VLAN-based multicast replication is not supported in a Layer 2 multicast QinQ scenario with VPLS.  4. IPv6 multicast is not supported.  In the preceding scenarios, the corresponding multicast function does not take effect. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| IGMP must be configured on main interfaces for VPN users. IGMP configurations on sub-interfaces do not take effect for VPN users. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Static multicast and dynamic multicast share multicast program and bandwidth resources. If the multicast program or bandwidth resource limit is reached, dynamic multicast is controlled. That is, static multicast users preempt the resources of dynamic multicast users. As a result, a user may fail to dynamically order a program after the user leaves the multicast group program and the applied resource is released. This is because the released resource may be occupied by a static multicast user. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Static multicast virtual scheduling supports only Layer 2 users, PPPoE users, and IPoE users, but does not support Layer 2 leased line users. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Static multicast supports RUI. Only replication by session and by vlan are supported. Other replication modes, if configured, do not take effect.  In RUI scenarios, run the "multicast copy by-session" or "multicast copy by-vlan" command in the BAS interface view. Other replication modes are not supported. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| User-side multicast on BAS interfaces supports Layer 2 common users, Layer 2 leased line users, and Layer 3 leased line users. Layer 3 common users and L2-VPN leased line users cannot join multicast groups. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| User-side multicast CAC does not take effect in the following scenarios:  1, Coexistence with dual-edge virtual scheduling of multicast traffic  2, IPv6 access  3, Logical interfaces, such as trunk interfaces  You are recommended tod deploy user-side multicast CAC in scenarios that support this feature. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| User-side multicast does not support global VE interfaces. The function does not take effect after being configured. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |