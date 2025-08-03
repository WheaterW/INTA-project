Configuring Defense Against Man-in-the-Middle Attacks and IP/MAC Address Spoofing
=================================================================================

This section describes how to configure the IP/MAC address
binding and Option 82 functions to prevent man-in-the-middle attacks
and IP/MAC address spoofing.

#### Applicable Environment

In man-in-the-middle
attacks and IP/MAC address spoofing, attackers pretend to be servers
and clients. The servers consider that all packets are sent from and
destined for the clients, and so do the clients. Actually these packets
are second-hand information from man-in-the-middle, and in this manner
attackers can obtain the data on the servers and clients.

To
prevent man-in-the-middle attacks and IP/MAC address spoofing, enable
the Dynamic Host Configuration Protocol (DHCP) snooping function on
a device so that the device forwards a packet only if the packet info
matches an entry in the DHCP snooping binding table. If a packet does
not match any entry in the DHCP snooping binding table, the device
discards the packet.


#### Pre-configuration Tasks

Before you configure
defense against man-in-the-middle attacks and IP/MAC address spoofing,
configure DHCP snooping.


[Enabling DHCP Snooping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0036_3.html)

Before configuring DHCP snooping, you must enable it.

[Enabling DHCP Request Packet Check](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0042.html)

To prevent man-in-the-middle attacks and IP/MAC address spoofing, enable Dynamic Host Configuration Protocol (DHCP) request packet check. After packet check is enabled on a device, the device checks the received Address Resolution Protocol (ARP) or IP packets to see whether the combination of source IP addresses and source MAC addresses in the packets match entries in the DHCP snooping binding table.

[(Optional) Configuring the DHCP Snooping Binding Table](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0040.html)

Dynamic entries in the DHCP snooping binding table are automatically generated when DHCP snooping is enabled. Static entries in the DHCP snooping binding table must be manually configured.

[(Optional) Configuring Option 82 Field Insertion](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0016_1.html)

After Option 82 field insertion is enabled on a device, the device can record the location information of a DHCP client or create binding entries with accurate interface information based on the Option 82 information.

[(Optional) Configuring the Alarm Function for Discarded Man-in-the-Middle Attack and IP/MAC Address Spoofing Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0045.html)

By configuring the function described in this chapter, you can have an alarm generated when a specified number of man-in-the-middle attack and IP/MAC address spoofing packets are discarded.

[Verifying the Configuration of Defense Against Man-in-the-Middle Attacks and IP/MAC Address Spoofing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0043.html)

This section describes how to check the configuration of defense against man-in-the-middle attacks and IP/MAC address spoofing.