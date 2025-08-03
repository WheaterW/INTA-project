Maintaining OSPFv3
==================

Maintaining OSPFv3

#### Procedure

To clear running information of OSPFv3, run the following reset commands in the user view.

![](../public_sys-resources/notice_3.0-en-us.png) 

OSPFv3 information cannot be restored after it is cleared. Exercise caution when you run the reset commands.


**Table 1** Clearing OSPFv3 information
| Operation | Command |
| --- | --- |
| Clear OSPFv3 counters. | [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **counters** [ **neighbor** [ *interface-type* *interface-number* ] [ *nbrrouter-id* ] ]   * **counters** indicates OSPFv3 counters. * **neighbor** indicates neighbor information on the specified interface. |
| Delete the statistics about aged router-LSAs. | [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **counters** **maxage-lsa** |
| Perform OSPFv3 IP FRR recalculation. | [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **frr** |
| Re-establish OSPFv3 neighbor relationships. | [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **peer** [ *interface-type* *interface-number* ] *router-id* |

After an OSPFv3 routing policy or the protocol configuration is changed, you need to reset the involved OSPFv3 connections to enable the change to take effect. To reset OSPFv3 connections, run the following commands as required in the user view.

![](../public_sys-resources/notice_3.0-en-us.png) 

Resetting OSPFv3 connections using the [**reset ospfv3**](cmdqueryname=reset+ospfv3) command disconnects the OSPFv3 neighbor relationships between devices. Exercise caution when resetting an OSPFv3 connection.


**Table 2** Resetting OSPFv3 connections
| Operation | Command |
| --- | --- |
| Reset an OSPFv3 process. | [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } |
| Re-import routes. | [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **redistribution** |

To check OSPFv3 diagnostic information, perform the following operation in any view.

**Table 3** Checking OSPFv3 diagnostic information
| Operation | Command |
| --- | --- |
| Check diagnostic information about OSPFv3 neighbor disconnection. | **display ospfv3 troubleshooting** |