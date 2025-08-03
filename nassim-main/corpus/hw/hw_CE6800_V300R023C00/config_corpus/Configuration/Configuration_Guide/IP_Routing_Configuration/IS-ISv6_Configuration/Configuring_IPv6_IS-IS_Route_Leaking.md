Configuring IPv6 IS-IS Route Leaking
====================================

Configuring IPv6 IS-IS Route Leaking

#### Prerequisites

Before configuring IPv6 IS-IS route leaking, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

If multiple Level-1-2 devices in a Level-1 area are connected to a Level-2 area, the Level-1 LSPs sent by each Level-1-2 device carry the ATT bit set to 1. In this case, this Level-1 area will have multiple routes to the Level-2 area and other Level-1 areas.

By default, routing information in a Level-1 area is leaked to the Level-2 area, enabling Level-1-2 and Level-2 devices to learn the topology of the entire network. Devices in a Level-1 area are unaware of the entire network topology because they only maintain LSDBs in the local Level-1 area. Therefore, a device in a Level-1 area can forward traffic to a Level-2 device only through the nearest Level-1-2 device. The route used may not be the optimal route to the destination, as shown in [Figure 1](#EN-US_TASK_0000001176742061__fig981472054213).

* DeviceA, DeviceB, DeviceC, and DeviceD belong to area 10. DeviceA and DeviceB are Level-1 routing devices, and DeviceC and DeviceD are Level-1-2 routing devices.
* DeviceE and DeviceF belong to area 20 and are Level-2 devices.

**Figure 1** Network diagram of IPv6 IS-IS route leaking  
![](figure/en-us_image_0000001176742133.png)

The optimal route for DeviceA to send packets to DeviceF is DeviceA -> DeviceB -> DeviceD -> DeviceE -> DeviceF, as its cost is 40 (10 + 10 + 10 + 10 = 40), which is less than that (10 + 50 + 10 = 70) of the other route (DeviceA -> DeviceC -> DeviceE -> DeviceF). However, if you check routes on DeviceA, you can find that the selected route is the latter.

This is due to DeviceA being unaware of routes beyond the local area, and sending the packets beyond the local area to the nearest Level-1-2 device.

Enable route leaking on Level-1-2 devices (DeviceC and DeviceD) and then check the selected path. The path is DeviceA -> DeviceB -> DeviceD -> DeviceE -> DeviceF, which is the optimal route from DeviceA to DeviceF.

If you require the Level-2 area to be aware of only certain routes in the local Level-1 area, you can configure a policy so that only the desired routing information leaks to the Level-2 area.


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
  3. Configure IPv6 IS-IS to leak only some routing information from a Level-2 area and other Level-1 areas to the local Level-1 area.
     
     
     ```
     [ipv6 import-route isis level-2 into level-1](cmdqueryname=ipv6+import-route+isis+level-2+into+level-1) [ tag tag | filter-policy { acl6-number | acl6-name acl6-name-string | ipv6-prefix ipv6-prefix-name | route-policy route-policy-name } | direct { allow-filter-policy | allow-up-down-bit } * ] *
     ```
     
     
     
     By default, IS-IS IPv6 routing information in the Level-2 area is not leaked to Level-1 areas.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     This command can be run only on Level-1-2 devices connected to an external area.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure route leaking from the local Level-1 area to a Level-2 area.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure the device to leak some IPv6 IS-IS routes from the Level-1 area to the Level-2 area.
     
     
     ```
     [ipv6 import-route isis level-1 into level-2](cmdqueryname=ipv6+import-route+isis+level-1+into+level-2) [ tag tag | filter-policy { acl6-number | acl6-name acl6-name-string | ipv6-prefix ipv6-prefix-name | route-policy route-policy-name } | direct allow-filter-policy ] *
     ```
     
     By default, all Level-1 IPv6 IS-IS routing information, excluding default route information, is leaked to the Level-2 area. You can specify parameters as required in the command so that only information about the routes that meet specified conditions is leaked to the Level-2 area.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     This command can be run only on Level-1-2 devices connected to an external area.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display isis**](cmdqueryname=display+isis) *process-id* **route** **ipv6** [ *ipv6-address* [ *prefix-length* ] | { **level-1** | **level-2** } | **verbose** ] \* command to check IPv6 IS-IS route leaking information.