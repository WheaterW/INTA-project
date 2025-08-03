Configuration Precautions for Tunnel Management
===============================================

Configuration Precautions for Tunnel Management

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| To apply a tunnel policy to a service, you need to configure the tunnel policy and then apply it to the service. A nonexistent tunnel policy cannot be applied to a service. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When configuring a tunnel policy in tunnel binding mode to select a specified TE tunnel, you need to run the mpls te reserved-for-binding command in the view of the specified TE tunnel interface.  When the tunnel select-seq tunnel policy is configured to select TE tunnels based on types, the mpls te reserved-for-binding command cannot be run on the TE tunnel interface.  According to service deployment, the tunnel binding mode must be used together with the mpls te reserved-for-binding command on the TE interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If select-seq srpolicy is specified and select-seq is also configured for other types of tunnels when a tunnel policy is configured, the unmix option must be configured. That is, hybrid load balancing between SR-MPLS TE Policies and other types of tunnels is not allowed. If the configured tunnel policy cannot recurse routes to an SR-MPLS TE Policy (for example, due to color mismatch), other types of tunnels (such as TE and LDP tunnels) cannot be used together for load balancing. However, load balancing can performed based on the load-balance-number configuration among tunnels of the same type. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |