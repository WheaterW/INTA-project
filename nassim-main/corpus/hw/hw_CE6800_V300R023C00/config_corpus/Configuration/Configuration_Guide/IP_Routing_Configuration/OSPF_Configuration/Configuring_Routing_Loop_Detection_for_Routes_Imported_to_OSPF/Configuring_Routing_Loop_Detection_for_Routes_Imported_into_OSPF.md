Configuring Routing Loop Detection for Routes Imported into OSPF
================================================================

Configuring Routing Loop Detection for Routes Imported into OSPF

#### Context

Routing loops may occur when an OSPF process imports routes. If routing loop detection is enabled for routes imported to OSPF on a device and this device detects that it imports a route advertised by itself, it sends this route with a large link cost to other devices. After receiving this route, these devices preferentially select other paths, thereby preventing routing loops.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
   
   The *process-id* parameter specifies the ID of a process, and the default value is 1.
3. Enable the OSPF Opaque LSA capability.
   
   
   ```
   [opaque-capability enable](cmdqueryname=opaque-capability+enable)
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   OSPF uses opaque LSAs to implement loop detection on imported routes. Therefore, to enable loop detection on imported routes, run the [**opaque-capability enable**](cmdqueryname=opaque-capability+enable) command to enable the opaque LSA capability.
4. (Optional) Exit the routing loop detection alarm state and clear related alarms.
   
   
   ```
   [clear route loop-detect ospf alarm-state](cmdqueryname=clear+route+loop-detect+ospf+alarm-state)
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the device detects an OSPF routing loop, it reports an alarm. Because the device cannot automatically detect whether the routing loop is eliminated, you need to run this command after the routing loop is eliminated to prevent the device from advertising a large link cost for imported routes and manually clear the OSPF routing loop alarm. If this command is executed when the routing loop has not been eliminated, the alarm is reported again.
5. Enable routing loop detection for routes imported into OSPF.
   
   
   ```
   [route loop-detect ospf enable](cmdqueryname=route+loop-detect+ospf+enable)
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   To disable routing loop detection for routes imported into OSPF, run the [**undo route loop-detect ospf enable**](cmdqueryname=undo+route+loop-detect+ospf+enable) command.
6. (Optional) Enable routing loop detection for routes imported into OSPF.
   
   
   ```
   [route loop-detect ospf import-ospf enable](cmdqueryname=route+loop-detect+ospf+import-ospf+enable)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```