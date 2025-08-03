Defense Against ICMP Flood Attacks
==================================

Defense Against ICMP Flood Attacks

#### Security Policy

The rate at which ICMP messages are sent is set on a board, which helps prevent ICMP flood attacks on boards. Defense against ICMP Flood attacks can be enabled based on boards.


#### Attack Methods

During an ICMP Flood attack, ICMP packets are sent at a high rate. When a program sends more than 1000 packets per second, the program is considered a flood generator. A large number of ICMP Echo Request packets are sent to the target. The target host has to return a large number of ICMP Echo Reply or ICMP unreachable packets. After the attacker forges a source IP address, the target host sends back a large number of ICMP packets to the false address in vain. This consumes the host's system resources, and eventually the server may stop responding. The attack may also originate from other types of ICMP packets.


#### Configuration and Maintenance Methods

* Enable or disable defense against ICMP Flood attacks.
  
  [**car icmp cir 100 cbs 3000**](cmdqueryname=car+icmp+cir+100+cbs+3000)
  
  [**undo car icmp**](cmdqueryname=undo+car+icmp)
* Delete statistics about ICMP flood attacks on all interface boards or a specified interface board.
  
  [**reset cpu-defend car protocol icmp statistics**](cmdqueryname=reset+cpu-defend+car+protocol++icmp+statistics)

#### Verifying the Security Hardening Result

Check statistics about ICMP flood attacks on all interface boards or a specified interface board.

[**display cpu-defend car protocol icmp statistics**](cmdqueryname=display+cpu-defend+car+protocol++icmp+statistics)


#### Configuration and Maintenance Suggestions

None