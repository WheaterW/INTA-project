Preventing DoS Attacks by Changing the CHADDRField
==================================================

This section describes how to prevent attackers from attacking the Dynamic Host Configuration Protocol (DHCP) server by modifying the client hardware address (CHADDR) field.

#### Usage Scenario

Attackers may change the CHADDR field carried in DHCP packets to apply for IP addresses continuously. The device, however, only checks validity of packets based on the source media access control (MAC) address in the frame header. Attack packets can still be forwarded and the MAC address limit cannot take effect.

To prevent the attacker from changing the CHADDR field, configure DHCP snooping to check the CHADDR field carried in DHCP request packets. If the CHADDR field matches the source MAC address in the frame header, the packet is forwarded. Otherwise, the packet is discarded.


#### Pre-configuration Tasks

Before configuring defense against DoS attacks by changing the CHADDR field, configure DHCP snooping.


[Enabling DHCP Snooping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0036_1.html)

Before configuring DHCP snooping, you must enable it.

[Configuring CHADDR Field Check](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0011_1.html)

If you want your device to check the client hardware address (CHADDR) field validity, configure CHADDR field check.

[(Optional) Configuring the Alarm Function forDiscarded DHCP Packets with Incorrect CHADDR Fields](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0012_1.html)

By configuring the function described in this chapter, you can have an alarm generated when a specified number of Dynamic Host Configuration Protocol (DHCP) packets with incorrect client hardware address (CHADDR) fields are discarded.

[Checking the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0013_1.html)

This section describes how to check the configuration of the client hardware address (CHADDR) field check function.