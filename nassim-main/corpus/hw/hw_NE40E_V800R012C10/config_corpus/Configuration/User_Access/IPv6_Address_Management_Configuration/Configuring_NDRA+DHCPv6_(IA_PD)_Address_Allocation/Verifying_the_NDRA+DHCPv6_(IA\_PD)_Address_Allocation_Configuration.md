Verifying the NDRA+DHCPv6 (IA\_PD) Address Allocation Configuration
===================================================================

After configuring NDRA+DHCPv6 (IA\_PD) address allocation, verify the IPv6 address pool, IPv6 prefix pool, and domain configurations and the usage of the address pool bound to the domain.

#### Procedure

* Run the [**display ipv6 pool**](cmdqueryname=display+ipv6+pool) [ *pool-name* ] command to check the configurations of all IPv6 address pools or a specified one.
* Run the [**display ipv6 prefix**](cmdqueryname=display+ipv6+prefix) [ *prefix-name* [ **all** | **used** ] ] command to check the configurations of all IPv6 prefix pools or a specified one.
* Run the [**display domain**](cmdqueryname=display+domain) [ *domain-name* ] command to check the configurations of all domains or a specified one.
* Run the [**display ipv6-pool
  pool-usage**](cmdqueryname=display+ipv6-pool+pool-usage) [ **domain** *domain-name* | **pool-name** [ *pool-name* ] ] command to check the address pool usage
  of all domains or a specified one.
* Run the [**display ipv6-pool max-ratio domain**](cmdqueryname=display+ipv6-pool+max-ratio+domain) command to check the maximum IPv6 address pool or prefix pool usage in each domain on the device.
* Run the [**display ipv6-pool pool-usage**](cmdqueryname=display+ipv6-pool+pool-usage) { **upper-threshold** | **lower-threshold** | **all-threshold** } command to check information about domains whose IPv6 address pool or prefix pool usage exceeds a specified threshold.