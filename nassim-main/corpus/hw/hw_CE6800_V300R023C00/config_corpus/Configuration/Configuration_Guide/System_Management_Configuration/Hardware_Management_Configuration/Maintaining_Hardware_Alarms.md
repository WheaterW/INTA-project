Maintaining Hardware Alarms
===========================

Maintaining Hardware Alarms

#### Clearing Hardware Alarms

After confirming that hardware alarms need to be cleared, perform the following configurations:

![](public_sys-resources/caution_3.0-en-us.png) 

A deleted hardware alarm cannot be restored or obtained by an NMS in any way. In addition, the alarm is no longer reported even if the original fault persists. Therefore, exercise caution when deciding to clear hardware alarms.


**Table 1** Clearing hardware alarms
| Operation | Command |
| --- | --- |
| Clear hardware alarms. | [**clear device alarm hardware**](cmdqueryname=clear+device+alarm+hardware) { **all** | **slot** *slot-id* | **index** *index-id* } { **send-trap** | **no-trap** } |
| Clear historical hardware alarms. | [**clear device alarm hardware history**](cmdqueryname=clear+device+alarm+hardware+history) { **all** | **slot** *slot-id* } |



#### Monitoring Hardware Alarms

In routine O&M, you can run the following commands in any view to view desired hardware alarms on a device.

**Table 2** Monitoring hardware alarms
| Operation | Command |
| --- | --- |
| Check hardware alarms. | [**display device alarm hardware**](cmdqueryname=display+device+alarm+hardware) [ **slot** *slotid* ] |
| Check historical hardware alarms. | [**display device alarm hardware history**](cmdqueryname=display+device+alarm+hardware+history) { **all** | **slot** *slotid* } [ **verbose** ] |