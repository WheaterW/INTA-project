Configuring DAI
===============

Configuring DAI

#### Context

You can enable DAI to defend against MITM attacks, preventing authorized users' data from being intercepted. A device compares the source IP address, source MAC address, interface, and VLAN information in a received ARP message with DHCP snooping binding entries. If they match, the device considers the message valid and forwards it. If they do not match, the device considers the message invalid and discards it.

You can enable DAI in the interface, BD, or VLAN view. If DAI is enabled in the interface view, the device checks all ARP messages received by the interface against binding entries. If DAI is enabled in the VLAN or BD view, the device checks the ARP messages received by the interfaces that belong to the VLAN or BD against binding entries.

If a large number of ARP messages are discarded because they do not match binding entries, you can enable the alarm function for the ARP messages discarded by DAI. In this case, the device generates an alarm if the number of discarded ARP messages exceeds the alarm threshold.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable DAI on interfaces, in BDs, or in VLANs.
   
   
   * Enter the interface view and enable DAI.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [portswitch](cmdqueryname=portswitch)
     [arp anti-attack check user-bind enable](cmdqueryname=arp+anti-attack+check+user-bind+enable)
     [quit](cmdqueryname=quit)
     ```
   * Enter the BD view and enable DAI.
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     [arp anti-attack check user-bind enable](cmdqueryname=arp+anti-attack+check+user-bind+enable)
     [quit](cmdqueryname=quit)
     ```
   * Enter the VLAN view and enable DAI.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [arp anti-attack check user-bind enable](cmdqueryname=arp+anti-attack+check+user-bind+enable)
     [quit](cmdqueryname=quit)
     ```
   
   
   
   By default, DAI is disabled on a device.
3. (Optional) Configure items to be checked against binding entries for ARP messages.
   
   
   * Configure items to be checked against binding entries for ARP messages in the interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [portswitch](cmdqueryname=portswitch)
     [arp anti-attack check user-bind check-item](cmdqueryname=arp+anti-attack+check+user-bind+check-item) { ip-address | mac-address | vlan } *  
     [quit](cmdqueryname=quit)
     ```
   
   
   * Configure items to be checked against binding entries for ARP messages in the BD view.
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     [arp anti-attack check user-bind check-item](cmdqueryname=arp+anti-attack+check+user-bind+check-item) { ip-address | mac-address | interface } * 
     [quit](cmdqueryname=quit)
     ```
   * Configure items to be checked against binding entries for ARP messages in the VLAN view.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [arp anti-attack check user-bind check-item](cmdqueryname=arp+anti-attack+check+user-bind+check-item) { ip-address | mac-address | interface } * 
     [quit](cmdqueryname=quit)
     ```By default, a device checks the source IP address, source MAC address, interface, and VLAN information in ARP messages. To allow the ARP messages that match only one or two items in binding entries to pass through, configure a device to check ARP messages according to one or two specified items in binding entries.![](public_sys-resources/note_3.0-en-us.png) 
   
   Only IPv4 addresses are supported in binding entries. When a device compares IP addresses in ARP messages with binding entries, only IPv4 addresses are checked.
   
   The configured items to be checked against binding entries for ARP messages do not take effect on users configured with static binding entries, meaning that the device still checks ARP messages of these users against the static binding entries.
   
   If DAI is enabled both in a VLAN and on an interface that belongs to the VLAN, the device first checks ARP messages based on the items configured on the interface. If the ARP messages pass the check, the device checks the messages again based on the items configured in the VLAN.
   
   If DAI is enabled both in a BD and on an interface that belongs to the BD, the device first checks ARP messages based on the items configured on the BD. If the ARP messages pass the check, the device checks the messages again based on the items configured on the interface.
4. (Optional) Enable the alarm function for ARP messages discarded by DAI.
   
   
   ```
   [arp anti-attack check user-bind alarm enable](cmdqueryname=arp+anti-attack+check+user-bind+alarm+enable) 
   ```
   
   By default, the alarm function for ARP messages discarded by DAI is disabled on a device.
5. (Optional) Configure an alarm threshold for ARP messages discarded by DAI.
   
   
   ```
   [arp anti-attack check user-bind alarm threshold](cmdqueryname=arp+anti-attack+check+user-bind+alarm+threshold) threshold 
   ```
   
   By default, the alarm threshold for ARP messages discarded by DAI is that configured using this command in the system view. If no alarm threshold is configured in the system view, the default alarm threshold on an interface, in a BD, or in a VLAN is 100.
6. Configure a trusted interface.
   
   
   
   To prevent return messages from being discarded because they do not match binding entries, configure the interface directly or indirectly connected to an authorized DHCP server as a trusted one. After the interface is configured as a trusted one, the device directly forwards the messages received from the interface without checking them against binding entries.
   
   1. Enable DHCP globally.
      ```
      [dhcp enable](cmdqueryname=dhcp+enable)
      ```
      
      By default, DHCP is disabled globally.
   2. Enable DHCP snooping globally.
      ```
      [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
      ```
      
      By default, DHCP snooping is disabled globally.
   3. Enable DHCP snooping in the interface or VLAN view.
      ```
      [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
      ```
      
      By default, DHCP snooping is disabled on an interface, in a BD, or in a VLAN.
   4. Configure a trusted interface.
      * Configure an interface as a trusted interface in the interface view.
        ```
        [dhcp snooping trusted](cmdqueryname=dhcp+snooping+trusted) 
        ```
        
        By default, an interface is untrusted.
      * Configure an interface as a trusted interface in the VLAN view.
        ```
        [dhcp snooping trusted](cmdqueryname=dhcp+snooping+trusted) interface interface-type interface-number 
        ```
        
        By default, an interface is untrusted.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display arp anti-attack statistics check user-bind**](cmdqueryname=display+arp+anti-attack+statistics+check+user-bind) [ **vlan** [ *vlan-id* ] | **interface** [ *interface-type* *interface-number* ] | **bridge-domain** [ *bd-id* ] ] command to check statistics about ARP messages discarded because they do not match binding entries in the interface, BD, or VLAN view.
* Run the [**display arp anti-attack configuration check user-bind**](cmdqueryname=display+arp+anti-attack+configuration+check+user-bind) [ **vlan** [ *vlan-id* ] | **interface** [ *interface-type* *interface-number* ] | **bridge-domain** [ *bd-id* ] ] command to check the DAI configuration in the interface, BD, or BD view.