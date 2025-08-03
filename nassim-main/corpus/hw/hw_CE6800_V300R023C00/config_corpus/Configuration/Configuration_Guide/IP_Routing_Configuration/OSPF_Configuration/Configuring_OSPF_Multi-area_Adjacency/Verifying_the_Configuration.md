Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command to check brief OSPF information.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ *interface-name* | *interface-type**interface-number* | **all** ] [ **verbose** ] command to check OSPF interface information.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **peer** command to check information about OSPF neighbors in each area.
  
  
  
  After this command is run, check the multi-area adjacency interface information based on the **(M) Indicates MADJ interface**, **Multi-area interface**, and **Multi-area Interface Count** fields in the command output.