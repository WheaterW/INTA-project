Configuring Dynamic BFD for IPv4 Static Route
=============================================

Configuring Dynamic BFD for IPv4 Static Route

#### Prerequisites

Before configuring dynamic BFD for IPv4 static route, you have completed the following task:

* Set data link layer protocol parameters for interfaces to ensure that the data link layer protocol status of the interfaces is up.

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
4. (Optional) Set global BFD parameters to monitor IPv4 static routes.
   
   
   ```
   [ip route-static default-bfd](cmdqueryname=ip+route-static+default-bfd) { min-rx-interval min-rx-interval | min-tx-interval min-tx-interval | detect-multiplier multiplier }
   ```
   
   
   
   The default values of the global BFD parameters (used to monitor IPv4 static routes) **min-rx-interval**, **min-tx-interval**, and **detect-multiplier** are 10 ms, 10 ms, and 3, respectively.
5. Set BFD parameters for a single IPv4 static route.
   
   
   ```
   [ip route-static bfd](cmdqueryname=ip+route-static+bfd) { { interface-name | interface-type interface-number } nexthop-address [ local-address address ] | [ vpn-instance vpn-instance-name ] nexthop-address local-address address } [ min-rx-interval min-rx-interval | min-tx-interval min-tx-interval | detect-multiplier multiplier ] *
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the *interface-type* *interface-number* parameter is not specified, the **local-address** *address* parameter must be specified.
   
   If none of **min-rx-interval**, **min-tx-interval**, and **detect-multiplier** is specified, the default values of the BFD parameters are used globally.
6. Perform either of the following operations to configure an IPv4 static route and bind it to the dynamic BFD session.
   
   
   * Configure an IPv4 static route on the public network and bind it to the dynamic BFD session.
     ```
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } { nexthop-address | interface-type interface-number [ nexthop-address ] } bfd enable [ description text ]
     ```
   * Configure an IPv4 static route in a specified VPN instance and bind it to the dynamic BFD session.
     ```
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } { nexthop-address | interface-type interface-number [ nexthop-address ] } bfd enable [ description text ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support this command.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The outbound interface and next-hop IP address specified when an IPv4 static route is bound to a BFD session must be the same as those configured for the BFD session.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```