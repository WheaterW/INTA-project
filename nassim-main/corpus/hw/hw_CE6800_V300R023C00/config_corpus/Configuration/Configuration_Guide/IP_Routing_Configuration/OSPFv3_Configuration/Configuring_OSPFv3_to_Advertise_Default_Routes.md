Configuring OSPFv3 to Advertise Default Routes
==============================================

Configuring OSPFv3 to Advertise Default Routes

#### Prerequisites

Before configuring OSPFv3 to advertise default routes, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

If no route-policy is specified when a device is configured to advertise default routes to an OSPFv3 area, all default routes in the OSPFv3 routing table will be advertised to the area. Conversely, if a route-policy is specified during the configuration, only the default routes that are generated from processes other than the local OSPFv3 process and match the filtering rules will be advertised to the area through LSAs.

Perform the following steps on the device that runs OSPFv3.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Configure OSPFv3 to advertise default routes to areas.
   
   
   ```
   [default-route-advertise](cmdqueryname=default-route-advertise) [ [ always | permit-calculate-other ] | cost cost | type type | tag tag | distribute-delay delay | { route-policy route-policy-name } ] *
   ```
   
   Or
   
   ```
   [default-route-advertise](cmdqueryname=default-route-advertise) [ permit-calculate-other | cost cost | type type | tag tag | distribute-delay delay | { route-policy route-policy-name } | permit-preference-less-than preference-val ] *
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   To prevent loops, you are advised to specify **permit-preference-less-than** to prevent low-priority active default routes from being imported. This parameter is used only when **always** is not specified.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **routing** command to check information about the OSPFv3 routing table.