IPSG Does Not Take Effect on Hosts with Dynamic IP Addresses Because DHCP Snooping Is Not Configured
====================================================================================================

IPSG Does Not Take Effect on Hosts with Dynamic IP Addresses Because DHCP Snooping Is Not Configured

#### Fault Symptom

Hosts can dynamically obtain IP addresses from the DHCP server, but IPSG does not take effect after being enabled.

#### Possible Causes

DHCP is configured, but DHCP snooping is not configured.


#### Procedure

1. Check whether the DHCP snooping binding table exists. When hosts obtain IP addresses through DHCP, IPSG checks packets received by interfaces based on the DHCP snooping binding table. The device automatically generates a DHCP snooping binding table for online hosts only after DHCP snooping is enabled.
   
   
   ```
   [display ip source check user-bind status dynamic](cmdqueryname=display+ip+source+check+user-bind+status+dynamic) [ { interface interface-type interface-number | ip-address ip-address | mac-address mac-address | vlan  vlan-id } * ] [ valid | invalid ] [ slot slot-id ] 
   ```
2. If the DHCP snooping binding table does not exist, configure it according to [Configure a dynamic binding table](galaxy_IPSG_cfg_0011.html#EN-US_TASK_0000001512849694__cmd381714015111).
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After DHCP snooping is configured and the hosts go online again, the device generates DHCP snooping entries for the hosts. IPSG then takes effect. If you enable IPSG but the device does not generate a DHCP snooping binding table, the device rejects all IP packets except DHCP request packets. In this situation, communication between the DHCP hosts and servers is affected. Therefore, before enabling IPSG, configure DHCP snooping to enable the device to generate dynamic binding entries.