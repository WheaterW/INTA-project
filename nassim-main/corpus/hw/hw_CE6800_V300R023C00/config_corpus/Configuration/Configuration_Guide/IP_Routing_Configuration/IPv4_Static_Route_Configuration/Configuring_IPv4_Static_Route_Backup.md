Configuring IPv4 Static Route Backup
====================================

Configuring IPv4 Static Route Backup

#### Context

After multiple IPv4 static routes with the same destination but different preferences are configured on a device, the device can perform route backup. On the network shown in [Figure 1](#EN-US_TASK_0000001176662507__fig282064133919), two static routes from DeviceA to DeviceC are configured. In most cases, only the static route with DeviceB as a next hop is active in the routing table because this route has a higher preference. The other static route with DeviceD as a next hop functions as a backup route. The backup route is only activated to forward traffic after the active link fails. After the active link A recovers, the static route with DeviceB as a next hop becomes active again to take over the traffic. In this case, the backup route is also called a floating static route.

**Figure 1** Network diagram of IPv4 static route backup  
![](figure/en-us_image_0000001176662563.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Perform either of the following operations to configure an IPv4 static route. Repeat the operation to configure two or more IPv4 static routes with the same prefix and mask but different preferences.
   
   
   * Configure an IPv4 static route on the public network.
     ```
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } nexthop-address preference preference
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length }{ interface-name | interface-type interface-number } [ nexthop-address ] preference preference
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } vpn-instance vpn-instance-name preference preference
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } **vpn-instance** *vpn-instance-name* **preference** *preference*.
   * Configure an IPv4 static route in a VPN instance.
     ```
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length }{ interface-type interface-number } [ nexthop-address ] preference preference
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } nexthop-address preference preference
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } vpn-instance vpn-destination-name preference preference
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } **vpn-instance** *vpn-destination-name* **preference** *preference* command.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check information about active routes in the IPv4 routing table.