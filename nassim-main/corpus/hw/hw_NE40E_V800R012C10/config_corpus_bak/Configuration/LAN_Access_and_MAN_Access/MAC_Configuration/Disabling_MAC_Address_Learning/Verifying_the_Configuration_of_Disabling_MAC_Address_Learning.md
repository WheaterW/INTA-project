Verifying the Configuration of Disabling MAC Address Learning
=============================================================

After disabling MAC address learning on an interface and in a VLAN, verify the configuration.

#### Prerequisites

MAC address learning has been disabled on an interface and in a VLAN.
#### Procedure

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **interface** *interface-type interface-number* command to check whether MAC address learning has been disabled on this interface.
* Run the [**display vlan**](cmdqueryname=display+vlan) [ *vlan-id* [ **verbose** ] ] command to check whether MAC address learning has been disabled in this VLAN.