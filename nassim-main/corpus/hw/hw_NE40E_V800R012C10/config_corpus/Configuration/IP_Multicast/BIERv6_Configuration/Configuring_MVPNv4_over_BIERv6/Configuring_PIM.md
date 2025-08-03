Configuring PIM
===============

On an MVPNv4 over BIERv6 network, a PIM C-instance must be enabled on PEs and the network where the multicast source resides.

#### Context

Perform the following operations to enable a PIM C-instance on a PE's interface connected to a VPN.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.