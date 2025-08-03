(Optional) Configuring Association Between ARP and DHCP Snooping
================================================================

(Optional) Configuring Association Between ARP and DHCP Snooping

#### Context

After receiving a DHCPRELEASE message for releasing the IP address from a DHCP client, the DHCP snooping-enabled device immediately deletes the client's binding entry. However, if the client cannot send a DHCPRELEASE message because it is unexpectedly disconnected, the DHCP snooping-enabled device cannot immediately delete the client's binding entry.

To address this issue, you can configure association between ARP and DHCP snooping. After this is configured, the DHCP snooping-enabled device performs ARP probe on the IP address if it cannot find the ARP entry corresponding to the IP address in the DHCP snooping binding entry. If no client is detected after four consecutive ARP probes are performed, the DHCP snooping-enabled device deletes the DHCP snooping binding entry corresponding to the IP address. (The probe interval is 20 seconds; this interval and the number of probes cannot be changed.) If the DHCP snooping-enabled device supports the DHCP relay function, it then sends a DHCPRELEASE message on behalf of the DHCP client, instructing the DHCP server to release the IP address.

![](../public_sys-resources/note_3.0-en-us.png) 

Before enabling association between ARP and DHCP snooping, ensure that an IP address configured on the device is on the same network segment as the client's IP address for ARP probe.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable association between ARP and DHCP snooping.
   
   
   ```
   [dhcp snooping user-bind arp-detect enable](cmdqueryname=dhcp+snooping+user-bind+arp-detect+enable)
   ```
   
   
   
   By default, association between ARP and DHCP snooping is disabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```