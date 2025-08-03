Deleting IPv4 Multicast VPN Statistics
======================================

If IPv4 Multicast VPN statistics are not needed, you can delete them.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

All statistics about group switching messages will be deleted after you run the [**reset multicast-domain control-message counters**](cmdqueryname=reset+multicast-domain+control-message+counters) command. Exercise caution when running this command.



#### Procedure

* Run the [**reset multicast-domain**](cmdqueryname=reset+multicast-domain) { **vpn-instance** *vpn-instance-name* | **all-instance** } **control-message counters** command in the user view to delete IPv4 multicast VPN statistics.