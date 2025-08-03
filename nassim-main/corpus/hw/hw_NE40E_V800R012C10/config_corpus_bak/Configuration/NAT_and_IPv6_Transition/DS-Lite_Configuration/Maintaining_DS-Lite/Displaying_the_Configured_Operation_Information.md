Displaying the Configured Operation Information
===============================================

You can use **display** commands to monitor the DS-Lite operating status.

#### Context

In routine maintenance, you can run the following commands in any view to check the running status of DS-Lite services.


#### Procedure

* Run the [**display nat flow-defend**](cmdqueryname=display+nat+flow-defend) command to check the rate at which the first packet is sent to create a flow.
* Run the [**display ds-lite instance**](cmdqueryname=display+ds-lite+instance) command to check the configuration of a DS-Lite instance.
* Run the [**display nat memory-usage**](cmdqueryname=display+nat+memory-usage) command to check usage of each entry in memory of a service board.
* Run the [**display nat session aging-time**](cmdqueryname=display+nat+session+aging-time) command to check the configured aging time for DS-Lite session entries.
* Run the [**display nat session table**](cmdqueryname=display+nat+session+table) command to check DS-Lite session entry information.
* Run the [**display nat statistics**](cmdqueryname=display+nat+statistics) command to check DS-Lite service statistics.
* Run the [**display nat user-information**](cmdqueryname=display+nat+user-information) command to check DS-Lite user information.
* Run the [**display nat server-map**](cmdqueryname=display+nat+server-map) command to view server-map entry information about internal servers.