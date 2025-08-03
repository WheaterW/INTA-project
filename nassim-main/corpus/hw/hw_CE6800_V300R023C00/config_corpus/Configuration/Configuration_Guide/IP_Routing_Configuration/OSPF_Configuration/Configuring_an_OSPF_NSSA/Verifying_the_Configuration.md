Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **lsdb** command to check the OSPF LSDB information.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command to check information about the OSPF routing table.
  
  
  
  By comparing the routing tables before and after the NSSA is configured, you can reach the following conclusions:
  
  + After an area is configured as the NSSA, the number of entries in the routing table is reduced.
  + AS external routes are imported into the NSSA.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check information about OSPF interfaces.