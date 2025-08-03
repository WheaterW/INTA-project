Verifying the DHCPv6 (IA\_NA) Address Allocation Configuration
==============================================================

After configuring DHCPv6 address allocation, verify the IPv6 address pool, IPv6 prefix pool, and domain configurations and the usage of the address pool bound to the domain.

#### Procedure

* Run the [**display ipv6 pool**](cmdqueryname=display+ipv6+pool) [ *pool-name* ] command to check the IPv6 address pool configurations.
* Run the [**display ipv6 prefix**](cmdqueryname=display+ipv6+prefix) [ *prefix-name* [ **all** | **used** ] ] command to check the IPv6 prefix pool configurations.
* Run the [**display domain**](cmdqueryname=display+domain) [ *domain-name* ] command to check the domain configurations.
* Run the [**display ipv6-pool
  pool-usage**](cmdqueryname=display+ipv6-pool+pool-usage) [ **domain** *domain-name* | **pool-name** [ *pool-name* ] ] command to check the address pool usage
  of all domains or a specified one.
* Run the [**display ipv6-pool
  max-usage**](cmdqueryname=display+ipv6-pool+max-usage) { **pool** [ *pool-name* ] | **domain** [ *domain-name* ] } command in any view to check the historical
  maximum usage of addresses in IPv6 address pools.
* Run the [**display ipv6-pool max-ratio domain**](cmdqueryname=display+ipv6-pool+max-ratio+domain) command to check information about IPv6 address pool or prefix pool usage in all domains on the device.
* Run the [**display ipv6-pool pool-usage**](cmdqueryname=display+ipv6-pool+pool-usage) { **upper-threshold** | **lower-threshold** | **all-threshold** } command to check information about domains whose IPv6 address pool or prefix pool usage exceeds a specified threshold.