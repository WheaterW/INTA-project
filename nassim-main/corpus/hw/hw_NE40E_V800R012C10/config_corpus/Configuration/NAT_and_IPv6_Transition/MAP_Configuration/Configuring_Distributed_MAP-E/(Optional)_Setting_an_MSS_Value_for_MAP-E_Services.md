(Optional) Setting an MSS Value for MAP-E Services
==================================================

The maximum segment size (MSS) value defined in TCP specifies the maximum length of a TCP packet to be sent without fragmentation. Two devices exchange SYN packets to negotiate the MSS value for a TCP connection to be established. If the size of packets for MAP processing is larger than a link MTU, the packets are fragmented. You can reduce the MSS value in TCP, which prevents a service board from fragmenting packets and helps improve MAP efficiency.

#### Prerequisites

If the size of packets for processing is larger than a link MTU, IPv6 packets are fragmented. You can reduce the MSS value in TCP, which prevents a service board from fragmenting packets and helps improve MAP efficiency.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**map-e instance**](cmdqueryname=map-e+instance) *map-e-instance-name* [ **id** *id* ]
   
   
   
   The MAP-E instance view is displayed.
3. Run [**map tcp adjust-mss**](cmdqueryname=map+tcp+adjust-mss) *mss-value*
   
   
   
   An MSS value is set in TCP SYN and SYN ACK packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.