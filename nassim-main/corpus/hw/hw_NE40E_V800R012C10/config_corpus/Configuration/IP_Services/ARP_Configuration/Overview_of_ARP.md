Overview of ARP
===============

ARP provides a mechanism for mapping IP addresses to MAC addresses to implement data forwarding through Ethernet networks.

#### Introduction

The Address Resolution Protocol (ARP) is an Internet protocol used to map IP addresses to MAC addresses.

If two hosts need to communicate, the sender must know the network-layer IP address of the receiver. IP datagrams, however, must be encapsulated with MAC addresses before they can be transmitted over the physical network. Therefore, ARP is needed to map IP addresses to MAC addresses to ensure the transmission of datagrams.


#### ARP features

**Table 1** ARP features
| Feature | Description | Usage Scenario |
| --- | --- | --- |
| [Dynamic ARP](feature_0003994726.html) | Devices dynamically learn and update the mapping between IP and MAC addresses by exchanging ARP messages. | Real-time communication is a priority, or network resources are insufficient. |
| [Static ARP](feature_0003992428.html) | The mapping between IP and MAC addresses is manually created and cannot be dynamically modified. | Communication security is a priority, and network resources are sufficient. |
| [Gratuitous ARP](feature_0003992920.html) | Gratuitous ARP is used to check whether the local IP address conflicts with that of another device, to notify other devices on the same network segment of the new MAC address after the local network interface card is replaced or to notify a master/backup switchover in a VRRP group. | Gratuitous ARP is used to check whether the local IP address conflicts with that of another device, to notify other devices on the same network segment of the new MAC address after the local network interface card is replaced. |
| [Proxy ARP](feature_0003997722.html) | If a proxy ARP-enabled device receives an ARP request message that destined for another device, the proxy ARP-enabled device encapsulates its MAC address into an ARP reply message and sends the packet to the device that sends the ARP request message. | * Two hosts have the same network ID, but are located on different physical network segments. If the hosts need to communicate, routed proxy ARP must be enabled on the intermediate device. * Two hosts belong to the same VLAN, but host isolation is configured for the VLAN. If the two hosts need to communicate, intra-VLAN proxy ARP must be enabled on the termination interfaces or VLANIF interfaces of the device that connects the two hosts. * Two hosts belong to different VLANs. If the two hosts need to communicate at Layer 2, inter-VLAN proxy ARP must be enabled on the termination sub-interfaces or VLANIF interfaces of the device that connects the two hosts. * In the Ethernet virtual connection (EVC) mode, if two hosts belong to the same bridge domain (BD) for which host isolation is configured, you must enable local proxy ARP on the VBDIF interfaces that connect the two hosts. Otherwise, the two hosts cannot communicate. |
| [ARP-Ping](feature_0003997292.html) | ARP-Ping uses ARP or ICMP request messages to detect whether an IP or MAC address to be configured for a device is in use. | To prevent address conflict, send ARP messages to check whether an address is already in use on the network before configuring an IP or MAC address for a device. |
| [Dual-Device ARP Hot Backup](feature_0003998347.html) | Dual-device ARP hot backup enables ARP entries on the control and forwarding planes to be synchronized between the master and backup devices in real time. When the backup device switches to the master device, host route information is generated based on the backup ARP entries on the backup device. | Dual-device ARP hot backup prevents downlink traffic from being interrupted because the backup device does not learn ARP entries from a device on the user side during a master/backup VRRP switchover, which improves network reliability. |