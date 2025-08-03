Masking All Alarms
==================

Terminal users can mask all alarms.

#### Context

Terminal users include command line users and NMS users. If terminal users do not expect any alarms sent from the device, they can mask all alarms.


#### Procedure

* Command line users run the [**undo terminal alarm**](cmdqueryname=undo+terminal+alarm) command in the user view to mask all alarms.
* NMS users on the host named *host-name* perform the following operations to mask all alarms:
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**alarm**](cmdqueryname=alarm) command to enter the alarm management view.
  3. Run the [**undo alarm snmp target-host**](cmdqueryname=undo+alarm+snmp+target-host) *hostName* command to mask all alarms.