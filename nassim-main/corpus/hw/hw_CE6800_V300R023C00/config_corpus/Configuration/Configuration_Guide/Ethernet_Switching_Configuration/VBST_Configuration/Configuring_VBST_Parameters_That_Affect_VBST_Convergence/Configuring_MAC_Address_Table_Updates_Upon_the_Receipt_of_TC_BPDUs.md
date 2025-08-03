Configuring MAC Address Table Updates Upon the Receipt of TC BPDUs
==================================================================

Configuring MAC Address Table Updates Upon the Receipt of TC BPDUs

#### Context

VBST sends TC BPDUs to instruct devices to update MAC address entries when the network topology encounters any changes, for example, when a local device's interface goes from down to up. If a large number of MAC address entries are updated, unknown unicast or broadcast problems may occur. To resolve this issue, you can disable the device from updating the MAC address table when it receives TC BPDUs.

If MAC address entries are incorrect after the configuration is complete, traffic may be interrupted for a long time. Therefore, exercise caution when configuring this function.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable the device from updating MAC address entries upon receiving TC BPDUs.
   
   
   ```
   [stp flush disable](cmdqueryname=stp+flush+disable)
   ```
   
   By default, a device updates MAC address entries when it receives TC BPDUs.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the system view to check that the device does not update MAC address entries upon receiving TC BPDUs.