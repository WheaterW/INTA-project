Configuring Defense Against Bogus DHCP ServerAttacks
====================================================

To prevent bogus DHCP server attacks, configure DHCP snooping, which works in either trusted or untrusted mode.

#### Usage Scenario

A bogus DHCP server on the network may send a DHCP offer packet to the DHCP client. The DHCP offer packet contains incorrect information such as the incorrect gateway address, incorrect Domain Name Server (DNS) server, and incorrect IP address. As a result, the DHCP client cannot connect to the network or may connect to an incorrect network.

To prevent a bogus DHCP server attack, configure DHCP snooping on the device, configure the network-side interface to be trusted and the user-side interface to be untrusted, and configure the device to discard DHCP reply packets received from untrusted interfaces.

In addition, you can configure bogus DHCP server detection to obtain DHCP server information by checking DHCP reply packets and record the information in logs. This helps network administrators maintain networks.


#### Pre-configuration Tasks

Before you configure defense against bogus DHCP server attacks, configure the DHCP server.


[Enabling DHCP Snooping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0005_1.html)

To configure Dynamic Host Configuration Protocol (DHCP) snooping functions, enable DHCP snooping first.

[Configuring an Interface as a Trusted Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0006_1.html)

After Dynamic Host Configuration Protocol (DHCP) snooping is enabled, trusted interfaces must be configured so that clients can go online through trusted interfaces.

[(Optional) Enabling Bogus DHCP Server Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0007_1.html)

After bogus Dynamic Host Configuration Protocol (DHCP) server detection is enabled, the system generates logs about DHCP servers.

[(Optional) Configuring the Alarm Function forDiscarded DHCP Reply Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0008_1.html)

If an alarm needs to be generated when a specified number of Dynamic Host Configuration Protocol (DHCP) reply packets are discarded, you can configure the alarm function for discarded DHCP reply packets.

[Checking the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0009_1.html)

This section describes how to check the configuration of defense against bogus Dynamic Host Configuration Protocol (DHCP) server attacks.