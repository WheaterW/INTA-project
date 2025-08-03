Defense Against Invalid IPv6 Packets
====================================

Defense Against Invalid IPv6 Packets

#### Security Policy

If a device does not find the DHCPv6 snooping binding table based on the source IPv6 address, prefix, VLAN ID, and VPN information in a received IPv6 packet, it directly discards the packet. If a device finds the DHCPv6 snooping binding table based on the source IPv6 address, prefix, VLAN ID, and VPN information in a received IPv6 packet, and the source MAC address and interface information in the packet match those in the table, the packet is forwarded normally. Otherwise, the packet is considered as an attack one and is discarded.


#### Attack Methods

An attacker sends a large number of IPv6 packets carrying invalid source MAC addresses and interface information to attack a DHCPv6 server.


#### Configuration and Maintenance Methods

Enable the invalid IPv6 packet check function on an interface.

```
<HUAWEI> system-view
[~HUAWEI] interface gigabitethernet0/1/0
[~HUAWEI-Gigabitethernet0/1/0] dhcpv6 snooping check ipv6 enable
[*HUAWEI-Gigabitethernet0/1/0] commit
```

#### Configuration and Maintenance Suggestions

Note that configuring this function affects user access.