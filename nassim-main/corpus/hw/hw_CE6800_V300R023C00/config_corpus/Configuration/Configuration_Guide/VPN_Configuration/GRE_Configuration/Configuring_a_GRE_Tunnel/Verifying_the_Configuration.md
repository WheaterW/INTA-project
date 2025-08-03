Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) [ *interface-number* ] command to check the operating status of the tunnel interface.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check the IP routing table. The command output shows that the IP routing table contains a route with the tunnel interface as the outbound interface.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command to check the IPv6 routing table. The command output shows that the IPv6 routing table contains an IPv6 route with the tunnel interface as the outbound interface.
* Run the [**ping**](cmdqueryname=ping) **-a** *source-ip-address* *host* command to check whether the two ends of the tunnel can communicate with each other using IPv4 addresses.
* Run the [**ping ipv6**](cmdqueryname=ping+ipv6) **-a** *source-ipv6-address* *destination-ipv6-address* command to check whether the two ends of the tunnel can communicate with each other using IPv6 addresses.