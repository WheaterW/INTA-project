Traffic Forwarding When an M-LAG Works Properly (Active/Standby Mode)
=====================================================================

After an M-LAG is set up successfully, the M-LAG master member interface forwards traffic and the M-LAG backup member interface does not forward traffic. The following describes how an M-LAG forwards traffic under normal circumstances.

#### Unicast Traffic Forwarding

In [Figure 1](#EN-US_CONCEPT_0000001564128885__fig8165131607), active and standby NICs of a server are connected to an M-LAG. Known unicast traffic is forwarded as follows:

For north-south unicast traffic at the M-LAG access side, when DeviceA in the M-LAG receives traffic from the active NIC of the server, DeviceA forwards the traffic to the network side based on its routing table. For north-south unicast traffic at the M-LAG network side, when DeviceA receives traffic from the network side, DeviceA forwards the traffic to the server through the M-LAG master member interface. When DeviceB receives traffic from the network side, DeviceB forwards the traffic to DeviceA through the peer-link interface, and then DeviceA forwards the traffic to the server through the M-LAG master member interface.

For east-west unicast traffic, if an M-LAG is set up and there is no non-M-LAG member interface, both Layer 2 traffic and Layer 3 traffic are forwarded through the M-LAG master member interface.

**Figure 1** Known unicast traffic forwarding through an M-LAG  
![](../images/en-us_image_0000001564009233.png)

#### Multicast Traffic Forwarding

**M-LAG Connecting to a Layer 2 Network**

If an M-LAG is connected to an upstream Layer 2 network, traffic from the Layer 2 network to the M-LAG can be sent to only one M-LAG member device; otherwise, a loop may occur. In [Figure 2](#EN-US_CONCEPT_0000001564128885__fig9824933163012), the active and standby NICs of ServerA are connected to DeviceA and DeviceB in an M-LAG, respectively. Assume that the uplink interface of DeviceA where the M-LAG master member interface resides is blocked by a spanning tree protocol.

When the multicast source is on the network side, ServerB functions as a multicast source, and ServerA functions as a multicast group member, only the device where the M-LAG master member interface resides can forward multicast traffic. When only one copy of traffic is diverted from the network side, DeviceB receives the traffic and forwards the traffic to the M-LAG member interface of DeviceA through the peer-link.

If the M-LAG master member interface on DeviceA fails, the link where the interface resides goes down. DeviceA detects the interface fault, switches the M-LAG master member interface to the M-LAG backup member interface, and notifies DeviceB of the fault. After receiving the notification, DeviceB switches the M-LAG backup member interface to the M-LAG master member interface. In addition, when the active NIC of the server detects a link fault, the standby NIC becomes the active NIC and sends packets for electing the M-LAG master member interface. After receiving the packets from the server, the M-LAG backup member interface on DeviceB also becomes the M-LAG master member interface. In this case, multicast traffic is switched to the member interface of DeviceB in the M-LAG, as shown in [Figure 3](#EN-US_CONCEPT_0000001564128885__fig10746101111315).

If the uplink interface of DeviceB where the M-LAG backup member interface resides is blocked by a spanning tree protocol, DeviceA directly forwards received traffic through the local M-LAG member interface.

When the multicast source is on the access side, ServerA functions as a multicast source, and ServerB functions as a multicast group member, traffic from the multicast source is sent to the M-LAG master device DeviceA. Because the uplink interface of DeviceA is blocked, the outbound interface of multicast traffic is the peer-link interface. If the M-LAG master member interface on DeviceA fails, multicast traffic is switched to the member interface on the other M-LAG device DeviceB.

**Figure 2** Multicast traffic forwarding when an M-LAG is connected to a Layer 2 network  
![](../images/en-us_image_0000001563769285.png)
**Figure 3** Multicast traffic forwarding when an M-LAG is connected to a Layer 2 network and an M-LAG member interface fails  
![](../images/en-us_image_0000001938968532.png)

**M-LAG Connecting to a Layer 3 Network**

If an M-LAG is connected to an upstream Layer 3 network, M-LAG member devices need to support both Layer 2 multicast and Layer 3 multicast. In [Figure 4](#EN-US_CONCEPT_0000001564128885__fig1849619553310), the active and standby NICs of ServerA are connected to DeviceA and DeviceB in an M-LAG respectively, and the M-LAG forwards multicast traffic.

When the multicast source is on the network side, ServerB functions as a multicast source, and ServerA functions as a multicast group member, both M-LAG master and backup devices divert traffic from the multicast source, search the local multicast forwarding table, and forward multicast traffic to the multicast group member based on the following rules:

* After receiving multicast traffic, the M-LAG device where the M-LAG master member interface resides directly forwards the traffic to the multicast group member.
* After receiving multicast traffic, the M-LAG device where the M-LAG backup member interface resides directly discards outgoing multicast traffic on the M-LAG backup member interface.

When the multicast source is on the access side, ServerA functions as a multicast source, ServerB functions as a multicast group member, and no other multicast group members are connected to the M-LAG, traffic from the multicast source is sent to DeviceA. After receiving the traffic, DeviceA searches the local multicast forwarding table and forwards the traffic. The receiver selects a link based on a unicast route to send IGMP Join messages. Only one M-LAG device receives the IGMP Join messages. Assume that DeviceA receives the messages.

**Figure 4** Multicast traffic forwarding when an M-LAG is connected to a Layer 3 network  
![](../images/en-us_image_0000001939128364.png)
When an M-LAG in active/standby mode forwards multicast traffic, an independent Layer 3 link needs to be configured between the two M-LAG devices, which is similar to that in an M-LAG in dual-active mode. The reason is that only one uplink exists at the network side when a fault occurs, and the independent Layer 3 link deployed between the two M-LAG devices can transmit multicast packets. In [Figure 5](#EN-US_CONCEPT_0000001564128885__fig18332836368), the network-side device is connected to DeviceB whose M-LAG member interface is in the backup state. Outgoing multicast traffic on the M-LAG backup member interface is directly discarded and cannot be forwarded to the M-LAG member interface on the peer device. In this case, multicast packets can be forwarded to the peer device whose M-LAG member interface is in the master state in either of the following ways:

* Multicast packets are forwarded to the device whose M-LAG member interface is in the master state through an independent Layer 3 link.
* Use the peer-link as the bypass link. Configure a VLAN and the corresponding VLANIF interface. The VLAN can contain only peer-link interfaces. In this case, multicast packets can be forwarded to the master device through the peer-link.

**Figure 5** Multicast traffic forwarding when an M-LAG is connected to a Layer 3 network through one uplink  
![](../images/en-us_image_0000001512689830.png)

#### Broadcast Traffic Forwarding

**M-LAG Connecting to a Layer 2 Network**

In [Figure 6](#EN-US_CONCEPT_0000001564128885__fig798410512597), the active and standby NICs of ServerA are connected to DeviceA and DeviceB in an M-LAG, respectively. Assume that the uplink interface of DeviceB is blocked by a spanning tree protocol. After receiving broadcast traffic, DeviceA forwards the traffic to each next hop. Network-side broadcast traffic is forwarded to ServerA and DeviceB, and access-side broadcast traffic is forwarded to the network-side device and DeviceB.

When traffic is broadcast to the peer M-LAG device through the peer-link, the traffic is forwarded from the M-LAG backup member interface to the standby NIC of ServerA because the M-LAG in active/standby mode does not deliver the unidirectional isolation configuration of the corresponding M-LAG member interface. However, the standby NIC of ServerA does not process the received traffic. Therefore, no loop occurs.

**Figure 6** Broadcast traffic forwarding when an M-LAG is connected to a Layer 2 network  
![](../images/en-us_image_0000001513048966.png)

**M-LAG Connecting to a Layer 3 Network**

In [Figure 7](#EN-US_CONCEPT_0000001564128885__fig1832962922517), the active and standby NICs of ServerA are connected to DeviceA and DeviceB in an M-LAG, respectively. After receiving broadcast traffic from ServerA, DeviceA forwards the traffic to each next hop. When traffic is broadcast to the peer M-LAG device through the peer-link, the traffic is forwarded from the M-LAG backup member interface to the standby NIC of ServerA because the M-LAG in active/standby mode does not deliver the unidirectional isolation configuration of the corresponding M-LAG member interface. However, the standby NIC of ServerA does not process the received traffic. Therefore, no loop occurs.

**Figure 7** Broadcast traffic forwarding when an M-LAG is connected to a Layer 3 network  
![](../images/en-us_image_0000001563769325.png)