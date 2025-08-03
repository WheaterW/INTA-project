Monitoring the Running Status of IGMP Snooping over VXLAN
=========================================================

Monitoring the Running Status of IGMP Snooping over VXLAN

#### Context

To check the running status of IGMP snooping over VXLAN during routine maintenance, run the following commands in any view.


#### Procedure

* Run the [**display igmp snooping querier**](cmdqueryname=display+igmp+snooping+querier) **bridge-domain** [ *bd-id* ] command to check IGMP snooping querier configurations.
* Run the [**display igmp snooping statistics**](cmdqueryname=display+igmp+snooping+statistics) **bridge-domain** [ *bd-id* ] command to check the IGMP snooping statistics.
* Run the [**display igmp snooping group**](cmdqueryname=display+igmp+snooping+group) command to check dynamically learned multicast group information.