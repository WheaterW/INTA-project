(Optional) Configuring a Policy for Checking Invalid IPv6 Packets
=================================================================

When an IPv6/MAC spoofing attack occurs in a DHCPv6 scenario, you can configure the IPv6 packet check function to allow the device to check whether the source IPv6 address and source MAC address in an IPv6 packet match an entry in the DHCPv6 snooping binding table.

#### Context

The policy for checking IPv6 packets based on the DHCPv6 snooping binding table can be classified as a discard policy or forward policy.

* Discard policy: If no matching entry is found in the DHCPv6 snooping binding table based on the source IPv6 address, prefix, VLAN ID, and VPN information in an IPv6 packet, the IPv6 packet is discarded. If a matching entry is found in the DHCPv6 snooping binding table based on the source IPv6 address, prefix, VLAN ID, and VPN information in the IPv6 packet but the source MAC address and interface information in the IPv6 packet do not match this entry, the IPv6 packet is also discarded.
* Forward policy: If no matching entry is found in the DHCPv6 snooping binding table based on the source IPv6 address, prefix, VLAN ID, and VPN information in an IPv6 packet, the packet can be properly forwarded. If a matching entry is found in the DHCPv6 snooping binding table based on the source IPv6 address, prefix, VLAN ID, and VPN information in the IPv6 packet but the source MAC address and interface information in the IPv6 packet do not match this entry, the IPv6 packet is discarded.

#### Procedure

* Configure a policy for checking invalid IPv6 packets in the system view.
  1. Run the **system-view** command to enter the system view.
  2. Run the [**dhcpv6 snooping nomatch-packet ipv6 action**](cmdqueryname=dhcpv6+snooping+nomatch-packet+ipv6+action) **forward** command to configure a forward policy for checking IPv6 packets based on the DHCPv6 snooping binding table.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a policy for checking invalid IPv6 packets in the interface view.
  1. Run the **system-view** command to enter the system view.
  2. Run the **interface** *interface-type* *interface-number* command to enter the interface view.
  3. Run the [**dhcpv6 snooping nomatch-packet ipv6 action**](cmdqueryname=dhcpv6+snooping+nomatch-packet+ipv6+action) **forward** command to configure a forward policy for checking IPv6 packets based on the DHCPv6 snooping binding table on the interface.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.