Configuring Defense Against DHCP Exhaustion Attacks
===================================================

This section describes how to prevent the attackers from attacking the Dynamic Host Configuration Protocol (DHCP) server by forging the DHCP packets for extending IP address leases.

#### Applicable Environment

Attackers disguise as authorized clients to send DHCP request packets for extending the IP address lease. As a result, DHCP servers cannot reclaim IP addresses assigned to clients.

This problem can be resolved by enabling DHCP snooping. After DHCP snooping is enabled, when receiving a DHCP request packet, the device checks whether the IP address and VLAN ID carried in the packet match an entry in the DHCP snooping binding table. If no matching entry exists, the device considers the DHCP request packet as a new request packet and forwards it. If a matching entry exists, the device considers the DHCP request packet as a lease renewal packet and checks whether the MAC address carried in the packet matches any entry in the binding table. If a matching entry exists, the device forwards the packet. If no matching entry exists, the device discards the packet.


#### Pre-configuration Tasks

Before you configure defense against attacks by sending bogus DHCP packets to extend IP address leases, configure the DHCP server.


[Enabling DHCP Snooping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0036_01_1.html)

Before configuring DHCP snooping, you must enable it.

[Enabling DHCP Request Packet Check](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0015_1.html)

To prevent unauthorized clients from sending Dynamic Host Configuration Protocol (DHCP) request packets to request IP addresses, the device checks whether information carried in a received DHCP request packet matches an entry in the DHCP snooping binding table. The checked information includes the source IP and MAC addresses. If a matching entry exists, the device considers the packet valid and forwards it. If no matching entry exists, the device considers the packet an attack packet and discards it.

[(Optional) Configuring Option 82 Field Insertion](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0016_1_2.html)

After Option 82 field insertion is enabled on a device, the device can record the location information of a DHCP client or create binding entries with accurate interface information based on the Option 82 information.

[(Optional) Configuring the Alarm Function forDiscarded DHCP Packets for Extending the IP Address Lease](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0018_1.html)

By configuring the function described in this chapter, you can have an alarm generated when a specified number of Dynamic Host Configuration Protocol (DHCP) packets for extending the IP address lease are discarded.

[Checking the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0019_1.html)

This section describes how to check the configuration of defense against the attacker from sending bogus Dynamic Host Configuration Protocol (DHCP) packets for extending the IP address leases.