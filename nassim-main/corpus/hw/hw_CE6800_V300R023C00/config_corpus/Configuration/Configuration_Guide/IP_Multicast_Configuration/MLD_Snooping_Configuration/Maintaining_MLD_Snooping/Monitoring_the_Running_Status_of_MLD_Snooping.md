Monitoring the Running Status of MLD Snooping
=============================================

Monitoring the Running Status of MLD Snooping

#### Context

In routine maintenance, users can run the following commands in any view to view the operating status of MLD snooping.


#### Procedure

* Run the [**display mld snooping**](cmdqueryname=display+mld+snooping) [ **vlan** [ *vlan-id* ] ] command to check MLD snooping running parameters of a VLAN.
* Run the [**display mld snooping**](cmdqueryname=display+mld+snooping) [ **vlan** [ *vlan-id* ] ] **configuration** command to check the MLD snooping configuration of a VLAN.
* Run the [**display mld snooping port-info**](cmdqueryname=display+mld+snooping+port-info) [ **vlan***vlan-id* [ **group-address** *ipv6-group-address* ] ] [ **slot** *slot-id* ] [ **verbose** ] command to check information about member ports.
* Run the [**display mld snooping router-port**](cmdqueryname=display+mld+snooping+router-port) [ **vlan** *vlan-id* ] command to check router port information.
* Run the [**display mld snooping querier**](cmdqueryname=display+mld+snooping+querier) **vlan** [ *vlan-id* ] command to check information about the MLD snooping querier.
* Run the [**display mld snooping statistics**](cmdqueryname=display+mld+snooping+statistics) **vlan** [ *vlan-id* ] command to check MLD snooping statistics.
* Run the [**display mld snooping group**](cmdqueryname=display+mld+snooping+group) [ **interface** { *interface-type* *interface-number* | *interface-name* } **vlan** *vlan-id* [ [ **source-address** *source-address* ] **group-address** *group-address* ] ] command to check information about dynamically learned multicast groups.