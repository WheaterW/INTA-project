Overview of Ping and Tracert
============================

![](../public_sys-resources/note_3.0-en-us.png) 

The device does not support the multicast trace route (MTrace) function and can only forward received MTrace IGMP messages. If the destination address of an IGMP Tracert Response message is a multicast address, the device sends the message to all PIM-enabled interfaces except the interface that receives the message. The message is looped on the ring network until the TTL value becomes 0. Then, the message is discarded.


#### Definition

**Ping**

Packet Internet Groper (Ping) is a typical debugging tool used to test the reachability of network devices. You can perform a ping operation on a source to send an Internet Control Message Protocol (ICMP) Echo message to a destination. After receiving the message, the destination returns an ICMP Echo Reply message to the source. You can test the following items using ping:

* Reachability of a remote device
* Round-trip time (RTT) in communication with a remote device
* ICMP Echo message loss

**Tracert**

Tracert tests reachability of each hop on the path from a source to a destination. You can perform a tracert operation on a source to send UDP packets with different TTL values to a destination. During packet forwarding, the TTL value of a packet is decremented by one each time the packet reaches a hop. If a hop receives a packet with the TTL value of 0, this hop sends an ICMP Time Exceeded message to the source. If the destination receives such a packet, it sends an ICMP Port Unreachable message to the source. You can test the following items using tracert:

* Reachability of each hop on the path from a source to a destination
* RTT in communication between the source and each hop

#### Purpose

If a network service is unavailable, the network provider needs to test reachability of network devices and locate the network fault. As most network devices support ping and tracert functions, network providers can use ping to test device reachability and use tracert to test reachability of each hop on a network path.


#### Benefits

The ping and tracert functions help users test network reachability and RTT, facilitating network fault locating.