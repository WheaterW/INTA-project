Deleting (S, G) Information from an SA Cache
============================================

To reset contents in a source active (SA) cache, you can delete all (S, G) information from the SA cache.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Deleted (S, G) information in an SA cache cannot be restored. Therefore, exercise caution when running the [**reset msdp**](cmdqueryname=reset+msdp) command.



#### Procedure

1. To delete the (S, G) information from an SA cache, run the [**reset msdp**](cmdqueryname=reset+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **sa-cache** [ *group-address* ] command in the user view.