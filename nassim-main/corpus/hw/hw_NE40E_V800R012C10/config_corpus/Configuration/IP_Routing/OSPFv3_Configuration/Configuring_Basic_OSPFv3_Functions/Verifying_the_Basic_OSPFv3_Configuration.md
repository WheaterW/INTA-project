Verifying the Basic OSPFv3 Configuration
========================================

After configuring basic OSPFv3 functions, verify information about neighbors, interfaces, and the OSPFv3 routing table.

#### Prerequisites

Basic OSPFv3 functions have been configured.


#### Procedure

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] [ **area** *area-id* ] **peer** [ *interface-type* *interface-number* ] [ **verbose** ] command in any view to view information about OSPFv3 neighbors.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] [ **area** *area-id* ] [ *interface-type* *interface-number* ] command in any view to view information about an OSPFv3 interface.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **routing** command in any view to view information about an OSPFv3 routing table.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **cumulative** command in any view to view OSPFv3 statistics.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **error** [ **lsa** | **interface** *interface-type* *interface-number* ] command in any view to view OSPFv3 errors.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **next-hop** command in any view to view the OSPFv3 next-hop routing table.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **request-list** [ **statistics** | [ **area** *area-id* | **peer**  *router-id* | **interface** *interface-type* *interface-number* ] \* ] command in any view to view the statistics of the request list of OSPFv3.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **retrans-list** [ **statistics** | { **area** *area-id* | **peer**  *router-id* | **interface** *interface-type* *interface-number* } \* ] command in any view to view the statistics of the OSPFv3 retransmission list.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **spf-statistics** [ **verbose** ] command in any view to view OSPFv3 route calculation statistics.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **statistics updated-lsa** [ **originate-router** *advertising-router-id* | **history** ] command in any view to view the frequent updates of the Link State Advertisements (LSAs) that the Link-state Database (LSDB) receives.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **topology** [ **area** *area-id* ] [ **statistics** | **verbose** ] command in any view to view information about the topology in an OSPFv3 area.