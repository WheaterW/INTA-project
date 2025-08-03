Enabling Alarm Status Re-check
==============================

After you enable alarm status re-check for a device, the device re-checks the status of a specified type of status change alarm and reports alarms again.

#### Context

Alarms generated due to interface or protocol status changes are cleared after the system is reset. The alarms are not reported again. A status change alarm is triggered only when the status changes. As a result, this type of alarms cannot be found after the system is reset. Therefore, to enable the device to report alarms again after a system reset, enable alarm status re-check.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**alarm**](cmdqueryname=alarm) command to enter the alarm management view.
3. Run the [**alarm alarm-name**](cmdqueryname=alarm+alarm-name) *alarm-name* **initial-startup enable** command to enable the alarm status re-check function.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.