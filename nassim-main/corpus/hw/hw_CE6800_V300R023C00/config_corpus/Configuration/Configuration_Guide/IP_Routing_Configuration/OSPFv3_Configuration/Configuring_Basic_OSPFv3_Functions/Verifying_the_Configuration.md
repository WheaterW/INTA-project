Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] [ **area** *area-id* ] **peer** [ *interface-type* *interface-number* ] [ **verbose** ] command to check information about OSPFv3 neighbors.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **area** *area-id* ] [ *interface-type* *interface-number* ] command to check OSPFv3 interface information.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **routing** command to check information about the OSPFv3 routing table.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **cumulative** command to check OSPFv3 statistics.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **error** [ **lsa** | **interface** *interface-type* *interface-number* ] command to check information about OSPFv3 errors.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **next-hop** command to check information about the OSPFv3 next-hop routing table.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **request-list** [ **statistics** | { **area** *area-id* | **peer** *router-id* | **interface** *interface-type* *interface-number* } \* ] command to check information about an OSPFv3 request list.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **retrans-list** [ **statistics** | { **area** *area-id* | **peer** *router-id* | **interface** *interface-type* *interface-number* } \* ] command to check information about an OSPFv3 retransmission list.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **spf-statistics** [ **verbose** ] command to check route calculation statistics in an OSPFv3 process.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **statistics updated-lsa** [ **originate-router** *advertising-router-id* | **history** ] command to check information about the frequent updates of the LSAs that the LSDB receives.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **topology** [ **area** *area-id* ] [ **statistics** | **verbose** ] command to check the topology information in an OSPFv3 area.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id*] **lsdb** **statistics** command to check OSPFv3 LSDB information.