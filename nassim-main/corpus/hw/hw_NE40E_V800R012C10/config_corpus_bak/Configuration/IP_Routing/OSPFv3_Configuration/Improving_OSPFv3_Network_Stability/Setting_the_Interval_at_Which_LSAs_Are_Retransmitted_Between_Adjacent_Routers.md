Setting the Interval at Which LSAs Are Retransmitted Between Adjacent Routers
=============================================================================

You can set an appropriate interval at which LSAs are retransmitted based on network conditions in order to accelerate convergence.

#### Context

After sending an LSA to its neighbor, a device waits for a response. If the device does not receive an acknowledgement packet within the Nth LSA retransmission interval, the device retransmits the LSA to the neighbor.

First LSA retransmission interval = Configured interval at which LSAs are retransmitted, which is *interval*

Second LSA retransmission interval = Configured interval at which LSAs are retransmitted, which is *interval*

Third LSA retransmission interval = Configured interval at which LSAs are retransmitted, which is *interval*

Fourth LSA retransmission interval = Configured interval at which LSAs are retransmitted (*interval*) x 2

Fifth LSA retransmission interval = Configured interval at which LSAs are retransmitted (*interval*) x 2^2

... ...

Nth LSA Retransmission Interval = Configured interval at which LSAs are retransmitted (*interval*) x 2^(n-3).

If *interval* x 2^(n-3) is greater than 30, the Nth LSA retransmission interval is 30.

If the configured interval at which LSAs are retransmitted (*interval*) is greater than 30, the Nth LSA retransmission interval equals *interval*.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The OSPFv3 interface view is displayed.
3. Run [**ospfv3 timer retransmit**](cmdqueryname=ospfv3+timer+retransmit) *interval* [ **instance** *instance-id* ]
   
   
   
   An interval for retransmitting LSAs to the adjacent device is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Set the LSA retransmission interval to a proper value. An excessively short interval will cause unnecessary retransmission. Generally, the interval should be longer than the time taken for round-trip packet transmission between two ends.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.