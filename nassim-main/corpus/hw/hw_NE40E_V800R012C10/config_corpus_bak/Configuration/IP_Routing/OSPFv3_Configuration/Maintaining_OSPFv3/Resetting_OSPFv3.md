Resetting OSPFv3
================

Restarting OSPFv3 can reset OSPFv3.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Resetting an OSPFv3 connection interrupts the OSPFv3 adjacency between devices. Therefore, exercise caution when resetting an OSPFv3 connection.

After modifying the OSPFv3 routing policy or protocol, reset the OSPFv3 connection to validate the modification. To reset OSPFv3 connections, run the following commands as required in the user view.


#### Procedure

* Run the [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } command to restart the OSPFv3 process.
* Run the [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **peer** [ *interface-type* *interface-number* ] *router-id* command to restart an OSPFv3 neighbor.
* Run the [**reset ospfv3**](cmdqueryname=reset+ospfv3) { *process-id* | **all** } **redistribution** command to import routes again.