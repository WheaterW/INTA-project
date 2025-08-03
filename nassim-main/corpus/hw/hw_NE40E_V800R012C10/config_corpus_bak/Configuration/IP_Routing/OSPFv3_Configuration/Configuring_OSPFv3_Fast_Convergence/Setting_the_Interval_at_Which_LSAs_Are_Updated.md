Setting the Interval at Which LSAs Are Updated
==============================================

You can set the interval at which LSAs are updated based on network connections and router resources.

#### Context

To prevent excessive consumption of network bandwidth and router resources caused by frequent network connection or route flapping, you can set the **intelligent-timer** parameter to specify the interval for updating LSAs on a stable network that requires fast route convergence. In this manner, topology or route changes can be immediately advertised to the network through LSAs, speeding up route convergence on the network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**lsa-originate-interval**](cmdqueryname=lsa-originate-interval) { **0** | **intelligent-timer** *max-interval* *start-interval* *hold-interval* [ **other-type** *interval* ] | **other-type** *interval* [ **intelligent-timer** *max-interval* *start-interval* *hold-interval* ] }
   
   
   
   The device is configured to set the interval for updating OSPFv3 LSAs based on the intelligent SPF timer.
4. (Optional) Run [**lsa-originate-interval suppress-flapping**](cmdqueryname=lsa-originate-interval+suppress-flapping) *interval* [ **threshold** *count* ]
   
   
   
   The suppression period that takes effect when sent OSPFv3 LSAs flap is configured.
   
   
   
   If no flapping occurs among sent OSPFv3 LSAs, the configuration of the [**lsa-originate-interval**](cmdqueryname=lsa-originate-interval) command prevents the device from frequently sending LSAs. If sent OSPFv3 LSAs flap, the configuration of the [**lsa-originate-interval suppress-flapping**](cmdqueryname=lsa-originate-interval+suppress-flapping) command minimizes the impact of the flapping on services. The larger value of the two intervals is used as the suppression period.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.