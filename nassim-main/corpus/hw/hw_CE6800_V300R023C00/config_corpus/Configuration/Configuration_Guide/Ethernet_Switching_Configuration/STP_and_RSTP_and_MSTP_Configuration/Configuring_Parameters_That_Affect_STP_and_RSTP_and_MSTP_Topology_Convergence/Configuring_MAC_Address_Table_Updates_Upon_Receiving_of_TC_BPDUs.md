Configuring MAC Address Table Updates Upon Receiving of TC BPDUs
================================================================

Configuring MAC Address Table Updates Upon Receiving of TC BPDUs

#### Context

STP, RSTP, or MSTP sends TC BPDUs to instruct devices to update MAC address entries when the network topology encounters any changes, for example, when a local device's interface goes from down to up. If a large number of MAC address entries are updated, packet forwarding may be affected. To resolve this issue, you can disable the device from updating the MAC address table when it receives TC BPDUs.

If MAC address entries are incorrect after the configuration is complete, traffic will be interrupted for a long time. Therefore, exercise caution when configuring this function.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enter the MSTP process view.
   
   
   
   Perform this step to set system parameters only when the MSTP process ID is not 0. Skip this step if the MSTP process ID is 0.
   
   ```
   [stp process](cmdqueryname=stp+process) process-id
   ```
3. Disable the device from updating MAC address entries upon receiving TC BPDUs.
   
   
   ```
   [stp flush disable](cmdqueryname=stp+flush+disable)
   ```
   
   By default, a device updates MAC address entries when it receives TC BPDUs.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the system view or MSTP process view to check that the device does not update MAC address entries upon receiving TC BPDUs.