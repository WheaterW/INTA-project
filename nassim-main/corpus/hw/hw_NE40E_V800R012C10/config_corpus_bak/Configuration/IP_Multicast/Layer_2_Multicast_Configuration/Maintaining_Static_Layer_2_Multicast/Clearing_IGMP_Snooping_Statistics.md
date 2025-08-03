Clearing IGMP Snooping Statistics
=================================

IGMP snooping statistics include the number of protocol messages (Report, Query, and Leave messages) received in the broadcast domain. You can reset the statistics for a new round of statistics collection.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The cleared IGMP snooping statistics cannot be restored. Exercise caution while performing this operation.



#### Procedure

* Run the [**reset igmp-snooping statistics**](cmdqueryname=reset+igmp-snooping+statistics) { **vlan** { *vlan-id* | **all** } | **vsi** { *vsi-name* | **all**} | **all** } command in the user view to clear IGMP snooping statistics.