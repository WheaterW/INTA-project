Displaying the Outbound Interface of the Traffic with a Specified 5-Tuple
=========================================================================

Displaying the Outbound Interface of the Traffic with a Specified 5-Tuple

#### Context

The 5-tuple information of packets includes the source IP address, destination IP address, source port number, destination port number, and protocol type. Traffic transmitted on interfaces often carries different 5-tuple information, source MAC addresses, and destination MAC addresses. If the outbound interface of packets is an Eth-Trunk interface or packets have multiple ECMP next hops, you can view the outbound interface of packets with the specified 5-tuple, source MAC address, and destination MAC address to facilitate fault locating and identify traffic forwarding paths.

![](public_sys-resources/note_3.0-en-us.png) 

This configuration is not supported on the CE6885-LL (low latency mode).



#### Procedure

1. Check the outbound interface of packets with the specified 5-tuple, source MAC address, and destination MAC address.
   
   
   ```
   [display port forwarding-path](cmdqueryname=display+port+forwarding-path) { src-ip src-ip-data [ ip-mask-len | source-ip-mask ] | dst-ip dst-ip-data [ ip-mask-len | dst-ip-mask ] | src-mac src-mac-data | dst-mac dst-mac-data | protocol { protocol-number | gre | icmp | igmp | ip | ipinip | ospf | tcp [ l4-src-port src-port-data | l4-dst-port dst-port-data ] * | udp [ l4-src-port src-port-data | l4-dst-port dst-port-data ] * } } *
   ```