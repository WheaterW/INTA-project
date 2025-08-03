Understanding Defense Against Malformed Packet Attacks
======================================================

A malformed packet attack is a type of attack in which malformed IP packets are sent to a target device, causing the device to encounter an error or even crash when processing such packets and ultimately impacting services running on the device. Defense against malformed packet attacks enables a device to detect and discard malformed packets in real time to protect the device.

Malformed packet attacks are classified into the following types.

#### Flood Attack from IP Null Payload Packets

An IP null payload packet has only a 20-byte IP header, and no data section. Attackers often construct a large number of packets with only IP headers, known as IP null payload packets, which constitute a flood attack. Processing such packets causes devices to encounter an error or even crash, impacting services.

With defense against malformed packet attacks enabled, the device directly discards the received IP null payload packets, thereby preventing service interruption.


#### Attack from IGMP Null Payload Packets

A normal IGMP packet consists of a 20-byte IP header and an 8-byte data part, equating to a total length of 28 bytes. An IGMP null payload packet, on the other hand, consists of less than 28 bytes. Processing IGMP null payload packets causes devices to encounter an error or even crash, impacting services.

With defense against malformed packet attacks enabled, the device directly discards the received IGMP null payload packets, thereby preventing service interruption.


#### LAND Attack

A Local Area Network Denial (LAND) attacker targets the defects in the three-way handshake mechanism of TCP, sending a SYN packet in which both the source and destination addresses are the target host's address and the source and destination ports are the same. After receiving the SYN packet, the target host creates a null TCP connection by using its own address as both the source and destination addresses, and retains this connection until it times out. The target host will create many null TCP connections after receiving a large number of such SYN packets, wasting network resources or even crashing the system.

With defense against malformed packet attacks enabled, the device checks source and destination addresses or ports in TCP SYN packets, and considers TCP SYN packets with the same source and destination addresses or ports as malformed packets and discards them.


#### Smurf Attack

An attacker sends an ICMP Request packet with a source address as the target host's address and a destination address as the broadcast address of the target network. As such, all hosts on the target network receive the ICMP Request packet, after which they send ICMP Reply packets to the target host. This inevitably leads to the target host receiving an excessive number of packets, consuming excessive resources crashing the system or network.

With defense against malformed packet attacks enabled, the device checks whether the destination addresses in ICMP Request packets are the broadcast or subnet broadcast addresses, discarding them if so.


#### Attack from Packets with Invalid TCP Flag Bits

A TCP packet contains six flag bits: URG, ACK, PSH, RST, SYN, and FIN. Different systems respond differently to the combination of these flag bits.

* If the six flag bits are all 1s, the attack is a Christmas tree attack. A device subject to a Christmas tree attack may crash.
* An attacker sends a TCP packet in which SYN and FIN are 1 to a target host. If the receiving interface is disabled, the receiver replies with an RST | ACK message. If the receiving interface is enabled, the receiver replies with an SYN | ACK message. Such an attack is used to detect whether a host is online or offline and whether an interface is enabled or disabled.
* An attacker sends a TCP packet in which the six flag bits are all 0s to a target host. If the receiving interface is disabled, the receiver replies with an RST | ACK message, which can be used by the attacker to detect whether the host is online or offline. If the receiving interface is enabled, the target host does not respond if running Linux or UNIX but replies with an RST | ACK message if running Windows. This attack is used to detect the type of operating system on the target host.

With defense against malformed packet attacks enabled, the device checks each flag bit in TCP packets to prevent attacks from packets with invalid TCP flag bits. If any of the following conditions is met, the device discards the TCP packets:

* The six flag bits are all 1s.
* Both SYN and FIN are 1.
* The six flag bits are all 0s.