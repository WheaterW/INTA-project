(Optional) Configuring the ERPS Protection Switching Function
=============================================================

(Optional) Configuring the ERPS Protection Switching Function

#### Context

To ensure that an ERPS ring function properly when a node or link fails, configure the switching mode, port blocking mode, and timers.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a created ERPS ring.
   
   
   ```
   [erps ring](cmdqueryname=erps+ring) ring-id
   ```
3. Configure the revertive or non-revertive switching mode for the ERPS ring.
   
   
   ```
   [revertive](cmdqueryname=revertive) { enable | disable }  
   ```
   
   
   
   By default, an ERPS ring works in revertive switching mode.
4. Exit the ERPS ring view to enter the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the view of a port to be blocked.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number   
   ```
6. Configure the port blocking mode.
   
   
   ```
   [erps](cmdqueryname=erps) ring ring-id [protect-switch](cmdqueryname=protect-switch) { force | manual }
   ```
   
   
   
   The ERPS ring specified by **ring** *ring-id* must be the one to which the port is added.
   
   To cancel port blocking, run the [**clear**](cmdqueryname=clear) command in the ERPS ring view.
7. Exit the ERPS ring view to enter the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```