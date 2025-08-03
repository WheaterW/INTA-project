Verifying the Configuration
===========================

After OSPF attributes are set on networks of different types, you can check OSPF neighbor and interface information.

#### Prerequisites

OSPF attributes have been configured on networks of different types.


#### Procedure

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check OSPF interface information.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **peer** command to check information about OSPF neighbors.
* Run the [**display ospf brief**](cmdqueryname=display+ospf+brief) command to check the interval at which polling packets are sent on an NBMA network.