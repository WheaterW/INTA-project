Maintaining RIP
===============

Maintaining RIP

#### Procedure

To clear RIP statistics, run the **reset** **rip** command in the user view. To enable RIP debugging, run the [**debugging rip**](cmdqueryname=debugging+rip) command in the user view.

To clear RIP information, run the **reset** command in the user view.

![](public_sys-resources/notice_3.0-en-us.png) 

RIP statistics cannot be restored after being cleared. Exercise caution when clearing the statistics


**Table 1** Clearing RIP statistics
| Scenario | Command |
| --- | --- |
| Reset the system configuration parameters of a specified RIP process. | [**reset rip**](cmdqueryname=reset+rip) { *process-id* | **all** } **configuration** |
| Clear the routes (routes of other dynamic routing protocols and direct routes) imported from other routing protocols, and import these routes to RIP again. | [**reset rip**](cmdqueryname=reset+rip) { *process-id* | **all** } **imported-routes** |
| Clear the statistics of the counter maintained by a special RIP process. | [**reset rip**](cmdqueryname=reset+rip) *process-id* **statistics** **interface** *interface-type* *interface-number*  [**reset rip**](cmdqueryname=reset+rip) **all** **statistics** |