Clearing QinQ Statistics
========================

Clear existing QinQ packet statistics before you are able to collect statistics about QinQ packets for a specific period of time.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics about QinQ packets cannot be restored after they are cleared. Exercise caution before you decide to clear the statistics.

To clear QinQ packet statistics, run the following command in the user view:


#### Procedure

1. Run the [**reset qinq statistics**](cmdqueryname=reset+qinq+statistics) **interface** *interface-type interface-number.subinterface-number* **vlan-group** *group-id* command to clear statistics about QinQ packets on the specified interface.