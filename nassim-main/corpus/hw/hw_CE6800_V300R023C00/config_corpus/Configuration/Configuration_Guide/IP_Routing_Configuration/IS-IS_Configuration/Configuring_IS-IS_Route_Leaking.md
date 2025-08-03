Configuring IS-IS Route Leaking
===============================

Configuring IS-IS Route Leaking

#### Context

When Level-1 and Level-2 areas both exist on an IS-IS network, Level-2 routing devices do not advertise the learned routing information about a Level-1 area and the backbone area to any other Level-1 area by default. As a result, Level-1 routing devices do not know the routing information beyond the local area, unable to select the optimal route to a destination beyond the local area.

With route leaking, Level-1-2 devices can select routes of other Level-1 areas and the backbone area using routing policies or tags and advertise the selected routes to the local Level-1 area. [Figure 1](#EN-US_TASK_0000001130784106__fig_dc_vrp_isis_feature_003201) shows the typical networking for route leaking.

* Devices A, B, C, and D belong to area 10. DeviceA and DeviceB are Level-1 devices, and DeviceC and DeviceD are Level-1-2 devices.
* DeviceE and DeviceF belong to area 20 and are Level-2 devices.

**Figure 1** Network diagram of route leaking  
![](figure/en-us_image_0000001176743813.png "Click to enlarge")

The optimal route for DeviceA to send packets to DeviceF is DeviceA -> DeviceB -> DeviceD -> DeviceE -> DeviceF, as its cost is 40 (10 + 10 + 10 + 10 = 40), which is less than that (10 + 50 + 10 = 70) of the other route (DeviceA -> DeviceC -> DeviceE -> DeviceF). However, if you check routes on DeviceA, you can find that the selected route is the latter.

This is due to DeviceA being unaware of routes beyond the local area, and sending the packets beyond the local area to the nearest Level-1-2 device.

Enable route leaking on Level-1-2 devices (DeviceC and DeviceD) and then check the selected path. The path is DeviceA -> DeviceB -> DeviceD -> DeviceE -> DeviceF, which is the optimal route from DeviceA to DeviceF.


#### Procedure

* Configure route leaking from a Level-2 area to the local Level-1 area.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure route leaking from a Level-2 area to the local Level-1 area.
     
     
     ```
     [import-route isis level-2 into level-1](cmdqueryname=import-route+isis+level-2+into+level-1) [ tag tag | filter-policy { acl-number | acl-name acl-name | ip-prefix ip-prefix-name | { route-policy route-policy-name } } | direct { allow-filter-policy | allow-up-down-bit } * ] *
     ```
     
     
     
     By default, Level-2 routing information is not leaked to Level-1 areas.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     This command can be run only on Level-1-2 devices connected to an external area.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure route leaking from the local Level-1 area to the Level-2 area.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure route leaking from the local Level-1 area to the Level-2 area.
     
     
     ```
     [import-route isis level-1 into level-2](cmdqueryname=import-route+isis+level-1+into+level-2) [ tag tag-value | filter-policy { acl-number | acl-name acl-name-value | ip-prefix ip-prefix-name | { route-policy route-policy-name } } | direct allow-filter-policy ] *
     ```
     
     By default, all routing information (except default route information) in the Level-1 area is leaked to the Level-2 area. You can specify parameters as required in the command so that only information about the routes that meet specified conditions is leaked to the Level-2 area.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     This command can be run only on Level-1-2 devices connected to an external area.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] command to check IS-IS route leaking information.


[Example for Configuring IS-IS Route Leaking](vrp_isis_ipv4_cfg_0114.html)