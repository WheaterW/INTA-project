Configuring a Frequency Offset Threshold for Clock Signals
==========================================================

Configuring a Frequency Offset Threshold for Clock Signals

#### Context

After a frequency offset threshold is configured for clock signals, the clock source is considered unreliable and automatic clock source selection may be triggered if the frequency offset of clock signals exceeds the configured threshold.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a frequency offset threshold for clock signals.
   
   
   ```
   [clock alarm-threshold frequency-offset](cmdqueryname=clock+alarm-threshold+frequency-offset) frequency-offset-value
   ```
   
   By default, the frequency offset threshold for clock signals is 9200 ppb.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```