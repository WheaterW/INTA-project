Suppressing an IPv6 IS-IS Interface from Advertising Its IPv6 Address
=====================================================================

Suppressing an IPv6 IS-IS Interface from Advertising Its IPv6 Address

#### Prerequisites

Before suppressing an IPv6 IS-IS interface from advertising its IPv6 address, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

By default, an IPv6 IS-IS interface advertises its IPv6 address so that all devices on the network can learn the routes to the interface. To prevent other devices from obtaining the IPv6 address of an IPv6 IS-IS interface, you can suppress the interface from advertising its IPv6 address.

![](public_sys-resources/note_3.0-en-us.png) 

Even through an IPv6 IS-IS interface is suppressed from advertising its IPv6 address, the interface can still establish IPv6 IS-IS neighbor relationships with other interfaces.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable IPv6 on the interface.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable) 
   ```
5. Enable IPv6 IS-IS on the interface.
   
   
   ```
   [isis ipv6 enable](cmdqueryname=isis+ipv6+enable) [ process-id ]
   ```
6. Suppresses the IS-IS interface from advertising its address.
   
   
   ```
   [isis ipv6 suppress-reachability](cmdqueryname=isis+ipv6+suppress-reachability)
   ```
   
   By default, an IPv6 IS-IS interface advertises its IPv6 address.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```