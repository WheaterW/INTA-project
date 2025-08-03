Configuration Precautions for IPv6 over IPv4 Tunnel
===================================================

Configuration_Precautions_for_IPv6_over_IPv4_Tunnel

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The interface, source address, and destination address of an IPv6 over IPv4 tunnel do not support L3VPN. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| IPv4 routes used by IPv6 over IPv4 tunnels and 6to4 tunnels can be used only for IP forwarding. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The 6to4, 6over4, and 6rd tunnels with the same source address cannot be controlled separately. If one of them is configured, the other two types of tunnels can forward packets normally. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After the source IP address of the 6to4 tunnel is changed, traffic from the original 6to4 address can still be forwarded. After smoothing, traffic is interrupted. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |