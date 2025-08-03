Traffic Forwarding When an M-LAG Works Properly (Dual-Active Mode)
==================================================================

After an M-LAG is set up successfully, M-LAG master and backup devices load balance traffic. The following describes how an M-LAG forwards traffic under normal circumstances.

#### Unicast Traffic Forwarding

In [Figure 1](#EN-US_CONCEPT_0000001512849222__dc_cfg_m-lag_0046_fig_01), an access device is dual-homed to an M-LAG. Known unicast traffic is forwarded as follows:

North-south unicast traffic from the access device is load balanced to M-LAG master and backup devices through Eth-Trunks. After receiving the traffic, the two devices forward it to the network side based on their respective routing table.

For east-west unicast traffic, once an M-LAG is set up and no non-M-LAG member interface exists, Layer 2 traffic is preferentially forwarded through the M-LAG member interface on the local device, and Layer 3 traffic is forwarded through M-LAG master and backup devices which are configured as dual-active gateways. Layer 2 and Layer 3 east-west unicast traffic is not forwarded through the peer-link, and is instead directly forwarded to corresponding member interfaces by M-LAG master and backup devices.

**Figure 1** Known unicast traffic forwarding through an M-LAG  
![](figure/en-us_image_0000001512849266.png)
#### Multicast Traffic Forwarding

**M-LAG Connecting to a Layer 2 Network**

If an M-LAG is connected to an upstream Layer 2 network, traffic from the Layer 2 network to the M-LAG can be sent to only one M-LAG member device; otherwise, a loop may occur. When the multicast source is on the network side, both the devices where the M-LAG master and backup member interfaces reside respectively can forward multicast traffic. However, due to the unidirectional isolation mechanism between peer-link interfaces and M-LAG member interfaces, multicast group members receive only one copy of traffic.

[Figure 2](#EN-US_CONCEPT_0000001512849222__fig4531101813437) uses traffic forwarding on an M-LAG backup device as an example. Assume that the M-LAG uplink interface on the M-LAG master device is blocked by a spanning tree protocol. After receiving multicast traffic, the M-LAG backup device forwards the traffic to each next hop. Network-side traffic is forwarded to ServerA and the M-LAG master device. Upon receiving the traffic through its peer-link interface, the M-LAG master device does not forward the traffic to ServerA due to the unidirectional isolation mechanism between peer-link interfaces and M-LAG member interfaces. This mechanism ensures that an M-LAG member device will not forward the traffic received through a peer-link interface to its M-LAG member interface connecting to downstream devices (ServerA in this example).

In a scenario where the multicast source is on the access side, [Figure 2](#EN-US_CONCEPT_0000001512849222__fig4531101813437) uses traffic forwarding on an M-LAG backup device as an example. Assume that the uplink interface on the M-LAG master device is blocked by a spanning tree protocol. When ServerA functions as a multicast source, ServerB functions as a multicast group member, and no other multicast group members are connected to the M-LAG, traffic sent by the multicast source is load balanced to M-LAG master and backup devices. Because the uplink interface on the M-LAG master device is blocked by a spanning tree protocol, the outbound interface of multicast traffic is changed to the peer-link interface. The M-LAG master device sends the received traffic to the M-LAG backup device. Therefore, the traffic received by both M-LAG member devices is sent to ServerB through the M-LAG backup device. Although the traffic received by the M-LAG backup device is also forwarded to the M-LAG master device through the peer-link, the M-LAG master device does not forward the traffic to ServerA due to the unidirectional isolation mechanism between peer-link interfaces and M-LAG member interfaces, and does not forward the traffic to ServerB because its uplink interface is blocked.

**Figure 2** Multicast traffic forwarding when an M-LAG is connected to a Layer 2 network  
![](figure/en-us_image_0000001654243264.png)

**M-LAG Connecting to a Layer 3 Network**

If an M-LAG is connected to an upstream Layer 3 network, M-LAG member devices need to support both Layer 2 multicast and Layer 3 multicast. In [Figure 3](#EN-US_CONCEPT_0000001512849222__dc_cfg_m-lag_0046_fig_04), an access device is dual-homed to an M-LAG dual-active system and multicast traffic is forwarded as follows:

When the multicast source is on the network side, ServerB functions as a multicast source, and ServerA functions as a multicast group member, both M-LAG master and backup devices divert traffic from the multicast source, search the local multicast forwarding table, and load balance the traffic to the multicast group member based on the following rules:

* If the last digit of the multicast group address is an odd number (for example, 225.1.1.1), the M-LAG device where the M-LAG master member interface resides forwards the traffic to the multicast group member.
* If the last digit of the multicast group address is an even number (for example, 225.1.1.2), the M-LAG device where the M-LAG backup member interface resides forwards the traffic to the multicast group member.

When the multicast source is on the access side, ServerA functions as a multicast source, ServerB functions as a multicast group member, and no other multicast group members are connected to the M-LAG, traffic sent by the multicast source is load balanced to M-LAG master and backup devices. After receiving the traffic, M-LAG master and backup devices search the local multicast forwarding table and forward the traffic. The receiver selects a link based on a unicast route to send IGMP Join messages. Only one M-LAG device receives the IGMP Join messages. Assume that the M-LAG master device receives the messages.

**Figure 3** Multicast traffic forwarding when an M-LAG is connected to a Layer 3 network  
![](figure/en-us_image_0000001966365589.png)

According to multicast traffic forwarding in the figure, an independent Layer 3 link needs to be configured between M-LAG devices when the M-LAG forwards multicast traffic, which is different from unicast traffic forwarding. The reason is that only one uplink exists at the network side when a fault occurs, and the independent Layer 3 link deployed between M-LAG master and backup devices can transmit multicast packets.

In [Figure 4](#EN-US_CONCEPT_0000001512849222__dc_cfg_m-lag_0046_fig_06), the network-side device is connected to the M-LAG backup device. Multicast packets forwarded by the peer-link interface cannot be forwarded to a specified M-LAG member interface due to unidirectional isolation. In this case, there are two methods to forward the multicast packets with the last digit of the multicast group address being an odd number to the M-LAG device where the M-LAG master member interface resides:

* Multicast packets are forwarded to the master device through an independent Layer 3 link.
* Use the peer-link as the bypass link. Configure a VLAN and the corresponding VLANIF interface. The VLAN can contain only peer-link interfaces. In this case, the unidirectional isolation mechanism is disabled so that multicast packets can be forwarded to the master device through the peer-link.

**Figure 4** Multicast traffic forwarding when an M-LAG is connected to a Layer 3 network through one uplink  
![](figure/en-us_image_0000001939127132.png)

#### Broadcast Traffic Forwarding

**M-LAG Connecting to a Layer 2 Network**

If an M-LAG is connected to an upstream Layer 2 network, traffic from the Layer 2 network to the M-LAG can be sent to an access device through only one Eth-Trunk interface. That is, the traffic can be sent to the access device dual-homed to the M-LAG through only one M-LAG member interface. Otherwise, two copies of traffic will be sent. [Figure 5](#EN-US_CONCEPT_0000001512849222__dc_cfg_m-lag_0046_fig_07) uses traffic forwarding on an M-LAG master device as an example. Assume that the M-LAG uplink interface on the M-LAG backup device is blocked by a spanning tree protocol. After receiving broadcast traffic, the M-LAG master device forwards the traffic to each next hop. Broadcast traffic on the network side is forwarded to DeviceA and the M-LAG backup device, and broadcast traffic on the access side is forwarded to the network-side device and the M-LAG backup device. Upon receiving the traffic through its peer-link interface, the M-LAG backup device does not forward the traffic to DeviceA due to the unidirectional isolation mechanism between peer-link interfaces and M-LAG member interfaces. This mechanism ensures that an M-LAG member device will not forward the traffic received through a peer-link interface to its M-LAG member interface connecting to downstream devices (DeviceA in this example).**Figure 5** Broadcast traffic forwarding when an M-LAG is connected to a Layer 2 network  
![](figure/en-us_image_0000001513168822.png)

**M-LAG Connecting to a Layer 3 Network**

[Figure 6](#EN-US_CONCEPT_0000001512849222__dc_cfg_m-lag_0046_fig_08) uses traffic forwarding on an M-LAG backup device as an example. The M-LAG backup device forwards received broadcast traffic to each next hop. Upon receiving the traffic, the M-LAG master device does not forward it to DeviceA due to the unidirectional isolation mechanism between peer-link interfaces and M-LAG member interfaces.**Figure 6** Broadcast traffic forwarding when an M-LAG is connected to a Layer 3 network  
![](figure/en-us_image_0000001563769177.png)