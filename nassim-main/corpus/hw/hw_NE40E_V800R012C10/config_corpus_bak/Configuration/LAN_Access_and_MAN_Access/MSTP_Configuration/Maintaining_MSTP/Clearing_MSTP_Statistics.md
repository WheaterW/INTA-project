Clearing MSTP Statistics
========================

You can run the **reset** commands to reset Multiple Spanning Tree Protocol (MSTP) statistics to 0.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

MSTP statistics cannot be restored after you clear them. Therefore, exercise caution when using the **reset** commands.

After you confirm that MSTP statistics need to be cleared, run the following command in the user view.


#### Procedure

1. Run the [**reset stp**](cmdqueryname=reset+stp) [ **interface** *interface-type* *interface-number* | **vsi** *vsi-name* **pw** *pw-name* ] **statistics** command to clear spanning-tree statistics.