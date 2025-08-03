Configuring Suppression Timers
==============================

Suppression timers can prevent routing loops and reduce
the possibility of generating incorrect routing information due to
the receiving of incorrect routes.

#### Context

When hop count of a route increases, a device starts suppression
timers and accepts the Update packet of this route and updates the
routing table until the suppression timers expire.

Suppression
timers delays the addition of incorrect routes to the routing table
and slows down route convergence on the entire network as well. Therefore,
exercise caution when configuring the suppression timers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) *process-id*
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Run [**timers rip**](cmdqueryname=timers+rip) *update* *age* *suppress* *garbage-collect*
   
   
   
   The
   suppression timers are set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.

#### Follow-up Procedure

RIP has four timers: *update*, *age*, *suppress*, and *garbage-collect*. The value of *update* is less than that of *age*, and the value of *suppress* is less
than that of *garbage-collect*. Setting improper
values for the timers affects RIP convergence speed and even causes
route flapping on the network. For example, if the value of *update* is greater than that of *age*,
a device cannot inform its neighbors of the change of RIP routes immediately.

For the configurations of *update*, *age*, *suppress*, and *garbage-collect*, see [Configuring RIP Timers](dc_vrp_rip_cfg_0033.html).