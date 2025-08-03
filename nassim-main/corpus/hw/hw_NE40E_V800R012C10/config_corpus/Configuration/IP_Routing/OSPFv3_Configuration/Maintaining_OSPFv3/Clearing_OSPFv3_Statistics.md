Clearing OSPFv3 Statistics
==========================

This section describes how to clear OSPFv3 statistics, including statistics about OSPFv3 counters and statistics about session-CAR.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

OSPFv3 information cannot be restored after you clear it. Exercise caution when clearing it.

To clear OSPFv3 information, run the following reset commands in the user view.


#### Procedure

* Run the [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **counters** [ **neighbor** [ *interface-type* *interface-number* ] [ *nbrrouter-id* ] ] command to reset OSPFv3 counters.
* Run the [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **counters** **maxage-lsa** command to delete the statistics about router-LSAs that have reached the aging time.
* Run the [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **frr** command to perform OSPFv3 IP FRR calculation again.
* Run the [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **peer** [ *interface-type* *interface-number* ] *router-id* command to restart an OSPFv3 neighbor.
* Run the [**reset cpu-defend whitelist-v6 session-car**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car) **ospfv3** **statistics** **slot** *slot-id* command to clear statistics about whitelist session-CAR for OSPFv3 on a specified interface board.