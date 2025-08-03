Setting the Interval at Which LSAs Are Received
===============================================

You can set the interval at which LSAs are received based on network connections and router resources.

#### Context

In OSPF, the defined interval at which LSAs are received is 1s. This aims to prevent network connections or frequent route flapping from consuming excessive network bandwidth or device resources.

On a stable network that requires fast route convergence, you can cancel the interval at which LSAs are received by setting the interval to 0s. After the interval is set to 0s, topology or route changes can be immediately advertised on the network through LSAs, which speeds up route convergence.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**lsa-arrival-interval**](cmdqueryname=lsa-arrival-interval) { *interval* | **intelligent-timer** *max-interval* *start-interval* *hold-interval* }
   
   
   
   The interval at which LSAs are received is set.
   
   
   
   * *interval*: specifies the interval at which LSAs are received, in milliseconds.
   * **intelligent-timer**: indicates that the interval for updating OSPF router LSAs and network LSAs is set through an intelligent timer.
   * *max-interval*: specifies the maximum interval at which OSPF LSAs are received, in milliseconds.
   * *start-interval*: specifies the initial interval at which OSPF LSAs are received, in milliseconds.
   * *hold-interval*: specifies the hold interval at which OSPF LSAs are received, in milliseconds.
4. (Optional) Run [**lsa-arrival-interval suppress-flapping**](cmdqueryname=lsa-arrival-interval+suppress-flapping) *suppress-interval* [ **threshold** *threshold* ]
   
   
   
   The suppression period that takes effect when received OSPF LSAs flap is configured.
   
   
   
   If no flapping occurs among received OSPF LSAs, the configuration of the [**lsa-arrival-interval**](cmdqueryname=lsa-arrival-interval) command prevents the device from frequently receiving LSAs. If received OSPF LSAs flap, the configuration of the [**lsa-arrival-interval suppress-flapping**](cmdqueryname=lsa-arrival-interval+suppress-flapping) command reduces the impact of the flapping on services. If both of them are configured, the device uses the larger value as the flapping suppression time.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.