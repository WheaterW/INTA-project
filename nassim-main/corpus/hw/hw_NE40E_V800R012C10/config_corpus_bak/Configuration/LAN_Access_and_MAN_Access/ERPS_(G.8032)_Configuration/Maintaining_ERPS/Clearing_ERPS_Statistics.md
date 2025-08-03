Clearing ERPS Statistics
========================

The reset command can be used to reset the ERPS statistics to 0 so that statistics can be re-collected.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

ERPS statistics cannot be restored after they are cleared. Exercise caution when running the reset command.



#### Procedure

1. Run the [**display erps**](cmdqueryname=display+erps) [ **ring** *ring-id* ] **statistics** command in the user view to check statistics on the sent and received packets on the device ports added to the ERPS ring.
2. Run the [**reset erps**](cmdqueryname=reset+erps) [ **ring** *ring-id* ] **statistics** command in the user view to clear ERPS statistics on the device.