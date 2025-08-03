Configuring an IS-IS Interface as a Silent Interface
====================================================

Configuring an IS-IS Interface as a Silent Interface

#### Prerequisites

Before configuring an IS-IS interface as a silent interface, you have completed the following tasks:

* [Configure basic IS-IS functions](vrp_isis_ipv4_cfg_0011.html).
* Enable IS-IS on the interface.

#### Context

To enable devices on an IS-IS network in an AS to learn routes to an outbound interface, IS-IS must be enabled on the outbound interface. With IS-IS, the outbound interface advertises IIHs to its network segment. Consequently, the external AS connected to the local AS can learn the route to the IS-IS network. To prevent this outbound interface from diverting traffic from the external AS, you can configure it as a silent interface so that it does not send or receive IS-IS packets. Despite this configuration, the route to the network segment where the silent interface resides can still be advertised.


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
5. Configure the IS-IS interface as a silent interface.
   
   
   ```
   isis silent [ advertise-zero-cost ]
   ```
   
   By default, an IS-IS interface is not configured as a silent interface.
   
   The **advertise-zero-cost** parameter sets the route cost to 0 on the interface.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```