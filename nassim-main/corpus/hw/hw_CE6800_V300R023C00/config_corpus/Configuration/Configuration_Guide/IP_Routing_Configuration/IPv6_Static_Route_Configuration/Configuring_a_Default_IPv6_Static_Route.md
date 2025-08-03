Configuring a Default IPv6 Static Route
=======================================

Configuring a Default IPv6 Static Route

#### Context

Default static routes are special routes that can be manually configured. Default static routes are used only when packets to be forwarded do not match any entry in the routing table. The destination address and subnet mask of the default route are all 0s in the routing table.

If the destination address of a packet does not match any entry in the routing table, a device selects the default route to forward this packet. If no default route exists and the destination address of the packet does not match any entry in the routing table, the packet is discarded. An Internet Control Message Protocol (ICMP) message is then sent, informing the source host that the destination host or network is unreachable.

When the destination address and mask are set to all 0s in the **ipv6 route-static** command, a default route is configured. This simplifies the network configuration. On the network shown in [Figure 1](#EN-US_TASK_0000001176743139__fig93041029142419), the next hop of packets sent from DeviceA to networks 3, 4, and 5 is DeviceB. In this situation, you can configure a default route on DeviceA, without the need to configure the three static routes to networks 3, 4, and 5. Similarly, only one default route to DeviceB needs to be configured on DeviceC, without the need to configure the three static routes destined for networks 1, 2, and 3.

**Figure 1** Network diagram of static routes  
![](figure/en-us_image_0000001130623704.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Perform either of the following operations to configure a default IPv6 static route:
   
   
   * Configure a default IPv6 static route on the public network.
     ```
     [ipv6 route-static](cmdqueryname=ipv6+route-static) :: 0 nexthop-ipv6-address 
     [ipv6 route-static](cmdqueryname=ipv6+route-static) :: 0 { interface-name | interface-type interface-number } [ nexthop-ipv6-address ] 
     ```
   * Configure a default IPv6 static route in a specified VPN instance.
     ```
     [ipv6 route-static vpn-instance](cmdqueryname=ipv6+route-static+vpn-instance) vpn-source-name :: 0 nexthop-ipv6-address [ public ]
     [ipv6 route-static vpn-instance](cmdqueryname=ipv6+route-static+vpn-instance) vpn-source-name :: 0 { interface-name | interface-type interface-number } [ nexthop-ipv6-address ]
     [ipv6 route-static vpn-instance](cmdqueryname=ipv6+route-static+vpn-instance) vpn-source-name :: 0 { vpn-instance vpn-destination-name [ nexthop-ipv6-address ] | public } 
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command to check whether the IPv6 routing table contains routes with the prefix of 0::0/0.