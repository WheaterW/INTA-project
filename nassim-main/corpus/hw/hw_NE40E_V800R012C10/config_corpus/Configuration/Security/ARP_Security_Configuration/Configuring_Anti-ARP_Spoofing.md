Configuring Anti-ARP Spoofing
=============================

You can configure ARP packet filtering, validity check of ARP packets, and check the Destination IP Addresses of ARP Packets. These anti-ARP spoofing mechanisms improve network security and stability.

#### Usage Scenario

Attackers send fake ARP packets to modify ARP entries on gateways or valid hosts. As a result, valid ARP packets cannot be transmitted. To protect against ARP spoofing attacks, configure the following anti-ARP spoofing functions.


#### Pre-configuration Tasks

Before configuring anti-ARP spoofing, complete the following tasks:

* Configure the physical parameters for the interface and ensure that the physical layer status of the interface is Up.
* Configure the link layer parameters for the interface and ensure that the link layer protocol status of the interface is Up.


[Validity Check of ARP Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0006.html)

After validity check of Address Resolution Protocol (ARP) packets is enabled, when receiving an ARP packet, the device checks whether the source and destination MAC addresses in the Ethernet header match those in the Data field of the packet.

[Filtering ARP Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_arpsec_cfg_5013.html)

This section describes how to filter out ARP packets, including invalid ARP packets, gratuitous ARP packets, and ARP packets with non-null destination MAC addresses.

[Checking the Destination IP Addresses of ARP Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_arpsec_cfg_5014.html)

This section describes how to check the destination addresses of ARP packets, therefore discarding packets with incorrect destination addresses and enhancing CPU protection.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0008.html)

This section describes how to verify the configuration of anti-ARP spoofing.