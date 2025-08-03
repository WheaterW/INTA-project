Configuring Load Balancing Among IPv4 Static Routes
===================================================

Configuring Load Balancing Among IPv4 Static Routes

#### Context

According to route selection rules, if IPv4 static routes have the same prefix, mask length, and preference, they load-balance traffic by default.

On the network shown in [Figure 1](#EN-US_TASK_0000001806226240__fig64141640103610), two static routes with the same prefix, mask length, and preference from DeviceA to DeviceC need to be configured. Both routes will be added to the routing table and are used to forward data.

**Figure 1** Network diagram of load balancing among static routes  
![](figure/en-us_image_0000001852945213.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Perform the following operations as needed to configure an IPv4 static route. Then repeat the operations to configure another or more IPv4 static routes with the same prefix, mask, and preference.
   
   
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
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   By default, IPv4 static routes with the same prefix, mask, and preference can implement load balancing.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check routes with the same prefix and mask but multiple outbound interfaces and next hops in the IPv4 routing table.