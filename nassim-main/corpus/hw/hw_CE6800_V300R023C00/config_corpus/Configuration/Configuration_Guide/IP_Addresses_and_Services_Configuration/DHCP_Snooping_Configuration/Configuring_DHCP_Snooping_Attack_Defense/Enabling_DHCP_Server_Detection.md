Enabling DHCP Server Detection
==============================

Enabling DHCP Server Detection

#### Context

After DHCP snooping is enabled and a trusted interface is configured, the device can ensure that DHCP clients obtain IP addresses from a valid DHCP server. This prevents attacks from a bogus DHCP server. However, the bogus DHCP server cannot be located. Therefore, it still poses security risks on the network.

After DHCP server detection is enabled, the DHCP snooping-enabled device checks information about the DHCP server, such as the IP address and port number, in all DHCP reply messages and records the information in a log. The network administrator can determine whether any bogus DHCP server exists on the network based on the log.

By default, a DHCP snooping-enabled device checks DHCP reply messages based only on MAC addresses for server identification. If the device cannot identify servers based only on MAC addresses, run the **dhcp snooping check server-vlan enable** command. After the command is run, the DHCP snooping-enabled device checks DHCP reply messages based on both MAC addresses and VLAN information for server identification.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable DHCP server detection.
   
   
   ```
   [dhcp snooping server record](cmdqueryname=dhcp+snooping+server+record)
   ```
   
   By default, DHCP server detection is disabled on a device.
3. (Optional) Enable the DHCP snooping-enabled device to check VLAN information in DHCP reply messages.
   
   
   ```
   [dhcp snooping check server-vlan enable](cmdqueryname=dhcp+snooping+check+server-vlan+enable)
   ```
   
   By default, a DHCP snooping-enabled device does not check VLAN information in DHCP reply messages.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```