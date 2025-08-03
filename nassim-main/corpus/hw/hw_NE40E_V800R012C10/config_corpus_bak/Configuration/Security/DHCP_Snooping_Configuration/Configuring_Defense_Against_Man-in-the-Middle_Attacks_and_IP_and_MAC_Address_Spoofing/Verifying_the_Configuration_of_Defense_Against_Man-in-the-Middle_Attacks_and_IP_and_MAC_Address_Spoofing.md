Verifying the Configuration of Defense Against Man-in-the-Middle Attacks and IP/MAC Address Spoofing
====================================================================================================

This section describes how to check the configuration of defense against man-in-the-middle attacks and IP/MAC address spoofing.

#### Prerequisites

The configuration of defense against man-in-the-middle attacks and IP/MAC address spoofing is complete.


#### Procedure

* Run the [**display dhcp snooping global**](cmdqueryname=display+dhcp+snooping+global) command to check the global DHCP snooping information.
* Run the [**display dhcp snooping bind-table**](cmdqueryname=display+dhcp+snooping+bind-table) { **all** | **dynamic** | **interface** *interface-type* *interface-number* | **ip-address** *ip-address* | **mac-address** *mac-address* | **static** | **vlan** *vlan-id* [**interface** *interface-type* *interface-number* ] | **vsi** *vsi-name* | **bridge-domain** *bd-id* } command to check the information about the Dynamic Host Configuration Protocol (DHCP) snooping binding table.
* Run the [**display dhcp snooping**](cmdqueryname=display+dhcp+snooping) { **interface** *interface-type* *interface-number* | **vlan** *vlan-id* [ **interface** *interface-type* *interface-number* ] | **bridge-domain** *bd-id* } command to check the DHCP snooping configuration.
* Run the [**display dhcp option82**](cmdqueryname=display+dhcp+option82) **configuration** [ **interface** *interface-type* *interface-number* | **vlan** *vlan-id* | **bridge-domain** *bd-id* ] command to check the Option 82 configuration.