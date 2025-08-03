Enabling the Packet Check Function
==================================

To prevent IPv6/MAC spoofing attacks on a device, you can enable the packet check function on the device. Upon receipt of an IPv6 packet, the device checks whether the source IPv6 address and source MAC address of the IPv6 packet match an entry in the DHCPv6 snooping binding table.

#### Context

After DHCPv6 snooping is enabled, binding entries are automatically generated when DHCPv6 users go online. If DHCPv6 users are statically assigned IPv6 addresses, you need to manually configure static binding entries for the users.


#### Procedure

1. Run the **system-view** command to enter the system view.

1. Run the **interface** *interface-type* *interface-number* command to enter the interface view.
2. Run the [**dhcpv6 snooping check ipv6 enable**](cmdqueryname=dhcpv6+snooping+check+ipv6+enable) command to enable the IPv6 packet check function on the interface.
3. Run the **commit** command to commit the configuration.