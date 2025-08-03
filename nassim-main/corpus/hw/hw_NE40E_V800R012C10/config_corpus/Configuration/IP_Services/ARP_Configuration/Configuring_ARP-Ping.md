Configuring ARP-Ping
====================

ARP-Ping is classified as ARP-Ping IP or ARP-Ping MAC.

#### Usage Scenario

Before configuring an IP address for a device on a LAN, run the [**arp-ping ip**](cmdqueryname=arp-ping+ip) command to check whether the IP address to be configured is being used by another device on the network.

The [**ping**](cmdqueryname=ping) command can also be used to check whether this IP address is used by another device on the network. If the destination host and the Router that are enabled with the firewall function are configured not to reply to ping packets, the destination host and the Router do not reply to ping packets. This means that the ping always fails and the IP address mistakenly considered available. To resolve this problem, use the ARP-Ping IP feature. ARP packets are Layer 2 protocol messages and, in most cases, can pass through a firewall configured not to respond to ping messages.

When a device knows a specific MAC address on a network segment but does not know the corresponding IP address, the [**arp-ping mac**](cmdqueryname=arp-ping+mac) command can be run on the device to broadcast ICMP packets to obtain the corresponding IP address.


#### Pre-configuration Tasks

Before configuring ARP-Ping, configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is Up.


[Configuring ARP-Ping IP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2055.html)

ARP-Ping IP sends ARP packets onto a LAN to check whether an IP address is being used by another device on the LAN.

[Configuring ARP-Ping MAC](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2056.html)

ARP-Ping MAC sends ICMP packets onto a LAN to check whether a MAC address is used by another device on the LAN.