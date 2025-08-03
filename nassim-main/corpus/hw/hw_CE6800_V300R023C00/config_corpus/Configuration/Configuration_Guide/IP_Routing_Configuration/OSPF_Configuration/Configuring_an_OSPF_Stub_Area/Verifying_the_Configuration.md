Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **lsdb** command to check information about the OSPF LSDB.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **peer** command to check information about OSPF neighbors.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command to check information about the OSPF routing table.
  
  
  
  If the device resides in a common area, AS external routes exist in the routing table. After the common area is configured as a stub area, AS external routes no longer exist in the routing table, and the **ASE** field is displayed as 0 in the command output.