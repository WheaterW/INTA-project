Understanding Smart Link
========================

Understanding Smart Link

#### Basic Concepts of Smart Link

Smart Link is implemented through a pair of interfaces that form a Smart Link group. Smart Link uses Flush packets and control VLANs to better implement its functions.

* Master and slave interfaces: When the two interfaces are both up, the master interface preferentially enters the forwarding state, and the slave interface remains in the standby state. If the link where the master interface resides fails, the slave interface becomes active and switches to the forwarding state.
* Flush packets: When a link switchover occurs and MAC address entries and ARP entries need to be updated across the network, the Smart Link group sends Flush packets to instruct other devices to update the entries.
* Control VLANs: Control VLANs are classified into transmit control VLANs and receive control VLANs. A transmit control VLAN is used by a device configured with a Smart Link group to broadcast Flush packets. A receive control VLAN is used by upstream devices to receive and process Flush packets. The IDs of the transmit control VLAN and receive control VLAN must be the same.

**Figure 1** Basic networking of Smart Link  
![](figure/en-us_image_0000001176743181.png)

[Figure 1](#EN-US_CONCEPT_0000001176743169__fig0609193685719) shows the basic networking of Smart Link. The following describes basic working principles of Smart Link starting with links in their normal state, then covering link faults, and finally link recovery.


#### Both Links in a Normal State

When the two uplinks are working properly, interface1 on DeviceA functions as the master interface and is in the forwarding state. The link where the master interface resides is the primary link, and data is transmitted along the path DeviceA -> DeviceB -> DeviceD. The slave interface (interface2) is in the standby state, and the link where interface2 resides is the secondary link.


#### Primary Link Fails

As shown in [Figure 1](#EN-US_CONCEPT_0000001176743169__fig0609193685719), when the primary link on DeviceA fails, the master interface (interface1) switches to the standby state, and the slave interface (interface2) switches to the forwarding state. In this case, existing MAC address entries and ARP entries on the devices no longer apply to the new topology. A mechanism is required to update MAC address entries and ARP entries. Two mechanisms are available:

**Entry update triggered by Flush packets**

This mechanism applies to scenarios where upstream devices support Smart Link. As shown in [Figure 1](#EN-US_CONCEPT_0000001176743169__fig0609193685719), to implement a fast link switchover, DeviceA must be configured to send Flush packets, and all interfaces on upstream devices along the dual uplinks must be configured to receive and process Flush packets.

1. After link switchover on DeviceA, Flush packets are sent by interface2 over the new primary link.
2. Upon receipt of a Flush packet, the upstream device checks whether the transmit control VLAN in the Flush packet is in the receive control VLAN table on the interface that receives the packet. If it is so, the device processes the Flush packet and updates MAC address and ARP entries. If it is not, the device directly forwards the Flush packet.

The device forwards data packets to the destination device based on the updated MAC address entries or ARP entries.

**Automatic entry update triggered by traffic**

This mechanism applies to scenarios where upstream devices do not support Smart Link (including scenarios where upstream devices are non-Huawei devices). These devices update MAC address entries and ARP entries upon receipt of upstream traffic.

As shown in [Figure 1](#EN-US_CONCEPT_0000001176743169__fig0609193685719), even if the downstream device does not send upstream traffic to trigger the upstream device to update its MAC address entries and ARP entries, DeviceD still forwards data packets destined for DeviceA through interface3. However, packets cannot reach DeviceA at this point, and packets are lost until the MAC address entries or ARP entries age out automatically.

MAC address entries and ARP entries learned on interface1 are deleted after the primary link fails. If DeviceA needs to send upstream traffic, it must rebroadcast ARP packets first. When the upstream traffic reaches DeviceD through interface4, DeviceD updates its MAC address entries and ARP entries. When receiving packets destined for DeviceA, DeviceD forwards the packets through interface4. The packets are then forwarded by DeviceC to DeviceA.


#### Primary Link Recovers

As shown in [Figure 1](#EN-US_CONCEPT_0000001176743169__fig0609193685719), when the original primary link (DeviceA -> DeviceB -> DeviceD) recovers, interface1 remains in the blocked state by default to ensure that traffic transmission is stable. To switch traffic back to the original primary link, use either of the following mechanisms:

* Enable the switchback function of the Smart Link group on DeviceA. Once enabled, interface2 is blocked and switches to the standby state after the wait to restore (WTR) timer expires. Interface1 switches to the forwarding state, and the Smart Link group automatically switches traffic to the original primary link.
* Run a command to forcibly switch traffic to the original primary link. After the command is run, interface2 is immediately blocked and switches to the standby state, and interface1 switches to the forwarding state.