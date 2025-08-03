Monitoring the Operating Status of MLD
======================================

To monitor the operating status of MLD, check information about MLD groups, Source-Specific Multicast (SSM) mapping, MLD-enabled interfaces, and MLD routing tables.

#### Context

Run the following commands in any view to check the MLD operating status.


#### Procedure

* Run the [**display mld group**](cmdqueryname=display+mld+group) [ *ipv6-group-address* | **interface** *interface-type* *interface-number* ] \* [ **static** ] [ **verbose** ] command to check MLD group information on an interface.
* Run the [**display mld group**](cmdqueryname=display+mld+group) [ *ipv6-group-address* | **interface** *interface-type* *interface-number* ] \* **ssm-mapping** [ **verbose** ] command to check MLD groups configured with SSM mapping.
* Run the [**display mld interface**](cmdqueryname=display+mld+interface) [ *interface-type* *interface-number* ] [ **verbose** ] command to check the configurations and operating status of MLD on an interface.
* Run the [**display mld ssm-mapping**](cmdqueryname=display+mld+ssm-mapping) **group** [ *ipv6-group-address* ] command to check SSM mapping rules of a specified MLD group.
* Run the [**display mld control-message counters**](cmdqueryname=display+mld+control-message+counters) [ **interface** *interface-type* *interface-number* ] [ **message-type** { **query** | **report** } ] command to check the statistics of MLD messages received by the interface.