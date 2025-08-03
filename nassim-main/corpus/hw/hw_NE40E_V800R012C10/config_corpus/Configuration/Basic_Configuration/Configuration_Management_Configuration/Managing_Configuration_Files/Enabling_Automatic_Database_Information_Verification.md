Enabling Automatic Database Information Verification
====================================================

Enabling Automatic Database Information Verification

#### Context

The device data is
saved in the central database and service process databases. Each
service process database needs to synchronize data from the central
database. If the data in a service process database is inconsistent
with that in the central database, the host behaviors may not meet
operator expectations, causing service function exceptions. Therefore,
automatic data verification needs to be enabled to periodically check
data consistency between service process databases and the central
database. If any inconsistency is detected, an alarm is reported immediately,
notifying you of analyzing the impact on services timely. You can
restart the board or device to rectify the fault.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration process is supported only on the Admin-VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set configuration appdata auto-check enable**](cmdqueryname=set+configuration+appdata+auto-check+enable)
   
   
   
   The function to automatically check whether data in the service process database is the same as that in the central database is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.