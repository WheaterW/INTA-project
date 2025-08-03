Verifying the Configuration
===========================

After configuring IP services on the VLAN tag termination sub-interface, verify the configuration.

#### Prerequisites

The IP service access configurations on the VLAN tag termination sub-interface have been complete.


#### Procedure

* Run the [**display dot1q information termination**](cmdqueryname=display+dot1q+information+termination) [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check configured dot1q VLAN tag termination information.
* Run the [**display qinq information termination**](cmdqueryname=display+qinq+information+termination) [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check configured QinQ VLAN tag termination information.
* Run the [**display vrrp**](cmdqueryname=display+vrrp) command to check information about the VRRP group.
* Run the [**display dhcp relay address**](cmdqueryname=display+dhcp+relay+address) **all** command to check the DHCP configuration on the interface that has DHCP relay enabled.