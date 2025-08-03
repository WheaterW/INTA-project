Clearing MPLS OAM Statistics
============================

Before you use MPLS OAM to monitor performance, clear MPLS OAM statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Once MPLS OAM statistics are deleted, the statistics cannot be restored. Excise caution before performing the operation.



#### Procedure

* After you confirm to clear MPLS OAM statistics on bidirectional co-routed LSPs, run the [**reset mpls oam statistic-type**](cmdqueryname=reset+mpls+oam+statistic-type) command. { **lost-measure single-ended** | **delay-measure two-way** } **bidirectional-tunnel** { *tunnel-name* | **tunnel** *tunnel-number* } command.
* After you confirm to clear MPLS OAM statistics on the ingress of an LSP, run the [**reset mpls oam statistic-type**](cmdqueryname=reset+mpls+oam+statistic-type) { **lost-measure single-ended** | **delay-measure two-way** } **ingress** { *tunnel-name* | **tunnel** *tunnel-number* } command.
* After you confirm to clear MPLS OAM statistics on PWs, run the [**reset mpls oam statistic-type**](cmdqueryname=reset+mpls+oam+statistic-type) { **lost-measure single-ended** | **delay-measure two-way** } **l2vc** **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* command.