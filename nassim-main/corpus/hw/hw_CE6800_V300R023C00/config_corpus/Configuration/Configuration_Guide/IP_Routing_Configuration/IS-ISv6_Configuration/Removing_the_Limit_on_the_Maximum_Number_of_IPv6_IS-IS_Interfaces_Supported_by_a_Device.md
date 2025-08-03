Removing the Limit on the Maximum Number of IPv6 IS-IS Interfaces Supported by a Device
=======================================================================================

Removing the Limit on the Maximum Number of IPv6 IS-IS Interfaces Supported by a Device

#### Context

A limit on the maximum number of IPv6 IS-IS interfaces supported can be configured on each routing router. To remove such a limit, you can run the [**isis interface limit disable**](cmdqueryname=isis+interface+limit+disable) command.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Remove the limit on the maximum number of IPv6 IS-IS interfaces supported by the device.
   
   
   ```
   [isis interface limit disable](cmdqueryname=isis+interface+limit+disable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```