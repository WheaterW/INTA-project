Resetting OSPF
==============

You can reset OSPF by restarting OSPF.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Resetting an OSPF connection interrupts the OSPF adjacency between devices. Exercise caution when running the command.

To reset OSPF connections, perform the following operation:


#### Procedure

* Run the [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **process** command to restart the OSPF process.
  
  
  
  After the [**reset ospf**](cmdqueryname=reset+ospf) **process** command is used to restart OSPF, the following situations may occur:
  
  + If the router ID is changed, the new router ID takes affect after the [**reset ospf**](cmdqueryname=reset+ospf) **process** command is run.
  + The DR and BDR are re-selected after the [**reset ospf**](cmdqueryname=reset+ospf) **process** command is run.
* Run the [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **spf** to recalculate OSPF routes.
* Run the [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **redistribution** to reset OSPF route redistribution.