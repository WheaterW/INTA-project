Maintaining FM
==============

Maintaining FM

#### Clearing Alarms

After identifying alarms to be cleared, perform the following operations in the alarm management view:

![](public_sys-resources/caution_3.0-en-us.png) 

After an alarm is cleared, an NMS cannot obtain the alarm information. Cleared alarms cannot be restored. In addition, the alarm is no longer reported even if the original fault persists. Therefore, exercise caution when you run this command.


**Table 1** Clearing alarms
| Operation | Command |
| --- | --- |
| Clear active alarms. | [**clear alarm active**](cmdqueryname=clear+alarm+active) { **all** | **sequence-number** *sequence-number* } |
| Clear historical alarms. | [**clear alarm history**](cmdqueryname=clear+alarm+history) { **all** | **sequence-number** *sequence-number* } |
| Clear alarm statistics. | [**reset statistics**](cmdqueryname=reset+statistics) [ **name** *alarm-name* ] |



#### Monitoring Alarms

You can run the following commands in any view to check the alarm information in routine maintenance.

**Table 2** Monitoring alarms
| Operation | Command |
| --- | --- |
| View active alarms. | [**display alarm active**](cmdqueryname=display+alarm+active) [ [**verbose**](cmdqueryname=verbose) ] |
| View active root alarms. | [**display alarm active root**](cmdqueryname=display+alarm+active+root)  [ [**verbose**](cmdqueryname=verbose) ] |
| View historical alarms. | [**display alarm history**](cmdqueryname=display+alarm+history) [ [**verbose**](cmdqueryname=verbose) ] |
| View alarm configurations. | [**display alarm information**](cmdqueryname=display+alarm+information) [ **name** *alarm-name* ] |
| View alarm statistics. | [**display alarm statistics**](cmdqueryname=display+alarm+statistics) [ **name** *alarm-name* ] |