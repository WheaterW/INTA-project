Clearing DHCPv6 Relay Statistics
================================

This section describes how to use the reset command to clear DHCPv6 relay message statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

DHCPv6 relay statistics cannot be restored after they are cleared. Exercise caution when running the reset commands.



#### Procedure

* Run the [**reset dhcpv6 relay statistics**](cmdqueryname=reset+dhcpv6+relay+statistics) command to clear DHCPv6 relay message statistics.
* Run the [**reset dhcpv6 relay userinfo table**](cmdqueryname=reset+dhcpv6+relay+userinfo+table) command to clear DHCPv6 client information on a DHCPv6 relay agent so that all resources allocated to clients are released.
* Run the [**reset dhcpv6 relay client-info**](cmdqueryname=reset+dhcpv6+relay+client-info) command to clear DHCPv6 client login and logout records on a DHCPv6 relay agent.
* Run the [**reset cpu-defend whitelist-v6 session-car**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car) **dhcpv6** **statistics** **slot** *slot-id* command to clear whitelist session-CAR statistics about DHCPv6 messages on a specified interface board.