Clearing 1588v2 Statistics
==========================

This section describes how to clear 1588v2 statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

ACL statistics cannot be restored after being cleared. Exercise caution when running the [**reset**](cmdqueryname=reset) command.


After you confirm to clear 1588v2 statistics, run the following command.
#### Procedure

1. Run the [**reset ptp statistics**](cmdqueryname=reset+ptp+statistics) { **all** | **interface** *interface-type* *interface-number* } command in the user view to clear statistics about 1588v2 packets.