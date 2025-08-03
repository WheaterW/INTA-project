Verifying the Configuration of Adjusting DS-Lite Performance
============================================================

After configuring the DS-Lite performance parameters, you can run display commands to verify the configuration.

#### Prerequisites

Basic DS-Lite functions have been configured.


#### Procedure

* Run the [**display nat session aging-time**](cmdqueryname=display+nat+session+aging-time) command to check the configured aging time for DS-Lite session entries.
* Run the [**display nat session-table size**](cmdqueryname=display+nat+session-table+size) [ **slot** *slot-id* ] command to check information about DS-Lite session entries assigned to each service board.