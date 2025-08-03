Configuring Dynamic BFD for IPv6 Static Route
=============================================

Configuring Dynamic BFD for IPv6 Static Route

#### Prerequisites

Before configuring dynamic BFD for IPv6 static route, you have completed the following task:

* Set data link layer protocol parameters for interfaces to ensure that the data link layer protocol status of each interface is up.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally.
   
   
   ```
   [bfd](cmdqueryname=bfd)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Running the [**undo bfd**](cmdqueryname=undo+bfd) command will delete the parameters of the BFD session bound to the static route. As a result, the static route status may change, and services may be interrupted.
3. Exit the BFD session view and return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. (Optional) Set global BFD parameters to monitor IPv6 static routes.
   
   
   ```
   [ipv6 route-static default-bfd](cmdqueryname=ipv6+route-static+default-bfd) { min-rx-interval min-rx-interval | min-tx-interval min-tx-interval | detect-multiplier multiplier } *
   ```
   
   
   
   The default values of the global BFD parameters **min-rx-interval**, **min-tx-interval**, and **detect-multiplier** for IPv6 static routes are 10 ms, 10 ms, and 3, respectively.
5. Set BFD parameters for a single IPv6 static route.
   
   
   ```
   [ipv6 route-static bfd](cmdqueryname=ipv6+route-static+bfd) { interface-name | interface-type interface-number } nexthop-address [ local-address ipv6-address ] [ min-rx-interval min-rx-interval | min-tx-interval min-tx-interval | detect-multiplier multiplier ] *
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the *interface-type* *interface-number* parameter is not specified, the **local-address** *address* parameter must be specified.
   
   If none of **min-rx-interval**, **min-tx-interval**, and **detect-multiplier** is specified, the global default values of the BFD parameters are used.
6. Perform either of the following operations to associate an IPv6 static route with a BFD session.
   
   
   * Configure an IPv6 static route on the public network and bind it to the dynamic BFD session.
     ```
     [ipv6 route-static](cmdqueryname=ipv6+route-static) dest-ipv6-address prefix-length nexthop-ipv6-address bfd enable
     ```
   * Configure an IPv6 static route in a specified VPN instance and bind it to the static BFD session.
     ```
     [ipv6 route-static](cmdqueryname=ipv6+route-static) dest-ipv6-address prefix-length vpn-instance vpn-instance-name nexthop-ipv6-address bfd enable
     ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```