Configuring PIM
===============

Configure PIM for a VPN, so that multicast VPN routing tables can be created to guide multicast data forwarding.

#### Context

NG MVPN uses PIM as the multicast routing protocol. Configure PIM-SM on interfaces to allow devices to set up PIM neighbor relationships and create multicast VPN routing tables.

Perform the following steps on PEs' interfaces bound to VPN instances and on CEs' interfaces.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
   
   
   
   Multicast routing is enabled. This command needs to be run only on the CE.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.