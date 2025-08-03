Maintaining OSPF
================

Maintaining OSPF

#### Procedure

To clear running information of OSPF, run the following **reset** commands in the user view.

![](../public_sys-resources/notice_3.0-en-us.png) 

OSPF information cannot be restored after it is cleared. Exercise caution when you run the **reset** commands.


**Table 1** Clearing OSPF information
| Operation | Command |
| --- | --- |
| Clear OSPF counters. | [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **counters** [ **neighbor** [ *interface-type* *interface-number* [ **all-areas** | **area** { *area-id* | *area-id* } ] ] [ *router-id* ] ] |
| Delete the statistics about aged router LSAs. | [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **counters** **maxage-lsa** |
| Perform OSPF IP FRR recalculation. | [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **frr** |
| Re-establish OSPF neighbor relationships. | [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **peer** [ *interface-type* *interface-number* ] *router-id* |

To reset OSPF connections, run the following **reset** commands in the user view.

![](../public_sys-resources/notice_3.0-en-us.png) 

Resetting OSPF connections using the [**reset ospf**](cmdqueryname=reset+ospf) command disconnects the OSPF neighbor relationships between devices. Exercise caution when resetting an OSPF connection.


**Table 2** Resetting OSPF connections
| Operation | Command |
| --- | --- |
| Restart an OSPF process. | [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **process**   * If a router ID is changed, the new router ID takes effect after the [**reset ospf**](cmdqueryname=reset+ospf) **process** command is run. * Running the [**reset ospf**](cmdqueryname=reset+ospf) **process** command causes DR/BDR reelection. |
| Restart OSPF route calculation. | [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **spf** |
| Re-import routes. | [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **redistribution** |

To check OSPF diagnostic information, perform the following operation in any view.

**Table 3** Checking OSPF diagnostic information
| Operation | Command |
| --- | --- |
| Check diagnostic information about OSPF neighbor disconnection. | **[**display ospf troubleshooting**](cmdqueryname=display+ospf+troubleshooting)** |