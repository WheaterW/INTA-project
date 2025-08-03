Setting the Receive Interval for LSAs
=====================================

Setting the Receive Interval for LSAs

#### Prerequisites

Before setting the receive interval for LSAs, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

OSPF sets a 1-second receive interval for LSAs. This prevents network connections or frequent route flapping from consuming excessive network bandwidth or device resources.

On a stable network that requires fast route convergence, you can cancel the receive interval by setting the interval to 0 seconds. This speeds up route convergence as LSAs indicating topology or route changes can be received immediately.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
   
   The *process-id* parameter specifies the ID of a process, and the default value is 1.
3. Set the receive interval for LSAs.
   
   
   ```
   [lsa-arrival-interval](cmdqueryname=lsa-arrival-interval) { interval | intelligent-timer max-interval start-interval hold-interval }
   ```
   
   Parameters in this command are described as follows:
   
   * *interval*: specifies the receive interval for LSAs, in milliseconds.
   * **intelligent-timer**: uses the intelligent timer to set the receive interval for router LSAs and network LSAs.
   * *max-interval*: specifies the maximum interval at which LSAs are received, in milliseconds.
   * *start-interval*: specifies the initial interval at which LSAs are received, in milliseconds.
   * *hold-interval*: specifies the hold interval at which LSAs are received, in milliseconds.
   
   By default, the intelligent timer is enabled; the maximum interval, initial interval, and hold interval at which LSAs are received are 1000 ms, 500 ms, and 500 ms, respectively.
4. (Optional) Configure a suppression period that takes effect when received OSPF LSAs flap.
   
   
   ```
   [lsa-arrival-interval suppress-flapping](cmdqueryname=lsa-arrival-interval+suppress-flapping) suppress-interval [ threshold threshold ]
   ```
   
   If the device receives normal OSPF LSAs, setting an interval using the [**lsa-arrival-interval**](cmdqueryname=lsa-arrival-interval) command prevents the device from receiving frequent LSAs.
   
   If the device receives a large number of updated LSAs indicating a flapping link, setting a suppression period using the [**lsa-arrival-interval suppress-flapping**](cmdqueryname=lsa-arrival-interval+suppress-flapping) command minimizes the impact that the flapping poses on services.
   
   If the [**lsa-arrival-interval**](cmdqueryname=lsa-arrival-interval) *interval* command and the [**lsa-arrival-interval suppress-flapping**](cmdqueryname=lsa-arrival-interval+suppress-flapping) *suppress-interval* command are both run, the device compares the two configured values and uses the larger value as the actual suppression period.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```