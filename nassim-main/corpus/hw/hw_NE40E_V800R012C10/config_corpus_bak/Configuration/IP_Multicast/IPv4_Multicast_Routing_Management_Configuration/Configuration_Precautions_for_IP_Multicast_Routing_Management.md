Configuration Precautions for IP Multicast Routing Management
=============================================================

Configuration_Precautions_for_IP_Multicast_Routing_Management

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| In a multicast scenario with equal-cost links or primary and secondary links, PIM is enabled only for the active link in use, but not enabled on the other links. After a link switchover occurs due to a configuration, route, or link change, multicast services will be interrupted, because PIM is not enabled on the newly selected link.  If multicast services are transmitted over the optimal route among unequal-cost links, PIM must also be enabled. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In CU separation scenarios, multicast-related commands can be delivered only from the CP to UPs and cannot be directly executed on UPs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The following types of outbound interfaces are supported by multicast RPF routes:  1. Common physical outbound interface.  2. Outbound interface of an LDP tunnel. The tunnel can be recursed to a physical outbound interface.  3. Outbound interface of the TE tunnel, which is the outbound interface of the IGP Shortcut route.  4. Outbound interface of the VXLAN tunnel. The VXLAN tunnel is used as the IPMSI tunnel of the NG MVPN.  If the outbound interface of the multicast RPF route is not one of the supported types, multicast traffic cannot be forwarded. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |