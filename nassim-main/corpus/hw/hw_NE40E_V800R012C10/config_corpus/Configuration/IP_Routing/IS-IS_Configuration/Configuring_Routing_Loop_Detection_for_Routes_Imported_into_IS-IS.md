Configuring Routing Loop Detection for Routes Imported into IS-IS
=================================================================

Configuring Routing Loop Detection for Routes Imported into IS-IS

#### Usage Scenario

When an IS-IS process imports routes, routing loops may occur. If a device on which routing loop detection is enabled for routes imported into IS-IS detects that it imports a route advertised by itself, it sends this route with a large link cost to other devices. After receiving this route, these devices preferentially select other paths, preventing routing loops.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. (Optional) Run the [**clear route loop-detect isis alarm-state**](cmdqueryname=clear+route+loop-detect+isis+alarm-state) command to exit the routing loop detection alarm state and clear related alarms.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the device detects an IS-IS routing loop, it reports an alarm. Because the device cannot automatically detect whether the routing loop is eliminated, you need to run this command after the routing loop is eliminated to prevent the device from advertising a large link cost for imported routes and manually clear the IS-IS routing loop alarm. If this command is executed when the routing loop has not been eliminated, the alarm is reported again.
3. Run the [**route loop-detect isis enable**](cmdqueryname=route+loop-detect+isis+enable) command to enable routing loop detection for routes imported into IS-IS.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.