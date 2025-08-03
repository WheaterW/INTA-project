Configuring PIM
===============

On a GTMv6 over BIERv6 network, a PIM instance must be enabled on PEs and the network where the multicast source resides.

#### Context

Enable a PIM instance on PEs' interfaces connected to the user-side public network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim ipv6 sm**](cmdqueryname=pim+ipv6+sm)
   
   
   
   IPv6 PIM-SM is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.