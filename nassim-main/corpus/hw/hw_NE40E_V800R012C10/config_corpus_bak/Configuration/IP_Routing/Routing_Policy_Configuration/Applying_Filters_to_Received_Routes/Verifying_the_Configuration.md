Verifying the Configuration
===========================

After applying filters to the received routes, check information about the routing table of each protocol.

#### Prerequisites

Filters have been applied to the received routes.
#### Procedure

* Run the [**display rip**](cmdqueryname=display+rip) *process-id* [**route**](cmdqueryname=route) command to check information about the RIP routing table.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] [**routing**](cmdqueryname=routing) command to check information about the OSPF routing table.
* Run the [**display isis**](cmdqueryname=display+isis) [ *process-id* ] [**route**](cmdqueryname=route) command to check information about the IS-IS routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check information about the IP routing table.
  
  
  
  Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on the local Router, and you can view that the routes matching the filtering rules of the neighbor have been filtered out or the **apply** action has been performed.