Configuring a Device Role
=========================

Configuring a Device Role

#### Context

You can configure a role for a device, which facilitates device management through the NMS.


#### Procedure

1. Enter the system view.
   
   
   ```
   system-view
   ```
2. Configure a device role.
   
   
   ```
   [set system role](cmdqueryname=set+system+role) { core | spine | leaf }
   ```
   
   By default, no role is configured for a device.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display system role**](cmdqueryname=display+system+role) command to check the role configured for the device.