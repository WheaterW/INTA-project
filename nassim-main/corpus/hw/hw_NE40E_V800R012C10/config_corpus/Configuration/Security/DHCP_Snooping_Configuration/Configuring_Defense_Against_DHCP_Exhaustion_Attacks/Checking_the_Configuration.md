Checking the Configuration
==========================

This section describes how to check the configuration of defense against the attacker from sending bogus Dynamic Host Configuration Protocol (DHCP) packets for extending the IP address leases.

#### Prerequisites

The configurations of defense against the attacker from sending bogus DHCP packets for extending the IP address leases are complete.


#### Procedure

* Run the [**display dhcp snooping**](cmdqueryname=display+dhcp+snooping) { **interface** *interface-type* *interface-number* | **vlan** *vlan-id* [ **interface** *interface-type* *interface-number* ] | **bridge-domain** *bd-id* } command to check the DHCP snooping configuration.
* Run the [**display dhcp option82**](cmdqueryname=display+dhcp+option82) **configuration** [ **interface** *interface-type* *interface-number* | **vlan** *vlan-id* | **bridge-domain** *bd-id* ] command to check the configuration of the option 82 field insertion function.