Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **abr-asbr** [ *router-id* ] command to check information about the ABRs and ASBRs.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **cumulative** command to check OSPF statistics.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **peer** command to check information about OSPF neighbors.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **nexthop** command to check information about OSPF next hops.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **error** [ **lsa** | **interface** *interface-type* *interface-number* ] command to check information about OSPF errors.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check information about the OSPF interface.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command to check information about the OSPF routing table.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **topology** [ **area** *area-id* ] [ **statistics** | **verbose** ] command to check information about the topology based on which OSPF routes are calculated.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **spf-statistics** [ **verbose** ] command to check route calculation statistics in an OSPF process.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **request-queue** [ *interface-type* *interface-number* ] [ *neighbor-id* ] command to check information about an OSPF request list.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **statistics** **updated-lsa** [ **originate-router** *adv-rtr-id* | **history** ] command to check information about the frequent updates of the LSAs that the LSDB receives.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **router-id conflict** command to check information about router ID conflicts (if any).
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id*] **lsdb** [ **brief**] command to check OSPF LSDB information.