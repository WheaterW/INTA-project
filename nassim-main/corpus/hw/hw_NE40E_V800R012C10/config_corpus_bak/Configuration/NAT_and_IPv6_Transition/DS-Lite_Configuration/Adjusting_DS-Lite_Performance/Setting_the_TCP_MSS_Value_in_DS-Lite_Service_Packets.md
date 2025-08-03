Setting the TCP MSS Value in DS-Lite Service Packets
====================================================

The maximum segment size (MSS) value defined in TCP specifies the length of a TCP packet to be sent without fragmentation. Two devices exchange SYN packets to negotiate the MSS value for a TCP connection to be established.

#### Context

If the size of packets for DS-Lite processing is larger than a link MTU, the packets are fragmented. You can reduce the TCP MSS value, which prevents a DS-Lite board from fragmenting packets and helps improve DS-Lite efficiency.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat tcp-mss**](cmdqueryname=nat+tcp-mss) *mss-value*
   
   
   
   The MSS value carried in TCP SYN packets for DS-Lite processing is set.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
4. (Optional) Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ] A DS-Lite instance is created, and the DS-Lite instance view is displayed.
5. (Optional) Run [**ds-lite tcp adjust-mss**](cmdqueryname=ds-lite+tcp+adjust-mss) *mss-value*
   
   
   
   The TCP MSS is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If an MSS value is set in both the DS-Lite instance view and system view, the setting in the DS-Lite instance view takes effect. If no MSS value is set in the DS-Lite instance view, the MSS value in the system view takes effect.