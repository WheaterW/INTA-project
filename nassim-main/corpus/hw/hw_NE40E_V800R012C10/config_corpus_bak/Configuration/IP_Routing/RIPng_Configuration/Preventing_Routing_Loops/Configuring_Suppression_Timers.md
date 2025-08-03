Configuring Suppression Timers
==============================

Suppression timers can prevent routing loops and reduce the possibility that receiving incorrect routes results in incorrect routing information.

#### Context

When the hop count of a route increases to a value less than 16, a routing device starts the suppress timer. The routing device does not update the routing table within the period specified by the timer and updates the routing table until the suppress timer expires.

Suppression timers delays the addition of incorrect routes to the routing Table and slows down route convergence on the entire network as well. Therefore, exercise caution when configuring the suppression timers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ripng**](cmdqueryname=ripng) *process-id*
   
   
   
   The RIPng process is created, and the RIPng view is displayed.
3. Run [**timers ripng**](cmdqueryname=timers+ripng) *update* *age* *suppress* *garbage-collect*
   
   
   
   Suppression timers are set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is submitted.

#### Follow-up Procedure

RIPng has four timers: *update*, *age*, *suppress*, and *garbage-collect*. The value of *update* is less than that of *age*, and the value of *suppress* is less than that of *garbage-collect*. Setting improper values for the timers affects RIP convergence speed and even causes route flapping on the network. For example, if the value of *update* is greater than that of *age*, a device cannot inform its neighbors of the change of RIP routes immediately.

For the configurations of *update*, *age*, *suppress*, and *garbage-collect*, see [Configuring RIPng Timers](dc_vrp_ripng_cfg_0022.html).