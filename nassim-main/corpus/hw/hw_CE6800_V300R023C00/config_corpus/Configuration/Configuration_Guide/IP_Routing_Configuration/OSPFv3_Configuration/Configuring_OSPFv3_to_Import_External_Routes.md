Configuring OSPFv3 to Import External Routes
============================================

Configuring OSPFv3 to Import External Routes

#### Prerequisites

Before configuring OSPFv3 to import external routes, you have completed the following tasks:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).
* To use a route-policy to filter the routes to be imported, create the route-policy first.
* To use an IP prefix list to filter the routes to be imported, create the IP prefix list first.

#### Context

Because OSPFv3 is a link-state routing protocol and cannot filter LSAs to be advertised directly, it can only filter routes when importing them. As such, only the routes that match the filtering conditions can be used to generate LSAs to be advertised.

Perform the following steps on the device that runs OSPFv3.

![](../public_sys-resources/notice_3.0-en-us.png) 

OSPFv3 and other dynamic routing protocols such as IS-IS and BGP often import routes from each other. If no routing policy is configured or a routing policy is incorrectly configured on a device where IS-IS, OSPFv3, and BGP import routes from each other, a Layer 3 routing loop may occur due to a route selection result change. As a result, services are compromised. For details about the cause of the routing loop, see [Understanding Routing Loop Detection for Routes Imported to OSPFv3](vrp_ospfv3_cfg_0163.html).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Import external routes.
   
   
   ```
   [import-route](cmdqueryname=import-route) { bgp [ permit-ibgp ] | direct | static | { ripng | ospfv3 | isis } [ process-id ] } [ { cost cost | inherit-cost } | tag tag | type type | { route-policy route-policy-name } ] *
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The [**import-route**](cmdqueryname=import-route) command cannot be used to import external default routes.
4. (Optional) Set default parameter values for imported routes.
   
   
   ```
   [default](cmdqueryname=default) { cost costvalue | tag tagvalue | type typevalue } *
   ```
   
   You can set default values for the parameters (such as the cost, route tag, and route type) of the external routes imported by OSPFv3. The route tag can be used to differentiate AS numbers carried in BGP4+ routes imported by OSPFv3.
5. (Optional) Set a limit on the number of imported external routes that can be advertised by OSPFv3.
   
   
   ```
   [import-route limit](cmdqueryname=import-route+limit) limit-number [ threshold-alarm { upper-limit upper-limit-value | lower-limit lower-limit-value }* ]
   ```
   
   If OSPFv3 imports a large number of external routes and advertises them to a device with a small routing table capacity, the device may restart unexpectedly. To prevent this problem, configure a limit on the number of imported external routes that can be advertised by OSPFv3. This ensures stable device running.
   
   Ensure that *upper-limit-value* is greater than or equal to *lower-limit-value*.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **routing** command to check information about the OSPFv3 routing table.