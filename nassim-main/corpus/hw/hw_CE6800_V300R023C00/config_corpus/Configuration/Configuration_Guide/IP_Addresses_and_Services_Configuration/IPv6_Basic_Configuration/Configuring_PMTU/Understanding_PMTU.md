Understanding PMTU
==================

Understanding PMTU

#### Application Scenarios

IPv6 packets cannot be fragmented on the transit node. Therefore, the packet length is often greater than the path MTU (PMTU). The source node then needs to keep retransmitting the IPv6 packets, which reduces transmission efficiency. If the source node uses the minimum IPv6 MTU of 1280 bytes as the maximum fragment length, in most cases, the PMTU is greater than the minimum IPv6 MTU of the link, and the fragments sent by a node are much less than the PMTU. As a result, network resources are wasted. To resolve this issue, deploy the PMTU discovery mechanism.


#### Fundamentals

The PMTU discovery mechanism uses ICMPv6 Packet Too Big messages to determine a proper IPv6 MTU value for the path from the source to the destination. When an IPv6 node has a large amount of data to send to another node, the data is transmitted in a series of IPv6 fragments. When these fragments are of the maximum length allowed in successful transmission from the source node to the destination node, the fragment length is considered optimal and called PMTU.

A source node assumes that the PMTU of a path is the known IPv6 MTU of the first hop on the path. If any of the packets sent on that path are too large to be forwarded, the transit node discards these packets and returns an ICMPv6 Packet Too Big message to the source node. The source node sets the PMTU for the path based on the IPv6 MTU in the received message.

When the PMTU learned by a node is less than or equal to the actual PMTU, the PMTU discovery process is complete. Before the PMTU discovery process is completed, ICMPv6 Packet Too Big messages may be repeatedly sent or received because there may be links with smaller IPv6 MTUs further along the path.

[Figure 1](#EN-US_CONCEPT_0000001176741599__fig1283163515312) shows an example of PMTU discovery.

**Figure 1** PMTU discovery  
![](figure/en-us_image_0000001176661711.png)

Packets are transmitted through four links with MTU values of 1500, 1500, 1400, and 1300 bytes, respectively. Before sending a packet, the source node fragments the packet based on a PMTU value of 1500 bytes. When a fragment is sent to the outbound interface with an MTU value of 1400 bytes, the corresponding device returns a Packet Too Big message carrying an MTU value of 1400 bytes. The source node then fragments the packet based on a PMTU value of 1400 bytes and sends a fragment again. When the fragment is sent to the outbound interface with an MTU value of 1300 bytes, the corresponding device returns a Packet Too Big message carrying an MTU value of 1300 bytes. The source node receives the message and fragments the packet based on a PMTU value of 1300 bytes. In this way, the source node sends the packet to the destination and discovers the PMTU of the path.

![](public_sys-resources/note_3.0-en-us.png) 

IPv6 requires a minimum MTU value of 1280 bytes at the link layer. Therefore, the PMTU value must be greater than 1280 bytes. A PMTU value of 1500 bytes is recommended.