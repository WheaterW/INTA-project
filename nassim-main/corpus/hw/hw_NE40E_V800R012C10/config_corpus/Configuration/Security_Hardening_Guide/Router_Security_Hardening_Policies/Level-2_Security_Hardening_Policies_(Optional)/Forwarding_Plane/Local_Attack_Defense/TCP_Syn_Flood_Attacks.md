TCP Syn Flood Attacks
=====================

TCP Syn Flood Attacks

#### Security Policy

The TCP Syn Flood attacks are common and effective. The TCP Syn Flood attack is a Denial of Service (DoS) attack, which exploits the TCP connection establishment procedure.

Huawei devices limit the rate of TCP SYN packets to prevent exhaustion of system resources if a TCP Syn Flood attack occurs.


#### Attack Methods

During the three handshake processes of a TCP connection, when the server receives the initial SYN packet from the client, it sends back a SYN-ACK packet to the client and creates an input interface in memory. While the server is waiting for the final ACK packet from the client, the connection is in half-connected mode. If the server fails to receive the ACK packet, it resends a SYN-ACK packet to the client. If the server sends the SYN-ACK packet multiple times and does not receive any ACK packet from the client, it ends the session and refreshes the session in memory. The time between sending the first SYN-ACK packet and the end of the session is about 30s.

During this time period, the attacker may send thousands of SYN packets to the open port without replying to the SYN-ACK packet sent by the server. The server is quickly overloaded and cannot support new connection requests. Therefore, the server disconnects all the present connections.

The attacker seldom receives SYN-ACK packets. Therefore, they can forge a different source address of the SYN packet to make locating the actual address of attacks more difficult.

The SYN-ACK packet is not sent to the attacker, which conserves bandwidth for the attacker.


#### Configuration and Maintenance Methods

* Enable or disable the defense against TCP Syn Flood attacks.
  
  [**tcpsyn-flood enable**](cmdqueryname=tcpsyn-flood+enable)
  
  [**undo tcpsyn-flood enable**](cmdqueryname=undo+tcpsyn-flood+enable)
  
  [**ipv6-tcpsyn-flood enable**](cmdqueryname=ipv6-tcpsyn-flood+enable)
  
  [**undo ipv6-tcpsyn-flood enable**](cmdqueryname=undo+ipv6-tcpsyn-flood+enable)
  
  **car tcpsyn cir 1000 cbs 10000**
  
  **undo car tcpsyn**
* Delete statistics about TCP Syn Flood attacks on a specific or all interface boards.
  
  **reset cpu-defend car index 48 statistics [ slot** *slot-number* **]**

#### Verifying the Security Hardening Result

Check statistics about TCP Syn Flood attacks on all interface boards or a specified interface board.

**display cpu-defend car index 48 statistics [ slot** *slot-number* **]**


#### Configuration and Maintenance Suggestions

None