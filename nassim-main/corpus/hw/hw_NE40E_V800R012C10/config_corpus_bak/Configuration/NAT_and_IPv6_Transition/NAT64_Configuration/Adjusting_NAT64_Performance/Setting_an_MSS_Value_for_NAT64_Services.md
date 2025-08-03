Setting an MSS Value for NAT64 Services
=======================================

The maximum segment size (MSS) value defined in TCP specifies the maximum length of a TCP packet to be sent without fragmentation. Two devices exchange SYN packets to negotiate the MSS value for a TCP connection to be established.

#### Context

If the size of packets for NAT64 processing is larger than a link MTU, IPv6 packets are fragmented. You can reduce the MSS value in TCP, which prevents a NAT64 board from fragmenting packets and helps improve NAT64 efficiency.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* **id** *id*
   
   
   
   The NAT64 instance view is displayed.
3. Run [**nat64 tcp adjust-mss**](cmdqueryname=nat64+tcp+adjust-mss) *mss-value*
   
   
   
   An MSS value is set in TCP SYN and SYN ACK packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.