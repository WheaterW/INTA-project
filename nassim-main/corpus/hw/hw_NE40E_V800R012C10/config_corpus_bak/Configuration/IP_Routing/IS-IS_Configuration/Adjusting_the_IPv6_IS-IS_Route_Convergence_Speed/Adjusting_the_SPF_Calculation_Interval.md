Adjusting the SPF Calculation Interval
======================================

By adjusting the SPF calculation interval, you can ensure that IS-IS responds to network changes in time and reduce the system resources consumed by SPF calculation.

#### Context

When a network changes frequently, IS-IS performs SPF calculation frequently. Frequent SPF calculation will consume excessive CPU resources, affecting services.

To solve this problem, configure an intelligent timer to control the SPF calculation interval. For example, to speed up IS-IS route convergence, set the interval for SPF calculation to a small value, and set the interval to a large value after the IS-IS network becomes stable.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**timer spf**](cmdqueryname=timer+spf) *max-interval* [ *init-interval* [ *incr-interval* ] ]
   
   
   
   The SPF intelligent timer is configured.
   
   
   
   The interval for SPF calculation is described as follows:
   * The delay for the first SPF calculation is *init-interval*; the delay for the second SPF calculation is *incr-interval*. From the third time on, the SPF calculation delay doubles each time the route changes until the delay reaches *max-interval*. If network flapping persists within the interval specified by *max-interval*, the delay remains *max-interval*. If the network does not flap within *max-interval* or the IS-IS process is restarted, the delay decreases to *init-interval*.
   * If *incr-interval* is not used, the delay for the first SPF calculation is *init-interval*. From the second time on, the delay remains *max-interval*. If the local routing information changes frequently within *max-interval*, the delay for SPF calculation remains *max-interval*. If the local routing information does not change within the interval specified by *max-interval* or the IS-IS process is restarted, the delay decreases to *init-interval*.
   * When only *max-interval* is used, the intelligent timer becomes a one-shot timer.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.