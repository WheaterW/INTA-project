Verifying the Configuration
===========================

After improving the OSPFv3 network stability, verify brief information about OSPFv3 and the IP routing table.

#### Procedure

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **no-peer** | **area** *area-id* ] [ *interface-type* *interface-number* ] command to view information about an OSPFv3 interface.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **routing** command to check information about the OSPFv3 routing table.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **statistics maxage-lsa** command to check information about MaxAge Router-LSAs.