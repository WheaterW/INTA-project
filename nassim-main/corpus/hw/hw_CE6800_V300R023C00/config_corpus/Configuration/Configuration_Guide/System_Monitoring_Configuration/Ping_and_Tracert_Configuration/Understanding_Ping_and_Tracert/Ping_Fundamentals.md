Ping Fundamentals
=================

Ping is a common tool used to test network device reachability. Based on the ICMP mechanism, the ping operation enables the source to send ICMP Echo Request messages to the destination. After receiving these messages, the destination returns ICMP Echo Reply messages. The source determines the reachability of the destination based on whether the ICMP Echo Reply messages are received within the timeout interval. If the destination is reachable, the source can then obtain the RTT.

#### Ping Process

The packet exchange during a ping operation is as follows:

1. A user performs a ping operation on the source (DeviceA), sending a batch of ICMP Echo Request messages to the specified destination. The sequence number of the ICMP Echo Request messages starts from 1 and is incremented by a step of 1, as shown in [Figure 1](#EN-US_CONCEPT_0000001130784784__fig11636123016486). The number of ICMP Echo Request messages sent in a ping operation is configurable and is 5 by default. After sending the ICMP Echo Request messages, the source starts the timeout timer and waits for the ICMP Echo Reply messages from the destination (DeviceB).
2. After receiving an ICMP Echo Request message, the destination sends an ICMP Echo Reply message with the same sequence number as the received message.
3. If the ICMP Echo Reply message reaches the source before the timer expires, the destination is considered reachable. The source can obtain the RTT by simply adding the time required for a request to be sent and that required for the corresponding response to be received.

**Figure 1** Packet exchange during a ping operation  
![](figure/en-us_image_0000001130784798.png)

A request timeout message will be displayed on the source if either of the following problems occurs:

* The TTL value of an ICMP Echo Request message is decremented to 0 before the message reaches the destination. The intermediate device that receives this message sends an ICMP Time Exceeded message to the source, indicating that the destination is unreachable.
* The network between the source and destination is disconnected, or the ICMP Echo Reply messages sent by the destination do not reach the source before the timer expires.

A ping operation on the source is assigned a process ID, which is used as an identifier for ICMP Echo Request messages. As a result, the source can still successfully distinguish ICMP Echo Reply messages, even if multiple ping operations are performed concurrently.


#### Application Scenarios of Ping

The ping function can be used to detect the reachability and response performance of different networks. The following table describes its application scenarios.

**Table 1** Application scenarios of ping
| Network Type | Detection Item | Description |
| --- | --- | --- |
| IP network | IPv4 or IPv6 network connectivity | Detect the connectivity between two devices on an IPv4 or IPv6 network. |
| Reachability of a Layer 3 trunk member interface | Detect the reachability of a specified Layer 3 trunk member interface on an IP network. |
| TCP connectivity on an IPv4 network | Detect the reachability of a TCP server on an IPv4 network and the time required for setting up a TCP connection with the TCP server. |
| VXLAN network | VXLAN or IPv6 VXLAN network connectivity | Detect the connectivity between virtual tunnel end points (VTEPs) of a VXLAN tunnel on a VXLAN or IPv6 VXLAN network. |