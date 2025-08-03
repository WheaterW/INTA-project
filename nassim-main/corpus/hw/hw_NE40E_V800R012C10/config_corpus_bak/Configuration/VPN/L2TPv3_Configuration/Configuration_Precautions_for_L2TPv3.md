Configuration Precautions for L2TPv3
====================================

Configuration_Precautions_for_L2TPv3

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Restrictions on L2TPv3:  1. Only static tunnels can be configured, and dynamic negotiation for tunnel establishment or teardown is not required .  You are advised to properly plan IPv6 addresses and the source and destination IP addresses of the tunnel. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Restrictions on L2TPv3:  1. The path mtu command is not supported. If the packet length exceeds the MTU of the public network-side interface, the packet is discarded.  2. The L2TPv3 tunnel cannot carry the terminated user-side VLAN priority to the downstream device. The default IPv6 ToS value on the L2TPv3 tunnel is 0.  3. If an interface is bound to an L2TPv3 tunnel, no VLAN segment can be configured for the interface. Similarly, if a VLAN segment is configured, the interface cannot be bound to an L2TPv3 tunnel.  4. An interface configured with a BD cannot be configured with an L2TPv3 tunnel. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |