Verifying the Configuration
===========================

After configuring static Layer 2 multicast, verify the port information table and Layer 2 multicast forwarding table to verify that the static Layer 2 multicast configurations are complete.

#### Prerequisites

The static Layer 2 multicast configurations are complete.


#### Procedure

* Run the [**display igmp-snooping router-port**](cmdqueryname=display+igmp-snooping+router-port) { **vlan** *vlan-id* | **vsi** *vsi-name* } command to check router port information.
* Run the [**display igmp-snooping port-info**](cmdqueryname=display+igmp-snooping+port-info) [ **vlan** *vlan-id* [ **group-address** *group-address* ] | **vsi** *vsi-name* [ **group-address** *group-address* ] ] [ **verbose** ] command to check information about static multicast group member ports.