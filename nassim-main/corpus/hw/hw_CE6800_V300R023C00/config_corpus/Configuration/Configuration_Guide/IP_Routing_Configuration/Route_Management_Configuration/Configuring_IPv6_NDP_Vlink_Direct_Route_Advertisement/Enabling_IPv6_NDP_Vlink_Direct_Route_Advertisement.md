Enabling IPv6 NDP Vlink Direct Route Advertisement
==================================================

Enabling IPv6 NDP Vlink Direct Route Advertisement

#### Prerequisites

Before configuring IPv6 NDP Vlink direct route advertisement, you have completed the following task:

* Set data link layer protocol parameters and IPv6 addresses for interfaces to ensure that the data link layer protocol status on each interface is up.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure IPv6 NDP Vlink direct route advertisement.
   
   
   ```
   [ipv6 nd direct-route enable](cmdqueryname=ipv6+nd+direct-route+enable)
   ```
   
   After the device is enabled to advertise IPv6 NDP Vlink direct routes, IPv6 NDP Vlink direct routes can be advertised only after they are imported to the routing table of a dynamic routing protocol. Perform one of the following operations based on the routing protocol running on the device:
   
   By default, IPv6 NDP Vlink direct routes are not advertised.
   
   * Enable RIPng to import and advertise IPv6 NDP Vlink direct routes.
     ```
     [import-route](cmdqueryname=import-route) direct [ cost cost | inherit-cost | route-policy route-policy-name ]*
     ```
   * Enable OSPFv3 to import and advertise IPv6 NDP Vlink direct routes.
     ```
     [import-route](cmdqueryname=import-route) direct [ cost cost | inherit-cost | type type | tag tag | route-policy route-policy-name ] *
     ```
   * Enable IS-IS to import and advertise IPv6 NDP Vlink direct routes.
     ```
     [ipv6 import-route](cmdqueryname=ipv6+import-route) direct [ cost cost | tag tag | route-policy route-policy-name | level-1 | level-2 | level-1-2 ] *
     ```
   * Enable BGP4+ to import and advertise IPv6 NDP Vlink direct routes.
     ```
     [import-route](cmdqueryname=import-route) direct [ med med | route-policy route-policy-name ] *
     ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
   ```
4. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Set a preference value for IPv6 NDP Vlink direct routes.
   
   
   ```
   [ipv6 nd direct-route preference](cmdqueryname=ipv6+nd+direct-route+preference) preference-value
   ```
   
   By default, no preference value is set for IPv6 NDP Vlink direct routes.
   
   IPv6 NDP Vlink direct routes can be advertised by different routing protocols. If there are multiple IPv6 NDP Vlink direct routes advertised by different routing protocols, you can run this command to change the route preference for route selection.
6. Disable the device from advertising IPv6 NDP Vlink host routes destined for link-local addresses.
   
   
   ```
   [ipv6 nd vlink-link-local no-advertise](cmdqueryname=ipv6+nd+vlink-link-local+no-advertise)
   ```
   
   
   
   By default, IPv6 NDP Vlink host routes destined for link-local addresses are advertised.
   
   You can run this command to control the size of the routing table and prevent the device from learning IPv6 NDP Vlink host routes corresponding to the link-local addresses of users.
7. Set the prefix and prefix length of summary IPv6 NDP Vlink direct routes.
   
   
   ```
   [ipv6 nd direct-route prefix](cmdqueryname=ipv6+nd+direct-route+prefix) ipv6-address [ prefix-length ]
   ```
   
   By default, the prefix length of summary IPv6 NDP Vlink direct routes is 128 bits.
   
   To control the size of the routing table and maintain the stability of the routing table, you can configure the device to summarize routes with the same network prefix into a network segment route to reduce the consumption of system resources.
8. Set a delay in advertising IPv6 NDP Vlink direct routes.
   
   
   ```
   [ipv6 nd direct-route delay](cmdqueryname=ipv6+nd+direct-route+delay) delay-time
   ```
   
   
   
   To prevent traffic loss caused when the creation of the IPv6 NDP Vlink direct route routing table is slower than traffic diversion, you can set a delay in advertising IPv6 NDP Vlink direct routes.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```