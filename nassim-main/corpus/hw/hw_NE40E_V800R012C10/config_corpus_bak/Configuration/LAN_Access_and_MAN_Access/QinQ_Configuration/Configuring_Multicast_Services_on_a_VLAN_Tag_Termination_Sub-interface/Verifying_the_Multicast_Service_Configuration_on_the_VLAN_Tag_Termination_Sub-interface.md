Verifying the Multicast Service Configuration on the VLAN Tag Termination Sub-interface
=======================================================================================

After configuring multicast services on a dot1q or QinQ VLAN tag termination sub-interface, verify the configuration.

#### Prerequisites

The multicast services have been configured for a dot1q or QinQ VLAN tag termination sub-interface.


#### Procedure

* Run the [**display dot1q information termination**](cmdqueryname=display+dot1q+information+termination) [ **interface** {*interface-name* |*interface-type interface-number* } ] command to check information about the dot1q VLAN tag termination sub-interface.
* Run the [**display qinq information termination**](cmdqueryname=display+qinq+information+termination) [ **interface** {*interface-name* |*interface-type interface-number* } ] command to check information about the QinQ VLAN tag termination sub-interface.
* Run the [**display igmp-snooping querier**](cmdqueryname=display+igmp-snooping+querier) { **vsi** *vsi-name* | **vlan** *vlan-id* } command to check whether the IGMP querier is configured successfully.
* Run the [**display igmp-snooping router-port**](cmdqueryname=display+igmp-snooping+router-port) { **vsi** *vsi-name* | **vlan** *vlan-id* } command to check whether a static router interface has been configured successfully.
* Run the [**display igmp-snooping port-info**](cmdqueryname=display+igmp-snooping+port-info) [ { **vlan** *vlan-id* | **vsi** *vsi-name* } [ **group-address** *group-address* ] ] [ **verbose** ] command to check information about Layer 2 multicast interfaces.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command to check IGMP configurations on an interface.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **group** [ *group-address* | **interface** *interface-type* *interface-number* ] [ **verbose** ] command to check information about IGMP multicast groups.