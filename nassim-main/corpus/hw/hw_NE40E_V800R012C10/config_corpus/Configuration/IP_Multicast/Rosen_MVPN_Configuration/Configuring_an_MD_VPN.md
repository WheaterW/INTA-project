Configuring an MD VPN
=====================

A router uses multicast domain (MD) to implement multicast VPN in Any-Source Multicast (ASM) mode, and in this situation multicast data of private networks can be transmitted over public networks.

#### Usage Scenario

MD VPN only supports IP multicast in ASM mode on the public network. PIM tunnels are set up on the public network to transmit multicast data between sites in a VPN.

Before transmitting multicast data in a VPN, ensure that this VPN functions properly. To allow a PE to receive data from multiple VPNs, configure a public network instance and multiple VPN instances on the PE. The public network instance is responsible for the communication with the P, and the VPN instances are responsible for the communication with their connected Customer Edges (CEs).

A share-MDT needs to be set up to forward multicast packets in an MD VPN. Or, a special switch-multicast distribution tree (MDT) can be set up to switch multicast data of private networks flowing to the public network from the share-MDT to the switch-MDT for transmission. Multicast data can therefore be transmitted on demand, and the pressure on Provider Edges (PEs) is reduced.


#### Pre-configuration Tasks

Before configuring an MD VPN, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* Configure BGP/MPLS VPN.
* Configure multicast on the public network.


[(Optional) Enabling IP Multicast VPN](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mcast_cfg_2001.html)

Specifying a board for centralized multicast VPN service processing is a prerequisite for implementing centralized multicast VPN.

[Enabling IP Multicast Routing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2123.html)

Enabling IP multicast routing for the public network instance and VPN instance is the first step in configuring multicast VPNs.

[Configuring a Share-Group and Binding it to an MTI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2124.html)

After configuring an IPv4 multicast VPN, configure a Share-Group address and a multicast tunnel interface (MTI) to be bound to the VPN instance.

[Configuring an MTI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2125.html)



[(Optional) Configuring a Switch-MDT](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2126.html)

A switch-multicast distribution tree (MDT) is set up for multicast traffic flowing from a private network to the public network. Multicast packets can be switched from the share-MDT to the switch-MDT. This reduces the pressure on PEs and bandwidth consumption and allows multicast data to be transmitted on demand.

[Verifying the MD VPN Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2127.html)

After configuring a multicast domain (MD) VPN, verify the Share-Group and multicast tunnel interface (MTI) information about a specified VPN instance.