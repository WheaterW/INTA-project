(Optional) Enabling Statistics Collection of TCP Flags
======================================================

There are six flag bits (URG, ACK, PSH, RST, SYN, and FIN) in a TCP packet header. The flag bits, together with the destination IP address, source IP address, destination port number, and source port number of a TCP packet, identify the function and status of the TCP packet on a TCP connection. TCP flags can be extracted from packets. Their statistics can be collected and sent to the NMS. The NMS checks the traffic volume of each flag and determines whether the network is attacked by TCP packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip netstream tcp-flag enable**](cmdqueryname=ip+netstream+tcp-flag+enable)
   
   
   
   Statistics collection of TCP flags is enabled.
   
   
   
   An original flow for each flag value is created. If statistics collection for TCP flags is enabled, the number of original flows will greatly increase.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.