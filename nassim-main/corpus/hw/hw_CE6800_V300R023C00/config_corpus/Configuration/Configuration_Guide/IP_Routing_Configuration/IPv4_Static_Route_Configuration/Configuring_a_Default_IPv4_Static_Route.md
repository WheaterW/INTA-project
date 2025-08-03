Configuring a Default IPv4 Static Route
=======================================

Configuring a Default IPv4 Static Route

#### Context

Default static routes are special routes that can be manually configured. Default static routes are used only when packets to be forwarded do not match any entry in the routing table. The destination address and subnet mask of the IPv4 default route are all 0s in the routing table.

If the destination address of a packet does not match any entry in the routing table, a device selects the default route to forward this packet. If no default route exists and the destination address of the packet does not match any entry in the routing table, the packet is discarded. An Internet Control Message Protocol (ICMP) message is then sent, informing the source host that the destination host or network is unreachable.

When you configure a static route using the **ip route-static** command and set the destination address and mask to all 0s (0.0.0.0 and 0.0.0.0) in the command, a default route is configured. This simplifies the network configuration. On the network shown in [Figure 1](#EN-US_TASK_0000001176662499__fig93041029142419), the next hop of packets sent from DeviceA to networks 3, 4, and 5 is DeviceB. Therefore, you can configure a default route on DeviceA to replace three static routes destined for networks 3, 4, and 5. Similarly, only one default route to DeviceB needs to be configured on DeviceC to replace the three static routes destined for networks 1, 2, and 3.

**Figure 1** Network diagram of static routes  
![](figure/en-us_image_0000001176662531.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Perform either of the following operations to configure a default IPv4 static route.
   
   
   * Configure a default IPv4 static route on the public network.
     ```
     [ip route-static](cmdqueryname=ip+route-static) 0.0.0.0 0.0.0.0 nexthop-address
     [ip route-static](cmdqueryname=ip+route-static) 0.0.0.0 0.0.0.0 { interface-name | interface-type interface-number} [ nexthop-address ]
     ```
   * Configure a default IPv4 static route in a specified VPN instance.
     ```
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name 0.0.0.0 0.0.0.0 { interface-type interface-number }
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name 0.0.0.0 0.0.0.0 nexthop-address
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name 0.0.0.0 0.0.0.0 vpn-instance vpn-destination-name
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support the preceding commands.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check information about the route with the prefix of 0.0.0.0 in the IPv4 routing table.