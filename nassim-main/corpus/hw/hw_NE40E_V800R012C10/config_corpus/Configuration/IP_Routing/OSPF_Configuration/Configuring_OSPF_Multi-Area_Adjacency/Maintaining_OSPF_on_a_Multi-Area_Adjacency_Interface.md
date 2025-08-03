Maintaining OSPF on a Multi-Area Adjacency Interface
====================================================

Maintaining OSPF on a Multi-Area Adjacency Interface

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

OSPF statistics cannot be restored after being cleared. Therefore, exercise caution before clearing the OSPF statistics.

To clear OSPF statistics, run the following command in the user view.


#### Procedure

* Run [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **counters** [ **neighbor** [ *interface-type* *interface-number* [ **all-areas** | **area** *area-id* ] ] | [ *interface-name* [ **all-areas** | **area** *area-id* ] ] [ *router-id* ] ]
  
  
  
  OSPF statistics are cleared.