Understanding ICMPv6
====================

Understanding ICMPv6

#### Definition

Internet Control Message Protocol for IPv6 (ICMPv6) is a basic IPv6 protocol that uses error or informational messages to report errors or information generated during packet processing.


#### ICMPv6 Message Classification

[Figure 1](#EN-US_CONCEPT_0000001176661701__fig16923334124214) shows the ICMPv6 message format.

**Figure 1** ICMPv6 message format  
![](figure/en-us_image_0000001130781960.png)  

An ICMPv6 message consists of the following fields:

* Type: message type. Values from 0 to 127 indicate an error message, and values from 128 to 255 indicate an informational message.
* Code: specific message type.
* Checksum: checksum of an ICMPv6 message.

Maintenance personnel can determine fault locations based on ICMPv6 message types, which are classified as follows:

**ICMPv6 error messages**

Destination Unreachable message (Type = 1). When an IPv6 node forwards an IPv6 packet and finds that the destination address of the packet is unreachable, it sends an ICMPv6 Destination Unreachable message to the source node of the packet. The code carried in the message identifies the cause of the error. Destination Unreachable messages are further classified into the following types:

* No route to destination (Code = 0)
* Communication with destination administratively prohibited (Code = 1)
* Address unreachable (Code = 3)
* Port unreachable (Code = 4)

Packet Too Big message (Type = 2, Code = 0). When an IPv6 node forwards IPv6 packets and finds that the size of the packets exceeds the outbound interface path MTU, it sends an ICMPv6 Packet Too Big message to the source node of the packets. The message carries the outbound interface path MTU. Path MTU discovery is implemented based on Packet Too Big messages.

Time Exceeded message (Type = 3). When a device receives a packet with a hop limit of 0 or reduces the hop limit to 0 during IPv6 packet transmission, it sends an ICMPv6 Time Exceeded message to the source node of the packets. An ICMPv6 Time Exceeded message is also generated if the fragment reassembly time is longer than the specified period. Time Exceeded messages are further classified into the following types:

* Hop limit exceeded in transit (Code = 0)
* Fragment reassembly time exceeded (Code = 1)

Parameter Problem message (Type = 4). A destination node checks the validity of an IPv6 packet it receives. If the node detects any of the following errors, it sends an ICMPv6 Parameter Problem message to the source node of the packet:

* Erroneous header field encountered (Code = 0)
* Unrecognized Next Header type encountered (Code = 1)
* Unrecognized IPv6 option encountered (Code = 2)

**ICMPv6 informational messages**

ICMPv6 informational messages are classified as either Echo Request (Type = 128, Code = 0) or Echo Reply (Type = 129, Code = 0). ICMPv6 informational messages can be used for network fault diagnosis, path MTU discovery, and ND. After receiving an Echo Request message during the interworking detection between two nodes, the destination node sends an Echo Reply message to the source node.

**Other ICMPv6 messages**

In addition to basic IPv4 ICMP functions, ICMPv6 supports ND.

ND defines the following ICMPv6 messages:

* Router Solicitation message (Type = 133, Code = 0)
* Router Advertisement message (Type = 134, Code = 0)
* Neighbor Solicitation message (Type = 135, Code = 0)
* Neighbor Advertisement message (Type = 136, Code = 0)
* Redirect message (Type = 137, Code = 0)


#### ICMPv6 Security

Under normal circumstances, a device can send and receive ICMPv6 messages properly. However, when network traffic is heavy, host unreachable or port unreachable events frequently occur, leading to a surge in ICMPv6 messages, which burdens the network and degrades device performance. Network attackers perform scans by using various types of packets, and devices reply to these packets with ICMPv6 messages. Network attackers then obtain network information from these received ICMPv6 messages and launch attacks on the network. In addition, when the device is busy sending ICMPv6 messages, transmission of normal service packets is affected.

To reduce the device's pressure in processing ICMPv6 messages and prevent ICMPv6 message attacks, the device can be configured to:

* Control the forwarding of ICMPv6 messages. The device can control the sending and receiving of ICMPv6 messages to control ICMPv6 traffic on the network.
* Limit the rate of ICMPv6 messages. If the number of ICMPv6 messages sent to the CPU exceeds the threshold, the device discards excess ICMPv6 messages.