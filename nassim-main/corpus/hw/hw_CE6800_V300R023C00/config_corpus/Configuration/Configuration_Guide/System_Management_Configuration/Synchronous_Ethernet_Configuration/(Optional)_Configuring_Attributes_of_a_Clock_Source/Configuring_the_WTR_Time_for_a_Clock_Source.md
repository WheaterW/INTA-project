Configuring the WTR Time for a Clock Source
===========================================

Configuring the WTR Time for a Clock Source

#### Context

When the system detects that a clock source has been restored to the normal state, the clock source status is updated only after the configured WTR time elapses. You can configure an appropriate WTR time to reduce the effect of frequent clock source status changes on clock source selection.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the WTR time for a clock source (excluding the PTP clock source).
   
   
   ```
   [clock wtr](cmdqueryname=clock+wtr) wtr-time
   ```
   
   
   
   By default, the WTR time of a clock source is 5 minutes.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```