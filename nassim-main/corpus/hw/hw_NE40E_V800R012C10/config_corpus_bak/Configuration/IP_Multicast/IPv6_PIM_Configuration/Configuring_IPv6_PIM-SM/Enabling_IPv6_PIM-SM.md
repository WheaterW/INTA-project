Enabling IPv6 PIM-SM
====================

To enable a Router interface to establish IPv6 PIM neighbor relationships with other Routers, enable IPv6 PIM-SM.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim ipv6 sm**](cmdqueryname=pim+ipv6+sm)
   
   
   
   IPv6 PIM-SM is enabled.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Running the [**undo pim ipv6 sm**](cmdqueryname=undo+pim+ipv6+sm) command will delete PIM neighbor relationships on the interface and interrupt the multicast service running on the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.