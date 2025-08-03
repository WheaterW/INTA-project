Clearing Routing Table Statistics
=================================

Clear historical statistics about protocol routes in the IPv4 and IPv6 routing table. This enables the router to re-collect statistics about protocol routes, facilitating route monitoring and fault location.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics in the IPv4 and IPv6 routing table cannot be restored after you clear them. Therefore, exercise caution when running the command.



#### Procedure

* To clear statistics about protocol routes in the IPv4 routing table, run the [**reset ip routing-table statistics protocol**](cmdqueryname=reset+ip+routing-table+statistics+protocol) command in the user view.
* To clear statistics about protocol routes in the IPv6 routing table, run the [**reset ipv6 routing-table statistics protocol**](cmdqueryname=reset+ipv6+routing-table+statistics+protocol) command in the user view.