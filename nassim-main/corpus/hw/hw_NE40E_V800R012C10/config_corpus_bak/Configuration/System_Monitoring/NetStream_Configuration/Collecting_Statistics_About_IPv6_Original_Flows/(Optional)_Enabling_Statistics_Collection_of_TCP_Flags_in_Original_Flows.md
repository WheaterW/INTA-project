(Optional) Enabling Statistics Collection of TCP Flags in Original Flows
========================================================================

There are six flag bits (URG, ACK, PSH, RST, SYN, and FIN) in a TCP packet header. The flag bits, together with the destination IP address, source IP address, destination port number, and source port number of a TCP packet, identify the function and status of the TCP packet on a TCP connection. TCP flags can be extracted from packets. Their statistics can be collected and sent to the NMS. The NMS checks the traffic volume of each flag and determines whether the network is attacked by TCP packets.

#### Context

Perform the following steps on the Router on which TCP flag statistics are to be collected.

By enabling statistics collection of TCP flags, you can extract the TCP-flag information from network packets and send it to the NMS. The NMS can determine whether there are flood attacks to the network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 netstream tcp-flag enable**](cmdqueryname=ipv6+netstream+tcp-flag+enable)
   
   
   
   Statistics collection of TCP flags in original flows is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.