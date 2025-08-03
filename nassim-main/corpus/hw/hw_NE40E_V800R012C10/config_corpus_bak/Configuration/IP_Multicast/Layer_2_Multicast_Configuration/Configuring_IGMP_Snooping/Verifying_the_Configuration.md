Verifying the Configuration
===========================

After configuring IGMP snooping, verify the router port and member port lists, forwarding table, and querier parameters.

#### Prerequisites

The configurations of IGMP snooping have been performed.


#### Procedure

* Run the [**display igmp-snooping**](cmdqueryname=display+igmp-snooping) [ **vlan** [ *vlan-id* ] ] [ **configuration** ] command to check IGMP snooping parameters in a specified VLAN.
* Run the [**display igmp-snooping**](cmdqueryname=display+igmp-snooping) [**vsi** [ *vsi-name* ] ] [ **configuration** ] command to check IGMP snooping parameters in a specified VSI.
* Run the [**display igmp-snooping router-port**](cmdqueryname=display+igmp-snooping+router-port) { **vlan** *vlan-id* | **vsi** *vsi-name* } command to check information about router ports in a specified VLAN or VSI.
* Run the [**display igmp-snooping port-info**](cmdqueryname=display+igmp-snooping+port-info) [ **vlan** *vlan-id* [ **group-address** *group-address* ] | **vsi** *vsi-name* [ **group-address** *group-address* ] ] [ **verbose** ] command to check information about interfaces in a specified VLAN or VSI.