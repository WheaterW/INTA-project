Deleting PIM Status Information from IPv6 PIM Routing Entries
=============================================================

If PIM status information in IPv6 PIM routing entries of a downstream interface is unnecessary, delete them from the downstream interface. The deletion does not affect Multicast Listener Discovery (MLD) or static group join status information.

#### Context

The device allows you to delete PIM status information in IPv6 PIM routing entries of a specified or all downstream interfaces.


#### Procedure

* To delete PIM status information from IPv6 PIM routing entries on a specified downstream interface, run the [**reset pim ipv6 routing-table**](cmdqueryname=reset+pim+ipv6+routing-table) **group** *group-address* **mask** *group-mask-length* **source** *source-address* **interface** *interface-type* *interface-number* command in the user view.
* To delete PIM status information from IPv6 PIM routing entries on all downstream interfaces, run the [**reset pim ipv6 routing-table all**](cmdqueryname=reset+pim+ipv6+routing-table+all) command in the user view.