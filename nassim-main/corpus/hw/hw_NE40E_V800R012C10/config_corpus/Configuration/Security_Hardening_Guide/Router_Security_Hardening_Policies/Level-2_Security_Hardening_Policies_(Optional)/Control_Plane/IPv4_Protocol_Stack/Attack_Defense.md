Attack Defense
==============

Attack Defense

#### Security Policy

The ever-increasing network attacks are having greater impact on the live network due to inherent weaknesses of communication protocols and network deployment issues. In particular, the attacks on network devices may lead to device failures or network breakdown.

Attack defense provides various ways of protecting packets based on the packet format and content. For example, attack defense allows routers to discard malformed packets and perform rate limit in response to flood attacks.

That is, attack defense discards attack packets sent to the local host or limits the rate of sending them to protect the local host. In this way, services can run normally.


#### Attack Methods

* Malformed packet attacks
  
  1. Flood attacks by using null payload IP packets
     
     Flood attackers send massive IP packets without any upper layer data. These massive IP packets form flood attacks. A packet with the IP packet header of only 20 bytes is considered a null payload IP packet and needs to be discarded.
  2. Attacks by using null payload IGMP packets
     
     An IGMP packet consists of a 20-byte IP packet header and an 8-byte IGMP data field. If an IGMP packet is shorter than 28 bytes, routers consider it abnormal and discard it directly.
  3. LAND attacks
     
     LAND attacks were invented by the Hacker organization RootShell and issued on Nov 20, 1997.
     
     LAND attacks use the design flaws of the TCP three-way handshake mechanism so that the target hosts that have received connection requests repeatedly reply to themselves, exhausting their resources and paralyzing the network. A LAND attack sends a spoofed SYN packet with the source and destination IP addresses set to address the same device and the source and destination ports set to the same port. After a device receives a SYN packet, it sends to its IP address a SYN+ACK packet. Consequently, it replies to itself a SYN+ACK packet and creates a null connection that persists until expiration.
  4. Smurf attacks
     
     A Smurf attack sends ICMP echo request packets that carry the broadcast address as the destination IP address and the target host's IP address as the source IP address. All the hosts on the network send reply with packets to the target. The target receives too many packets, leading to high CPU usage.
     
     If routers receive the ICMP echo request packets with the broadcast address or the subnet broadcast address as its destination address, the routers consider the packets abnormal and thus discard the packets.
* UDP flood attacks
  
  1. Fraggle attacks
     
     Fraggle attacks use UDP port 7 (UDP Echo Request). Port 7, similar with ICMP echo, sends back the payload of the received packet and tests the network conditions between the source and the destination.
     
     Similar with Smurf attacks, Fraggle hackers force the source address as the victim's address and the destination address as the broadcast address, and use port 7. If multiple hosts use UDP echo services on the broadcast network, the victim receives excessive response packets. As a result, the system becomes busy and the Fraggle attack succeeds. Routers consider packets from UDP port 7 attack packets and thus discard them directly.
  2. UDP diagnosis port attacks
     
     If the hacker sends packets to the UDP diagnosis port (7-echo, 13-daytime, and 19-Chargen) in a huge number at the same time, the flood is caused and the network devices cannot work normally. Routers consider packets from UDP ports 7, 13, and 19 attack packets and thus discard them directly.

#### Configuration and Maintenance Methods

None


#### Verifying the Security Hardening Result

None


#### Configuration and Maintenance Suggestions

None