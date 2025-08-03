Defense Against UDP Flood Attacks
=================================

Defense Against UDP Flood Attacks

#### Security Policy

Packets sent by UDP ports 7, 13, and 19 are considered attack packets and discarded.

You can enable defense against UDP flood attacks.


#### Attack Methods

* Fraggle attacks
  
  During a Fraggle attack, attackers use UDP port 7 (UDP echo request) to attack network devices. The service of port 7 is basically the same as that of ICMP echo, that is, port 7 sends back all the received packet payloads without making any modifications to test the network connection between the source IP address and the destination IP address. Fraggle attacks are similar to Smurf attacks. During a Fraggle attack, the IP address of the victim is used as the source IP address and a broadcast address is used as the destination IP address. The destination port ID is 7, and the source port ID may be 7 or another ID. If the UDP echo service is enabled on a lot of hosts on this broadcast network, the victim will receive a lot of response packets. In this way, the victim is attacked.
* UDP diagnosis port attacks
  
  Packets are sent to a diagnosis port (7-echo, 13-daytime, or 19-Chargen) at random. If a great number of packets are sent simultaneously, UDP packets flood occurs, affecting the normal running of network devices. A lot of vendors enable small servers by default for network diagnosis or device management, which results in potential attacks. For example, during a Pepsi attack, attackers send a huge number of packets to a diagnosis port of a device, causing DoS of the device.

#### Configuration and Maintenance Methods

* Enable or disable the defense against UDP Flood attacks.
  
  [**udp-packet-defend enable**](cmdqueryname=udp-packet-defend+enable)
  
  [**undo udp-packet-defend enable**](cmdqueryname=undo+udp-packet-defend+enable)
  
  [**ipv6-udp-packet-defend enable**](cmdqueryname=ipv6-udp-packet-defend+enable)
  
  [**undo ipv6-udp-packet-defend enable**](cmdqueryname=undo+ipv6-udp-packet-defend+enable)
* Delete statistics about UDP flood attacks on a specific or all interface boards.
  
  [**reset cpu-defend tcpip-defend statistics**](cmdqueryname=reset+cpu-defend+tcpip-defend+statistics) [ **slot** *slot-number* ]
  
  [**reset cpu-defend tcpip-defend-v6 statistics**](cmdqueryname=reset+cpu-defend+tcpip-defend-v6+statistics) [ **slot** *slot-number* ]

#### Verifying the Security Hardening Result

Check statistics about UDP flood attacks on all interface boards or a specified interface board.

[**display cpu-defend tcpip-defend statistics**](cmdqueryname=display+cpu-defend+tcpip-defend+statistics) [ **slot** *slot-number* ]

[**display cpu-defend tcpip-defend-v6 statistics**](cmdqueryname=display+cpu-defend+tcpip-defend-v6+statistics) [ **slot** *slot-number* ]


#### Configuration and Maintenance Suggestions

None