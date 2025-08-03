Configuring an IPv6 IS-IS Interface as a Silent Interface
=========================================================

Configuring an IPv6 IS-IS Interface as a Silent Interface

#### Prerequisites

Before configuring an IPv6 IS-IS interface as a silent interface, you have completed the following tasks:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).
* Enable IPv6 IS-IS on a silent interface.

#### Context

To enable devices on an IPv6 IS-IS network in an AS to learn routes to an outbound interface, IPv6 IS-IS must be enabled on the outbound interface. With IPv6 IS-IS, the outbound interface advertises IPv6 Hello packets to its network segment. Consequently, the external AS connected to the local AS can learn the route to the IPv6 IS-IS network. To prevent this outbound interface from diverting traffic from the external AS, you can configure it as a silent interface so that it does not send or receive IPv6 IS-IS packets. Despite this configuration, the route to the network segment where the silent interface resides can still be advertised.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
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
6. Configure the IPv6 IS-IS interface as a silent interface.
   
   
   ```
   isis silent [ advertise-zero-cost ]
   ```
   
   By default, an IPv6 IS-IS interface is not configured as a silent interface.
   
   The **advertise-zero-cost** parameter sets the route cost to 0 on the interface.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```