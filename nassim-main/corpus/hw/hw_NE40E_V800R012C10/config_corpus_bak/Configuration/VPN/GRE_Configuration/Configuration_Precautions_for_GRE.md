Configuration Precautions for GRE
=================================

Configuration_Precautions_for_GRE

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Routes with GREv4 destination addresses cannot recurse to IPv6 or SRv6. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After the pathMTU function is enabled, the device cannot fragment or reassemble GRE keepalive detection packets. If the size of a Keepalive detection packet encapsulated in a GRE tunnel exceeds the MTU of the interface, the packet can be forwarded out of the device without being fragmented. If the device functioning as the destination end of the tunnel receives fragmented packets, the packet is incorrectly decapsulated and discarded. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the Keepalive function is enabled for a GRE tunnel, the tunnel interface may frequently alternate between up and down due to insufficient ACL resources. When configuring the Keepalive function, you are advised to configure flapping control to reduce the impact on device and network stability. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When multiple mGRE tunnels of DSVPN share the same source, they can share an IPsec policy only in share mode. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |