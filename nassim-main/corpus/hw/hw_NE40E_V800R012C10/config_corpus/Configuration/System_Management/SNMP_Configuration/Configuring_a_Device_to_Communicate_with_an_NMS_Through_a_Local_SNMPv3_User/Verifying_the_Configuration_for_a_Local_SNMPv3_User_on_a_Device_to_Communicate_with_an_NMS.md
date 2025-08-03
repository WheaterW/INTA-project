Verifying the Configuration for a Local SNMPv3 User on a Device to Communicate with an NMS
==========================================================================================

After configuring basic SNMPv3 functions, verify the configuration.

#### Prerequisites

Basic SNMPv3 functions have been configured.


#### Procedure

* Run the [**display snmp-agent sys-info**](cmdqueryname=display+snmp-agent+sys-info) **version** command to check the enabled SNMP version.
* Run the [**display snmp-agent sys-info**](cmdqueryname=display+snmp-agent+sys-info) **contact** command to check the device administrator's contact information.
* Run the [**display snmp-agent sys-info**](cmdqueryname=display+snmp-agent+sys-info) **location** command to check the location of the Router.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | **include** **max-size** command to check the allowable maximum size of an SNMP packet.
* Run the [**display snmp-agent local-user**](cmdqueryname=display+snmp-agent+local-user) [ **username** *user-name* ] command to check local SNMP user information.