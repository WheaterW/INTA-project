Configuring IPv6/MAC Spoofing Attack Defense
============================================

This section describes how to configure the IPv6 packet check function, a static binding table, and a policy for detecting IPv6 packets to prevent IPv6/MAC spoofing attacks against a DHCPv6 server.

#### Usage Scenario

When an IPv6/MAC spoofing attack occurs on a network, the attacker forges a DHCPv6 client, and the DHCPv6 server incorrectly considers that all the packets are sent to or received from this client. However, these packets actually have been tampered with. In this way, the attacker can obtain data from the DHCPv6 server.

To prevent IPv6/MAC spoofing attacks, you can configure DHCPv6 snooping on a device. The device then forwards a packet only when the information in the packet matches an entry in the DHCPv6 snooping binding table. Otherwise, the device discards the packet.


#### Pre-configuration Tasks

Before configuring IPv6/MAC spoofing attack defense on a Layer 3 device, complete the following task:

* Configure DHCPv6 snooping.


[Enabling DHCPv6 Snooping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6-snooping_cfg_0036.html)

Before configuring DHCPv6 snooping, you must enable DHCPv6 snooping.

[Enabling the Packet Check Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6-snooping_cfg_0042.html)

To prevent IPv6/MAC spoofing attacks on a device, you can enable the packet check function on the device. Upon receipt of an IPv6 packet, the device checks whether the source IPv6 address and source MAC address of the IPv6 packet match an entry in the DHCPv6 snooping binding table.

[(Optional) Configuring a DHCPv6 Snooping Binding Table](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6-snooping_cfg_0040.html)

After DHCPv6 snooping is enabled, dynamic DHCPv6 snooping binding entries are automatically generated when users go online. Static DHCPv6 snooping binding entries need to be manually configured.

[(Optional) Configuring a Policy for Checking Invalid IPv6 Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6-snooping_cfg_0042_1.html)

When an IPv6/MAC spoofing attack occurs in a DHCPv6 scenario, you can configure the IPv6 packet check function to allow the device to check whether the source IPv6 address and source MAC address in an IPv6 packet match an entry in the DHCPv6 snooping binding table.

[(Optional) Configuring the Alarm Function for IPv6/MAC Spoofing Attacks](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6-snooping_cfg_0045.html)

This section describes how to configure the device to generate an alarm when the number of discarded IPv6/MAC spoofing attack packets reaches the specified threshold.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6-snooping_cfg_0043.html)

After configuring IPv6/MAC spoofing attack defense, you can view statistics about discarded IPv6 and DHCPv6 packets and the binding relationships between interface names, MAC addresses, and IPv6 addresses in the DHCPv6 snooping binding table.