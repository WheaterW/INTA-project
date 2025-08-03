Configuring Defense Against Bogus DHCP Message Attacks
======================================================

Configuring Defense Against Bogus DHCP Message Attacks

#### Context

On a DHCP network, if an attacker pretends to be an authorized user and sends DHCP messages to the DHCP server, the authorized user cannot use the IP address or is logged out unexpectedly. After a DHCP snooping binding table is generated, the device checks DHCP messages against the binding table. Only DHCP messages that match entries are forwarded, and those that do not match entries are discarded. This prevents unauthorized users from sending bogus DHCP messages to renew the IP address lease or release IP addresses.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to check DHCP messages against the binding table.
   
   
   * System view
     1. Enable the device to check DHCP messages from a specified VLAN against the binding table.
        ```
        [dhcp snooping check dhcp-request enable](cmdqueryname=dhcp+snooping+check+dhcp-request+enable) [ [vlan](cmdqueryname=vlan) { vlan-id1 [ [to](cmdqueryname=to) vlan-id2 ] } &<1-10> ]
        ```
     2. Enable the device to check whether the CHADDR field value is the same as the source MAC address in the header of a DHCPREQUEST message in a specified VLAN.
        ```
        [dhcp snooping check dhcp-chaddr enable](cmdqueryname=dhcp+snooping+check+dhcp-chaddr+enable) [ [vlan](cmdqueryname=vlan) { vlan-id1 [ [to](cmdqueryname=to) vlan-id2 ] } &<1-10> ]
        ```
        
        By default, a device does not check whether the CHADDR field value is the same as the source MAC address in the header of a DHCPREQUEST message.
   * Interface view
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     portswitch
     [dhcp snooping check dhcp-request enable](cmdqueryname=dhcp+snooping+check+dhcp-request+enable)
     [dhcp snooping check dhcp-chaddr enable](cmdqueryname=dhcp+snooping+check+dhcp-chaddr+enable) 
     [quit](cmdqueryname=quit)
     ```
   * VLAN view
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp snooping check dhcp-request enable](cmdqueryname=dhcp+snooping+check+dhcp-request+enable)
     [dhcp snooping check dhcp-chaddr enable](cmdqueryname=dhcp+snooping+check+dhcp-chaddr+enable)
     [quit](cmdqueryname=quit)
     ```
   
   By default, a device does not check DHCP messages against the binding table.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```