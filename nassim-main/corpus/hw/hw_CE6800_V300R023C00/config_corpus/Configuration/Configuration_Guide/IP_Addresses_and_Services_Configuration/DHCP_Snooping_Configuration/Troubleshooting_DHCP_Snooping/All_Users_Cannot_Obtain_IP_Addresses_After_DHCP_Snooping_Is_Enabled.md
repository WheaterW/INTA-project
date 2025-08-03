All Users Cannot Obtain IP Addresses After DHCP Snooping Is Enabled
===================================================================

All Users Cannot Obtain IP Addresses After DHCP Snooping Is Enabled

#### Fault Symptom

All users cannot obtain IP addresses after DHCP snooping is enabled.



#### Possible Causes

* The interface connected to the DHCP server is not configured as a trusted one.
* After DHCP snooping is enabled globally, DHCP snooping is not enabled on the interface connected to users or in the VLAN to which the interface belongs.


#### Procedure

1. Check whether the interface connected to the DHCP server is a trusted one.
   
   
   * Check the VLANs and interfaces where DHCP snooping is enabled.
     ```
     display dhcp snooping configuration
     ```
   * Check whether "Trusted interface: Yes" is displayed on the interface connected to the DHCP server.
     ```
     display dhcp snooping [ [interface](cmdqueryname=interface) interface-type interface-number | vlan vlan-id ]
     ```
     
     By default, an interface is untrusted. After receiving DHCP reply messages from network-side interfaces, the device processes only those from the trusted interface and discards those from the untrusted interfaces. After receiving request messages from user-side interfaces, the device forwards them only to the trusted interface.
   * If the interface is not a trusted one, configure it as a trusted one in the VLAN or interface view.
     ```
     [dhcp snooping trusted](cmdqueryname=dhcp+snooping+trusted) 
     ```
2. If the interface is a trusted one, check whether DHCP snooping is enabled on the interface connected to users or in the VLAN to which the interface belongs.
   
   
   * Check whether DHCP snooping is enabled on the interface connected to users or in the VLAN to which the interface belongs.
     ```
     display dhcp snooping configuration
     display dhcp snooping [ [interface](cmdqueryname=interface) interface-type interface-number | vlan vlan-id ]
     ```
   
   
   * If DHCP snooping is not enabled on the interface connected to users or in the VLAN to which the interface belongs, enable it in the VLAN or interface view.
     ```
     [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable) 
     ```