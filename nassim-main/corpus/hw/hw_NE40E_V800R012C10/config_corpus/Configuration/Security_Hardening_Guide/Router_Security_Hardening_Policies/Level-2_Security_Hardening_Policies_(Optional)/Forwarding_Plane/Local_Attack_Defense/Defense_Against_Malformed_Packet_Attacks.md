Defense Against Malformed Packet Attacks
========================================

Defense Against Malformed Packet Attacks

#### Security Policy

A malformed packet attack sends malformed IP packets to a target. The target may encounter errors or crash when handling these packets.

Malformed packet attacks are as follows:

* Flood attacks using IP packets with null payload
* Attacks using IGMP packets with null payload
* LAND attacks
* Smurf attacks
* TCP flag invalid attacks

#### Attack Methods

* Flood attacks using IP packets with null payload
  
  Flood attackers send massive IP packets without any upper layer data. These massive IP packets form flood attacks. The IP packets without upper layer data are useless, and therefore must be discarded.
* Attacks using IGMP packets with null payload
  
  An IGMP packet consists of a 20-byte IP packet header and an 8-byte IGMP body. If an IGMP packet is shorter than 28 bytes, the device considers it malformed and discards it.
* LAND attacks
  
  LAND attacks were invented by the Hacker organization RootShell and issued on Nov 20, 1997. LAND attacks use the design flaws of the TCP three-way handshake mechanism so that the target hosts that have received connection requests repeatedly reply to themselves, exhausting their resources and paralyzing the network. A LAND attack sends a spoofed SYN packet with the source and destination IP addresses set to address the same device and the source and destination ports set to the same port. After a device receives a SYN packet, it sends to its IP address a SYN+ACK packet. Consequently, it replies to itself a SYN+ACK packet and creates a null connection that persists until expiration.
  
  **Figure 1** LAND attack  
  ![](figure/en-us_image_0000001134623516.png)
  
  If the destination host receives a SYN+ACK packet, it interprets the packet as a connection request (ignoring the ACK packet) and replies with a SYN+ACK packet. The ACK packet is used to acknowledge the last SYN packet. Consequently, the destination host determines that it is receiving a connection request again. The cycle continues.
  
  Even though the destination host does not consider the SYN+ACK packet as a connection request, it considers the SYN+ACK packet as a half connection as a result of sending of the SYN+ACK packet. If there are excessive packets, it becomes a SYN flood attack. As a result, an excess of half connections is set up, and the system fails.
  
  The device considers LAND attacks malformed packet attacks. If a received TCP SYN packet carries the same source and destination IP addresses, the device considers it an attack packet and discards it.

* Smurf attacks
  
  The principle of a Smurf attack is that an attacker sends ICMP Echo Request packets with the destination IP address set to a broadcast IP address and the source IP address set to the target's IP address. All the hosts on the network send reply with packets to the target. The target receives too many packets, leading to high CPU usage. The target interprets packets with their destination set to a broadcast address or a subnet broadcast address as malformed and discards them to defend against Smurf attacks.
* TCP flag invalid attacks
  
  A TCP packet contains six flag bits, including URG, ACK, PSH, RST, SYN, and FIN. Replies to combinations of these flag bits vary according t systems.
  
  If the six flag bits are all 1s, the attack is a Christmas tree attack.
  
  If the six flag bits are all 0s and the TCP port is disabled, the receiver responds with an RST|ACK packet. If the six flag bits are all 0s and the TCP port is enabled, a device running Linux or UNIX does not respond, whereas, but a device running Windows responds with an RST|ACK packet. This helps identify the operating system.
  
  If ACK is used with another flag bit (except RST) as a combination, the receiver that does not send any request, but still sends an RST response packet, regardless of whether the TCP port is enabled. This helps determine whether a host exists.
  
  The reception of an SYN+FIN+URG packet triggers the receiver to respond with an RST+ACK packet, regardless of whether the TCP port is enabled. This helps determine whether a host exists.
  
  Upon receipt of an SYN, SYN+FIN, SYN+PUSH, SYN+FIN+PUSH, SYN+URG, SYN+URG+PUSH, or SYN+FIN+URG+PUSH packet, the receiver responds with an RST+ACK packet if the TCP port is disabled or to respond with an SYN+ACK packet if the TCP port is enabled. This assists in host detection and port detection.
  
  Upon receipt of a FIN, URG, PUSH, URG+FIN, URG+PUSH, FIN+PUSH, or URG+FIN+PUSH packet, the receiver responds with an RST+ACK reply if the TCP port is disabled. If the six flag bits are all 0s and the TCP port is enabled, a device running Linux or UNIX does not respond, whereas, but a device running Windows responds with an RST|ACK packet. This helps identify the operating system.
  
  The device checks the flag bit in each TCP packet and discards packets the packet if the packet meets any of the following conditions:
  
  + The six flag bits are all 1s.
  + The six flag bits are all 0s.
  + Both SYN and FIN are 1s.

#### Configuration and Maintenance Methods

* Enable or disable the defense against malformed packet attacks.
  
  [**abnormal-packet-defend enable**](cmdqueryname=abnormal-packet-defend+enable)
  
  [**undo abnormal-packet-defend enable**](cmdqueryname=undo+abnormal-packet-defend+enable)
  
  [**ipv6-abnormal-packet-defend enable**](cmdqueryname=ipv6-abnormal-packet-defend+enable)
  
  [**undo ipv6-abnormal-packet-defend enable**](cmdqueryname=undo+ipv6-abnormal-packet-defend+enable)
* Delete statistics about malformed packet attacks on a specific or all interface boards.
  
  [**reset cpu-defend tcpip-defend statistics**](cmdqueryname=reset+cpu-defend+tcpip-defend+statistics) [ **slot** *slot-number* ]
  
  [**reset cpu-defend tcpip-defend-v6 statistics**](cmdqueryname=reset+cpu-defend+tcpip-defend-v6+statistics) [ **slot** *slot-number* ]

#### Verifying the Security Hardening Result

Check statistics about malformed packet attacks on all interface boards or a specified interface board.

[**display cpu-defend tcpip-defend statistics**](cmdqueryname=display+cpu-defend+tcpip-defend+statistics) [ **slot** *slot-number* ]

[**display cpu-defend tcpip-defend-v6 statistics**](cmdqueryname=display+cpu-defend+tcpip-defend-v6+statistics) [ **slot** *slot-number* ]


#### Configuration and Maintenance Suggestions

None