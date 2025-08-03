Configuring PIM
===============

Configuring PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

#### Context

NG MVPNs also use PIM as the multicast routing protocol on the user network. PIM neighbor relationships can be established between devices only after PIM-SM is enabled on interfaces. Then a VPN multicast routing table can be established to guide multicast traffic forwarding.

Perform the following steps on the PE interfaces bound to VPN instances.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.