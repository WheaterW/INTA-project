Configuring OSPF to Import External Routes
==========================================

Configuring OSPF to Import External Routes

#### Prerequisites

Before configuring OSPF to import external routes, you have completed the following tasks:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).
* To use a route-policy to filter the routes to be imported, create the route-policy first.
* To use an IP prefix list to filter the routes to be imported, create the IP prefix list first.

#### Context

When a device on an OSPF network needs to access a device running a non-OSPF routing protocol, the device needs to import the routes of the non-OSPF routing protocol into the OSPF network.

OSPF provides loop-free intra-area routes and inter-area routes; however, OSPF cannot prevent external routing loops. Therefore, you should exercise caution when configuring OSPF to import external routes.

Perform the following steps on the ASBR running OSPF.

![](../public_sys-resources/notice_3.0-en-us.png) 

OSPF and other dynamic routing protocols such as IS-IS and BGP often import routes from each other. If no routing policy is configured or a routing policy is incorrectly configured on a device where IS-IS, OSPF, and BGP import routes from each other, a Layer 3 routing loop may occur due to a route selection result change. As a result, services are compromised. For details about the cause of the routing loop, see [Understanding Routing Loop Detection for Routes Imported to OSPF](vrp_ospf_cfg_0302.html).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Import routes from another protocol.
   
   
   ```
   [import-route](cmdqueryname=import-route) { bgp [ permit-ibgp ] | direct | rip [ process-id-rip ] | static | isis [ process-id-isis ] | ospf [ process-id-ospf ] } [ { inherit-cost | cost cost } | tag tag | type type | route-policy route-policy-name ] *
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The [**import-route**](cmdqueryname=import-route) command cannot be used to import external default routes.
4. (Optional) Set the default values of parameters (the cost, tag, and type) for the imported routes.
   
   
   ```
   [default](cmdqueryname=default) { cost { costvalue | inherit-metric } | tag tagvalue | type typevalue } *
   ```
   
   You can set default values for the parameters (such as the cost, route tag, and route type) of the external routes imported by OSPF. The route tag can be used to differentiate AS numbers carried in BGP routes imported by OSPF.
   
   The default values are as follows:
   
   * The cost of the external routes imported by OSPF is 1.
   * A maximum of 2,147,483,647 routes can be imported each time.
   * The type of the imported external routes is Type 2.
   * The tag value of the imported routes is 1.![](../public_sys-resources/note_3.0-en-us.png) Run one of the following commands to set a cost for imported routes. The commands are listed in descending order of priority:
   * Run the [**apply cost**](cmdqueryname=apply+cost) command to apply a cost to routes filtered by a route-policy.
   * Run the [**import-route**](cmdqueryname=import-route) command to set a cost for imported routes.
   * Run the [**default**](cmdqueryname=default) command to set a default cost for imported routes.
5. (Optional) Set a limit on the number of LSAs generated when OSPF imports routes.
   
   
   ```
   [import-route limit](cmdqueryname=import-route+limit) limit-number [ threshold-alarm { upper-limit upper-limit-value | lower-limit lower-limit-value }* ]
   ```
   If OSPF imports a large number of external routes and advertises them to a device with a small routing table capacity, the device may restart unexpectedly. To address this problem, set a limit on the number of LSAs generated when OSPF imports external routes. This ensures stable device running. You can check the overload status based on the value of the **Current status** field in the [**display ospf brief**](cmdqueryname=display+ospf+brief) command output.
   * Normal: The number is less than or equal to the lower alarm threshold.
   * Approach limit: The number has reached or exceeded 90% of the upper alarm threshold.
   * Exceed limit: The number has reached or exceeded the limit.
   
   Ensure that *upper-limit-value* is greater than or equal to *lower-limit-value*.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command to check information about the OSPF routing table.