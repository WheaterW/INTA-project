Configuring an EVC to Transmit Layer 3 Multicast Services
=========================================================

To enable an EVC-capable BD to communicate with a Layer 3 multicast network, configure a VBDIF interface for the BD, so that the EVC can transmit Layer 3 multicast services and implement on-demand data forwarding.

#### Context

EVC applies to Layer 2 interfaces and does not support IP address configurations. To enable an EVC-capable BD to communicate with Layer 3 interfaces, configure a logical VBDIF interface for the BD. A VBDIF interface is a network-layer interface and supports IP address configuration. By configuring a VBDIF interface for a BD, you can enable an EVC to transmit Layer 3 multicast services, , which simplifies network planning and management.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
   
   
   
   IP multicast routing is enabled.
3. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The BD view is displayed.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface vbdif**](cmdqueryname=interface+vbdif) *bd-id*
   
   
   
   A VBDIF interface is created, and the interface view is displayed.
6. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.