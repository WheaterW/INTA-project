M-LAG Loop Prevention Mechanism
===============================

M-LAG has a loop prevention mechanism that helps construct a loop-free network. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001564128889__fig1546120157115), unicast traffic from the access device or network-side device to M-LAG devices is forwarded through the local M-LAG device preferentially, and the peer-link does not transmit data traffic under normal circumstances. When traffic is broadcast to the peer M-LAG device through the peer-link, the traffic received through the peer-link is not forwarded through the M-LAG member interface because unidirectional traffic isolation is configured between the peer-link and M-LAG member interface, preventing a loop. This is the unidirectional isolation mechanism of M-LAG.

**Figure 1** Traffic forwarding when an M-LAG is connected to a Layer 2 network  
![](../images/en-us_image_0000001564009261.png)
#### Unidirectional Isolation Mechanism

**Prerequisites for the Mechanism to Take Effect**

When M-LAG master and backup devices are negotiated, the system checks whether an access device is dual-homed to the M-LAG using M-LAG synchronization packets.

* If the access device is dual-homed to the M-LAG, the two M-LAG devices automatically deliver the unidirectional isolation configuration of the corresponding M-LAG member interface to isolate traffic from peer-link interfaces to M-LAG member interfaces.![](../public_sys-resources/note_3.0-en-us.png) 
  
  Unidirectional isolation in the M-LAG loop prevention mechanism takes effect for Layer 2 traffic (including unicast, multicast, and broadcast traffic) and Layer 3 multicast traffic, and does not take effect for Layer 3 unicast traffic.
* If the access device is single-homed to the M-LAG, the M-LAG does not deliver the unidirectional isolation configuration of the corresponding M-LAG member interface.
* In active/standby mode, the M-LAG does not deliver the unidirectional isolation configuration of the corresponding M-LAG member interface.

**Implementation of the Unidirectional Isolation Mechanism**

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001564128889__fig574564411193), when a device is dual-homed to an M-LAG, unidirectional isolation is implemented between peer-link interfaces and M-LAG member interfaces through the port isolation function, isolating flooding traffic such as broadcast traffic sent from peer-link interfaces to M-LAG member interfaces.

The two M-LAG devices automatically deliver the unidirectional isolation configuration of the corresponding M-LAG member interface. Interfaces in the same port isolation group cannot communicate with each other. When an M-LAG device detects that the local M-LAG member interface is down, the device sends M-LAG synchronization packets through the peer-link to instruct the peer device to automatically delete the corresponding M-LAG member interface from the isolation group.

**Figure 2** M-LAG unidirectional isolation  
![](../images/en-us_image_0000001513049014.png)