Verifying the Configuration
===========================

After OSPF route selection is adjusted, you can check OSPF routing table and interface information.

#### Prerequisites

OSPF route selection has been adjusted.
#### Procedure

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check information about OSPF interfaces.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command to check information about the OSPF routing table.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **ecmp-group** command to check information about OSPF ECMP groups