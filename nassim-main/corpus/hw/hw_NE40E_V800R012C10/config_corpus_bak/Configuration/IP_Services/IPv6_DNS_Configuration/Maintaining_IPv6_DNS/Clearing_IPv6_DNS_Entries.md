Clearing IPv6 DNS Entries
=========================

This section describes how to clear IPv6 DNS entries.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Dynamic IPv6 DNS entries cannot be restored after they are cleared. Exercise caution when running the reset command.



#### Procedure

1. After confirming the dynamic IPv6 DNS entries to be deleted from the cache, run the [**reset dns ipv6 dynamic-host**](cmdqueryname=reset+dns+ipv6+dynamic-host+vpn-instance) [ **vpn-instance** *vpn-name* ] [ *hostname* ] command in the user view.