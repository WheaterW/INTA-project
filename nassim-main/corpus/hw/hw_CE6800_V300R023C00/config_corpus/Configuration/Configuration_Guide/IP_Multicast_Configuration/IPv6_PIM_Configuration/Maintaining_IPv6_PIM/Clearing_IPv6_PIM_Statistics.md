Clearing IPv6 PIM Statistics
============================

Clearing IPv6 PIM Statistics

#### Context

This section describes how to clear IPv6 PIM statistics, including statistics about IPv6 PIM control messages and IPv6 PIM status of a specified downstream interface in an IPv6 PIM entry.

![](public_sys-resources/notice_3.0-en-us.png) 

Cleared IPv6 PIM statistics cannot be restored. Therefore, exercise caution when clearing them.

To clear IPv6 PIM statistics, run the following commands in the user view.

**Table 1** Clearing PIM statistics
| Operation | Command |
| --- | --- |
| Clear statistics about IPv6 PIM control messages on an interface. | [**reset pim ipv6**](cmdqueryname=reset+pim+ipv6) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message** **counters** [ **interface** *interface-type* *interface-number* ] |
| Clear the PIM status of a specified downstream interface in a specified IPv6 PIM entry. | [**reset pim ipv6**](cmdqueryname=reset+pim+ipv6) [ **vpn-instance** *vpn-instance-name* ] [ **vpn-instance** *vpn-instance-name* ] **routing-table** **group** *group-address* **mask** { *group-mask-length* | *group-mask* } **source** *source-address* **interface** *interface-type* *interface-number* |