Disabling MAC Address Learning in a VLAN
========================================

Disabling MAC Address Learning in a VLAN

#### Context

If network devices do not change often, you can disable MAC address learning in a VLAN to increase security. If MAC address learning is disabled in a VLAN, a device will not learn new MAC addresses from the interfaces that belong to the VLAN. In such cases, the device cannot communicate with other devices through the VLAN, which improves network stability and security.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Disable MAC address learning.
   
   
   ```
   [mac-address learning disable](cmdqueryname=mac-address+learning+disable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vlan**](cmdqueryname=display+vlan) [ *vlan-id* [ **verbose** ] ] command to check whether MAC address learning has been disabled in the VLAN.