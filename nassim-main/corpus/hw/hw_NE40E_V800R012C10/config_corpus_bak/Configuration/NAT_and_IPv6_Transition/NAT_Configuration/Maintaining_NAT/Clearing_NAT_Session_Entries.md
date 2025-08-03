Clearing NAT Session Entries
============================

This section describes how to use the [**reset**](cmdqueryname=reset) command to clear NAT session entries.

#### Context

To delete unnecessary NAT session entries, run the [**reset nat session table**](cmdqueryname=reset+nat+session+table) command. This allows new NAT session entries to be created for fault location and rectification.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Services will be interrupted after NAT session entries are cleared. Exercise caution when performing this operation.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.



#### Procedure

* After determining the NAT session entries to be cleared, run [**reset nat session table**](cmdqueryname=reset+nat+session+table)