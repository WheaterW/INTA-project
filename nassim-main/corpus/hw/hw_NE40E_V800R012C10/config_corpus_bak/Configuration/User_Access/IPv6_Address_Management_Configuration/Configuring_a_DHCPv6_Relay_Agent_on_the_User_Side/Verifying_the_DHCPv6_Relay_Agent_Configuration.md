Verifying the DHCPv6 Relay Agent Configuration
==============================================

After configuring a DHCPv6 relay agent, verify the DHCPv6 server group configurations, including the DHCP unique identifier (DUID) and the address pool bound to the domain.

#### Procedure

* Run the [**display ipv6 pool**](cmdqueryname=display+ipv6+pool) [ *pool-name* ] command to check the configurations of all IPv6 address pools or a specified one.
* Run the [**display ipv6 prefix**](cmdqueryname=display+ipv6+prefix) [ *prefix-name* [ **all** | **used** ] ] command to check the configurations of all IPv6 prefix pools or a specified one.
* Run the [**display dhcpv6-server statistics**](cmdqueryname=display+dhcpv6-server+statistics) { *ipv6-address* [ **vpn-instance** *vpn-instance* ] | **interface** *interface-type interface-number* } command to check packet statistics on a DHCPv6 server.
* Run the [**display dhcpv6-server item**](cmdqueryname=display+dhcpv6-server+item) { *ipv6-address* [ **vpn-instance** *vpn-instance* ] | **interface** *interface-type interface-number* } command to check information about a DHCPv6 server.
* Run the [**display ipv6-pool max-ratio domain**](cmdqueryname=display+ipv6-pool+max-ratio+domain) command to check the maximum IPv6 address pool or prefix pool usage of each domain on the device.
* Run the [**display ipv6-pool pool-usage**](cmdqueryname=display+ipv6-pool+pool-usage) { **upper-threshold** | **lower-threshold** | **all-threshold** } command to check information about domains whose IPv6 address pool or prefix pool usage exceeds a specified threshold.
* Run the [**display cpu-defend whitelist-v6 session-car dhcpv6-server statistics slot**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car+dhcpv6-server+statistics+slot) *slot-id* command to check DHCPV6-SERVER protocol whitelist session-CAR statistics on a specified interface board.