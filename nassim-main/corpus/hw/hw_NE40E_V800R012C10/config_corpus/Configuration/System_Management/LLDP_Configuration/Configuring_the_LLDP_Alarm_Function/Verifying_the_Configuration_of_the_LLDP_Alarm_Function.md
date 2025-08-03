Verifying the Configuration of the LLDP Alarm Function
======================================================

After configuring the LLDP alarm function, verify the configuration.

#### Prerequisites

All configurations for the LLDP alarm function are complete.


#### Procedure

* Run the [**display snmp-agent trap feature-name**](cmdqueryname=display+snmp-agent+trap+all) **lldp all** command to check all trap messages about the LLDP module.
* Run the [**display lldp local**](cmdqueryname=display+lldp+local) [ **interface** *interface-type interface-number* ] command to check local LLDP status information on a device.