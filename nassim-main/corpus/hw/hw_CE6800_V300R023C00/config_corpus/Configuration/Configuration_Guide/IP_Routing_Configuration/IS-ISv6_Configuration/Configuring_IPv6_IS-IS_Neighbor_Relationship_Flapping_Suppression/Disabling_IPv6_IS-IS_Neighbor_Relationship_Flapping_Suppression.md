Disabling IPv6 IS-IS Neighbor Relationship Flapping Suppression
===============================================================

Disabling IPv6 IS-IS Neighbor Relationship Flapping Suppression

#### Prerequisites

Before disabling IPv6 IS-IS neighbor relationship flapping suppression, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

By default, IPv6 IS-IS neighbor relationship flapping suppression is enabled on all interfaces. You can disable IPv6 IS-IS neighbor relationship flapping suppression on all interfaces or on a specified interface as required.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Disable IPv6 IS-IS neighbor relationship flapping suppression globally.
   
   
   ```
   [suppress-flapping peer disable](cmdqueryname=suppress-flapping+peer+disable)
   ```
   
   
   
   By default, IPv6 IS-IS neighbor relationship flapping suppression is enabled globally.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
6. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
7. Disable IPv6 IS-IS neighbor relationship flapping suppression on the interface.
   
   
   ```
   [isis suppress-flapping peer disable](cmdqueryname=isis+suppress-flapping+peer+disable)
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display isis**](cmdqueryname=display+isis) [ *process-id* ] **interface** *interface-type* *interface-number* **verbose** command to check the status of IPv6 IS-IS neighbor relationship flapping suppression.
* Run the [**display current-configuration configuration isis**](cmdqueryname=display+current-configuration+configuration+isis) command to check the status of IPv6 IS-IS neighbor relationship flapping suppression on interfaces.