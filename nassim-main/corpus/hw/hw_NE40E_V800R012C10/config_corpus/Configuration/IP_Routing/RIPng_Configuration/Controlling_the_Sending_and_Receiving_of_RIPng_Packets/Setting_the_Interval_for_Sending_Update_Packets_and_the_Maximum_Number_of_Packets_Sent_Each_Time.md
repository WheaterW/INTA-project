Setting the Interval for Sending Update Packets and the Maximum Number of Packets Sent Each Time
================================================================================================

By setting the interval for sending packets and the maximum number of packets to be sent each time, you can optimize the RIPng performance.

#### Context

Perform the following steps on the RIPng Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ripng pkt-transmit**](cmdqueryname=ripng+pkt-transmit) { **interval** *interval* | **number** *packet-count* } \*
   
   
   
   The interval for sending RIPng Update packets and the maximum number of packets sent each time are set on the specified interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is submitted.