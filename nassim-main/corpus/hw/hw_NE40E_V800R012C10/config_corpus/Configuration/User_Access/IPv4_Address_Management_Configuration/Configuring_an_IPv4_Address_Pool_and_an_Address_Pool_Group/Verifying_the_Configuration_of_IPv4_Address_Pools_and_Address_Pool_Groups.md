Verifying the Configuration of IPv4 Address Pools and Address Pool Groups
=========================================================================

After configuring IPv4 address pools or pool groups, verify the configurations of all IP address pools or pool groups. You can also verify the configurations of a specified IP address pool or pool group.

#### Prerequisites

IPv4 address pools or pool groups have been configured.


#### Procedure

* Run the [**display ip pool**](cmdqueryname=display+ip+pool) [ **name** *pool-name* [ *section-num* [ *start-ip-address* [ *end-ip-address* ] ] | **all** | **used** ] ] [ **vpn-instance** *instance-name* ] command to check the configurations of all IP address pools or a specified one.
* Run the [**display ip pool-group**](cmdqueryname=display+ip+pool-group) [ **name** *group-name* ] [ **vpn-instance** *instance-name* ] command to check the configurations of all IP address pool groups or a specified one.
* Run the [**display ip-pool pool-usage**](cmdqueryname=display+ip-pool+pool-usage) [ **domain** *dname* | **pool-name** [ *pool-name* ] ] command to check the address pool usage of all domains or a specified one.
* Run the [**display ip-pool max-ratio domain**](cmdqueryname=display+ip-pool+max-ratio+domain) command to check the maximum address pool usage of each domain on the device.
* Run the [**display ip-pool pool-usage**](cmdqueryname=display+ip-pool+pool-usage) { **upper-threshold** | **lower-threshold** | **all-threshold** } command to check the usage of the IPv4 address pool in a domain when the threshold is exceeded.