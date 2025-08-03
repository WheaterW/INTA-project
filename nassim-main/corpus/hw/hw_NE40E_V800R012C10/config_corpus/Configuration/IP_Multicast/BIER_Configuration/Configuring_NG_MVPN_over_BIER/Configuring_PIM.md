Configuring PIM
===============

Configuring PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

#### Context

MVPNs also use PIM as the multicast routing protocol. PIM neighbor relationships can be established between devices only after PIM-SM is enabled on interfaces. Then a VPN multicast routing table can be established to guide multicast traffic forwarding.

Perform the following steps on PEs' interfaces bound to VPN instances and on CEs' interfaces.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
   
   
   
   Multicast routing is enabled. This command needs to be configured only on CEs.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.