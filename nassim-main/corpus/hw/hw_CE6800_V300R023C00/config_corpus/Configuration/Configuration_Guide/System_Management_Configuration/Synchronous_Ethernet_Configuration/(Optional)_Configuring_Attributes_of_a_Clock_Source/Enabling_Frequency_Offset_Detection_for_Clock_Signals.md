Enabling Frequency Offset Detection for Clock Signals
=====================================================

Enabling Frequency Offset Detection for Clock Signals

#### Context

You can enable frequency offset detection if a clock synchronization network has high requirements for the frequency offset of clock signals. After frequency offset detection is enabled, the system checks the frequency offset of clock signals. The results of the check may affect automatic clock source selection. By default, if the frequency offset exceeds 9200 ppb, the clock source is considered unreliable. In this case, the system may trigger automatic clock source selection again.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable frequency offset detection.
   
   
   ```
   [clock freq-deviation-detect enable](cmdqueryname=clock+freq-deviation-detect+enable)
   ```
   
   By default, frequency offset detection is not enabled for clock signals.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```