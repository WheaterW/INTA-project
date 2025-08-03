Definition and Classification of MAC Address Entries
====================================================

Definition and Classification of MAC Address Entries

#### Definition of a MAC Address Table

A MAC address table records the mapping between interfaces, VLANs, and MAC addresses. Before forwarding a packet, a device looks up the destination MAC address of the packet in the MAC address table. If a MAC address entry matches the destination MAC address, the device forwards the packet to the outbound interface in the MAC address entry. If no MAC address entry matches the destination MAC address, the device broadcasts the packet to all interfaces in the corresponding VLAN, except the inbound interface receiving the packet.


#### Classification of MAC Address Entries

MAC address entries are classified into dynamic, static, and blackhole entries.

**Table 1** Characteristics and functions of different MAC address entries
| MAC Address Entry Type | Characteristics | Function |
| --- | --- | --- |
| Dynamic MAC address entry | Dynamic MAC address entries are obtained by learning source MAC addresses of packets received on an interface, and will age out.  Dynamic MAC address entries are lost after a system restart, card hot swap, or card reset. | You can check whether data is forwarded between two connected devices by checking dynamic MAC address entries.  You can obtain the number of users connected to an interface by checking the number of specified dynamic MAC address entries. |
| Static MAC address entry | Static MAC address entries are manually configured and delivered to each card. Static MAC address entries never age out.  The static MAC address entries saved in the system are not lost after a system restart, card hot swap, or card reset.  Each static MAC address entry can have only one outbound interface.  After an interface is statically bound to a MAC address, other interfaces discard packets originating from that MAC address.  Statically binding an interface to a MAC address does not affect the learning of dynamic MAC address entries on the interface. | When static MAC address entries are configured, authorized users can use network resources, and other users are prevented from using the bound MAC addresses. This can block certain attacks. |
| Blackhole MAC address entry | Blackhole MAC address entries are manually configured and delivered to each card. Blackhole MAC address entries never age out.  The blackhole MAC address entries saved in the system are not lost after a system restart, card hot swap, or card reset.  After blackhole MAC address entries are configured, the device discards packets originating from or destined for the blackhole MAC addresses. | Blackhole MAC address entries can filter out unauthorized users. |