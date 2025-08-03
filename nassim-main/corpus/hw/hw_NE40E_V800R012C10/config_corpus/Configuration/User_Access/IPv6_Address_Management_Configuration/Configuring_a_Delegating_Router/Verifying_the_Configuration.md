Verifying the Configuration
===========================

After configuring a delegating router, you can view the configurations of IPv6 address pool, the prefix pool, and statistics about the DHCPv6 server.

#### Procedure

* Run the [**display ipv6 pool**](cmdqueryname=display+ipv6+pool) [ *pool-name* ] command to check the configurations of all IPv6 address pools or a specific one.
* Run the [**display ipv6 prefix**](cmdqueryname=display+ipv6+prefix) [ *prefix-name* [ **all** | **used** | *start-ipv6-prefix* [ *end-ipv6-prefix* ] ] ] command to check the configurations of all IPv6 prefix pools or a specific one.
* Run the [**display dhcpv6 upgrade**](cmdqueryname=display+dhcpv6+upgrade) command to check the lease configuration of DHCPv6 users so that the time when the device restarts can be determined.
* Run the [**display dhcpv6-access user-table**](cmdqueryname=display+dhcpv6-access+user-table) { **mac-address** *mac-address* [ [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* } [ **pe-vlan** *pevlan-id* [ **ce-vlan** *cevlan-id* ]] | **index** *index* | **prefix** *prefix-address* | **interface** { *interface-name* | *interface-type* *interface-number* } | **vpn-instance** *vpn-instance* | **user-id** *user-id* | **all** } command to check detailed information about online DHCPv6 users.
* Run the [**display dhcpv6-access statistic**](cmdqueryname=display+dhcpv6-access+statistic) command to check statistics about packets exchanged between DHCPv6 users and the DHCPv6 server.
* Run the [**display ipv6-pool max-ratio domain**](cmdqueryname=display+ipv6-pool+max-ratio+domain) command to check information about IPv6 address pool or prefix pool usage in all domains on the device.
* Run the [**display ipv6-pool pool-usage**](cmdqueryname=display+ipv6-pool+pool-usage) { **upper-threshold** | **lower-threshold** | **all-threshold** } command to check information about domains whose IPv6 address pool or prefix pool usage exceeds a specified threshold.