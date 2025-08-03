Monitoring the IGMP Snooping Running Status
===========================================

Monitoring the IGMP Snooping Running Status

#### Context

To check the IGMP snooping running status during routine maintenance, run the following commands in any view.


#### Procedure

* Run the [**display igmp snooping**](cmdqueryname=display+igmp+snooping) [ **vlan** [ *vlan-id* ] ] command to check the IGMP snooping running parameters of VLANs.
* Run the [**display igmp snooping**](cmdqueryname=display+igmp+snooping) [ **vlan** [ *vlan-id* ] ] **configuration** command to check the IGMP snooping configuration of VLANs.
* Run the [**display igmp snooping qinq-port-info**](cmdqueryname=display+igmp+snooping+qinq-port-info) **interface** *interface-type interface-number* command to check interface information entries of multicast groups on an interface.
* Run the [**display igmp snooping router-port**](cmdqueryname=display+igmp+snooping+router-port) [ **vlan** *vlan-id* ] command to check the router port information.
* Run the [**display igmp snooping querier**](cmdqueryname=display+igmp+snooping+querier) **vlan** [ *vlan-id* ] command to check the IGMP snooping querier information.
* Run the [**display igmp snooping statistics**](cmdqueryname=display+igmp+snooping+statistics) **vlan** [ *vlan-id* ] command to check the IGMP snooping statistics.
* Run the [**display igmp snooping group**](cmdqueryname=display+igmp+snooping+group) [ **interface** { *interface-type* *interface-number* | *interface-name* } { **vlan** *vlan-id* | **pe-vid** *pe-vid* [ **ce-vid** *ce-vid* ] } [ **bridge-domain** *bd-id* ] [ [ **source-address** *source-address* ] **group-address** *group-address* ] ] command to check dynamically learned multicast group information.