Configuring a Convergence Priority for Some IPv6 IS-IS Routes
=============================================================

Configuring a Convergence Priority for Some IPv6 IS-IS Routes

#### Prerequisites

Before configuring convergence priority for some IPv6 IS-IS routes, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

You can configure the highest convergence priority for some IPv6 IS-IS routes so that these routes converge first when a network topology changes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure a convergence priority for the IPv6 IS-IS routes that match a specified filtering rule.
   
   
   ```
   [ipv6 prefix-priority](cmdqueryname=ipv6+prefix-priority) [ level-1 | level-2 ] { critical | high | medium } { ipv6-prefix prefix-name | tag tag-value }
   ```
   
   
   
   By default, the convergence priority of IPv6 IS-IS host routes (with a 32-bit mask) is **medium**, and the convergence priority of the other IPv6 IS-IS routes is **low**.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the [**ipv6 prefix-priority**](cmdqueryname=ipv6+prefix-priority) command is run, the convergence priority of 32-bit IS-IS host routes is changed from medium to low, and the convergence priorities of the other IS-IS routes are changed based on the configuration of the [**ipv6 prefix-priority**](cmdqueryname=ipv6+prefix-priority) command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```