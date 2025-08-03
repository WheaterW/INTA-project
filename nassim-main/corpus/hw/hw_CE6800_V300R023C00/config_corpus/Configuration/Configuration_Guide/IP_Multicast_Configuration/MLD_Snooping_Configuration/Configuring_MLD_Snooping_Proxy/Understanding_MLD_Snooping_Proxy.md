Understanding MLD Snooping Proxy
================================

Understanding MLD Snooping Proxy

#### Fundamentals

A device configured with MLD snooping proxy acts as a host for its upstream devices and as a querier for its downstream devices. MLD snooping proxy can help reduce the number of MLD messages transmitted on the network segment where user hosts reside. After this function is configured on a Layer 2 multicast device, the device substitutes the upstream Layer 3 device to send MLD Query messages to user hosts, and substitutes user hosts to send MLD Report/Done messages to the upstream Layer 3 device.

In [Figure 1](#EN-US_CONCEPT_0000001372550993__fig_01), Device runs MLD snooping and directly forwards the Query messages sent by the upstream device (Router) and the Report/Done messages sent by downstream hosts, without changing the messages. If there are many hosts, redundant MLD messages may overload the upstream device.

When MLD snooping proxy is configured on the device, Device can terminate MLD Query messages sent by the upstream device, construct new Query messages, and send them to downstream hosts. In addition, Device can terminate MLD Report/Done messages sent by downstream hosts, construct new Report/Done messages, and send them to the upstream device.

**Figure 1** MLD snooping proxy network  
![](figure/en-us_image_0000001494711461.png)

After the Layer 2 device is configured with MLD snooping proxy, it no longer functions as a transparent forwarding device and instead directly interacts with the upstream device and downstream hosts. Furthermore, the Layer 3 device is aware of only one user. As such, MLD snooping proxy minimizes the number of MLD message exchanges, thereby conserving bandwidth. By preventing a large number of host-side protocol messages from being sent to the upstream Layer 3 device and implementing the querier function, MLD snooping proxy reduces the load of the upstream Layer 3 device.


#### Implementation

A device that runs MLD snooping proxy sets up and maintains a Layer 2 multicast forwarding table, based on which the device sends multicast data to hosts that need the data. [Table 1](#EN-US_CONCEPT_0000001372550993__tab_01) describes how MLD snooping proxy processes MLD messages.

**Table 1** MLD message processing by MLD snooping proxy
| MLD Message Type | Processing Method |
| --- | --- |
| MLD General Query | The device sends an MLD General Query message to all interfaces (except its own interface that received such a message) in the corresponding VLAN. In addition, the device generates a Report message based on the locally maintained group memberships and sends it to all router ports. |
| MLD Group-Specific/Group-Source-Specific Query message | If the forwarding entry of the corresponding group contains member ports, the device sends a Report message to all router ports. |
| MLD Report | If no forwarding entry exists for the multicast group, the device creates a forwarding entry, adds the interface that received the message to the outbound interface list as a dynamic member port, starts an aging timer, and sends a Report message to all router ports.  If a forwarding entry exists for the multicast group and the interface that received the message is already added to the outbound interface list as a dynamic member port, the device resets the aging timer.  If a forwarding entry exists for the multicast group but the interface that received the message has not been added to the outbound interface list, the device adds the interface to the list as a dynamic member port, and starts an aging timer. |
| MLD Done | The device sends a Group-Specific Query message to the interface that received the message. The device sends a Done message to all router ports only after the last member port is deleted from the forwarding entry of the corresponding multicast group. |