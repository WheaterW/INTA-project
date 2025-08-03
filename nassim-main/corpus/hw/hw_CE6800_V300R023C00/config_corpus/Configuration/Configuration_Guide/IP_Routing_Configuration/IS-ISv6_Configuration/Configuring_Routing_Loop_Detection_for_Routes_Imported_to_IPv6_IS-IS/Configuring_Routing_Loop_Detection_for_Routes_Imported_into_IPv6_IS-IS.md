Configuring Routing Loop Detection for Routes Imported into IPv6 IS-IS
======================================================================

Configuring Routing Loop Detection for Routes Imported into IPv6 IS-IS

#### Context

Routing loops may occur when an IS-IS process imports routes. If routing loop detection is enabled for routes imported into IS-IS on a device and this device detects that it imports a route advertised by itself, it sends this route with a large link cost to other devices. After receiving this route, these devices preferentially select other paths, thereby preventing routing loops.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Exit the routing loop detection alarm state and clear related alarms.
   
   
   ```
   [clear route loop-detect isis alarm-state](cmdqueryname=clear+route+loop-detect+isis+alarm-state)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the device detects an IS-IS routing loop, it reports an alarm. Because the device cannot automatically detect whether the routing loop is eliminated, you need to run this command after the routing loop is eliminated to prevent the device from advertising a large link cost for imported routes and manually clear the IS-IS routing loop alarm. If this command is executed when the routing loop has not been eliminated, the alarm is reported again.
3. Enable routing loop detection for routes imported into IS-IS.
   
   
   ```
   [route loop-detect isis enable](cmdqueryname=route+loop-detect+isis+enable)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To disable routing loop detection for routes imported into IS-IS, run the [**undo route loop-detect isis enable**](cmdqueryname=undo+route+loop-detect+isis+enable) command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```