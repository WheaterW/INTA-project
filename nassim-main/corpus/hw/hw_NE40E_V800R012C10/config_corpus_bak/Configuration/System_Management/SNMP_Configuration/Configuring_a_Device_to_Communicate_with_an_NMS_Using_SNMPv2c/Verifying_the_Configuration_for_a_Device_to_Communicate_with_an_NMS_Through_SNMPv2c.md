Verifying the Configuration for a Device to Communicate with an NMS Through SNMPv2c
===================================================================================

After configuring basic SNMPv2c functions, verify the configuration.

#### Prerequisites

Basic SNMPv2c functions have been configured.


#### Procedure

* Run the [**display snmp-agent community**](cmdqueryname=display+snmp-agent+community) command to check the configured community name.
* Run the [**display snmp-agent sys-info**](cmdqueryname=display+snmp-agent+sys-info) **version** command to check the enabled SNMP version.
* Run the [**display acl**](cmdqueryname=display+acl) *acl-number* command to check the rules in the specified ACL.
* Run the [**display snmp-agent mib-view**](cmdqueryname=display+snmp-agent+mib-view) command to check the MIB view.
* Run the [**display snmp-agent mib modules**](cmdqueryname=display+snmp-agent+mib+modules) command to check information about a loaded MIB file.
* Run the [**display snmp-agent sys-info**](cmdqueryname=display+snmp-agent+sys-info) **contact** command to check the device administrator's contact information.
* Run the [**display snmp-agent sys-info**](cmdqueryname=display+snmp-agent+sys-info) **location** command to check the location of the Router.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **| include** **max-size** command to check the allowable maximum size of an SNMP packet.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **| include** **trap** command to check trap configuration.
* Run the [**display snmp-agent target-host**](cmdqueryname=display+snmp-agent+target-host) command to check information about the target host.
* Run the [**display snmp-agent inform**](cmdqueryname=display+snmp-agent+inform) command to check Inform parameters of all target hosts or a specified target host.
* Run the [**display snmp-agent notification-log**](cmdqueryname=display+snmp-agent+notification-log) command to check Inform logs stored in the log buffer.
* Run the [**display snmp-agent vacmgroup**](cmdqueryname=display+snmp-agent+vacmgroup) command to check all the configured View-based Access Control Model (VACM) groups.