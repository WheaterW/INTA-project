Verifying the Configuration
===========================

After you configure session and bandwidth resources for a dedicated board, you can check the resources assigned by the license.

#### Prerequisites

NAT session and bandwidth resources have been allocated successfully, and the service boards are running properly.


#### Procedure

* Run the [**display nat session-table size**](cmdqueryname=display+nat+session-table+size) [ **slot** *slot-id* ] command to check the session resources allocated to service boards.
* Run the [**display nat bandwidth**](cmdqueryname=display+nat+bandwidth) [ **slot** *slot-id* ] command to check the bandwidth resources allocated to the service board.