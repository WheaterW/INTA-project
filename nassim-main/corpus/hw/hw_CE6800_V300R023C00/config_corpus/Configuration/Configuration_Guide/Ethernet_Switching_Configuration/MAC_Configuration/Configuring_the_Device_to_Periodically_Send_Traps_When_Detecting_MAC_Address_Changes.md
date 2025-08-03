Configuring the Device to Periodically Send Traps When Detecting MAC Address Changes
====================================================================================

Configuring the Device to Periodically Send Traps When Detecting MAC Address Changes

#### Context

To learn MAC address changes, you can configure the device to send traps when learning MAC addresses or detecting aged MAC address entries.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Set the interval at which the device checks whether new MAC addresses are learned or whether a MAC address entry is aged out.
   
   
   ```
   [mac-address notification interval](cmdqueryname=mac-address+notification+interval) interval-time
   ```
   
   By default, a device checks whether new MAC addresses are learned and whether a MAC address entry is aged out at an interval of 10s.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode from Layer 3 to Layer 2. Determine whether to perform this step based on the current interface working mode.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
5. Configure the device to send traps when learning MAC addresses and detecting aged MAC address entries.
   
   
   ```
   [mac-address notification](cmdqueryname=mac-address+notification) { aging | learning | all }
   ```
   
   By default, a device does not send traps when they learn MAC addresses and detect aged MAC address entries.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```