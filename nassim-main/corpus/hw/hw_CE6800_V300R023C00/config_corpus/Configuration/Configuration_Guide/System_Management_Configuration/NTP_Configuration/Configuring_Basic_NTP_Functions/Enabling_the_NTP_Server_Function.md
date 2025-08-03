Enabling the NTP Server Function
================================

Enabling the NTP Server Function

#### Context

After NTP-related commands are configured on a device, it automatically disables the NTP server function to prevent external devices from synchronizing their clocks with the device's clock. In addition, the device generates the [**ntp**](cmdqueryname=ntp) [ **ipv6** ] **server** **disable** configuration in its configuration file. To use the device as an NTP server, enable the NTP server function on the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the NTP server function.
   
   
   ```
   [undo ntp](cmdqueryname=undo+ntp) [ ipv6 ] server disable
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   By default, the NTP server function is enabled. To improve security, the system automatically disables the NTP server function when the first configuration command of the NTP function takes effect.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```