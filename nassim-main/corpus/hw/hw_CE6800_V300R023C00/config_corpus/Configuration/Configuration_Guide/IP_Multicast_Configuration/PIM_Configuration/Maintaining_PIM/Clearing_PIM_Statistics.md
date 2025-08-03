Clearing PIM Statistics
=======================

Clearing PIM Statistics

#### Context

This section describes how to clear PIM statistics, including statistics about PIM control messages and PIM status of a specified downstream interface in a PIM entry.

![](public_sys-resources/notice_3.0-en-us.png) 

Cleared PIM statistics cannot be restored. Therefore, exercise caution when clearing them.

To clear PIM statistics, run the following commands in the user view.

**Table 1** Clearing PIM statistics
| Operation | Command |
| --- | --- |
| Clear statistics about PIM control messages on an interface. | [**reset pim**](cmdqueryname=reset+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message** **counters** [ **interface** *interface-type* *interface-number* ] |
| Clear the PIM status of a specified downstream interface in a specified PIM entry. | [**reset pim**](cmdqueryname=reset+pim) [ **vpn-instance** *vpn-instance-name* ] **routing-table** **group** *group-address* **mask** { *group-mask-length* | *group-mask* } **source** *source-address* **interface** *interface-type* *interface-number* |