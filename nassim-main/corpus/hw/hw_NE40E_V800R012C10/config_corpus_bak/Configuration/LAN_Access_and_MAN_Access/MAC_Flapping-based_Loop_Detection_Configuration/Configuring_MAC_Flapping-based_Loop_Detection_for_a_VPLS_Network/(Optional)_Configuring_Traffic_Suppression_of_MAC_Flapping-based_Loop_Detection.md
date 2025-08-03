(Optional) Configuring Traffic Suppression of MAC Flapping-based Loop Detection
===============================================================================

If a loop occurs on a network, broadcast storms will occur in the broadcast domain. To prevent other broadcast domains from being affected, traffic suppression of MAC flapping-based loop detection must be enabled.

#### Context

Traffic suppression of MAC flapping-based loop detection is enabled by default. You can set a threshold for this function to determine when the system implements traffic suppression. When the network topology becomes stable and no loops occur, disable this function.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**loop-detect traffic-suppression threshold**](cmdqueryname=loop-detect+traffic-suppression+threshold) *suppression-threshold*
   
   
   
   A threshold is set for traffic suppression of MAC flapping-based loop detection.
   
   
   
   When the network topology becomes stable and no loops occur, run the [**loop-detect traffic-suppression disable**](cmdqueryname=loop-detect+traffic-suppression+disable) command to disable this function.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.