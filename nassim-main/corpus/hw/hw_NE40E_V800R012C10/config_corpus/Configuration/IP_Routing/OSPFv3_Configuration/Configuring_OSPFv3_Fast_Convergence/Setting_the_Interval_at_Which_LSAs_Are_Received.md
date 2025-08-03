Setting the Interval at Which LSAs Are Received
===============================================

You can set the interval at which LSAs are received based on network connections and router resources.

#### Context

Setting the interval at which LSAs are received can prevent network connections or frequent route flapping from causing frequent update of LSAs. After the interval is set on a router, the router updates an LSA only after the specified interval expires.

On a stable network that requires fast route convergence, you can change the interval at which OSPFv3 LSAs are received to 0s. In this manner, the device can fast respond to topology or route changes, which speeds up route convergence.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**lsa-arrival-interval**](cmdqueryname=lsa-arrival-interval) { *interval* | **intelligent-timer** *max-interval* *start-interval* *hold-interval* }
   
   
   
   The interval at which LSAs are received is configured.
4. (Optional) Run [**lsa-arrival-interval suppress-flapping**](cmdqueryname=lsa-arrival-interval+suppress-flapping) *interval* [ **threshold** *count* ]
   
   
   
   The suppression period that takes effect when received OSPFv3 LSAs flap is configured.
   
   
   
   If no flapping occurs among received OSPFv3 LSAs, the configuration of the [**lsa-arrival-interval**](cmdqueryname=lsa-arrival-interval) command prevents the device from frequently receiving LSAs. If received OSPFv3 LSAs flap, the configuration of the [**lsa-arrival-interval suppress-flapping**](cmdqueryname=lsa-arrival-interval+suppress-flapping) command minimizes the impact of the flapping on services. The larger value of the two intervals is used as the suppression period.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.