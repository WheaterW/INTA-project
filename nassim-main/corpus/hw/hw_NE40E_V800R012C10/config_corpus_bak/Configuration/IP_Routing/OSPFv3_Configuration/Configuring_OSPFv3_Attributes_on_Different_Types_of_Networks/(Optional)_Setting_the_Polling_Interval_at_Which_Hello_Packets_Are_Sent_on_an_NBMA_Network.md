(Optional) Setting the Polling Interval at Which Hello Packets Are Sent on an NBMA Network
==========================================================================================

On an NBMA network, a device sends Hello packets to a neighbor that is Down at a polling interval.

#### Context

Perform the following steps on the Router running OSPFv3.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The OSPFv3 interface view is displayed.
3. Run [**ospfv3 timer poll**](cmdqueryname=ospfv3+timer+poll) *interval* [ **instance** *instance-id* ]
   
   
   
   The polling interval at which Hello packets are sent is set on the NBMA interface.
   
   The parameter **poll** *interval* specifies the polling interval at which Hello packets are sent.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.