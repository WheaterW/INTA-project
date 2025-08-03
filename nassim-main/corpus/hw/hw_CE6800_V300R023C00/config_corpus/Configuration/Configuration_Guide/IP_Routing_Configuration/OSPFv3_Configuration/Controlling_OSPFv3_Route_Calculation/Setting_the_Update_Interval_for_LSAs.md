Setting the Update Interval for LSAs
====================================

Setting the Update Interval for LSAs

#### Prerequisites

Before setting the update interval for LSAs, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

Setting the update interval for LSAs can prevent network connections or frequent route flapping from consuming excessive network bandwidth or device resources. On a stable network that requires fast route convergence, you can specify an update interval for LSAs. In this manner, LSAs indicating topology or route changes can be advertised immediately, which speeds up route convergence.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Set the update interval for OSPFv3 LSAs.
   
   
   ```
   [lsa-originate-interval](cmdqueryname=lsa-originate-interval) { 0 | intelligent-timer max-interval start-interval hold-interval [ other-type interval ] | other-type interval [ intelligent-timer max-interval start-interval hold-interval ] }
   ```
   
   By default, the intelligent timer is enabled, and the maximum interval, initial interval, and hold interval at which OSPFv3 LSAs are updated are 5000 ms, 500 ms, and 1000 ms, respectively.
   
   If the device sends normal OSPFv3 LSAs, the configuration of the [**lsa-originate-interval**](cmdqueryname=lsa-originate-interval) command prevents the device from frequently sending LSAs.
4. (Optional) Set a suppression period that takes effect if the device sends a large number of updated LSAs indicating a flapping link.
   
   
   ```
   [lsa-originate-interval suppress-flapping](cmdqueryname=lsa-originate-interval+suppress-flapping) interval [ threshold count ]
   ```
   
   If the device sends a large number of updated OSPFv3 LSAs indicating a flapping link, the configuration of the [**lsa-originate-interval suppress-flapping**](cmdqueryname=lsa-originate-interval+suppress-flapping) command minimizes the impact that this flapping poses on services. In this case, the device selects the larger value between [**lsa-originate-interval**](cmdqueryname=lsa-originate-interval) and [**lsa-originate-interval suppress-flapping**](cmdqueryname=lsa-originate-interval+suppress-flapping) as the flapping suppression period.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] command to check brief information about OSPFv3. The **LSA Originate Intelligent Timer** and **LSA Originate Interval** fields in the command output show the update interval for LSAs.