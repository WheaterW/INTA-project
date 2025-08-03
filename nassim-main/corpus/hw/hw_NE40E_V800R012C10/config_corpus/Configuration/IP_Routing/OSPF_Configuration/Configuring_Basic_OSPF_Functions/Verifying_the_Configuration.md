Verifying the Configuration
===========================

After configuring basic OSPF functions, verify information about OSPF neighbors, interfaces, and routes.

#### Prerequisites

Basic OSPF functions have been configured.


#### Procedure

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **abr-asbr** [ *router-id* ] command in any view to check information about the ABRs and ASBRs of OSPF.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **cumulative** command in any view to check information about OSPF statistics.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **peer** command in any view to check information about OSPF neighbors.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **nexthop** command in any view to check information OSPF next hop information.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **error** [ **lsa** | **interface** *interface-type* *interface-number* ] command in any view to check information about OSPF error information.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **vlink** command in any view to check information about OSPF virtual links.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command in any view to check information about OSPF interfaces.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command in any view to check information about the OSPF routing table.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **topology** [ **area** *area-id* ] [ **statistics** | **verbose** ] command in any view to check information about the topology calculated for OSPF routes.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **spf-statistics** [ **verbose** ] command in any view to check information about route calculation statistics in OSPF processes.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **request-queue** [ *interface-type* *interface-number* ] [ *neighbor-id* ] command in any view to check information about OSPF request list.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **retrans-queue** [ *interface-type* *interface-number* ] [ *neighbor-id* ] command in any view to check information about OSPF retransmission list.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **statistics** **updated-lsa** [ **originate-router** *advertising-router-id* | **history** ] command in any view to check information about the frequent updates of the LSAs that the LSDB receives
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **statistics** **maxage-lsa** command to check information about router LSAs that have reached the aging time.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **router-id conflict** command in any view to check information about router ID conflicts (if any).