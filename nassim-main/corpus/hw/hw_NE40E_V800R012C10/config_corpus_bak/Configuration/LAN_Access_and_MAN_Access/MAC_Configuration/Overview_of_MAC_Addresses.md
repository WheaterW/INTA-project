Overview of MAC Addresses
=========================

This section briefly describes the basic concept of a MAC address table, modes for generating MAC address entries, MAC address entry classification, and MAC address-based packet forwarding.

#### Basic Concept of a MAC Address Table

Each device maintains a MAC address table. A MAC address table stores MAC addresses, VLAN IDs, and outbound interfaces learned from other devices, listed in [Table 1](#EN-US_CONCEPT_0172362688__tab_dc_vrp_mac_cfg_000101). To forward data, the device searches the MAC address table to quickly locate the outbound interface based on the destination MAC address and VLAN ID in the data frame. This implementation reduces broadcast traffic.

**Table 1** MAC address entries
| MAC Address | VLAN ID | Outbound Interface |
| --- | --- | --- |
| 00e0-fc12-3458 | 10 | GE 0/3/1 |
| 00e0-fc12-3456 | 20 | GE 0/2/4 |
| 00e0-fc12-3457 | 30 | Eth-Trunk 20 |


If a destination host is added to multiple VLANs, one MAC address corresponds to multiple VLAN IDs in the MAC forwarding entries.


#### Modes for Generating MAC Address Entries

* Automatic generation
  
  Usually, a device automatically generates a MAC address table by learning source MAC addresses. The MAC address table needs to be updated constantly to meet the requirements of network changes. The entries automatically generated are not always valid. If a MAC address entry is not updated before its aging time expires, the entry will be deleted. The aging time is called a lifecycle. If an entry is updated before its aging time expires, the aging time will be recalculated for the entry.
* Manual configuration
  
  When a device sets up a MAC address table automatically by learning source MAC addresses, the system cannot identify whether the packets are sent from authorized users or hackers, bringing security risks. If hackers disguise the source MAC addresses of attack packets as authorized MAC addresses and send the attack packets with the forged MAC addresses to the device through another interface, the device will learn incorrect MAC address entries. As a result, the packets that should be forwarded to authorized users are forwarded to hackers. To improve interface security, a network administrator can add specific MAC address entries to the MAC address table to bind related user terminals to interfaces. In this way, the device can stop unauthorized users from obtaining data. The configured MAC address entries take precedence over automatically generated entries.


#### Classification of MAC Address Entries

MAC address entries can be classified as dynamic, static, or blackhole MAC address entries.

* Static MAC address entry: configured by users. A packet with the destination MAC address matching a static MAC address entry is forwarded from the specified interface. Packet forwarding based on static MAC address entries prevents packets with forged MAC addresses from attacking the device. Static MAC address entries take precedence over dynamic MAC address entries.
* Dynamic MAC address entry: learned by an interface after source MAC address learning is enabled on the interface.
* Static blackhole MAC address entry: configured by users. To prevent invalid MAC address entries (unauthorized users, for example) from using the MAC address table space and prevent hackers from attacking a device or network using forged MAC addresses, configure MAC addresses of untrusted users as blackhole MAC addresses. A device discards packets destined for static blackhole MAC addresses. Blackhole MAC address entries take precedence over dynamic entries.
* Dynamic blackhole MAC address entry: created by a device by learning source MAC addresses. On an EVPN network, to prevent MAC address entries from frequently flapping, the MAC address entries can be set to dynamic blackhole entries, so that related interfaces are blocked, and loops are rapidly eliminated.


#### MAC Address-based Packet Forwarding

A device forwards packets in either of the following modes based on MAC address entries:

* Unicast mode: If the MAC address table contains an entry matching the destination MAC address of a packet, the device forwards the packet from the outbound interface in the entry.
* Broadcast mode: If a packet received by a device is a broadcast or multicast packet, or if the MAC address table of the device does not contain an entry matching the destination MAC address of the packet, the device broadcasts the packet through all interfaces except the interface that has received the packet.