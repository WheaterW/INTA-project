Overview of Layer 2 Traffic Suppression
=======================================

Layer 2 traffic suppression limits the bandwidth for forwarding unknown unknown multicast traffic, which ensures bandwidth for forwarding unicast traffic.

#### Definition

Traffic on a Layer 2 network is classified into the following types:

* Unicast traffic: consists of unicast packets whose destination MAC addresses are in the MAC table. The device forwards these packets in unicast mode according to the information in the MAC address table.
* Unknown unicast traffic: consists of unicast packets whose destination MAC addresses are not in the MAC address table. The device broadcasts these packets.
* Multicast traffic: consists of packets that use multicast addresses as destination MAC addresses. The device broadcasts these packets.
* Unknown multicast traffic: consists of packets that use multicast addresses as destination MAC or IP addresses and do not have matching multicast forwarding entries. After Layer 2 multicast is enabled, the device broadcasts these packets.

#### Purpose

Layer 2 traffic suppression limits the bandwidth for forwarding unknown multicast traffic, which ensures bandwidth for forwarding unicast traffic.