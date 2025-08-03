Overview of ARP
===============

Overview of ARP

#### Definition

The Address Resolution Protocol (ARP) resolves IP addresses to MAC addresses.


#### Purpose

If two hosts need to communicate, the sender must know the network-layer IP address of the receiver. IP datagrams, however, must be encapsulated with MAC addresses before they can be transmitted over the physical network. If the sender does not know the MAC address of the receiver, ARP is needed to map the receiver's IP address to the receiver's MAC address.


#### Benefits

ARP maps IP addresses at the network layer to MAC addresses at the data link layer on Ethernet networks to ensure communication between the data link and network layers.