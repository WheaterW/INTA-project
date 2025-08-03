Configuring a Stub Router
=========================

Configuring a Stub Router

#### Prerequisites

Before configuring a stub router, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

Maintenance operations, such as device upgrade, can potentially trigger route flapping. To prevent an OSPF route from going through a path that includes a device under upgrade or maintenance, you can configure the device as a stub router. Then, after the configuration is performed, the route on the stub router will not be selected. The link cost on the stub router is automatically set to the maximum value 65535, thereby preventing traffic from being routed to the stub router. This configuration task generally applies to device upgrade or maintenance scenarios.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Configure the device as a stub router.
   
   
   ```
   [stub-router](cmdqueryname=stub-router) [ [ on-startup [ interval ] ] | [ include-stub ] | [ external-lsa [ externallsa-metric ] ] | [ summary-lsa [ summarylsa-metric ] ] ] *
   ```
   
   By default, no device is configured as a stub router.
   
   If a device is configured as a stub router, the device keeps serving as the role for 500 seconds by default.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The stub router configured using this command is irrelevant to the devices in a stub area.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command to check information about the OSPF routing table.