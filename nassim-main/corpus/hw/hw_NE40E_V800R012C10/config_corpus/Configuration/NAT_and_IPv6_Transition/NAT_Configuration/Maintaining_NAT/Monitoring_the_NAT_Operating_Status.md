Monitoring the NAT Operating Status
===================================

You can use [**display**](cmdqueryname=display) commands to monitor the NAT operating status.

#### Context

In routine maintenance, you can run the following commands in any view to check the NAT running status.


#### Procedure

* Run the [**display nat flow-defend**](cmdqueryname=display+nat+flow-defend) command to check the configured rate at which the first packet is sent to create sessions for a user.
* Run the [**display nat instance**](cmdqueryname=display+nat+instance) command to check the configuration of a NAT instance.
* Run the [**display nat memory-usage**](cmdqueryname=display+nat+memory-usage) command to check entry-specific memory usage on a NAT service board.
* Run the [**display nat session aging-time**](cmdqueryname=display+nat+session+aging-time) command to check the configured aging time for NAT session entries.
* Run the [**display nat session table**](cmdqueryname=display+nat+session+table) command to check NAT session entry information.
* Run the [**display nat statistics**](cmdqueryname=display+nat+statistics) command to check NAT service statistics.
* Run the [**display nat user-information**](cmdqueryname=display+nat+user-information) command to check NAT user information.
* Run the [**display nat server-map**](cmdqueryname=display+nat+server-map) command to check server-map entry information about one or more internal servers.
* Run the [**display nat syslog flexible session template**](cmdqueryname=display+nat+syslog+flexible+session+template) command in any view to check the log format of a flexible log template.
* Run the [**display nat statistics port-usage distribute**](cmdqueryname=display+nat+statistics+port-usage+distribute) command in any view to check statistics about users who are assigned a specified port range.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.