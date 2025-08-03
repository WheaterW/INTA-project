Configuring Routing Loop Detection for Routes Imported to OSPFv3
================================================================

Configuring Routing Loop Detection for Routes Imported to OSPFv3

#### Context

Routing loops may occur when an OSPFv3 process imports routes. If routing loop detection is enabled for routes imported to OSPFv3 on a device and this device detects that it imports a route advertised by itself, it sends this route with a large link cost to other devices. After receiving this route, these devices preferentially select other paths, thereby preventing routing loops.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Exit the routing loop detection alarm state and clear related alarms.
   
   
   ```
   [clear route loop-detect ospfv3 alarm-state](cmdqueryname=clear+route+loop-detect+ospfv3+alarm-state)
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   After detecting an OSPFv3 routing loop, the device reports an alarm. Because the device cannot automatically detect whether the routing loop is eliminated, you need to run this command after the routing loop is eliminated to prevent the device from advertising a large cost for imported routes and manually clear the OSPFv3 routing loop alarm. If this command is executed when the routing loop has not been eliminated, the alarm is reported again.
3. Enable routing loop detection for routes imported to OSPFv3.
   
   
   ```
   [route loop-detect ospfv3 enable](cmdqueryname=route+loop-detect+ospfv3+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```