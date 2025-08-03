Understanding ICMP
==================

Understanding ICMP

#### ICMP Message Classification

ICMP is an error-reporting mechanism that is often used by IP or an upper-layer protocol (TCP or UDP). An ICMP message is encapsulated as a part of an IP datagram and transmitted through the Internet.

An IP datagram contains information about only the source and destination, and can record information about all nodes along the path it traverses only if its Record Route option is set. Therefore, a device that detects an error reports it to only the source and not to intermediate devices.

When an error occurs during IP datagram forwarding, ICMP reports the error to the source of the IP datagram, but does not rectify the error or notify the intermediate devices of it. A majority of errors occur on the source. If an error occurs on an intermediate device, however, the source cannot locate the device on which the error occurs even after receiving the error report.

ICMP uses error or query messages to report errors or information generated during packet processing. [Figure 1](#EN-US_CONCEPT_0000001130623778__fig11536617919) shows the ICMP message format.

**Figure 1** ICMP message format  
![](figure/en-us_image_0000001176663341.png)  

An ICMP message consists of the following fields:

* Type: message type.
* Code: specific message type.
* Checksum: checksum of an ICMP message.

Maintenance personnel can determine fault locations based on ICMP message types. [Table 1](#EN-US_CONCEPT_0000001130623778__table7153062095) describes ICMP message classification.

**Table 1** ICMP message classification
| Type | Code | Description | Query/Error |
| --- | --- | --- | --- |
| 0 â Echo Reply | 0 | Echo reply | Query |
| 3 â Destination Unreachable | 0 | Destination network unreachable | Error |
| 1 | Destination host unreachable | Error |
| 2 | Destination protocol unreachable | Error |
| 3 | Destination port unreachable | Error |
| 4 | Fragmentation required, and DF flag set | Error |
| 5 | Source route failed | Error |
| 6 | Destination network unknown | Error |
| 7 | Destination host unknown | Error |
| 8 | Source host isolated | Error |
| 9 | Network administratively prohibited | Error |
| 10 | Host administratively prohibited | Error |
| 11 | Network unreachable for ToS | Error |
| 12 | Host unreachable for ToS | Error |
| 13 | Communication administratively prohibited | Error |
| 14 | Host precedence violation | Error |
| 15 | Precedence cutoff in effect | Error |
| 4 - Source Quench | 0 | Source quench message | Error |
| 5 â Redirect | 0 | Redirect datagram for the network | Error |
| 1 | Redirect datagram for the host | Error |
| 2 | Redirect datagram for the ToS and network | Error |
| 3 | Redirect datagram for the ToS and host | Error |
| 8 â Echo Request | 0 | Echo request | Query |
| 9 â Router Advertisement | 0 | Router advertisement | Query |
| 10 â Router Solicitation | 0 | Router discovery/selection/solicitation | Query |
| 11 â Time Exceeded | 0 | TTL expired in transit | Error |
| 1 | Fragment reassembly time exceeded | Error |
| 12 â Parameter Problem | 0 | Pointer indicates the error | Error |
| 1 | Missing a required option | Error |
| 2 | Bad length | Error |
| 13 â Timestamp | 0 | Timestamp | Query |
| 14 â Timestamp Reply | 0 | Timestamp reply | Query |
| 15 â Information Request | 0 | Information request | Query |
| 16 â Information Reply | 0 | Information reply | Query |



#### ICMP Security

Under normal circumstances, a device can send and receive ICMP messages properly. However, when network traffic is heavy, host unreachable or port unreachable events frequently occur, leading to a surge in ICMP messages. The increase in the volume of messages not only burdens the network, but also degrades the performance of devices. Network attackers perform scans by using various types of packets, and devices reply to these packets with ICMP messages. Network attackers then obtain network information from these received ICMP messages and launch attacks on the network. In addition, when the device is busy sending ICMP messages, transmission of normal service packets is affected.

To reduce the device's pressure in processing ICMP messages and prevent ICMP message attacks, the device can be configured to:

* Control the forwarding of ICMP messages. The device can control the sending and receiving of ICMP messages to control ICMP traffic on the network.
* Discard ICMP messages of a certain type. For example, the device can be configured to discard those with TTL of 1 or 0, or those carrying route options.
* Limit the rate of ICMP messages. If the number of ICMP messages sent to the CPU exceeds the threshold, the device discards excess ICMP messages.