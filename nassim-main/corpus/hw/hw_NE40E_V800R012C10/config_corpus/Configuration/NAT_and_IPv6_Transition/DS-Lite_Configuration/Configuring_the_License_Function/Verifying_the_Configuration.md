Verifying the Configuration
===========================

After configuring the license function on a service board, you can view information about the DS-Lite bandwidth allocated by the license.

#### Prerequisites

Bandwidth resources have been assigned, and the service board is working properly.


#### Procedure

* Run the [**display nat session-table size**](cmdqueryname=display+nat+session-table+size) [ **slot** *slot-id* ] command to check information about session table resources assigned to each service board.
* Run the [**display nat bandwidth**](cmdqueryname=display+nat+bandwidth) [ **slot** *slot-id* ] command to check the configured license bandwidth.
* Run the [**display ds-lite vsuf status**](cmdqueryname=display+ds-lite+vsuf+status) [ **slot** *slot-id* ] command to check DS-Lite license status information.