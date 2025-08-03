(Optional) Configuring the Device to Delete the Corresponding MAC Address Entry Immediately When a Client Is Disconnected
=========================================================================================================================

(Optional) Configuring the Device to Delete the Corresponding MAC Address Entry Immediately When a Client Is Disconnected

#### Context

If a DHCP client is disconnected but its dynamic MAC address entry is not aged out, the device forwards the message whose destination address is this client's IP address based on the dynamic MAC address entry. This deteriorates device performance.

To address this issue, you can enable the device to delete the MAC address entry of the client whose DHCP snooping binding entry has been deleted.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to delete the MAC address entry of an offline DHCP client whose DHCP snooping binding entry has been deleted.
   
   
   ```
   [dhcp snooping user-offline remove mac-address](cmdqueryname=dhcp+snooping+user-offline+remove+mac-address)
   ```
   
   
   
   By default, the device does not delete the MAC address entry of an offline DHCP client whose DHCP snooping binding entry has been deleted.
   
   After this function is enabled, secure dynamic MAC address entries learned by running the **port-security enable** command are also deleted.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```