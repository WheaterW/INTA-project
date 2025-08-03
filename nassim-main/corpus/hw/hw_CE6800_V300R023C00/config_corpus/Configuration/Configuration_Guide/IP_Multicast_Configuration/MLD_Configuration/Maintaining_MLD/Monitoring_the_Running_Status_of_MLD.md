Monitoring the Running Status of MLD
====================================

Monitoring the Running Status of MLD

#### Context

During routine maintenance, you can run the following commands in any view to check the running status of MLD.


#### Procedure

* Run the [**display mld group**](cmdqueryname=display+mld+group) [ *ipv6-group-address* | **interface** *interface-type* *interface-number* ]\* [ **static** ] [ **verbose** ] command to check MLD group information on an interface.
* Run the [**display mld group**](cmdqueryname=display+mld+group) [ *ipv6-group-address* | **interface** *interface-type* *interface-number* ]\* **ssm-mapping** [ **verbose** ] command to check information about MLD groups configured with SSM mapping.
* Run the [**display mld interface**](cmdqueryname=display+mld+interface) [ *interface-type* *interface-number* ] [ **verbose** ] command to check the configurations and operating status of MLD on interfaces.
* Run the [**display mld ssm-mapping**](cmdqueryname=display+mld+ssm-mapping) **group** [ *ipv6-group-address* ] command to check SSM mapping rules of a specified MLD group.
* Run the [**display mld control-message counters**](cmdqueryname=display+mld+control-message+counters) [ **interface** *interface-type* *interface-number* ] [ **message-type** { **query** | **report** } ] command to check statistics about MLD control messages received on an interface.
* Run the [**display mld invalid-packet**](cmdqueryname=display+mld+invalid-packet) [ **interface** *interface-type interface-number* | **message-type** { **done** | **query** | **report** } ]\* command to check statistics about invalid MLD messages received by the device.