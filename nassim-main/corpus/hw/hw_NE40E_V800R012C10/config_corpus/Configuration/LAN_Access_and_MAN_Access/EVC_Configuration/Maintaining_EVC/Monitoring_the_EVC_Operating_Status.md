Monitoring the EVC Operating Status
===================================

This section describes how to monitor the EVC operating status.

#### Context

In routine maintenance, you can run the following command in any view to view the EVC operating status.


#### Procedure

* Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) *bd-id* **statistics** command to view packet statistics in a specified bridge domain.
  
  
  
  Before you run the [**display bridge-domain statistics**](cmdqueryname=display+bridge-domain+statistics) command to view VLAN packet statistics and locate faults, run the [**statistic enable**](cmdqueryname=statistic+enable) command in the specific BD view to enable the device to collect VLAN packet statistics. If the device is disabled from collecting VLAN packet statistics, you cannot obtain the statistics.
* Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) *bd-id* **statistics** command to check statistics about discarded BUM packets in a specified BD.
  
  
  
  Before you run the [**display bridge-domain statistics**](cmdqueryname=display+bridge-domain+statistics) command to check statistics about discarded BUM packets in a BD for fault locating, run the [**statistic discard enable**](cmdqueryname=statistic+discard+enable) command in the BD view to enable collection of statistics about discarded BUM packets. If you do not run the [**statistics discard enable**](cmdqueryname=statistics+discard+enable) command, the statistics cannot be collected.
* Run the [**display ethernet uni statistics**](cmdqueryname=display+ethernet+uni+statistics) **interface** *interface-type interface-number.subinterface-number* [ **verbose** ] command to view traffic statistics on an EVC Layer 2 sub-interface.
  
  
  
  Before running the [**display ethernet uni statistics**](cmdqueryname=display+ethernet+uni+statistics) command, you must run the [**statistic enable mode**](cmdqueryname=statistic+enable+mode) **multiple** command in the EVC Layer 2 sub-interface view to enable traffic statistics collection in multiple mode.
  
  Before obtaining new traffic statistics on an EVC Layer 2 sub-interface, you can run the [**reset ethernet uni statistics interface**](cmdqueryname=reset+ethernet+uni+statistics+interface) { *interface-type interface-number.subinterface-number* | *interface-name* } command to clear the existing statistics. This facilitates subsequent query of new statistics.