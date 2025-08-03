Enabling DHCPv6 Snooping
========================

Before configuring DHCPv6 snooping, you must enable DHCPv6 snooping.

#### Context

Enable DHCPv6 snooping in the following sequence:

1. Enable DHCPv6 snooping globally.
2. Enable DHCPv6 snooping on an interface.

#### Procedure

1. Run the **system-view** command to enter the system view.
2. Run the **dhcpv6 snooping enable** command to enable DHCPv6 snooping globally.
3. Run the **interface** *interface-type* *interface-number* command to enter the interface view.
4. Run the **dhcpv6 snooping enable** command to enable DHCPv6 snooping on the interface.