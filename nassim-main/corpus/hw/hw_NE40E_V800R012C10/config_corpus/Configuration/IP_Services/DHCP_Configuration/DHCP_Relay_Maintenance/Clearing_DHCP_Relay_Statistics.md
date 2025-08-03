Clearing DHCP Relay Statistics
==============================

This section describes how to clear DHCP relay statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

DHCP relay statistics cannot be restored after they are cleared. Exercise caution when running the [**reset dhcp relay statistics**](cmdqueryname=reset+dhcp+relay+statistics) command.



#### Procedure

* Run the [**reset dhcp relay statistics**](cmdqueryname=reset+dhcp+relay+statistics) command in user view to clear message statistics on the DHCP relay agent.
* Run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **dhcp** **statistics** **slot** *slot-id* command to clear whitelist session-CAR statistics about DHCP messages on a specified interface board.
* Run the [**reset dhcp relay proxy user**](cmdqueryname=reset+dhcp+relay+proxy+user) command in the user view to clear DHCP proxy user entries on the DHCP relay agent.