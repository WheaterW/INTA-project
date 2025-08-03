Configuring the Status of the Device ID Indicator
=================================================

Configuring the Status of the Device ID Indicator

#### Context

When a device needs to be located and repaired, you can run the **set device id-led** command to remotely set the status of the device ID indicator to help onsite maintenance personnel quickly find the target device.


#### Procedure

1. (Optional) Check the status of the device ID indicator.
   
   
   ```
   [display device id-led](cmdqueryname=display+device+id-led)
   ```
2. Set the status of the device ID indicator.
   
   
   ```
   [set device id-led](cmdqueryname=set+device+id-led) { off | on } [ slot slotid ]
   ```
   
   By default, the device ID indicator is steady off.
   
   If no slot ID is specified, this command takes effect for all slots.