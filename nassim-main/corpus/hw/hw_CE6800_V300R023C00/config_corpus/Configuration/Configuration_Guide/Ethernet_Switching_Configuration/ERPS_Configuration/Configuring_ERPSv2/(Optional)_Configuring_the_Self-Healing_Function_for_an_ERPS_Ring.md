(Optional) Configuring the Self-Healing Function for an ERPS Ring
=================================================================

(Optional) Configuring the Self-Healing Function for an ERPS Ring

#### Context

On a stable ERPS ring, if a node where the RPL owner port does not reside incorrectly sends R-APS SF messages when no fault occurs, the RPL owner port may be unblocked, causing a loop. After the self-healing function is enabled, the device eliminates the loop caused by incorrectly sent messages through status detection.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a created ERPS ring.
   
   
   ```
   [erps ring](cmdqueryname=erps+ring) ring-id
   ```
3. Disable the self-healing function for the ERPS ring.
   
   
   ```
   [erps self-heal disable](cmdqueryname=erps+self-heal+disable)
   ```
   
   
   
   By default, this function is enabled.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```