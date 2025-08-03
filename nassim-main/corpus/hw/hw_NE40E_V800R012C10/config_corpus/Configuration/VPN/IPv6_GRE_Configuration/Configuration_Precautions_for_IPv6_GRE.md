Configuration Precautions for IPv6 GRE
======================================

Configuration Precautions for IPv6 GRE

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| IPv4 GRE carries IPv6 packets. If the length of a packet exceeds the interface MTU, the packet cannot be fragmented based on the MTU and will be discarded.  Preventive meansures:  1. Disable path MTU for the IPv4 GRE tunnel.  2. If the IPv4 GRE tunnel is enabled with the path MTU function and needs to carry IPv6 packets, check the IPv4 MTU configuration on the transit node of the IPv4 GRE tunnel to ensure that the IPv4 MTU is not less than 1312 bytes. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After packets entering an IPv6 GRE tunnel are encapsulated, if the packet length exceeds the interface MTU, the packets cannot be fragmented and are discarded.  Check the IPv6 MTU configuration on the transit node of the IPv6 GRE tunnel. Ensure that the IPv6 MTU is not less than 1332 bytes. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |