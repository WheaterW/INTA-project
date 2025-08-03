Configuring Time Parameters for Synchronizing the Client Clock
==============================================================

Configuring Time Parameters for Synchronizing the Client Clock

#### Context

If the server clock changes or multiple NTP servers are available, you need to set the clock synchronization parameters on the client clock. Such parameters include the interval and the maximum synchronization distance threshold for synchronizing the client clock. The client clock synchronizes with the clock source based on the configured clock synchronization parameters.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a clock synchronization interval on the client.
   
   
   ```
   [ntp sync-interval](cmdqueryname=ntp+sync-interval) interval
   ```
   
   By default, the clock synchronization interval is not configured on the client.
3. (Optional) Configure the maximum synchronization threshold.
   
   
   ```
   [ntp max-distance](cmdqueryname=ntp+max-distance) max-distance-value
   ```
   
   By default, the maximum NTP synchronization distance threshold is 1s.
4. (Optional) Configure the offset threshold for clock synchronization.
   
   
   ```
   [ntp offset-limit](cmdqueryname=ntp+offset-limit) maxOffset
   ```
   
   By default, the offset threshold for clock synchronization is not configured on the client.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the time offset between the clock source and the client is greater than the offset threshold, the client does not synchronize with the clock source.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```