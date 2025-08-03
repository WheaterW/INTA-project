Verifying the Configuration
===========================

After you configure session and bandwidth resources for a dedicated board, you can check the resources assigned by the license.

#### Prerequisites

Bandwidth resources have been assigned, and the service board is working properly.


#### Procedure

* Run the [**display nat session-table size**](cmdqueryname=display+nat+session-table+size) [ **slot** *slot-id* ] command to check information about NAT64 session entries assigned to each service board.
* Run the [**display nat bandwidth**](cmdqueryname=display+nat+bandwidth) [ **slot** *slot-id* ] command to check information about bandwidth resources configured in the license.
* Run the [**display nat64 vsuf status**](cmdqueryname=display+nat64+vsuf+status) [ **slot** *slot-id* ] command to check NAT64 license status information.