Clearing RIP Statistics
=======================

To clear RIP information, run the **reset** command in the user view.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

RIP statistics cannot be restored after being cleared. Exercise caution when clearing the statistics



#### Procedure

* To clear the system configuration parameters of a specific RIP process, run the [**reset rip**](cmdqueryname=reset+rip) { *process-id* | **all** } **configuration** command. When a RIP process starts, all the parameters of the process retain their default values.
* To clear the routes imported from other routing protocols (including dynamic routes and direct routes) before re-importing them to RIP, run the [**reset rip**](cmdqueryname=reset+rip) { *process-id* | **all** } **imported-routes** command.
* To clear the statistics of the counter maintained by a specified RIP process, run the [**reset rip**](cmdqueryname=reset+rip) *process-id* **statistics** [ **interface** *interface-type* *interface-number* ] or [**reset rip all statistics**](cmdqueryname=reset+rip+all+statistics) command. This command is used to re-record statistics during debugging.