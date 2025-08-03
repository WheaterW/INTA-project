Setting the MSS Value for NAT Services
======================================

The MSS value defined in TCP specifies the length of a TCP packet. Two devices exchange SYN packets to negotiate the MSS value for a TCP connection to be established.

#### Context

If the size of packets for NAT processing is larger than a link MTU, the packets are fragmented. You can reduce the MSS value in TCP, which prevents a NAT service board from fragmenting packets and helps improve NAT efficiency.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat tcp-mss**](cmdqueryname=nat+tcp-mss) *mss-value*
   
   
   
   The MSS value carried in TCP SYN packets for NAT processing is set.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only the NE40E-M2K and NE40E-M2K-B support the following configurations.
4. (Optional) Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
   
   
   
   A NAT instance is created, and its view is displayed.
5. (Optional) Run [**nat tcp adjust-mss**](cmdqueryname=nat+tcp+adjust-mss) *mss-value*
   
   
   
   The MSS value of packets sent by the interfaces at both ends in the negotiation is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the configured MSS value is smaller than the MSS value of TCP packets and the MSS values are configured in both the NAT instance view and system view, the MSS value configured in the NAT instance view takes precedence over that configured in the system view. In other situations, the globally configured MSS value takes effect.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.