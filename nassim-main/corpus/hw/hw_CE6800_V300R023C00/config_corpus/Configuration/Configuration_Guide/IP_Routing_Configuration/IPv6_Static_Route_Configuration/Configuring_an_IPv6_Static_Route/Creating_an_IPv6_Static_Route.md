Creating an IPv6 Static Route
=============================

Creating an IPv6 Static Route

#### Prerequisites

Before creating an IPv6 static route, you have completed the following task:

* Set data link layer protocol parameters for interfaces to ensure that the data link layer protocol status of each interface is up.

#### Context

Setting the same preference value for IPv6 static routes to the same destination implements load balancing among these routes, whereas setting different preference values for such routes implements route backup. Setting the destination IP address and mask to all 0s configures a default IPv6 static route. By default, no default IPv6 static route is configured.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an IPv6 static route.
   
   
   * Configure an IPv6 static route on the public network.
     ```
     [ipv6 route-static](cmdqueryname=ipv6+route-static) dest-ipv6-address prefix-length interface-type interface-number [ nexthop-ipv6-address ] [ preference preference | tag tag ] * [ description text ]
     [ipv6 route-static](cmdqueryname=ipv6+route-static) dest-ipv6-address prefix-length nexthop-ipv6-address [ preference preference | tag tag ] * [ description text ]
     [ipv6 route-static](cmdqueryname=ipv6+route-static) dest-ipv6-address prefix-length vpn-instance vpn-instance-name [ preference preference | tag tag ] * [ description text ]
     [ipv6 route-static](cmdqueryname=ipv6+route-static) dest-ipv6-address prefix-length vpn-instance vpn-instance-name nexthop-ipv6-address [ preference preference | tag tag ] * [ description text ]
     ```
   * Configure an IPv6 static route in a specified VPN instance.
     ```
     [ipv6 route-static vpn-instance](cmdqueryname=ipv6+route-static+vpn-instance) vpn-source-name dest-ipv6-address prefix-length { interface-name | interface-type interface-number } [ nexthop-ipv6-address ] [ preference preference | tag tag ] * [ description text ]
     [ipv6 route-static vpn-instance](cmdqueryname=ipv6+route-static+vpn-instance) vpn-source-name dest-ipv6-address prefix-length nexthop-ipv6-address [ public ] [ preference preference | tag tag ] * [ description text ]
     [ipv6 route-static vpn-instance](cmdqueryname=ipv6+route-static+vpn-instance) vpn-source-name dest-ipv6-address prefix-length { vpn-instance vpn-instance-name | public } [ preference preference | tag tag ] * [ description text ]
     [ipv6 route-static vpn-instance](cmdqueryname=ipv6+route-static+vpn-instance) vpn-source-name dest-ipv6-address prefix-length vpn-instance vpn-instance-name nexthop-ipv6-address [ preference preference | tag tag ] * [ description text ]
     ```
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   In a static route load balancing scenario, to allow a static route with an Ethernet outbound interface to participate in load balancing with other static routes, you must specify a next hop along with the outbound interface for the former static route.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```