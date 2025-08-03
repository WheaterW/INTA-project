Clearing MLD Snooping Statistics
================================

MLD snooping statistics mainly include the number of Report, Query, Done and other protocol messages received from broadcast domains. If such statistics are not needed or new statistics need to be collected, clear existing MLD snooping statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

MLD snooping statistics cannot be restored after you clear them. Exercise caution when performing this action.



#### Procedure

* To clear MLD snooping statistics, run the [**reset mld-snooping statistics**](cmdqueryname=reset+mld-snooping+statistics) { **vlan** { *vlan-id* | **all** } | **vsi** { [**name**](cmdqueryname=name) *vsi-name* | **all** } | **all** } command in the user view.