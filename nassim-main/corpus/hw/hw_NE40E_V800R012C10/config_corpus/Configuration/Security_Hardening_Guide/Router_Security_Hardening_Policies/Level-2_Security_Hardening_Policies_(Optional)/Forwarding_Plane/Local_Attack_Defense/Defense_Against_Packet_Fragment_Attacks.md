Defense Against Packet Fragment Attacks
=======================================

Defense Against Packet Fragment Attacks

#### Security Policy

Teardrop attacks target fragments that are not properly reassembled. To defend a system against teardrop attacks, the system must reassemble packet fragments properly and discard packets that are not properly reassembled. For repeated packet fragment attacks, no effective measures are available. An interface board may fail to receive all fragments due to trunk and load sharing on an IP network. Therefore, packet fragments cannot be reassembled on an interface board. If packet fragments are reassembled on a main control board, the CPU of the main control board and inter-board communication resources are consumed. To defend the system against repeated packet fragment attacks, the forwarding engine sets a committed access rate (CAR) for packet fragments separately on an interface board to prevent great numbers of packet fragments from attacking the CPU. The CAR parameter can be configured.


#### Attack Methods

Packet fragment attacks are classified into the following categories:

* Excessive fragments
  
  Attackers produce a great number of fragments with a minimum size of 8 bytes. Normally, the IP header contains 20 bytes, and the maximum IP payload is 65515 bytes. If the data is fragmented and each IP payload contains 8 bytes, a total of 8189. 375 fragments are obtained. (If a packet is divided into 8189 fragments, the IP payload does not reach 65515 bytes. If a packet is divided into 8190 fragments, the IP payload exceeds 65515 bytes.) A large number of small fragments are often malicious. If these small fragments are sent to a Router, the Router attempts to reassemble these fragments, which consumes a large number of CPU resources.
* Teardrop attacks
  
  Teardrop attacks are the most famous IP fragmentation attacks. They are initiated by producing IP fragmentation errors in UDP packets, causing the second fragment to be contained in the first fragment. In the first fragment, the IP payload is 36 bytes, the total length is 56 bytes (correct), the protocol is UDP, and the UDP checksum is 0 (no CRC). In the second fragment, the IP payload is 4 bytes, the total length is 24 bytes (correct), the protocol is UDP, and the offset is 24 (3 x 8), which is incorrect. The correct offset is 36.
* Syndrop attacks
  
  The principle is similar to that of a teardrop attack, except that the TCP protocol is used, the flag is SYN, and a packet contains padding. In the first fragment, the IP payload is 28 bytes (byte 0 to byte 27, including the TCP header) and the IP header is 20 bytes. In the second fragment, the offset is 24, the total length of the payload is 4 bytes (byte 24 to byte 27), and the IP header is 20 bytes.
* Nesta attacks
  
  A packet is divided into three fragments. In the first fragment, the IP payload is 18 bytes (byte 0 to byte 17), the protocol is UDP, and the checksum is 0. In the second fragment, the offset is 6 x 8 = 48, the IP payload is 116 bytes. If there is no subsequent fragment, the second fragment is the end fragment. In the third fragment, the offset is 0, the **more frag** value is 1 (indicating there are subsequent fragments), the size of the IP option is 40 bytes (all EOL), and the IP payload is 224 bytes.
* FAWX attacks
  
  During a FAWX attack, incorrectly fragmented IGMP packets are sent. Two IGMP packet fragments are sent. The first fragment is 9 bytes. In the second fragment, the offset is 8, the IP payload is 16 bytes, and there is no end fragment.
* BONK attacks
  
  BONK attacks are similar to NewTear attacks, except that the IP payload of the first fragment is 36 bytes and the UDP checksum is 0; the offset of the second fragment is 32; the length is 4 bytes.
* Dead ping attacks
  
  The total length of an ICMP Echo Request exceeds 65535 bytes, causing the protocol stack to collapse. During this type of attack, IP packets are fragmented to cause the total length of the IP payload and the IP header exceed 65535 bytes.
* Jolt attacks
  
  Jolt attacks are similar to Dead Ping attacks. A packet contains a total of 173 fragments. The IP payload of each fragment is 380 bytes. Therefore, the total length is 65760 bytes (173 x 380 + 20), which far exceed 65535 bytes.
* Repeated packet fragment attacks
  
  During this type of attack, the same fragment is sent more than twice. This can bring about two different results. In the first case, the first and second fragments have the same sequence number because both may be retransmitted. In the second case, the first and second fragments have different sequence numbers, and the system needs to determine which fragment is to be reserved and which fragment is to be discarded, or whether both fragments are to be discarded.
* NewTear attacks
  
  NewTear attacks are similar to Syndrop attacks in terms of fragments, except that the protocol is UDP, the IP payload of the first fragment is 28 bytes (byte 0 to byte 27; including the UDP header; UDP checksum is 0), and the offset of the second fragment is 24. The total payload length is 4 bytes (byte 24 to byte 27).
* Rose attacks
  
  The IP protocol can be UDP or TCP.
  
  + TCP: There are a total of two fragments. The IP payload length of the first fragment is 48 bytes. The IP payload length of the second fragment is 32 bytes, but the offset is 65408, and the **more frag** value is 0 (indicating there is no subsequent fragment).
  + UDP: There are a total of two fragments. The IP payload length of the first fragment is 40 bytes. The IP payload length of the second fragment is 32 bytes, but the offset is 65408, and the **more frag** value is 0 (indicating there is no subsequent fragment).

#### Configuration and Maintenance Methods

* Enable or disable defense against packet fragment attacks.
  
  [**fragment-flood enable**](cmdqueryname=fragment-flood+enable)
  
  [**undo fragment-flood enable**](cmdqueryname=undo+fragment-flood+enable)
* Delete statistics about packet fragment attacks on all the interface boards or a specified interface board.
  
  [**reset cpu-defend car fragment statistics**](cmdqueryname=reset+cpu-defend+car+fragment+statistics)

#### Verifying the Security Hardening Result

* Check statistics about packet fragment attacks on all the interface boards or a specified interface board.
  
  [**display cpu-defend car fragment statistics**](cmdqueryname=display+cpu-defend+car+fragment+statistics)
* Check detailed information about attack source tracing.
  
  [**display attack-source-trace verbose**](cmdqueryname=display+attack-source-trace+verbose)

#### Configuration and Maintenance Suggestions

None