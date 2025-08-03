Setting the Device Name
=======================

Setting the Device Name

#### Context

To differentiate devices on the network, you can set a unique device name for each device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the device name.
   
   
   ```
   [sysname](cmdqueryname=sysname) host-name
   ```
   
   By default, the device name is HUAWEI.
   
   You can run the [**undo sysname**](cmdqueryname=undo+sysname) command to restore the default host name.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```