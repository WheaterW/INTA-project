Verifying the Configuration of a Layer 2 Interface-based VLAN
=============================================================

After configuring a Layer 2 interface-based VLAN, verify the configuration.

#### Prerequisites

All functions of a Layer 2 interface-based VLAN have been configured.


#### Procedure

* Run the [**display vlan**](cmdqueryname=display+vlan) command to check VLAN information.
* Run the [**display port vlan**](cmdqueryname=display+port+vlan) command to check information about all interfaces belonging to the configured VLANs.
* Run the [**display port vlan**](cmdqueryname=display+port+vlan) *interface-type interface-number* **active** command to check information about interfaces with specified types and numbers within the configured VLANs.