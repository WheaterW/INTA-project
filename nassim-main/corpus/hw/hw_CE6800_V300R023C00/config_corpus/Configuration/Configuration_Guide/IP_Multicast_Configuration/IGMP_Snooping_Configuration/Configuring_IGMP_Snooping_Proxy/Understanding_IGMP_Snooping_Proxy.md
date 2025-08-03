Understanding IGMP Snooping Proxy
=================================

Understanding IGMP Snooping Proxy

#### Fundamentals

A device configured with IGMP snooping proxy acts as a host for its upstream devices and as a querier for its downstream hosts. IGMP snooping proxy can help reduce the number of IGMP messages transmitted on the network segment where user hosts reside. After this function is configured on a Layer 2 multicast device, it substitutes the upstream Layer 3 device to send IGMP Query messages to user hosts, and substitutes user hosts to send Membership Report messages to the upstream Layer 3 device.

In [Figure 1](#EN-US_CONCEPT_0000001130622118__fig_01), Device runs IGMP snooping and directly forwards the Query messages sent from the upstream device (Router) and the Report/Leave messages sent from downstream hosts, without processing them. If there are many hosts, redundant IGMP messages overload the upstream device.

When IGMP snooping proxy is configured on Device, Device can terminate IGMP Query messages sent by the upstream device, construct new Query messages, and send them to downstream hosts. In addition, Device can terminate IGMP Report/Leave messages sent by downstream hosts, construct new Report/Leave messages, and send them to the upstream device.

**Figure 1** Network diagram of IGMP snooping proxy  
![](figure/en-us_image_0000001176741589.png)

After IGMP snooping proxy is deployed on the Layer 2 device, it no longer functions as a transparent forwarding device and instead directly interacts with the upstream device and downstream hosts. Furthermore, the Layer 3 device is aware of only one user. As such, IGMP snooping proxy minimizes the number of IGMP message exchanges, thereby conserving bandwidth. By disabling host-side protocol messages from being sent to the upstream Layer 3 device and implementing the querier function to maintain group memberships, IGMP snooping proxy reduces the load of the upstream Layer 3 device.


#### Implementation

A device that runs IGMP snooping proxy sets up and maintains a Layer 2 multicast forwarding table, based on which the device sends multicast data to hosts. [Table 1](#EN-US_CONCEPT_0000001130622118__tab_01) describes how an IGMP snooping proxy device processes IGMP messages.

**Table 1** Message processing by an IGMP snooping proxy device
| IGMP Message Type | Processing Method |
| --- | --- |
| IGMP General Query message | If querier election is disabled on a device, the device does not forward Query messages.  If querier election is enabled on the device:   * After a device is elected as a querier, the device processes a newly received IGMP General Query message as follows:   + If the source IP address of the IGMP General Query message is smaller than that of the querier, the querier sends the message to all interfaces except the interface that receives the message in the VLAN.   + If the source IP address of the IGMP General Query message is greater than that of the querier, the querier sends the message to all interfaces in the VLAN. * If the device is not a querier, it sends the IGMP General Query message to all interfaces except the interface that receives the IGMP General Query message in the VLAN.   At the same time, the device generates a Report message based on the locally maintained group memberships and sends the Report message to all router ports. |
| IGMP Group-Specific/Group-Source-Specific Query message | If the forwarding entry of the corresponding group contains member ports, the device sends a Report message to all router ports. |
| IGMP Report message | If no forwarding entry exists for the multicast group, the device creates a forwarding entry, adds the interface that received the message to the outbound interface list as a dynamic member port, starts an aging timer, and sends a Report message to all router ports.  If a forwarding entry exists for the multicast group and the interface that received the message is already added to the outbound interface list as a dynamic member port, the device resets the aging timer.  If a forwarding entry exists for the multicast group but the interface that received the message has not been added to the outbound interface list, the device adds the interface to the list as a dynamic member port, and starts an aging timer. |
| IGMP Leave message | The device sends a Group-Specific Query message to the interface that received the message. The device sends a Leave message to all router ports only after the last member port is deleted from the forwarding entry of the corresponding multicast group. |