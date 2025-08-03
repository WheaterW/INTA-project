Starting DHCP-based ZTP Without a Controller
============================================

Starting DHCP-based ZTP Without a Controller

#### Context

A device with factory configurations has never started ZTP before. In its factory configurations, the ZTP function is enabled by default. To start ZTP, you only need to power on the device. The ZTP function can be disabled on a device. If you log in to a device through the console port and disable the ZTP function when the device starts with empty configuration, the ZTP process is terminated. To enable the device to execute the ZTP process when it starts with empty configuration next time, you need to enable the ZTP function.


#### Procedure

1. Power on the device.
2. (Optional) Enable the ZTP function on the device.
   
   
   ```
   [set ztp enable](cmdqueryname=set+ztp+enable)
   ```
   
   By default, the ZTP function is enabled on a device.
   
   To disable a device from running the ZTP process upon startup with factory configurations, run the [**set ztp disable**](cmdqueryname=set+ztp+disable) command on the device.
3. (Optional) Restart the device with factory configurations.
   
   
   ```
   [reboot fast](cmdqueryname=reboot+fast)
   ```