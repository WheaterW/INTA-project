Verifying the Configuration of OSPFv3 Route Selection
=====================================================

After setting OSPFv3 route attributes, verify information about OSPFv3 interfaces and the routing table.

#### Prerequisites

OSPFv3 route attributes have been configured.


#### Procedure

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **no-peer** | **area** *area-id* ] [ *interface-type* *interface-number* ] command in any view to view information about an OSPFv3 interface.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **routing** command in any view to view information about an OSPFv3 routing table.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **ecmp-group** command in any view to view information about OSPFv3 ECMP groups.