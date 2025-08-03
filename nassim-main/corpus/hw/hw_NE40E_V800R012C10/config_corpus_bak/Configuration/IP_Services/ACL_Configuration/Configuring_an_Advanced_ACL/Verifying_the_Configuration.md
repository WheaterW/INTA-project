Verifying the Configuration
===========================

After configuring an advanced ACL, verify the configuration.

#### Prerequisites

An advanced ACL has been configured.


#### Procedure

* Run the [**display acl**](cmdqueryname=display+acl+name+all) { *acl-number* | **name** *acl-name* | **all** } command to check advanced ACL configurations.
* Run the [**display time-range**](cmdqueryname=display+time-range+all) { *time-name* | **all** } command to check the configuration and status within a specified time range or all time ranges.
* Run the [**display acl ip-pool**](cmdqueryname=display+acl+ip-pool+apply-interface-ip) *pool-name* **apply-interface-ip** command to check all the interface IP addresses that meet the conditions and are associated with the address pool.