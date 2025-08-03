Some Users Cannot Obtain IP Addresses After DHCP Snooping Is Enabled
====================================================================

Some Users Cannot Obtain IP Addresses After DHCP Snooping Is Enabled

#### Fault Symptom

Some users cannot obtain IP addresses after DHCP snooping is enabled.



#### Possible Causes

The number of DHCP users on the user-side interface has reached the configured maximum value.



#### Procedure

1. Check whether the number of DHCP access users has reached the configured maximum value.
   
   
   * Check whether **Dhcp user(dhcpv4) max number:** *XX* exists in the command output in the system, VLAN, or user-side interface view.
     ```
     display dhcp snooping [ [interface](cmdqueryname=interface) interface-type interface-number | vlan vlan-id | [bridge-domain](cmdqueryname=bridge-domain) bd-id ]
     ```
   * Check the number of DHCP snooping binding entries generated on the DHCP snooping-enabled interface of the device. If the number of entries has reached the configured maximum value, it is normal that new users cannot access the network.
     ```
     [display dhcp snooping user-bind all](cmdqueryname=display+dhcp+snooping+user-bind+all)
     ```
   * (Optional) Configure the maximum number of DHCP access users.
     ```
     [dhcp snooping user-bind max-number](cmdqueryname=dhcp+snooping+user-bind+max-number) max-number
     ```