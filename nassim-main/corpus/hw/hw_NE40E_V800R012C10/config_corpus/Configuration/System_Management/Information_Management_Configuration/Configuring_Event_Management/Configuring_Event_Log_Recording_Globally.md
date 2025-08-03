Configuring Event Log Recording Globally
========================================

This section describes how to enable or disable the function to record a type of event log globally. For this type of event log, only event traps are sent but logs are not recorded.

#### Context

Only event traps are sent for a type of event log. Therefore, you cannot view these logs in the log file. If you need to send these logs to a log file, enable the function to record event logs globally.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**info-center event logging all**](cmdqueryname=info-center+event+logging+all)
   
   
   
   Event log recording is enabled globally.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.