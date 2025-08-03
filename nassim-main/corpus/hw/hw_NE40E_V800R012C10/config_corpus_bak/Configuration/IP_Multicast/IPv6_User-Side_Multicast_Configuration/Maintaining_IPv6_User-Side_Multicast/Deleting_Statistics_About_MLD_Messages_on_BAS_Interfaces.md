Deleting Statistics About MLD Messages on BAS Interfaces
========================================================

To facilitate new MLD message statistics lookup, you can run the [**reset mld statistics**](cmdqueryname=reset+mld+statistics) command to delete existing MLD message statistics on BAS interfaces if they are not needed.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The deleted MLD message statistics cannot be restored. Therefore, exercise caution when running the [**reset mld statistics**](cmdqueryname=reset+mld+statistics) command.

This configuration task is supported only on the Admin-VS.



#### Procedure

* To delete existing statistics about MLD messages on BAS interfaces, run the [**reset mld statistics**](cmdqueryname=reset+mld+statistics) { **user-id** *user-id* | **all** | **all-user** } command.