Overview of Storm Suppression
=============================

Overview of Storm Suppression

#### Definition

Storm suppression is used to control broadcast packets, unknown multicast packets, and unknown unicast packets, thereby preventing broadcast storms that they may cause.

Storm suppression includes traffic suppression and storm control.

* Traffic suppression limits the rate of broadcast packets, unknown multicast packets, or unknown unicast packets by setting a threshold. When the traffic exceeds this threshold, the system discards excess traffic, allowing only packets within the threshold to pass through. In this way, the volume of traffic is kept within an appropriate range. Note that traffic suppression can also block outgoing packets on interfaces.
* Storm control blocks broadcast packets, unknown multicast packets, or unknown unicast packets by discarding packets or shutting down an interface. Storm control can also control the average rate of packets by suppressing them. When traffic exceeds the specified threshold, the system performs a predefined storm control action.

[Table 1](#EN-US_CONCEPT_0000001513168450__table19957135533016) compares traffic suppression and storm control.

**Table 1** Comparison between traffic suppression and storm control
| Item | Traffic Suppression | Storm Control |
| --- | --- | --- |
| Traffic control | * If traffic suppression is configured in the outbound direction of an interface, the system blocks all traffic of the corresponding packet type. * In other cases, the system discards the traffic exceeding the threshold and allows the packets within the threshold to pass through. | * If the storm control action is configured to suppress packets, when the average rate of packets received on the interface exceeds the configured upper threshold, the system discards excess traffic until the average rate of packets drops below the threshold. * In other cases, when traffic exceeds the specified threshold, the system blocks the traffic received by the interface or shuts down the interface. |
| Traffic detection | * Chip-based detection * If traffic exceeds the threshold, traffic suppression takes effect immediately. | * Software-based detection * If the average packet rate exceeds the threshold within the detection interval, storm control takes effect. |




#### Purpose

When a Layer 2 Ethernet interface on a device receives broadcast, unknown multicast, or unknown unicast packets, the device forwards these packets to other Layer 2 Ethernet interfaces in the same VLAN if the outbound interfaces cannot be determined based on the destination MAC addresses of these packets. As a result, a broadcast storm may be generated, degrading forwarding performance of the device. This problem also occurs on a Virtual eXtensible Local Area Network (VXLAN) network.

Traffic suppression and storm control can effectively control the traffic of these types of packets.