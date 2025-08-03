Monitoring the QinQ Operating Status
====================================

This section describes how to monitor the QinQ operating status.

#### Context

In routine maintenance, you can run the commands in any view to view the QinQ operating status.


#### Procedure

1. Run the [**display qinq statistics**](cmdqueryname=display+qinq+statistics) [ **interface** {  *interface-type interface-number* | *interface-name* } [ **vlan-group** *group-id* ]] [ **verbose** ] command to check QinQ packet statistics.
   
   
   
   The [**statistic enable**](cmdqueryname=statistic+enable) command must be run in the VLAN group view to enable the function of collecting QinQ packet statistics based on VLAN groups before you run the [**display qinq statistics**](cmdqueryname=display+qinq+statistics) command to view the number of QinQ packets sent or received by the sub-interface. These statistics help you deploy QoS policies or locate problems. If the function of collecting QinQ packet statistics is disabled, you cannot view the statistics on the sub-interface.
2. Run the [**display vlan-group**](cmdqueryname=display+vlan-group) [ *group-id* ] **interface** {  *interface-name* | *interface-type interface-number* } command to check the number of VLAN groups on a specified interface and the configuration of each VLAN group.