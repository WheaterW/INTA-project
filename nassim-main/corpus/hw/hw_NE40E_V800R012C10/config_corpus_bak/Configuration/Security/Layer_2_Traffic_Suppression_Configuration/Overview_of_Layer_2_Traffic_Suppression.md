Overview of Layer 2 Traffic Suppression
=======================================

The traffic involved in Layer 2 traffic suppression includes broadcast, multicast, and unknown unicast traffic.

#### Layer 2 Traffic Classification

Traffic on a Layer 2 network is classified into the following types:

* Unicast traffic: consists of unicast packets whose destination MAC addresses are in the MAC address table. The NE40E forwards these packets in unicast mode according to the information in the MAC address table.
* Unknown unicast traffic: consists of unicast packets whose destination MAC addresses are not in the MAC address table. The NE40E broadcasts these packets.
* Multicast traffic: consists of packets that use multicast addresses as destination MAC addresses. The NE40E broadcasts these packets.
* Unknown multicast traffic: consists of packets that use multicast addresses as destination MAC or IP addresses and do not have matching multicast forwarding entries. After Layer 2 multicast is enabled, the NE40E broadcasts these packets.
* Broadcast traffic: consists of packets that use broadcast addresses as destination MAC addresses. The NE40E broadcasts these packets.

To ensure the transmission of unicast traffic, the NE40E can limit the bandwidth for forwarding broadcast, multicast, unknown multicast, and unknown unicast traffic.


#### Traffic Suppression

Most Layer 2 network scenarios require unicast traffic to be much heavier than broadcast traffic. This is also a requirement for networking. If broadcast traffic is not suppressed, forwarding a large volume of such traffic consumes numerous bandwidth resources, reducing network performance and even causing a communication interruption.

In this case, you can configure broadcast traffic suppression on the NE40E to ensure that the device can reserve some bandwidth for forwarding unicast traffic when broadcast traffic bursts.