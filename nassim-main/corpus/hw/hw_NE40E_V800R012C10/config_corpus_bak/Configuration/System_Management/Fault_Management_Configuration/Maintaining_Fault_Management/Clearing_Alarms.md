Clearing Alarms
===============

You can clear alarms in the alarm management view as needed.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If alarms are cleared, the NMS cannot obtain information about the cleared alarms by any means. If a fault persists but the alarm triggered by this fault is cleared, the alarm of the same type will no longer be sent to the NMS. Therefore, before deleting alarms, be sure that the NMS no longer needs these alarms.

In routine maintenance, you can run the following commands in the alarm management view to clear alarms.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**alarm**](cmdqueryname=alarm) command to enter the alarm management view.
3. Run the [**clear alarm active**](cmdqueryname=clear+alarm+active) { **all** | **sequence-number** *sequence-number* } command to clear active alarms.
4. Run the [**clear alarm history**](cmdqueryname=clear+alarm+history) { **all** | **sequence-number** *sequence-number* } command to clear information about historical alarms in the system.