Configuring Time Parameters for Synchronizing the Client Clock
==============================================================

If the server clock changes or multiple NTP servers are available, you need to set clock synchronization parameters on the client clock, such as the interval and the maximum synchronization distance threshold for synchronizing the client clock. The client clock synchronizes with the clock source based on the configured clock synchronization parameters.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ntp-service sync-interval**](cmdqueryname=ntp-service+sync-interval) *interval*
   
   
   
   A time interval to update the client clock is configured.
   
   
   
   *interval* specifies the interval value, which ranges from 180 to 600, in seconds.
3. Run [**ntp-service max-distance**](cmdqueryname=ntp-service+max-distance) *max-distance-value*
   
   
   
   The maximum NTP synchronization distance threshold is configured.
4. (Optional) Run [**ntp-service offset-limit**](cmdqueryname=ntp-service+offset-limit) *maxOffset*
   
   
   
   The offset threshold for clock synchronization is configured on the client.
   
   
   
   If the time offset between the clock source and the client is greater than the configured offset threshold, the client does not synchronize with the clock source.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.