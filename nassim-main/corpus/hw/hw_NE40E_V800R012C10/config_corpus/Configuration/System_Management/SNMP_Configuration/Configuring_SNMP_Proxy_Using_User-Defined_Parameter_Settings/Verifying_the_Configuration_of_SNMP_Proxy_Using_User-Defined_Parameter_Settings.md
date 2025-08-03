Verifying the Configuration of SNMP Proxy Using User-Defined Parameter Settings
===============================================================================

After configuring SNMP proxy using user-defined parameters, verify the SNMP configuration on the managed device and check whether the middle-point device communicates with the managed device based on user-defined parameter settings.

#### Prerequisites

SNMP proxy has been configured using user-defined parameter settings.


#### Procedure

* Verify the SNMP proxy configuration on the middle-point device.
  
  
  + Run the [**display snmp-agent proxy community**](cmdqueryname=display+snmp-agent+proxy+community) command to check SNMP proxy community information.
  + Run the [**display snmp-agent proxy rule**](cmdqueryname=display+snmp-agent+proxy+rule) command to check proxy rules for SNMP packets.
  + Run the [**display snmp-agent proxy target-host**](cmdqueryname=display+snmp-agent+proxy+target-host) command to check target host information.
  + Run the [**display snmp-agent usm-user**](cmdqueryname=display+snmp-agent+usm-user) command to check SNMPv3 proxy user information.
  + Run the [**display snmp-agent proxy statistics**](cmdqueryname=display+snmp-agent+proxy+statistics) command to check statistics about SNMP proxy packets.
* Verify the SNMP configuration on the managed device.
  
  
  + For SNMPv1, see [Verifying the Configuration for a Device to Communicate with an NMS Through SNMPv1](dc_vrp_snmp_cfg_0008.html).
  + For SNMPv2c, see [Verifying the Configuration for a Device to Communicate with an NMS Through SNMPv2c](dc_vrp_snmp_cfg_0014.html).
  + For SNMPv3, see [Verifying the Configuration for a Device to Communicate with an NMS Using an SNMPv3 USM User](dc_vrp_snmp_cfg_0021.html).