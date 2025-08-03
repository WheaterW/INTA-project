Clearing MLD Snooping Statistics
================================

Clearing MLD Snooping Statistics

#### Context

MLD snooping statistics include the number of Report, Done, Query, and Hello messages received in a VLAN. You can run this command to set the statistics to 0 so that you can recollect statistics.

![](../public_sys-resources/notice_3.0-en-us.png) 

MLD snooping statistics cannot be restored after they are cleared. Exercise caution when performing this operation.



#### Procedure

* Run the [**reset mld snooping statistics**](cmdqueryname=reset+mld+snooping+statistics) { **vlan** { *vlan-id* | **all** }|**all** } command in the user view to clear MLD snooping statistics.