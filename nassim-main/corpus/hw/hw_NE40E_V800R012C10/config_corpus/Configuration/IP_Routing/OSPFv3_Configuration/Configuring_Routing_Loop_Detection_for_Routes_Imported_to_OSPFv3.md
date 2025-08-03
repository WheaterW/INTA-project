Configuring Routing Loop Detection for Routes Imported to OSPFv3
================================================================

Routing loop detection for routes imported into OSPFv3 enables a device to check whether routes advertised by the device are imported back. If routes advertised by the device are imported back, the device advertises a large link cost for the routes to prevent routing loops.

#### Usage Scenario

Routing loops may occur when an OSPFv3 process imports routes. If routing loop detection is enabled for routes imported to OSPFv3 on a device and this device detects that it imports a route advertised by itself, it sends this route with a large link cost to other devices. After receiving this route, these devices preferentially select other paths, thereby preventing routing loops.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route loop-detect ospfv3 enable**](cmdqueryname=route+loop-detect+ospfv3+enable)
   
   
   
   Routing loop detection is enabled for the routes imported into OSPFv3.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To reduce the impact of routing loops on services, you are advised to keep routing loop detection enabled for routes imported into OSPFv3.
3. (Optional) Run [**clear route loop-detect ospfv3 alarm-state**](cmdqueryname=clear+route+loop-detect+ospfv3+alarm-state)
   
   
   
   The routing loop detection alarm state exits, and related alarms are cleared.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After detecting an OSPFv3 routing loop, the device reports an alarm. Because the device cannot automatically detect whether the routing loop is eliminated, you need to run this command after the routing loop is eliminated to prevent the device from advertising a large cost for imported routes and manually clear the OSPFv3 routing loop alarm. If this command is executed when the routing loop has not been eliminated, the alarm is reported again.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.