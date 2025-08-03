Configuring Timers for an ERPS Ring
===================================

Configuring Timers for an ERPS Ring

#### Context

To prevent network flapping after a faulty node or link on an ERPS ring recovers, the device starts timers to reduce the traffic interruption time in the ERPS ring.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a created ERPS ring.
   
   
   ```
   [erps ring](cmdqueryname=erps+ring) ring-id
   ```
3. Configure the WTR timer, Guard timer, and Holdoff timer for the ERPS ring as required.
   
   
   
   **Table 1** Configuring timers for an ERPS ring
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configuring the WTR timer for an ERPS ring | [**wtr-timer**](cmdqueryname=wtr-timer) *time-value* | By default, the WTR timer is 5 minutes in an ERPS ring. |
   | Configuring the Guard timer for an ERPS ring | [**guard-timer**](cmdqueryname=guard-timer) *time-value* | By default, the Guard timer is 200 centiseconds in an ERPS ring. |
   | Configuring the Holdoff timer for an ERPS ring | [**holdoff-timer**](cmdqueryname=holdoff-timer) *time-value* | By default, the Holdoff timer is 0 deciseconds in an ERPS ring. |
   
   For details about the differences between timers, see [Timers](vrp_erps_cfg_0004.html#EN-US_CONCEPT_0000001141619014__section1486181230183241).
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```