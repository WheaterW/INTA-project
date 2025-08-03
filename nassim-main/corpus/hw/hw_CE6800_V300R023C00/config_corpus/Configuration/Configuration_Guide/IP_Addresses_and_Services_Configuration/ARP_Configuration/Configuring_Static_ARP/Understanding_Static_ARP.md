Understanding Static ARP
========================

Understanding Static ARP

#### Definition

Static ARP allows a network administrator to create a mapping between IP and MAC addresses.


#### Purpose

Configuring static ARP entries improves communication security. If a static ARP entry is configured on a device, the device can communicate with the peer device using only the specified MAC address. This improves communication security, because network attackers cannot modify the mapping between the IP and MAC addresses using ARP messages. Static ARP applies to networks with simple topologies, high stability, and high information security requirements.

**Table 1** Classification of static ARP entries
| Type | Description |
| --- | --- |
| Short static ARP entry | Short static ARP entries cannot be directly used to forward messages. A short static ARP entry contains IP and MAC addresses. An ARP Miss message must be triggered when users need to send packets. If the source IP and MAC addresses of a received reply message are the same as the configured IP and MAC addresses in a short static ARP entry, the device adds the interface that receives the ARP reply message to the short static ARP entry. The device can directly use this interface to forward subsequent messages.  Configuring a short static ARP entry enables a device and host to communicate using fixed IP and MAC addresses. |
| Long static ARP entry | In addition to IP and MAC addresses, a long static ARP entry contains a VLAN ID and outbound interface. Long static ARP entries can be directly used to forward messages.  Configure a long static ARP entry if you want a device and host to communicate only through the specified interface in a specified VLAN. |



#### Benefits

To ensure communication stability and security, deploy static ARP based on actual requirements and network resources.

* IP addresses can be bound to the MAC address of a specified gateway to ensure that only this gateway forwards the IP datagrams destined to these IP addresses.
* The destination IP addresses of certain IP datagrams sent by a specified host can be bound to a nonexistent MAC address, helping filter out unnecessary IP datagrams.