Verifying the Configuration of DHCPv6 Relay
===========================================

After configuring DHCPv6 relay on a host or router, verify the configuration.

#### Prerequisites

DHCPv6 relay has been configured and the DHCPv6 relay agent is able to forward DHCPv6 messages.


#### Procedure

* Run the [**display dhcpv6 relay statistics**](cmdqueryname=display+dhcpv6+relay+statistics) command to check message statistics on a DHCPv6 relay agent.
* Run the [**display dhcpv6 relay configuration**](cmdqueryname=display+dhcpv6+relay+configuration) command to check global configurations of a DHCPv6 relay agent.
* Run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **dhcpv6** **statistics** **slot** *slot-id* command to check whitelist session-CAR statistics about DHCPv6 messages on a specified interface board.
* Run the [**display dhcpv6 relay interface**](cmdqueryname=display+dhcpv6+relay+interface) { *interface-name* | *interface-type* *interface-num* } command to check the running information about a DHCPv6 relay interface.