Configuring Defense Against DHCP Server DoS Attacks
===================================================

Configuring Defense Against DHCP Server DoS Attacks

#### Context

If malicious DHCP users apply for IP addresses on the network, the IP addresses in the IP address pool will be quickly exhausted. As a result, the DHCP server cannot allocate IP addresses to authorized users. The DHCP server typically determines the MAC address of a DHCP client based on the CHADDR (client hardware address) field in a DHCPREQUEST message. If attackers apply for IP addresses by continuously changing the CHADDR field, addresses in the address pool on the DHCP server will be exhausted. As a result, authorized users cannot obtain IP addresses.

To prevent malicious DHCP users on some interfaces from applying for IP addresses, you can set the maximum number of DHCP snooping binding entries that can be learned by an interface to control the number of online users. When the number of online users reaches the maximum value, users can no longer obtain IP addresses through this interface. To prevent attackers from applying for IP addresses by continuously changing the CHADDR field in DHCPREQUEST messages, you can configure the device to check whether the CHADDR field value is the same as the source MAC address in the header of a DHCPREQUEST message. If they are the same, the device forwards the message. Otherwise, the device discards it.

After the alarm function is enabled, alarms are generated if corresponding attacks occur and the number of discarded attack packets exceeds the threshold. The minimum interval for sending alarms is 1 minute. You can run the **dhcp snooping alarm threshold** command to set an alarm threshold.

![](../public_sys-resources/note_3.0-en-us.png) 

* When the maximum number of DHCP snooping binding entries to be learned on an interface is configured:
  + For the system view configuration, the sum of the maximum numbers of DHCP snooping binding entries that can be learned by all interfaces is the configured maximum number. For the VLAN view configuration, the maximum number of DHCP snooping binding entries that can be learned by any interface in the VLAN is the configured maximum number.
  + If the configuration is performed in the system, VLAN, and interface views, the maximum number of DHCP snooping binding entries that can be learned by the interface is the smallest value among the three views.
* When CHADDR field check is configured:
  
  If the function is configured in the system, VLAN, and interface views at the same time, the configurations in the three views all take effect.
* When an alarm threshold for the number of messages discarded by DHCP snooping is configured:
  
  If the function is configured in the system, VLAN, and interface views at the same time, the configurations in the three views all take effect.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the maximum number of DHCP snooping binding entries to be learned on an interface.
   
   
   * Enter the system view and configure the maximum number of DHCP snooping binding entries that can be learned by interfaces.
     ```
     [dhcp snooping user-bind max-number](cmdqueryname=dhcp+snooping+user-bind+max-number) max-number [ [vlan](cmdqueryname=vlan) { vlan-id1 [ [to](cmdqueryname=to) vlan-id2 ] } &<1-10> ]
     ```
   * Enter the interface view and configure the maximum number of DHCP snooping binding entries that can be learned by the interface.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     portswitch
     [dhcp snooping user-bind max-number](cmdqueryname=dhcp+snooping+user-bind+max-number) max-number
     [quit](cmdqueryname=quit)
     ```
   * Enter the VLAN view and configure the maximum number of DHCP snooping binding entries that can be learned by the interfaces in the VLAN.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp snooping user-bind max-number](cmdqueryname=dhcp+snooping+user-bind+max-number) max-number
     [quit](cmdqueryname=quit)
     ```
3. (Optional) Configure alarm thresholds for the percentage for DHCP snooping binding entries in the system view.
   
   
   ```
   [dhcp snooping user-alarm percentage](cmdqueryname=dhcp+snooping+user-alarm+percentage) percent-lower-value percent-upper-value
   ```
   
   By default, the lower and upper alarm thresholds for the percentage of DHCP snooping binding entries are 50 and 100, respectively.
4. Enable CHADDR field check.
   
   
   * Enter the system view and configure CHADDR field check.
     ```
     [dhcp snooping check dhcp-chaddr enable](cmdqueryname=dhcp+snooping+check+dhcp-chaddr+enable) [ [vlan](cmdqueryname=vlan) { vlan-id1 [ [to](cmdqueryname=to) vlan-id2 ] } &<1-10> ]
     ```
   * Enter the interface view and configure CHADDR field check.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     portswitch
     [dhcp snooping check dhcp-chaddr enable](cmdqueryname=dhcp+snooping+check+dhcp-chaddr+enable)
     [quit](cmdqueryname=quit)
     ```
   * Enter the VLAN view and configure CHADDR field check.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp snooping check dhcp-chaddr enable](cmdqueryname=dhcp+snooping+check+dhcp-chaddr+enable)
     [quit](cmdqueryname=quit)
     ```
   
   
   
   By default, a device does not check whether the CHADDR field value is the same as the source MAC address in the header of a DHCPREQUEST message.
5. (Optional) Configure an alarm threshold for the number of messages discarded by DHCP snooping.
   
   
   * In the system view, enable the DHCP snooping alarm function, and configure an alarm threshold for the number of messages discarded by DHCP snooping.
     ```
     [dhcp snooping alarm](cmdqueryname=dhcp+snooping+alarm) { dhcp-request | dhcp-chaddr | dhcp-reply } enable
     [dhcp snooping alarm threshold](cmdqueryname=dhcp+snooping+alarm+threshold) threshold
     ```
     
     By default, the global alarm threshold for the number of messages discarded by DHCP snooping is 100.
   * Enter the interface view, enable the DHCP snooping alarm function, and configure an alarm threshold for the number of messages discarded by DHCP snooping.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     portswitch
     [dhcp snooping alarm](cmdqueryname=dhcp+snooping+alarm) { dhcp-request | dhcp-chaddr | dhcp-reply } enable
     [dhcp snooping alarm](cmdqueryname=dhcp+snooping+alarm) { dhcp-request | dhcp-chaddr | dhcp-reply } [threshold](cmdqueryname=threshold) threshold
     [quit](cmdqueryname=quit)
     ```
     
     By default, the alarm threshold for the number of messages discarded by DHCP snooping on an interface is the value configured using the **dhcp snooping alarm threshold** command in the system view.
   * Enter the VLAN view, enable the DHCP snooping alarm function, and configure an alarm threshold for the number of messages discarded by DHCP snooping.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp snooping alarm](cmdqueryname=dhcp+snooping+alarm) { dhcp-request | dhcp-chaddr | dhcp-reply } enable
     [dhcp snooping alarm](cmdqueryname=dhcp+snooping+alarm) { dhcp-request | dhcp-chaddr | dhcp-reply } [threshold](cmdqueryname=threshold) threshold
     [quit](cmdqueryname=quit)
     ```
     
     By default, the alarm threshold for the number of messages discarded by DHCP snooping on an interface is the value configured using the **dhcp snooping alarm threshold** command in the system view.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```