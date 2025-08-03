Verifying the Configuration of OSPFv3 Routing Information Control
=================================================================

After controlling OSPFv3 routing information, verify the OSPFv3 LSDB.

#### Prerequisites

OSPFv3 routing information has been controlled.


#### Procedure

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **lsdb** command to view the OSPFv3 LSDB.
* Run either of the following commands to check OSPFv3 route information:
  
  
  + Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **abr-summary-list** [ *ipv6-address* *prefix-length* ] command to check information about the summarized routes on an ABR.
  + Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **asbr-summary** [ *ipv6-address* *prefix-length* ] [ **verbose** ] command to check information about the summarized routes on an ASBR.