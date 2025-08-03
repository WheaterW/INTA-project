Clearing VRRP Statistics
========================

If you want to check VRRP statistics within a period of time, you are advised to clear the existing ones.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

VRRP statistics cannot be restored after being cleared. Therefore, exercise caution when running the corresponding reset command.



#### Procedure

* Run the [**reset vrrp**](cmdqueryname=reset+vrrp) [ **interface** { *interface-type* *interface-number* } ] [ **vrid** *virtual-router-id* ] **statistics** command to clear statistics about sent and received packets of the VRRP group.