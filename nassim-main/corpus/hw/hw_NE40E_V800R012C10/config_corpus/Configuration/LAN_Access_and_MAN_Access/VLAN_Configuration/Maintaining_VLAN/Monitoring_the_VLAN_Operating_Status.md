Monitoring the VLAN Operating Status
====================================

This section describes how to monitor the VLAN operating status.

#### Context

In routine maintenance, you can run the following command in any view to check the VLAN operating status.


#### Procedure

* Run the [**display vlan**](cmdqueryname=display+vlan) *vlan-id* [**statistics**](cmdqueryname=statistics) command to view VLAN packet statistics.
  
  
  
  Before you run this command to view VLAN packet statistics to locate faults, run the [**statistics enable**](cmdqueryname=statistics+enable) command in the VLAN view to enable VLAN packet statistics collection. If VLAN packet statistics collection is disabled, you cannot obtain statistics.
* Run the [**display vlan**](cmdqueryname=display+vlan) *vlan-id* [**statistics**](cmdqueryname=statistics) command to check statistics about discarded BUM packets in a specified VLAN.
  
  
  
  Before you run the [**display vlan**](cmdqueryname=display+vlan) *vlan-id* [**statistics**](cmdqueryname=statistics) command to check statistics about discarded BUM packets in a VLAN for fault locating, run the [**statistic discard enable**](cmdqueryname=statistic+discard+enable) command in the VLAN view to enable collection on traffic statistics about discarded BUM packets. If you do not run the **statistic discard enable** command, the statistics cannot be collected.
* Run the [**display statistics**](cmdqueryname=display+statistics) **interface** *interface-type interface-number* **vlan** *vlan-id* command to view statistics about both sent and received packets on a specific interface in a specific VLAN.
  
  
  
  To view packet statistics on a specified interface in a specified VLAN for fault locating, run the [**statistics enable vlan**](cmdqueryname=statistics+enable+vlan) command in the interface view to enable VLAN-based packet statistics collection on the interface. If the [**statistics enable vlan**](cmdqueryname=statistics+enable+vlan) command is not executed, statistics cannot be displayed.
* Run the [**monitor interface-vlan-statistics**](cmdqueryname=monitor+interface-vlan-statistics) **interface** *interface-type* *interface-number* **vlan** *vlan-id* [ **interval** *interval-value* | **times** { *times-value* | **infinity** } ] command to monitor traffic statistics on an interface of a specified VLAN.