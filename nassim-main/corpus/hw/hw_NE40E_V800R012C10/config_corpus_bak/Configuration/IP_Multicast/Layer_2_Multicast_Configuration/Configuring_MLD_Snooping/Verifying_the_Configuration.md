Verifying the Configuration
===========================

After MLD snooping is configured, you can view the router port and member port lists, forwarding table, and querier parameters.

#### Prerequisites

MLD snooping has been configured.


#### Procedure

* Run the [**display mld-snooping**](cmdqueryname=display+mld-snooping) [ **vlan** [ *vlan-id* ] ] [ **configuration** ] command to check MLD snooping parameters in a specified VLAN.
* Run the [**display mld-snooping**](cmdqueryname=display+mld-snooping) [**vsi** [ *vsi-name* ] ] [ **configuration** ] command to check all configured MLD snooping parameters in a specified VSI.
* Run the [**display mld-snooping router-port**](cmdqueryname=display+mld-snooping+router-port) { **vlan** *vlan-id* | **vsi** *vsi-name* } command to check information about router ports in a specified VLAN or VSI.
* Run the [**display mld-snooping port-info**](cmdqueryname=display+mld-snooping+port-info) [ **vlan** *vlan-id* [ **group-address** *group-address* ] | **vsi** *vsi-name* [ **group-address** *group-address* ] ] [ **verbose** ] command to check information about ports in a specified VLAN or VSI.
* Run the [**display mld-snooping qinq-port-info**](cmdqueryname=display+mld-snooping+qinq-port-info) **interface** *interface-type interface-number* [ **group-address** *ipv6âgroup-address* ] command to check multicast entries on a specified QinQ/dot1q VLAN tag termination sub-interface.