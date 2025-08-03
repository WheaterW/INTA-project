Setting the Interval at Which LSAs Are Received
===============================================

Setting the Interval at Which LSAs Are Received

#### Prerequisites

Before setting the interval at which LSAs are received, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

Setting the interval at which LSAs are received can prevent network connections or frequent route flapping from causing frequent update of LSAs. After the interval is set on a device, the device updates an LSA only after the specified interval expires.

On a stable network that requires fast route convergence, set a small interval (in milliseconds) at which LSAs are received to ensure prompt LSA update. In this manner, topology or route changes can be detected in time, which speeds up LSDB synchronization.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Set the interval at which LSAs are received.
   
   
   ```
   [lsa-arrival-interval](cmdqueryname=lsa-arrival-interval) { interval | intelligent-timer max-interval start-interval hold-interval }
   ```
   
   By default, the intelligent timer is enabled, and the maximum interval, initial interval, and hold interval at which OSPFv3 LSAs are received are 10000 ms, 500 ms, and 500 ms, respectively.
   
   If the device receives normal OSPFv3 LSAs, setting an interval using the [**lsa-arrival-interval**](cmdqueryname=lsa-arrival-interval) command prevents the device from receiving frequent LSAs.
4. (Optional) Set a suppression period that takes effect if the device receives a large number of updated LSAs indicating a flapping link.
   
   
   ```
   [lsa-arrival-interval suppress-flapping](cmdqueryname=lsa-arrival-interval+suppress-flapping) interval [ threshold count ]
   ```
   
   If the device receives a large number of updated OSPFv3 LSAs indicating a flapping link, setting a suppression period using the [**lsa-arrival-interval suppress-flapping**](cmdqueryname=lsa-arrival-interval+suppress-flapping) command minimizes the impact that the flapping poses on services. In this case, the device selects the larger value between [**lsa-arrival-interval**](cmdqueryname=lsa-arrival-interval) and [**lsa-arrival-interval suppress-flapping**](cmdqueryname=lsa-arrival-interval+suppress-flapping) as the flapping suppression period.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] command to check brief information about OSPFv3. The **LSA Arrival Intelligent Timer** and **LSA Arrival Interval** fields in the command output show the receive interval for LSAs.