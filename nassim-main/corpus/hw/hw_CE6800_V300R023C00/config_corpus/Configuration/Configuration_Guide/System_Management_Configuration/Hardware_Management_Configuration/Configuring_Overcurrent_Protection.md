Configuring Overcurrent Protection
==================================

Configuring Overcurrent Protection

#### Context

After overcurrent protection is enabled on a device, if the current of a power module exceeds the rated current, the power module stops supplying power to the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure overcurrent protection.
   
   
   ```
   
   [undo device power over-current-protect](cmdqueryname=undo+device+power+over-current-protect) disable
   ```
   
   By default, overcurrent protection is enabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```