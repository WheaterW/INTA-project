Clearing Dynamic IPv4 DNS Entries
=================================

This section describes how to clear dynamic DNS entries using a [**reset**](cmdqueryname=reset) command.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The dynamic DNS entries cannot be restored after they are cleared. Exercise caution when running the [**reset**](cmdqueryname=reset) command.



#### Procedure

1. After confirming the dynamic DNS entries to be deleted from the cache, run the [**reset dns dynamic-host**](cmdqueryname=reset+dns+dynamic-host+vpn-instance) [ **vpn-instance** *vpn-name* ] [ *hostname* ] command in the user view.