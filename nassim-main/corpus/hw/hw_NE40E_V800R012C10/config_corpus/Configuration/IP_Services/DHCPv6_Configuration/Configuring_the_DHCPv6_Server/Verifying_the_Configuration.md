Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display dhcpv6 pool**](cmdqueryname=display+dhcpv6+pool) [ *pool-name* [ { **allocated** | **conflict** } **address** | **binding** [ *duid* ] | *ipv6-address* | *ipv6-prefix* | **allocated** **prefix** ] ] command to check the IPv6 address pool configuration.
* Run the [**display dhcpv6 pool**](cmdqueryname=display+dhcpv6+pool) *pool-name* **all** { **address** | **prefix** } command to check information about all assignable addresses and prefixes in the IPv6 address pool.
* Run the [**display dhcpv6 server**](cmdqueryname=display+dhcpv6+server) { **database** | **interface** { *interface-name* | *interface-type* *interface-number* } | **statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] } command to check information about the DHCPv6 server.