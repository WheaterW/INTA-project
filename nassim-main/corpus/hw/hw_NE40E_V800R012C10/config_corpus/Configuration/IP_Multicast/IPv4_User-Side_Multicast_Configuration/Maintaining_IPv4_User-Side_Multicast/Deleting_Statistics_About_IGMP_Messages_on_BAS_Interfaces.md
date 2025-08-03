Deleting Statistics About IGMP Messages on BAS Interfaces
=========================================================

To facilitate new IGMP message statistics lookup, you can run the [**reset igmp statistics**](cmdqueryname=reset+igmp+statistics) command to delete existing IGMP message statistics on BAS interfaces if they are not needed.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The deleted IGMP message statistics cannot be restored. Therefore, exercise caution when running the [**reset igmp statistics**](cmdqueryname=reset+igmp+statistics) command.

This configuration task is supported only on the Admin-VS.



#### Procedure

* To delete existing statistics about IGMP messages on BAS interfaces, run the [**reset igmp statistics**](cmdqueryname=reset+igmp+statistics) { **user-id** *user-id* | **all** | **all-user** } command.