Clearing STAMP Statistics
=========================

This section describes how to clear STAMP session statistics.

#### Context

If the existing STAMP session statistics are no longer applicable, you can clear them before re-collecting statistics.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

STAMP session statistics cannot be restored after being cleared. Exercise caution when clearing the statistics.



#### Procedure

* Run the [**reset stamp**](cmdqueryname=reset+stamp)[ **ipv4** | **ipv6** ] **statistics**{ **interface** { *interface-type**interface-number* | *interface-name* } | **all** }command to clear STAMP session statistics.