Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display multicast routing-table**](cmdqueryname=display+multicast+routing-table) [ **vpn-instance** *vpn-instance-name* ] **static** [ **config** ] [ *prefix* { *mask* | *masklength* } ] command to check whether the configured multicast static route takes effect.
* Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **rpf-info** *source-address* [ *group-address* ] [ **rpt** | **spt** ] [ **verbose** ] command to check the RPF route information of a specific multicast source.
* Run the [**display mrt routing-table**](cmdqueryname=display+mrt+routing-table) [ **vpn-instance** *vpn-instance-name* ] **statistics** command to check statistics about a specified multicast routing table.