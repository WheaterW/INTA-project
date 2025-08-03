Configuring IPv6 Static Route Backup
====================================

Configuring IPv6 Static Route Backup

#### Context

After multiple IPv6 static routes with the same destination and different preferences are set on a device, the device can perform route backup. On the network shown in [Figure 1](#EN-US_TASK_0000001176663225__fig282064133919), two static routes from DeviceA to DeviceC are configured. In most cases, only the static route with DeviceB as a next hop is active in the routing table because this route has a higher preference. The other static route with DeviceD as a next hop functions as a backup route. The backup route is only activated to forward traffic after the active link fails. After the active link A recovers, the static route with DeviceB as a next hop becomes active again to take over the traffic. In this case, the backup static route is also known as a floating static route.

**Figure 1** Network diagram of IPv6 static route backup  
![](figure/en-us_image_0000001130783482.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Perform either of the following operations to configure an IPv6 static route. Repeat the operation to configure two or more IPv6 static routes with the same prefix and mask and different preferences.
   
   
   * Configure an IPv6 static route on the public network.
     ```
     [ipv6 route-static](cmdqueryname=ipv6+route-static) dest-ipv6-address prefix-length { interface-name | interface-type interface-number } [ nexthop-ipv6-address ] preference preference [ bfd enable | track { bfd-session cfg-name | nqa admin-name test-name } ] [ description text ]
     ```
   * Configure an IPv6 static route in a specified VPN instance.
     ```
     [ipv6 route-static](cmdqueryname=ipv6+route-static) vpn-instance vpn-source-name dest-ipv6-address prefix-length { interface-name | interface-type interface-number } [ nexthop-ipv6-address ] preference preference [ bfd enable | track { bfd-session cfg-name | nqa admin-name test-name } ] [ description text ]
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command to check active routes in the IPv6 routing table.