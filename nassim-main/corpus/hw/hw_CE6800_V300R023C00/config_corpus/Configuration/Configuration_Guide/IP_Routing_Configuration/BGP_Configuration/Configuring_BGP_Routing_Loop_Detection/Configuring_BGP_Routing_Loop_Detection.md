Configuring BGP Routing Loop Detection
======================================

Configuring BGP Routing Loop Detection

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enable BGP routing loop detection.
   
   
   ```
   [route loop-detect bgp enable](cmdqueryname=route+loop-detect+bgp+enable)
   ```
   
   After this function is enabled, the device reports an alarm when detecting a BGP routing loop. Because the device cannot determine whether the routing loop is removed, the alarm will not be cleared automatically even if the routing loop is removed. To manually clear the BGP routing loop alarm, run the [**clear route loop-detect bgp alarm**](cmdqueryname=clear+route+loop-detect+bgp+alarm) command.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```