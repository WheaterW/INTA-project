Disabling LDP Interface Flapping Suppression
============================================

Disabling LDP Interface Flapping Suppression

#### Context

If LDP interface flapping suppression is disabled and an interface frequently flaps, LDP frequently sends Address and Address Withdraw messages to all LDP sessions. If there are a large number of sessions, the CPU usage of the device increases, causing protocol flapping. To prevent this problem, LDP interface flapping suppression is enabled by default. For a stable LDP network, you can disable LDP interface flapping suppression.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS globally and enter the MPLS view.
3. Run the [**mpls ldp**](cmdqueryname=mpls+ldp) command to enable LDP globally and enter the MPLS-LDP view.
4. Run the [**suppress-flapping interface disable**](cmdqueryname=suppress-flapping+interface+disable) command to disable LDP interface flapping suppression.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.