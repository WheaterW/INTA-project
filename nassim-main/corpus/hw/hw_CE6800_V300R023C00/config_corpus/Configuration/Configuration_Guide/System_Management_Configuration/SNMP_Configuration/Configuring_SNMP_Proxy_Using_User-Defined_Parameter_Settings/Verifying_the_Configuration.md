Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Verify the SNMP proxy configuration on the middle-point device.
  
  
  + Run the [**display snmp-agent proxy community**](cmdqueryname=display+snmp-agent+proxy+community) command to check SNMP proxy community information.
  + Run the [**display snmp-agent proxy rule**](cmdqueryname=display+snmp-agent+proxy+rule) command to check proxy rules for SNMP messages.
  + Run the [**display snmp-agent proxy target-host**](cmdqueryname=display+snmp-agent+proxy+target-host) command to check target host information.
  + Run the [**display snmp-agent usm-user**](cmdqueryname=display+snmp-agent+usm-user) command to check SNMPv3 proxy user information.
  + Run the [**display snmp-agent proxy statistics**](cmdqueryname=display+snmp-agent+proxy+statistics) command to check statistics about SNMP proxy messages.
* Verify the SNMP configuration on the managed device.
  
  
  + For SNMPv1, see [Verifying the Configuration](vrp_snmp_cfg_0023.html).
  + For SNMPv2c, see [Verifying the Configuration](vrp_snmp_cfg_0030.html).
  + For SNMPv3, see [Verifying the Configuration](vrp_snmp_cfg_0037.html).