Clearing VBST Statistics
========================

Clearing VBST Statistics

#### Context

Before you start a new statistics collection of VBST BPDUs, clear existing statistics to ensure accurate data in the new statistics collection.

![](public_sys-resources/notice_3.0-en-us.png) 

Cleared statistics on VBST BPDUs cannot be restored. Exercise caution when you perform this operation.



#### Procedure

* Run the [**reset stp vlan**](cmdqueryname=reset+stp+vlan) { *vlan-id* | **all** } **tc-bpdu** **statistics** command in the user view to clear statistics about TC and TCN BPDUs.
* Run the [**reset stp vlan**](cmdqueryname=reset+stp+vlan) { *vlan-id* | **all** } **bpdu** **statistics** command in the user view to clear statistics about BPDUs.