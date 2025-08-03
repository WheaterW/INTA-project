Configuration Precautions for DHCPv6 Snooping
=============================================

Configuration_Precautions_for_DHCPv6_Snooping

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| DHCPv6 snooping is implemented only for static users (users configured in the static binding table) on EVC sub-interfaces. All DHCPv6 protocol packets on EVC sub-interfaces enabled with DHCPv6 snooping are discarded, and DHCPv6 users cannot go online. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After DHCPv6 snooping is enabled on an EVC sub-interface, it cannot work with the DHCPv6 relay or server function on its VBDIF interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Avoid address overlapping between the new DHCPv6 snooping binding table and the existing DHCPv6 snooping binding table. If an IPv6 data packet matches two or more binding entries with overlapping IPv6 addresses on different interfaces, the final forwarding behavior of the packet may not meet the expectation. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| DHCPv6 snooping takes effect only in level-1 DHCPv6 relay scenarios (including LDRA interconnection scenarios) and does not take effect in multi-level DHCPv6 relay scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| DHCPv6 snooping supports attack defense only for IPv6 data packets on the forwarding plane, but not for protocol packets. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| DHCPv6 snooping supports only single-homing scenarios and does not support hot backup of binding entries between the master and backup devices in dual-homing scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| DHCPv6 snooping must be used together with DHCPv6 relay on a Layer 3 interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |