Suppressing an IS-IS Interface from Advertising Its IP Address
==============================================================

Suppressing an IS-IS Interface from Advertising Its IP Address

#### Prerequisites

Before suppressing an IS-IS interface from advertising its IP address, you have completed the following task:

* [Configure basic IS-IS functions](vrp_isis_ipv4_cfg_0011.html).

#### Context

By default, an IS-IS interface advertises its IP address so that all devices on the network can learn the routes to the interface. To prevent other devices from obtaining the IP address of an IS-IS interface, you can suppress the interface from advertising its IP address.

![](public_sys-resources/note_3.0-en-us.png) 

Even through an IS-IS interface is suppressed from advertising its IP address, the interface can still establish IS-IS neighbor relationships with other interfaces.



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
4. Enable IS-IS on the interface.
   
   
   ```
   [isis enable](cmdqueryname=isis+enable) [ process-id ]
   ```
5. Suppresses the interface from advertising its IP address.
   
   
   ```
   [isis suppress-reachability](cmdqueryname=isis+suppress-reachability)
   ```
   
   By default, an IS-IS interface advertises its IP address.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```