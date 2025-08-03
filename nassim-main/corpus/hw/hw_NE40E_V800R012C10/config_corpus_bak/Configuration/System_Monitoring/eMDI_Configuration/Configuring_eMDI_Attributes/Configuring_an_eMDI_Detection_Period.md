Configuring an eMDI Detection Period
====================================

This section describes how to configure an eMDI detection period.

#### Context

With eMDI, monitoring data can be obtained from a device on a regular basis and periodically send to uTraffic in various modes such as Telemetry. After analysis on uTraffic, the monitoring data can be displayed in various forms, such as a trend chart. To change a monitoring period, perform the following operations.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**emdi**](cmdqueryname=emdi)
   
   
   
   The eMDI view is displayed.
3. Run [**emdi monitor-period**](cmdqueryname=emdi+monitor-period) *period-value*
   
   
   
   An eMDI detection period is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.