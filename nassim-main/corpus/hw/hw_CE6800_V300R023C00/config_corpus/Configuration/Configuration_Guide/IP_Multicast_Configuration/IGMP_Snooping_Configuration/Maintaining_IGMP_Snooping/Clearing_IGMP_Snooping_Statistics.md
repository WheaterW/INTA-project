Clearing IGMP Snooping Statistics
=================================

Clearing IGMP Snooping Statistics

#### Context

IGMP snooping statistics include the numbers of IGMP Report, Leave, Query, and Hello messages received in a VLAN. If existing IGMP snooping statistics are no longer needed, you can clear them to facilitate new statistics query.

![](../public_sys-resources/notice_3.0-en-us.png) 

IGMP snooping statistics cannot be restored after they are cleared. Exercise caution when performing this operation.



#### Procedure

* Run the [**reset igmp snooping statistics**](cmdqueryname=reset+igmp+snooping+statistics) { **all** | **vlan** { *vlan-id* | **all** } } command in the user view to clear IGMP snooping statistics.