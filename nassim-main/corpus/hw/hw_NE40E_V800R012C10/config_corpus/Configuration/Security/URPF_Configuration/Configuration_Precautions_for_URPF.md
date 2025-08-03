Configuration Precautions for URPF
==================================

Configuration Precautions for URPF

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| In SRH-encapsulated packet scenarios, if flow-based URPF or interface-based URPF is configured for IPv6 packets with SRHs, strict URPF is degraded to loose URPF. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When strict URPF is configured on an interface, the source IP address of traffic exists in the routing table but does not match the traffic interface, and more than eight routes from the source IP address are used for load balancing, strict URPF is degraded to loose URPF. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After strict URPF is configured on an interface, Layer 3 loop detection does not take effect on the interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |