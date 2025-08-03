Configuring an Aging Time for Dynamic MAC Address Entries
=========================================================

Configuring an Aging Time for Dynamic MAC Address Entries

#### Context

Dynamic MAC address entries do not need to be created manually and will age out automatically. You can set an aging time for dynamic MAC address entries.

* If the aging time is set too high, the MAC address table on a device may store many useless MAC address entries, and exhaust the address table. As a result, the device cannot learn new MAC addresses.
* If the aging time is set too low, MAC address entries in the MAC address table of a device may be deleted when the device receives packets destined for the MAC addresses. As a result, the device broadcasts a large number of data packets, increasing the network load.

Therefore, it is important that the aging time be set according to the situation. For example, if the devices on the network do not change often, you can set a longer aging time to prevent devices from broadcasting a large number of data packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an aging time for dynamic MAC address entries.
   
   
   ```
   [mac-address aging-time](cmdqueryname=mac-address+aging-time) timeValue
   ```
   
   The aging time is an integer, in seconds. The default value is 300 seconds. The value 0 indicates that dynamic MAC address entries will never be aged out.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display mac-address aging-time**](cmdqueryname=display+mac-address+aging-time) command to check the aging time of dynamic MAC address entries.