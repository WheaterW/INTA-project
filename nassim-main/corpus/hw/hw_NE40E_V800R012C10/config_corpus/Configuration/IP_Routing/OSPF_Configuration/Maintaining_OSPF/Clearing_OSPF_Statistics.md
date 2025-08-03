Clearing OSPF Statistics
========================

This section describes how to clear OSPF statistics, including statistics about OSPF counters and statistics about session-CAR.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

OSPF information cannot be restored after you clear it. Exercise caution when clearing it.

To clear OSPF information, run the following reset commands in the user view.


#### Procedure

* Run the [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **counters** [ **neighbor** [ *interface-type* *interface-number* ] [ *router-id* ] ] command to reset OSPF counters.
  
  
  + **counters** indicates OSPF counters.
  + **neighbor** indicates neighbor information on the specified interface.
* Run the [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **counters** **maxage-lsa** command to delete the statistics about router LSAs that have reached the aging time.
* Run the [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **frr** command to perform OSPF IP FRR calculation again.
* Run the [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **peer** [ *interface-type* *interface-number* ] *router-id* command to restart an OSPF neighbor.
* Run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **ospf** **statistics** **slot** *slot-id* command to clear statistics about whitelist session-CAR for OSPF on a specified interface board.