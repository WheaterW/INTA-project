Clearing VRRP6 Statistics
=========================

If you want to check VRRP6 statistics within a period of time, you are advised to clear the existing ones.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

VRRP6 statistics cannot be restored after being cleared. Therefore, exercise caution when running the corresponding reset command.



#### Procedure

* Run the [**reset vrrp6**](cmdqueryname=reset+vrrp6) [ **interface** *interface-type* *interface-number* ] [ **vrid** *virtual-router-id* ] **statistics** command to clear the statistics about packets sent and received by a VRRP6 group.