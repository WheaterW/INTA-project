Disabling an Interface from Broadcasting Packets to Other Interfaces in a Bridge Domain
=======================================================================================

You can disable an EVC Layer 2 sub-interface from broadcasting packets to other EVC Layer 2 sub-interfaces in a bridge domain. This function helps devices from being attacked and improves network security.

#### Context

When an EVC Layer 2 sub-interface in a BD receives broadcast, unknown unicast, or unknown multicast packets, it broadcasts the packets to other interfaces in the BD.

If these packets are malicious, the device resources are occupied, causing the device performance to deteriorate or device breakdown. Disabling an EVC Layer 2 sub-interface from broadcasting received packets to other interfaces in the BD prevents malicious attacks.

This function applies to networks without user changes or networks with static MAC address-based forwarding paths.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The bridge domain view is displayed.
3. Perform one of the following steps to disable an interface from broadcasting packets to other interfaces in a bridge domain:
   
   
   * To disable an interface from broadcasting packets to other interfaces in a bridge domain, run the [**broadcast discard**](cmdqueryname=broadcast+discard) command.
   * To disable an interface from forwarding unknown unicast packets to other interfaces in a bridge domain, run the [**unknown-unicast discard**](cmdqueryname=unknown-unicast+discard) command.
   * To disable an interface from forwarding multicast packets to other interfaces in a bridge domain, run the [**unknown-multicast discard**](cmdqueryname=unknown-multicast+discard) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.