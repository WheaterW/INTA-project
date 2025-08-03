Understanding IGMP Snooping Proxy over VXLAN
============================================

Understanding IGMP Snooping Proxy over VXLAN

#### Definition

Based on IGMP snooping, IGMP snooping proxy enables a device to act as a substitute for an upstream Layer 3 device to send IGMP Query messages to downstream hosts and as a substitute for downstream hosts to send IGMP Report/Leave messages to an upstream device. IGMP snooping proxy conserves bandwidth between the upstream device and the local device.


#### Fundamentals

A device configured with IGMP snooping proxy acts as a host for its upstream devices and as a querier for its downstream hosts. IGMP snooping proxy can help reduce the number of IGMP messages transmitted on the network segment where user hosts reside. After this function is configured on a Layer 2 multicast device, the device substitutes the upstream Layer 3 device to send IGMP Query messages to user hosts, and substitutes user hosts to send IGMP Report/Leave messages to the upstream Layer 3 device.

In [Figure 1](#EN-US_CONCEPT_0000001145453112__fig_01), Device runs IGMP snooping and directly forwards the Query messages sent from the upstream device (Router) and the Report/Leave messages sent from downstream hosts, without processing the messages. If there are many hosts, redundant IGMP messages may overload the upstream device.

After Device is configured with IGMP snooping proxy and it receives IGMP Query messages from the upstream device, Device terminates them, and then constructs and sends new Query messages to downstream hosts. Similarly, after receiving IGMP Report/Leave messages from downstream hosts, Device terminates them, and then constructs and sends new Report/Leave messages to the upstream device.

**Figure 1** Network diagram of IGMP snooping proxy  
![](figure/en-us_image_0000001145477830.png)

After the Layer 2 device is configured with IGMP snooping proxy, it no longer functions as a transparent forwarding device and instead directly interacts with the upstream device and downstream hosts. Furthermore, the Layer 3 device is aware of only one user. As such, IGMP snooping proxy minimizes the number of IGMP message exchanges, thereby conserving bandwidth. By preventing a large number of host-side protocol messages from being sent to the upstream Layer 3 device and implementing the querier function, IGMP snooping proxy reduces the load of the upstream Layer 3 device.


#### Implementation

A device that runs IGMP snooping proxy sets up and maintains a Layer 2 multicast forwarding table, based on which the device sends multicast data to hosts that need the data. [Table 1](#EN-US_CONCEPT_0000001145453112__tab_01) describes how an IGMP snooping proxy device processes IGMP messages.

**Table 1** Processing of received messages by an IGMP snooping proxy device
| IGMP Message Type | Processing Method |
| --- | --- |
| IGMP General Query message | The device sends an IGMP General Query message to all interfaces (except its own interface that received such a message) in the corresponding BD. In addition, the device generates a Report message based on the locally maintained group memberships and sends it to all router ports. |
| IGMP Group-Specific/Group-and-Source-Specific Query message | If the forwarding entry of the corresponding group contains member ports, the device sends a Report message to all router ports. |
| IGMP Report message | * If no forwarding entry exists for the multicast group, the device creates a forwarding entry, adds the interface that received the message to the outbound interface list as a dynamic member port, starts an aging timer, and sends a Report message to all router ports. * If a forwarding entry exists for the multicast group and the interface that received the message is already added to the outbound interface list as a dynamic member port, the device resets the aging timer. * If a forwarding entry exists for the multicast group but the interface that received the message has not been added to the outbound interface list, the device adds the interface to the list as a dynamic member port and starts an aging timer. |
| IGMP Leave message | The device sends a Group-Specific Query message to the interface that received the message. The device sends a Leave message to all router ports only after the last member port is deleted from the forwarding entry of the corresponding multicast group. |