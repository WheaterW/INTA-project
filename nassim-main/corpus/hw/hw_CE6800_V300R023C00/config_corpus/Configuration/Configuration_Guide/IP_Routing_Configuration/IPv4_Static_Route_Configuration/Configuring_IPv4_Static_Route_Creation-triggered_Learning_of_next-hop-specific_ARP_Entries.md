Configuring IPv4 Static Route Creation-triggered Learning of next-hop-specific ARP Entries
==========================================================================================

Configuring IPv4 Static Route Creation-triggered Learning of next-hop-specific ARP Entries

#### Context

If the **arp-detect** *arp-interface-type arp-interface-number* parameter is specified when you configure an IPv4 static route, a device automatically learns next-hop-specific ARP entries when creating IPv4 static routes.

You need to configure an IPv4 static route to proactively learn next hop entries in the following scenarios:

* When a device forwards traffic through an IPv4 static route, if the device does not have the next-hop ARP entry of the static route, the device needs to trigger ARP entry learning through traffic forwarding. In this case, packet loss occurs when traffic is sent. After an IPv4 static route is configured to trigger the learning of the next-hop-specific ARP entry, the device can learn the next-hop-specific ARP entry before forwarding traffic. This ensures that no packet is lost during traffic forwarding.
* If the **arp-vlink-only** parameter is configured to enable static routes to recurse only to ARP Vlink direct routes, even though a local device has no ARP entry, the device cannot generate an ARP Vlink direct route due to the lack of the ARP entry. Consequently, no static route can recurse to the ARP Vlink direct route or go up. In the scenario where traffic can be imported only after the static route is advertised by another protocol, the static route cannot be advertised by another protocol and therefore traffic cannot be imported. As a result, the ARP entry cannot be learned. To address this problem, set the **arp-detect** *arp-interface-type arp-interface-number* value to configure a device to proactively learn next-hop-specific ARP entries.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Perform either of the following operations to configure an IPv4 static route and enable the device to learn a next-hop-specific ARP entry based on the specified IPv4 static route.
   
   
   * Configure an IPv4 static route on the public network and enable the device to learn a next-hop-specific ARP entry based on the specified IPv4 static route.
     ```
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } { nexthop-address | vpn-instance vpn-instance-name nexthop-address } [ recursive-lookup host-route [ arp-vlink-only ] ] arp-detect arp-interface-type arp-interface-number
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } interface-type interface-number nexthop-address [ arp-detect arp-interface-type arp-interface-number ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } { *nexthop-address* | **vpn-instance** *vpn-instance-name* *nexthop-address* } [ **recursive-lookup** **host-route** [ **arp-vlink-only** ] ] **arp-detect** *arp-interface-type arp-interface-number*.
   * Configure an IPv4 static route in a VPN instance and enable the device to proactively learn a next-hop-specific ARP entry based on the specified IPv4 static route.
     ```
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } { interface-name | interface-type interface-number } nexthop-address arp-detect { arp-interface-name | arp-interface-type arp-interface-number }
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } vpn-instance vpn-destination-name nexthop-address [ recursive-lookup host-route ] arp-detect { arp-interface-name | arp-interface-type arp-interface-number }
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } nexthop-address [ recursive-lookup host-route [ arp-vlink-only ] ] arp-detect { arp-interface-name | arp-interface-type arp-interface-number }
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } **vpn-instance** *vpn-destination-name* *nexthop-address* [ **recursive-lookup** **host-route** ] **arp-detect** { *arp-interface-name* | *arp-interface-type arp-interface-number* }.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check information about next-hop-specific ARP entries that the device proactively learns based on IPv4 static routes.