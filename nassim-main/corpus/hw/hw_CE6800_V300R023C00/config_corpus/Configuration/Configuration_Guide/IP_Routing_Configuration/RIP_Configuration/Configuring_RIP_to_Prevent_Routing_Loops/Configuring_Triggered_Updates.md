Configuring Triggered Updates
=============================

Configuring Triggered Updates

#### Context

Triggered updates can be configured to reduce the network convergence time and improve network reliability.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Adjust the RIP triggered update timer.
   
   
   ```
   [timers rip triggered](cmdqueryname=timers+rip+triggered) { minimum-interval minimum-interval | incremental-interval incremental-interval | maximum-interval maximum-interval } *
   ```
   
   By default, the triggered update timer is disabled.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```