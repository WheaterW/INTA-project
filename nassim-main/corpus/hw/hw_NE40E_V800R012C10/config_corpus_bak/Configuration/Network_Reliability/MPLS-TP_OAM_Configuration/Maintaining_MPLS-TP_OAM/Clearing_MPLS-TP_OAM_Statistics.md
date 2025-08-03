Clearing MPLS-TP OAM Statistics
===============================

This section describes how to clear Multiprotocol Label Switching Transport Profile (MPLS-TP) operation, administration and maintenance (OAM) statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

MPLS-TP OAM statistics cannot be restored after they are cleared. Therefore, exercise caution when you run the [**reset mpls-tp
oam**](cmdqueryname=reset+mpls-tp+oam) **meg** *meg-name* **statistic-type** { **lost-measure** { **single-ended** | **dual-ended** } | **delay-measure** { **one-way** | **two-way** } command.



#### Procedure

* Run the [**reset mpls-tp
  oam**](cmdqueryname=reset+mpls-tp+oam) **meg** *meg-name* **statistic-type** { **lost-measure** { **single-ended** | **dual-ended** } | **delay-measure** { **one-way** | **two-way** } command to clear MPLS-TP OAM statistics.