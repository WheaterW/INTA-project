Setting the Interval at Which Packets Are Sent and the Maximum Number of the Sent Packets
=========================================================================================

You can set the interval at which RIP packets are sent and the maximum number of packets that can be sent at a time to control the memory used by a device to process RIP update packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**rip pkt-transmit**](cmdqueryname=rip+pkt-transmit) { **interval** *interval* | **number** *pkt-count* | **bandwidth** *bandwidth-value* } \*
   
   
   
   The interval at which RIP packets are sent and the maximum number of packets sent each time are set by the interface.
4. Run **commit**
   
   
   
   The configuration is committed.