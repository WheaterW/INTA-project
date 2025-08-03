Configuring RIP Triggered Update
================================

You can speed up network convergence by changing the values
of triggered update timers.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Run [**timers rip triggered**](cmdqueryname=timers+rip+triggered) { **minimum-interval** *minimum-interval* | **incremental-interval** *incremental-interval* | **maximum-interval** *maximum-interval* } \*
   
   
   
   RIP triggered update timers are configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.