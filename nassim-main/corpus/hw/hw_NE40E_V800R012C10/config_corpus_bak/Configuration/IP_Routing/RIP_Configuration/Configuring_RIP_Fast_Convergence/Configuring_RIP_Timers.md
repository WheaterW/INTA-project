Configuring RIP Timers
======================

There are four RIP timers: Update, Age, Suppress, and Garbage-collect
timers. You can adjust the RIP convergence speed by changing the values
of RIP timers.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Run [**timers rip**](cmdqueryname=timers+rip) *update* *age* *suppress* *garbage-collect*
   
   
   
   RIP timers are configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.

#### Follow-up Procedure

The value of *update* is less than that
of *age*, and the value of *suppress* is less than that of *garbage-collect*. Setting
improper values for the timers affects RIP convergence speed and even
causes route flapping on the network. For example, if the value of *update* is greater than that of *age*,
a device cannot inform its neighbors of the change of RIP routes immediately.

Configuring the Suppress timer can prevent routing loops. For
details, see [Configuring Suppression Timers](dc_vrp_rip_cfg_0014.html).