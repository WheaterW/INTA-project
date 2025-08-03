Monitoring the Running Status of MLD Snooping
=============================================

MLD snooping monitoring commands display IPv6 Layer 2 multicast information, including the enabling status, forwarding table, port table, and protection group information.

#### Context

In routine maintenance, users can run the following commands in any view to view the operating status of MLD snooping.


#### Procedure

* To check MLD snooping configurations, run the [**display mld-snooping**](cmdqueryname=display+mld-snooping) [ **vlan** [ *vlan-id* ] | **vsi** [ *vsi-name* ] ] [**configuration** ] command.
* To check multicast group member ports, run the [**display mld-snooping port-info**](cmdqueryname=display+mld-snooping+port-info) [ **vlan** *vlan-id* [ **group-address** *group-address* ] ] [ **verbose** ] command.
* To check Router ports, run the [**display mld-snooping router-port**](cmdqueryname=display+mld-snooping+router-port) { **vlan** *vlan-id* | **vsi** *vsi-name* } command.
* To check MLD snooping statistics, run the [**display mld-snooping statistics**](cmdqueryname=display+mld-snooping+statistics) { **vlan** [ *vlan-id* ] | **vsi** [ *vsi-name* ] } command.
* To check MLD snooping querier information, run the [**display mld-snooping querier**](cmdqueryname=display+mld-snooping+querier) { **vlan** [ *vlan-id* ] | **vsi** [ *vsi-name* ] } command.