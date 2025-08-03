Verifying the Configuration of an Advanced ACL6
===============================================

After configuring an advanced ACL6, verify the configuration.

#### Prerequisites

An advanced ACL6 has been configured.


#### Procedure

* Run the [**display acl ipv6**](cmdqueryname=display+acl+ipv6+name+all) { *acl6-number* | **name** *acl6-name* | **all** } command to check advanced ACL6 configurations.
* Run the [**display time-range**](cmdqueryname=display+time-range+all) { *time-name* | **all** } command to check the configuration of a specified or all validity periods.
* Run the [**display acl ipv6-pool**](cmdqueryname=display+acl+ipv6-pool+apply-interface-ipv6) *pool-name* **apply-interface-ipv6** command to check all the interface IPv6 addresses that meet the conditions and are associated with the address pool.